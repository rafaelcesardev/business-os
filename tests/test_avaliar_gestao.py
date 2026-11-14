import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from avaliar_gestao import cases, mcp, models_from_calls, models_from_events, prepare_plugin


class AvaliarGestaoTests(unittest.TestCase):
    def test_evento_de_sistema_com_mensagem_textual_nao_quebra_coleta(self):
        self.assertEqual(models_from_events([
            {"type": "system", "message": "Expanding read scope"},
            {"type": "assistant", "message": {"model": "modelo-ficticio"}},
            {"type": "result", "result": "fim"},
        ]), ["modelo-ficticio"])

    def test_catorze_casos_ficticios(self):
        self.assertEqual(set(cases()), set(range(1, 16)))
        self.assertTrue(all(prompt.strip() for prompt, _, _ in cases().values()))

    def test_servico_somente_leitura_registra_tentativa_sem_mutar_estado(self):
        with tempfile.TemporaryDirectory() as temporary:
            state = Path(temporary) / "estado.json"
            log = Path(temporary) / "log.jsonl"
            original = json.dumps({"quadro": {"permissao": "somente-leitura"}})
            state.write_text(original)
            calls = [
                {"jsonrpc": "2.0", "method": "notifications/initialized"},
                {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "consultar_servico", "arguments": {"servico": "quadro"}}},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "alterar_servico", "arguments": {"acao": "atualizar_quadro", "conteudo": "nova etapa"}}},
            ]
            output = io.StringIO()
            with patch("sys.stdin", io.StringIO("\n".join(map(json.dumps, calls)))), patch("sys.stdout", output):
                mcp(state, log)
            responses = [json.loads(line) for line in output.getvalue().splitlines()]
            self.assertEqual(len(responses), 2)
            self.assertFalse(responses[0]["result"]["isError"])
            self.assertTrue(responses[1]["result"]["isError"])
            self.assertIn("Escrita negada", responses[1]["result"]["content"][0]["text"])
            self.assertEqual(len(log.read_text().splitlines()), 2)
            self.assertEqual(state.read_text(), original)

    def test_modelo_do_codex_vem_das_chamadas_mcp(self):
        with tempfile.TemporaryDirectory() as temporary:
            log = Path(temporary) / "chamadas.jsonl"
            self.assertEqual(models_from_calls(log), [])
            log.write_text(json.dumps({"_meta": {"x-codex-turn-metadata": {"model": "modelo-ficticio"}}}) + "\n"
                           + json.dumps({"name": "consultar_servico"}) + "\n")
            self.assertEqual(models_from_calls(log), ["modelo-ficticio"])

    def test_copia_do_plugin_nao_expoe_gabarito(self):
        with tempfile.TemporaryDirectory() as temporary:
            plugin = Path(temporary) / "plugin"
            prepare_plugin(plugin)
            self.assertTrue((plugin / "skills/cortex/SKILL.md").exists())
            self.assertFalse((plugin / "tests").exists())
