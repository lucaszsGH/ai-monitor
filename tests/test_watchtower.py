from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "lucas-deepwheel-ai-watchtower"
CREATE = SKILL / "scripts" / "create_watchtower.py"
VALIDATE = SKILL / "scripts" / "validate_watchtower.py"


class WatchtowerTests(unittest.TestCase):
    def test_clean_starter_generates_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "watchtower"
            created = subprocess.run(
                ["python3", str(CREATE), "--output", str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            validated = subprocess.run(
                ["python3", str(VALIDATE), str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(validated.returncode, 0, validated.stdout)
            self.assertIn("CLEAN", validated.stdout)

    def test_generator_refuses_nonempty_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "watchtower"
            output.mkdir()
            (output / "keep.txt").write_text("do not replace", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(CREATE), "--output", str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual((output / "keep.txt").read_text(encoding="utf-8"), "do not replace")

    def test_deprecated_color_returns_concerns(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "watchtower"
            shutil.copytree(SKILL / "assets" / "starter", output)
            with (output / "styles.css").open("a", encoding="utf-8") as handle:
                handle.write("\n.bad { color: #1D1D1F; }\n")
            result = subprocess.run(
                ["python3", str(VALIDATE), str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("deprecated DeepWheel color", result.stdout)

    def test_machine_path_returns_concerns_without_echoing_value(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "watchtower"
            shutil.copytree(SKILL / "assets" / "starter", output)
            private_value = "/" + "Users" + "/example/private/project"
            (output / "status.example.json").write_text(
                '{"path": "' + private_value + '"}', encoding="utf-8"
            )
            result = subprocess.run(
                ["python3", str(VALIDATE), str(output)],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("machine-specific path", result.stdout)
            self.assertNotIn(private_value, result.stdout)


if __name__ == "__main__":
    unittest.main()
