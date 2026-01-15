#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Preflight checks for skill structure.")
    parser.add_argument("--root", default=".", help="skill root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    required_dirs = ["agents", "assets", "references", "scripts"]
    required_files = ["SKILL.md"]

    issues: list[str] = []

    for d in required_dirs:
        if not (root / d).exists():
            issues.append(f"missing directory: {d}")

    for f in required_files:
        if not (root / f).exists():
            issues.append(f"missing file: {f}")

    if issues:
        print("preflight: FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("preflight: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
