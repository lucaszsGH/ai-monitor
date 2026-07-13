#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "lucas-deepwheel-ai-monitor"


def digest_tree(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare source and an installed Skill copy.")
    parser.add_argument("installed", help="Installed Skill directory")
    args = parser.parse_args()
    installed = Path(args.installed).expanduser().resolve()
    if not installed.is_dir():
        print("BLOCK: installed copy is missing")
        return 2
    if digest_tree(SOURCE) != digest_tree(installed):
        print("DRIFT: installed copy does not match source")
        return 1
    print("MATCH: installed copy matches source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

