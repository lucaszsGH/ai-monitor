#!/usr/bin/env python3
"""Create a privacy-safe AI Monitor starter without overwriting files."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create an AI Monitor starter.")
    parser.add_argument("--output", required=True, help="New or empty output directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = Path(args.output).expanduser().resolve()
    starter = Path(__file__).resolve().parents[1] / "assets" / "starter"

    if not starter.is_dir():
        print("BLOCK: packaged starter is missing", file=sys.stderr)
        return 2

    if output.exists() and any(output.iterdir()):
        print("BLOCK: output directory is not empty; refusing to overwrite", file=sys.stderr)
        return 2

    output.mkdir(parents=True, exist_ok=True)
    for source in starter.iterdir():
        destination = output / source.name
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

    print(f"CREATED: {output}")
    print("MODE: demo data only; no credentials or local session content were copied")
    print("NEXT 1/3: run validate_ai_monitor.py against the generated folder")
    print("NEXT 2/3: read the generated README.md and preview on 127.0.0.1")
    print("NEXT 3/3: confirm trusted Wi-Fi before allowing phone access")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
