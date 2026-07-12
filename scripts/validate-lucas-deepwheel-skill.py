#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "lucas-deepwheel-ai-watchtower"


def main() -> int:
    required = [
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "agents" / "risk-profile.json",
        SKILL / "references" / "capability-preflight.md",
        SKILL / "references" / "status-data-contract.md",
        SKILL / "references" / "deepwheel-landscape-ui.md",
        SKILL / "scripts" / "create_watchtower.py",
        SKILL / "scripts" / "validate_watchtower.py",
    ]
    missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file()]
    if missing:
        print("FAIL: missing " + ", ".join(missing))
        return 1
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name: lucas-deepwheel-ai-watchtower" not in text:
        print("FAIL: invalid SKILL.md frontmatter")
        return 1
    print("PASS: generic package validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

