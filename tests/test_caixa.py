import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/cortex/scripts"
sys.path.insert(0, str(SCRIPTS))
import caixa  # noqa: E402


class CaixaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "oficina-exemplo"

    def test_iniciar_cria_o_padrao_e_conferir_aprova(self):
        feitos = caixa.iniciar(self.root, titulo="Oficina Exemplo")
        self.assertIn("cerebro/RESUMO.md", feitos)
        self.assertIn("cerebro/conhecimento/README.md", feitos)
        versions = {json.loads((self.root / "cerebro" / m).read_text())["version"] for m in caixa.MANIFESTOS}
        self.assertEqual(versions, {"0.1.0"})
        self.assertIn("/cerebro/fontes/", (self.root / ".gitignore").read_text())
        self.assertEqual((self.root / "CLAUDE.md").read_text(), "@AGENTS.md\n")
        self.assertEqual(caixa.conferir(self.root), [])

    def test_repetir_nao_sobrescreve_conteudo_e_atualiza_o_bloco(self):
        caixa.iniciar(self.root, titulo="Oficina Exemplo")
        resumo = self.root / "cerebro/RESUMO.md"
        resumo.write_text("# Oficina Exemplo\n\nConserta bicicletas.\n")
        agents = self.root / "AGENTS.md"
        agents.write_text("# Regras da casa\n\n<!-- business-os:inicio -->\nbloco antigo\n<!-- business-os:fim -->\n\n## Depois\n")
        self.assertEqual(caixa.iniciar(self.root), ["AGENTS.md"])
        self.assertEqual(resumo.read_text(), "# Oficina Exemplo\n\nConserta bicicletas.\n")
        text = agents.read_text()
        self.assertTrue(text.startswith("# Regras da casa\n") and text.endswith("\n## Depois\n"))
        self.assertNotIn("bloco antigo", text)
        self.assertEqual(caixa.iniciar(self.root), [])

    def test_catalogo_existente_preserva_outras_entradas(self):
        (self.root / ".claude-plugin").mkdir(parents=True)
        catalog = self.root / ".claude-plugin/marketplace.json"
        catalog.write_text(json.dumps({"name": "casa", "owner": {"name": "Dona"}, "plugins": [
            {"name": "outro", "source": "./outro"},
            {"name": "oficina-exemplo", "source": "./.business-os"},
        ]}))
        caixa.iniciar(self.root)
        data = json.loads(catalog.read_text())
        self.assertEqual(data["owner"], {"name": "Dona"})
        self.assertEqual([p["source"] for p in data["plugins"]], ["./outro", "./cerebro"])

    def test_conferir_aponta_o_que_foge_do_padrao(self):
        caixa.iniciar(self.root)
        brain = self.root / "cerebro"
        (brain / "RESUMO.md").write_text("# Oficina\n\n[Sumiu](nao-existe.md) " + "palavra " * caixa.LIMITE_RESUMO)
        manifest = brain / ".claude-plugin/plugin.json"
        manifest.write_text(manifest.read_text().replace("0.1.0", "0.2.0"))
        (self.root / "AGENTS.md").write_text("sem bloco\n")
        problemas = "\n".join(caixa.conferir(self.root))
        for trecho in ["limite", "Link quebrado", "versão diferentes", "AGENTS.md", "Catálogo"]:
            self.assertIn(trecho, problemas)

    def test_pasta_legada_pede_renomear_e_nome_invalido_e_recusado(self):
        (self.root / ".business-os").mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "Renomeie"):
            caixa.iniciar(self.root)
        with self.assertRaisesRegex(ValueError, "--nome"):
            caixa.iniciar(Path(self.temp.name) / "Minha Empresa")

    def test_comando_sem_traceback(self):
        command = [sys.executable, str(SCRIPTS / "caixa.py")]
        ok = subprocess.run([*command, "iniciar", str(self.root)], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(subprocess.run([*command, "conferir", str(self.root)], capture_output=True).returncode, 0)
        (self.root / "cerebro/RESUMO.md").unlink()
        bad = subprocess.run([*command, "conferir", str(self.root)], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("RESUMO.md", bad.stderr)
        self.assertNotIn("Traceback", bad.stderr)


if __name__ == "__main__":
    unittest.main()
