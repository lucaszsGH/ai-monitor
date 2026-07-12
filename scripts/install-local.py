#!/usr/bin/env python3
"""Preview or apply a guarded local Skill copy."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "lucas-deepwheel-ai-watchtower"


def main() -> int:
    parser = argparse.ArgumentParser(description="Install AI Watchtower Skill locally.")
    parser.add_argument("--destination", required=True, help="Parent Skills directory")
    parser.add_argument("--apply", action="store_true", help="Copy after explicit review")
    args = parser.parse_args()

    destination = Path(args.destination).expanduser().resolve() / SOURCE.name
    print(f"SOURCE: {SOURCE}")
    print(f"DESTINATION: {destination}")

    if destination.exists():
        print("BLOCK: destination already exists; no overwrite is supported", file=sys.stderr)
        return 2
    if not args.apply:
        print("DRY RUN: no files created; rerun with --apply only after explicit confirmation")
        return 0

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination)
    print("INSTALLED: run host discovery and a demo generation smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

