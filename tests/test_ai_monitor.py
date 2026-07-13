from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "lucas-deepwheel-ai-monitor"
CREATE = SKILL / "scripts" / "create_ai_monitor.py"
VALIDATE = SKILL / "scripts" / "validate_ai_monitor.py"


class AiMonitorTests(unittest.TestCase):
    def test_clean_starter_generates_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "ai-monitor"
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
            output = Path(temp) / "ai-monitor"
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
            output = Path(temp) / "ai-monitor"
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
            output = Path(temp) / "ai-monitor"
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

    def test_session_cannot_contain_provider_usage(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "ai-monitor"
            shutil.copytree(SKILL / "assets" / "starter", output)
            status_path = output / "status.example.json"
            status = json.loads(status_path.read_text(encoding="utf-8"))
            status["providers"][0]["sessions"][0]["usage"] = {"remaining_percent": 50}
            status_path.write_text(json.dumps(status), encoding="utf-8")
            result = subprocess.run(
                ["python3", str(VALIDATE), str(output)], text=True, capture_output=True, check=False
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("provider usage must not appear inside a session", result.stdout)

    def test_starter_uses_equal_provider_columns_and_neutral_marks(self) -> None:
        css = (SKILL / "assets" / "starter" / "styles.css").read_text(encoding="utf-8")
        app = (SKILL / "assets" / "starter" / "app.js").read_text(encoding="utf-8")
        status = json.loads(
            (SKILL / "assets" / "starter" / "status.example.json").read_text(encoding="utf-8")
        )
        self.assertIn("grid-template-columns:repeat(2,minmax(0,1fr))", css)
        self.assertEqual([p["label"] for p in status["providers"]], ["Agent A", "Agent B"])
        serialized = json.dumps(status).lower()
        self.assertNotIn("claude", serialized)
        self.assertNotIn("codex", serialized)
        self.assertIn("safeParam === null ? Number.NaN", app)

    def test_starter_adapts_browser_and_home_screen_viewports(self) -> None:
        css = (SKILL / "assets" / "starter" / "styles.css").read_text(encoding="utf-8")
        app = (SKILL / "assets" / "starter" / "app.js").read_text(encoding="utf-8")
        self.assertIn("height:100dvh", css)
        self.assertIn("height:100lvh", css)
        self.assertIn("safe-area-inset-bottom", css)
        self.assertIn("is-standalone", app)
        self.assertIn("display-mode: standalone", app)

    def test_starter_has_deepwheel_icon_and_bilingual_switch(self) -> None:
        starter = SKILL / "assets" / "starter"
        app = (starter / "app.js").read_text(encoding="utf-8")
        html = (starter / "index.html").read_text(encoding="utf-8")
        icon = (starter / "icons" / "ai-monitor-icon.svg").read_text(encoding="utf-8")
        manifest = json.loads((starter / "manifest.webmanifest").read_text(encoding="utf-8"))
        self.assertIn('const language =', app)
        self.assertIn('class="language-switch"', app)
        self.assertIn('switchLanguage', app)
        self.assertIn('DeepWheel', icon)
        self.assertIn('#0071E3', icon)
        self.assertEqual(manifest["name"], "AI Monitor")
        self.assertEqual(manifest["short_name"], "AI Monitor")
        self.assertIn('apple-mobile-web-app-title" content="AI Monitor"', html)

    def test_starter_preserves_lucas_approved_visual_baseline(self) -> None:
        starter = SKILL / "assets" / "starter"
        css = (starter / "styles.css").read_text(encoding="utf-8")
        app = (starter / "app.js").read_text(encoding="utf-8")
        required_css = (
            '--usage-ample:#37C793',
            '--usage-normal:#4EA1FF',
            '--usage-low:#FF9B51',
            '--usage-critical:#FF5F57',
            '--type-caption:clamp(11px,calc(6px + 1.35vh),12px)',
            '--type-title:clamp(18px,calc(10px + 2.1vh),21px)',
            '.session-list{\n  position:relative;\n  top:-4px;',
            '.usage-main{display:grid;grid-template-columns:38% minmax(0,1fr)',
            '.session-meta.healthy b{color:#9CC5F5}',
            '.quota-legend{display:flex;',
        )
        for token in required_css:
            self.assertIn(token, css)
        self.assertIn('remaining >= 70', app)
        self.assertIn('remaining >= 50', app)
        self.assertIn('remaining >= 30', app)
        self.assertIn('class="dw-dot"', app)
        self.assertIn('class="pressure-bars"', app)


if __name__ == "__main__":
    unittest.main()
