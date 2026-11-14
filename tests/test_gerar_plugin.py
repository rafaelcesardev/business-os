import json
import runpy
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
gerar_plugin = runpy.run_path(str(ROOT / "skills/cortex/scripts/gerar_plugin.py"))["gerar_plugin"]


class GerarPluginTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "empresa"
        self.context = self.root / "cerebro"
        self.context.mkdir(parents=True)
        (self.context / "RESUMO.md").write_text("# Oficina Exemplo\n\nConserta bicicletas. Público: ciclistas da região.\n")
        (self.context / "negocio.md").write_text("# Negócio\n\nFaz manutenção de bicicletas.\n")
        (self.context / "fontes").mkdir()
        (self.context / "fontes/call.txt").write_text("Material bruto privado que não deve entrar na entrega.")
        self.config = {
            "nome": "oficina-exemplo", "titulo": "Oficina Exemplo",
            "versao": "0.1.0", "arquivos": ["RESUMO.md", "negocio.md"],
        }
        self.save()

    def save(self):
        (self.context / "compartilhar.json").write_text(json.dumps(self.config))

    def test_pacote_portatil_com_contexto_e_sem_fontes(self):
        before = {f.name: f.read_bytes() for f in self.context.glob("*") if f.is_file()}
        folder, archive = gerar_plugin(self.root)
        self.assertTrue(folder.is_dir())
        manifests = [json.loads((folder / f).read_text()) for f in
                     ["plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"]]
        self.assertTrue(all(m["name"] == "oficina-exemplo" and m["version"] == "0.1.0" for m in manifests))
        with zipfile.ZipFile(archive) as packed:
            self.assertIsNone(packed.testzip())
            self.assertIn("plugin.json", packed.namelist())
            self.assertIn("skills/contexto/SKILL.md", packed.namelist())
            self.assertEqual(
                packed.read("skills/contexto/references/negocio.md"),
                (self.context / "negocio.md").read_bytes(),
            )
            self.assertFalse(any("fontes" in n or "compartilhar.json" in n for n in packed.namelist()))
        after = {f.name: f.read_bytes() for f in self.context.glob("*") if f.is_file()}
        self.assertEqual(before, after)

    def test_pasta_legada_continua_aceita(self):
        self.context.rename(self.root / ".business-os")
        folder, _ = gerar_plugin(self.root)
        self.assertTrue((folder / "skills/contexto/references/RESUMO.md").exists())

    def test_repeticao_idempotente_e_recupera_zip_ausente(self):
        folder, archive = gerar_plugin(self.root)
        original = archive.read_bytes()
        self.assertEqual(gerar_plugin(self.root), (folder, archive))
        self.assertEqual(original, archive.read_bytes())
        archive.unlink()
        gerar_plugin(self.root)
        self.assertEqual(original, archive.read_bytes())

    def test_mudanca_exige_outra_versao_e_preserva_a_anterior(self):
        folder, archive = gerar_plugin(self.root)
        old_zip = archive.read_bytes()
        old_context = (folder / "skills/contexto/references/negocio.md").read_bytes()
        (self.context / "negocio.md").write_text("# Negócio\n\nTambém faz revisão de bicicletas.\n")
        with self.assertRaises(ValueError):
            gerar_plugin(self.root)
        self.assertEqual(old_zip, archive.read_bytes())
        self.assertEqual(old_context, (folder / "skills/contexto/references/negocio.md").read_bytes())
        self.config["versao"] = "0.1.1"
        self.save()
        new_folder, _ = gerar_plugin(self.root)
        self.assertNotEqual(folder, new_folder)
        self.assertTrue(folder.exists() and new_folder.exists())

    def test_caminhos_fora_fontes_ocultos_executaveis_e_normalizacao(self):
        for name in ["../fora.md", "/tmp/fora.md", "fontes/call.txt", ".env",
                     "script.py", ".", "", "pasta/../negocio.md", "pasta\\arquivo.md", "./negocio.md"]:
            with self.subTest(name=name):
                self.config["arquivos"] = ["RESUMO.md", name]
                self.save()
                with self.assertRaises(ValueError):
                    gerar_plugin(self.root)
        self.assertFalse((self.root / "entregas").exists())

    def test_link_simbolico_nao_e_exportado(self):
        outside = Path(self.temp.name) / "fora.md"
        outside.write_text("Privado")
        (self.context / "link.md").symlink_to(outside)
        self.config["arquivos"].append("link.md")
        self.save()
        with self.assertRaises(ValueError):
            gerar_plugin(self.root)
        self.assertFalse((self.root / "entregas").exists())

    def test_destino_simbolico_nao_e_usado(self):
        outside = Path(self.temp.name) / "outro"
        outside.mkdir()
        (self.root / "entregas").symlink_to(outside)
        with self.assertRaises(ValueError):
            gerar_plugin(self.root)
        self.assertEqual(list(outside.iterdir()), [])

    def test_link_local_precisa_estar_incluido(self):
        (self.context / "RESUMO.md").write_text("# Oficina Exemplo\n\n[Detalhes](negocio.md)\n")
        self.config["arquivos"] = ["RESUMO.md"]
        self.save()
        with self.assertRaisesRegex(ValueError, "Link local não incluído"):
            gerar_plugin(self.root)
        self.config["arquivos"].append("negocio.md")
        self.save()
        folder, _ = gerar_plugin(self.root)
        self.assertTrue((folder / "skills/contexto/references/negocio.md").exists())

    def test_configuracao_e_resumo_invalidos(self):
        cases = [
            {**self.config, "nome": "../outra"},
            {**self.config, "titulo": "Nome\ninválido"},
            {**self.config, "versao": "01.0.0"},
            {**self.config, "versao": "0.1"},
            {**self.config, "arquivos": ["negocio.md"]},
            {**self.config, "arquivos": ["RESUMO.md", "resumo.md"]},
            {**self.config, "arquivos": "RESUMO.md"},
        ]
        for case in cases:
            with self.subTest(case=case):
                (self.context / "compartilhar.json").write_text(json.dumps(case))
                with self.assertRaises(ValueError):
                    gerar_plugin(self.root)
        self.save()
        (self.context / "RESUMO.md").write_text("<!-- ainda vazio -->")
        with self.assertRaises(ValueError):
            gerar_plugin(self.root)

    def test_zip_diferente_nao_e_sobrescrito(self):
        folder, archive = gerar_plugin(self.root)
        archive.write_bytes(b"arquivo alterado fora do gerador")
        with self.assertRaises(ValueError):
            gerar_plugin(self.root)
        self.assertEqual(archive.read_bytes(), b"arquivo alterado fora do gerador")
        self.assertTrue(folder.exists())

    def test_logo_selecionada_e_usada_nos_dois_clientes(self):
        import struct
        import zlib
        def chunk(kind, data):
            return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", 512, 512, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress((b"\0" + b"\x80\x80\x80" * 512) * 512))
        png += chunk(b"IEND", b"")
        asset = self.context / "assets/logo.png"
        asset.parent.mkdir()
        asset.write_bytes(png)
        self.config.update({"logo": "assets/logo.png", "arquivos": ["RESUMO.md", "assets/logo.png"]})
        self.save()
        folder, _ = gerar_plugin(self.root)
        native = json.loads((folder / "plugin.json").read_text())["extensions"]["com.openai"]["interface"]
        codex = json.loads((folder / ".codex-plugin/plugin.json").read_text())["interface"]
        claude = json.loads((folder / ".claude-plugin/plugin.json").read_text())
        for target in [native["composerIcon"], native["logo"], codex["composerIcon"], claude["icon"]]:
            self.assertEqual((folder / target).read_bytes(), png)

    def test_logo_precisa_estar_selecionada_e_em_formato_compativel(self):
        self.config["logo"] = "assets/logo.png"
        self.save()
        with self.assertRaisesRegex(ValueError, "arquivo selecionado"):
            gerar_plugin(self.root)
        asset = self.context / "assets/logo.svg"
        asset.parent.mkdir()
        asset.write_text("<svg/>")
        self.config.update({"logo": "assets/logo.svg", "arquivos": ["RESUMO.md", "assets/logo.svg"]})
        self.save()
        with self.assertRaisesRegex(ValueError, "PNG ou JPEG"):
            gerar_plugin(self.root)

    def test_comando_completo_e_erro_sem_traceback(self):
        command = [sys.executable, str(ROOT / "skills/cortex/scripts/gerar_plugin.py"), str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("ZIP:", result.stdout)
        self.config["arquivos"] = ["RESUMO.md", "../fora.md"]
        self.save()
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Não foi possível gerar", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
