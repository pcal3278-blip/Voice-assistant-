import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from newscast_module import CAST25ScriptManager


class TestCAST25ScriptManager(unittest.TestCase):
    def setUp(self):
        self.manager = CAST25ScriptManager()

    def test_add_verified_news_to_block(self):
        self.manager.add_verified_news(
            "Block 1 - Open and Top Story",
            "Mayor announces transit upgrades.",
            source="City Hall Briefing",
        )

        rendered = self.manager.render_script()
        self.assertIn("[Source: City Hall Briefing] Mayor announces transit upgrades.", rendered)

    def test_rejects_unknown_block(self):
        with self.assertRaises(ValueError):
            self.manager.add_verified_news("Block 99", "Invalid block")

    def test_voice_validation(self):
        with self.assertRaises(ValueError):
            CAST25ScriptManager(voice="invalid")

    def test_export_script(self):
        self.manager.add_verified_news("Block 5 - Close", "Thanks for listening.")

        with TemporaryDirectory() as tmp:
            output = Path(tmp) / "cast25_script.txt"
            saved_path = self.manager.export_script(output)

            self.assertTrue(saved_path.exists())
            content = saved_path.read_text(encoding="utf-8")
            self.assertIn("CAST25 Script", content)
            self.assertIn("## Block 5 - Close", content)


if __name__ == "__main__":
    unittest.main()
