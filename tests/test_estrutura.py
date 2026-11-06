import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def local_links(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    for target in re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", text):
        link = urlsplit(target)
        if link.scheme or link.netloc or not link.path:
            continue
        yield (path.parent / unquote(link.path)).resolve()


class EstruturaTests(unittest.TestCase):
    def test_apenas_tres_entradas_descobertas_inclusive_em_subpastas(self):
        self.assertEqual(
            {p.relative_to(SKILLS).as_posix() for p in SKILLS.rglob("SKILL.md")},
            {"business-os/SKILL.md", "marketing/SKILL.md", "comercial/SKILL.md"},
        )

    def test_links_de_recursos_nao_quebram_nem_saem_do_plugin(self):
        documents = [ROOT / "README.md", ROOT / "AGENTS.md", *SKILLS.rglob("*.md")]
        for document in documents:
            for target in local_links(document):
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    self.assertTrue(target.is_relative_to(ROOT), "Recurso fora do plugin")
                    self.assertTrue(target.exists(), "Recurso ausente")

    def test_procedimentos_e_exportador_alcancaveis_pelas_entradas(self):
        pending = list(SKILLS.glob("*/SKILL.md"))
        reached = set()
        while pending:
            document = pending.pop().resolve()
            if document in reached:
                continue
            reached.add(document)
            if document.suffix == ".md":
                pending.extend(p for p in local_links(document) if p.is_file())
        resources = {
            p.resolve() for area in SKILLS.iterdir() if area.is_dir()
            for folder in (area / "references", area / "scripts")
            for p in folder.rglob("*")
            if p.is_file() and p.suffix in {".md", ".json", ".py"}
        }
        self.assertFalse(resources - reached, f"Recursos sem caminho de leitura: {resources - reached}")
