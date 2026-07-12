#!/usr/bin/env python3
"""Validate the public release package without printing matched sensitive text."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "lucas-deepwheel-ai-watchtower"

REQUIRED = [
    "README.md",
    "README.zh-CN.md",
    "VERSION",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/INSTALLATION.md",
    "docs/TEST-RUNS.md",
    "docs/REVIEW-RECORD.md",
    "docs/PUBLICATION-CHECKLIST.md",
    "docs/ROADMAP.md",
    "examples/example-prompts.md",
    ".github/workflows/validate.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "skills/lucas-deepwheel-ai-watchtower/SKILL.md",
    "skills/lucas-deepwheel-ai-watchtower/agents/openai.yaml",
    "skills/lucas-deepwheel-ai-watchtower/agents/risk-profile.json",
    "skills/lucas-deepwheel-ai-watchtower/scripts/create_watchtower.py",
    "skills/lucas-deepwheel-ai-watchtower/scripts/validate_watchtower.py",
    "scripts/install-local.py",
    "scripts/validate-version.py",
    "scripts/validate-lucas-deepwheel-skill.py",
    "scripts/verify-installed-copy.py",
    "scripts/device-matrix-smoke.py",
]

INTRO_ASSETS = [
    "assets/intro/watchtower-hero-en.svg",
    "assets/intro/watchtower-hero-en.png",
    "assets/intro/watchtower-hero-zh-CN.svg",
    "assets/intro/watchtower-hero-zh-CN.png",
    "assets/intro/watchtower-workflow-en.svg",
    "assets/intro/watchtower-workflow-en.png",
    "assets/intro/watchtower-workflow-zh-CN.svg",
    "assets/intro/watchtower-workflow-zh-CN.png",
    "assets/intro/watchtower-image2-concept-v2.png",
    "assets/intro/watchtower-phone-landscape-apple-17promax-final.png",
    "assets/intro/watchtower-phone-landscape-apple-iphonex-final.png",
]

SENSITIVE_ASSIGNMENT = re.compile(
    r"(?i)(?:authorization|cookie|sessionkey|password|private[_ -]?key)\s*[:=]\s*[\"']?[A-Za-z0-9]"
)
ABSOLUTE_HOME = re.compile(
    r"(?:/" + "Users" + r"/|/" + "home" + r"/)[A-Za-z0-9._-]+/"
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def main() -> int:
    findings: list[str] = []

    for relative in REQUIRED + INTRO_ASSETS:
        if not (ROOT / relative).is_file():
            findings.append(f"missing required file: {relative}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        if readme.is_file() and version not in readme.read_text(encoding="utf-8"):
            findings.append(f"version mismatch: {readme.name}")

    if not SKILL.is_dir():
        findings.append("Skill directory is missing")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.stat().st_size > 2_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if SENSITIVE_ASSIGNMENT.search(text):
            findings.append(f"credential-shaped assignment in {path.relative_to(ROOT)}")
        if ABSOLUTE_HOME.search(text):
            findings.append(f"machine-specific path in {path.relative_to(ROOT)}")

    if findings:
        for finding in sorted(set(findings)):
            fail(finding)
        return 1

    print(f"PASS: public package {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
