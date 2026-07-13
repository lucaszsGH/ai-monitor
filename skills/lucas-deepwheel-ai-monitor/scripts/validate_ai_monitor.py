#!/usr/bin/env python3
"""Static validation for a generated AI Monitor folder."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = {
    "index.html",
    "styles.css",
    "app.js",
    "manifest.webmanifest",
    "status.example.json",
    "README.md",
    "icons/apple-touch-icon.png",
    "icons/ai-monitor-192.png",
    "icons/ai-monitor-512.png",
    "icons/ai-monitor-icon.svg",
}

DEPRECATED_COLORS = {"#1D1D1F", "#1E6FE8", "#111720", "#F8FAFC"}
FORBIDDEN_MARKERS = (
    "authorization:",
    "cookie:",
    "sessionkey",
    "begin private key",
)
FORBIDDEN_JSON_KEYS = {
    "authorization", "cookie", "sessionkey", "password", "api_key", "apikey",
    "private_key", "prompt", "transcript", "messages", "full_log", "path",
}
ABSOLUTE_HOME = re.compile(
    r"(?:/" + "Users" + r"/|/" + "home" + r"/)[A-Za-z0-9._-]+/"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an AI Monitor starter.")
    parser.add_argument("target", help="AI Monitor output directory")
    return parser.parse_args()


def main() -> int:
    target = Path(parse_args().target).expanduser().resolve()
    if not target.is_dir():
        print("BLOCK: target directory is missing")
        return 2

    missing = sorted(name for name in REQUIRED if not (target / name).is_file())
    findings: list[str] = []
    if missing:
        findings.append("missing required files: " + ", ".join(missing))

    for path in target.rglob("*"):
        if not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        upper = text.upper()
        for color in DEPRECATED_COLORS:
            if color in upper:
                findings.append(f"deprecated DeepWheel color in {path.relative_to(target)}")
        lower = text.lower()
        for marker in FORBIDDEN_MARKERS:
            if marker in lower:
                findings.append(f"sensitive marker in {path.relative_to(target)}")
        if ABSOLUTE_HOME.search(text):
            findings.append(f"machine-specific path in {path.relative_to(target)}")

    css = (target / "styles.css").read_text(encoding="utf-8") if (target / "styles.css").is_file() else ""
    html = (target / "index.html").read_text(encoding="utf-8") if (target / "index.html").is_file() else ""
    js = (target / "app.js").read_text(encoding="utf-8") if (target / "app.js").is_file() else ""
    readme = (target / "README.md").read_text(encoding="utf-8") if (target / "README.md").is_file() else ""

    checks = {
        "safe-area": "safe-area-inset" in css,
        "reduced-motion": "prefers-reduced-motion" in css,
        "touch-target": "--dw-touch-min: 44px" in css,
        "browser-viewport": "100dvh" in css,
        "home-screen-viewport": "100lvh" in css,
        "home-screen-detection": "is-standalone" in js,
        "language-switch": "language-switch" in js and "switchLanguage" in js,
        "deepwheel-app-icon": "DeepWheel" in ((target / "icons" / "ai-monitor-icon.svg").read_text(encoding="utf-8") if (target / "icons" / "ai-monitor-icon.svg").is_file() else ""),
        "home-screen-name": 'apple-mobile-web-app-title" content="AI Monitor"' in html,
        "demo-label": "demo" in html.lower() or "模拟" in html,
        "example-status": "status.example.json" in js,
        "first-run-guide": all(marker in readme for marker in ("127.0.0.1", "0.0.0.0", "Control+C")),
    }
    for label, passed in checks.items():
        if not passed:
            findings.append(f"missing required behavior: {label}")

    status_path = target / "status.example.json"
    if status_path.is_file():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            findings.append("status.example.json is not valid JSON")
        else:
            if status.get("schema_version") != "2.0":
                findings.append("status schema must be 2.0")
            providers = status.get("providers")
            if not isinstance(providers, list) or len(providers) != 2:
                findings.append("status must contain exactly two demo providers")
            else:
                for provider in providers:
                    icon = provider.get("icon")
                    if icon is not None and not re.fullmatch(r"provider-icons/[A-Za-z0-9._-]+", str(icon)):
                        findings.append("provider icon must be a local relative provider-icons asset")
                    usage = provider.get("usage", {})
                    if usage.get("scope") != "provider_account":
                        findings.append("usage scope must be provider_account")
                    sessions = provider.get("sessions", [])
                    if not isinstance(sessions, list):
                        findings.append("sessions must be a list")
                    for session in sessions if isinstance(sessions, list) else []:
                        if "usage" in session or "quota" in session:
                            findings.append("provider usage must not appear inside a session")

            def scan_keys(value: object) -> None:
                if isinstance(value, dict):
                    for key, nested in value.items():
                        if key.lower() in FORBIDDEN_JSON_KEYS:
                            findings.append("status contains a forbidden field name")
                        scan_keys(nested)
                elif isinstance(value, list):
                    for nested in value:
                        scan_keys(nested)

            scan_keys(status)

    if findings:
        print("CONCERNS")
        for finding in sorted(set(findings)):
            print(f"- {finding}")
        return 1

    print("CLEAN: static structure, privacy markers, and DeepWheel baseline passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
