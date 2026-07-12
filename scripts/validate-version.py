#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    targets = [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "CHANGELOG.md"]
    missing = [path.name for path in targets if version not in path.read_text(encoding="utf-8")]
    if missing:
        print("FAIL: version mismatch in " + ", ".join(missing))
        return 1
    print(f"PASS: version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

