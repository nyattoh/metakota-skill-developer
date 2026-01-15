#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate required outputs for a phase.")
    parser.add_argument("--root", default=".", help="skill root directory")
    parser.add_argument("--require", action="append", default=[], help="required relative path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    issues: list[str] = []

    for rel in args.require:
        path = root / rel
        if not path.exists():
            issues.append(f"missing required output: {rel}")
        elif path.is_file() and path.stat().st_size == 0:
            issues.append(f"empty required output: {rel}")

    if issues:
        print("validate_phase_output: FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("validate_phase_output: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
