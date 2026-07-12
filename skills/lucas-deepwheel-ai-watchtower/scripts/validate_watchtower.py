#!/usr/bin/env python3
"""Static validation for a generated AI Watchtower folder."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED = {
    "index.html",
    "styles.css",
    "app.js",
    "manifest.webmanifest",
    "status.example.json",
}

DEPRECATED_COLORS = {"#1D1D1F", "#1E6FE8", "#111720", "#F8FAFC"}
FORBIDDEN_MARKERS = (
    "authorization:",
    "cookie:",
    "sessionkey",
    "begin private key",
)
ABSOLUTE_HOME = re.compile(
    r"(?:/" + "Users" + r"/|/" + "home" + r"/)[A-Za-z0-9._-]+/"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an AI Watchtower starter.")
    parser.add_argument("target", help="Watchtower output directory")
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

    checks = {
        "safe-area": "safe-area-inset" in css,
        "reduced-motion": "prefers-reduced-motion" in css,
        "touch-target": "--dw-touch-min: 44px" in css,
        "demo-label": "demo" in html.lower() or "模拟" in html,
        "example-status": "status.example.json" in js,
    }
    for label, passed in checks.items():
        if not passed:
            findings.append(f"missing required behavior: {label}")

    if findings:
        print("CONCERNS")
        for finding in sorted(set(findings)):
            print(f"- {finding}")
        return 1

    print("CLEAN: static structure, privacy markers, and DeepWheel baseline passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
