#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check_frontmatter(text: str, issues: list[str]) -> None:
    if not text.lstrip().startswith("---"):
        issues.append("SKILL.md: missing frontmatter start '---'")
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        issues.append("SKILL.md: frontmatter not closed with '---'")
        return
    fm = parts[1]
    if re.search(r"^\s*name\s*:", fm, re.MULTILINE) is None:
        issues.append("SKILL.md: frontmatter missing 'name'")
    if re.search(r"^\s*description\s*:", fm, re.MULTILINE) is None:
        issues.append("SKILL.md: frontmatter missing 'description'")


def _find_referenced_files(text: str, root: Path) -> list[str]:
    pattern = re.compile(r"(agents|references|scripts|assets)/[A-Za-z0-9_.-]+\.(md|py|js|yaml|yml|json|ts|sh)")
    refs = set(m.group(0) for m in pattern.finditer(text))
    missing = []
    for rel in sorted(refs):
        if not (root / rel).exists():
            missing.append(f"missing referenced file: {rel}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate minimal skill structure.")
    parser.add_argument("--root", default=".", help="skill root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    issues: list[str] = []

    for dirname in ["agents", "references", "scripts", "assets"]:
        if not (root / dirname).exists():
            issues.append(f"missing directory: {dirname}")

    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        issues.append("missing SKILL.md")
    else:
        text = _load_text(skill_md)
        _check_frontmatter(text, issues)
        issues.extend(_find_referenced_files(text, root))

    if issues:
        print("validate_skill_structure: FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("validate_skill_structure: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
