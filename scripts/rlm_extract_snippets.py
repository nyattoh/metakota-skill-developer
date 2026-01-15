#!/usr/bin/env python3
"""
Extract snippets around matching lines in a text file.

Usage:
  python rlm_extract_snippets.py --input file.txt --query "term" --context-lines 3
  python rlm_extract_snippets.py --input file.txt --query "term1" --query "term2"
"""

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract snippets around matching lines")
    parser.add_argument("--input", required=True, help="Input text file")
    parser.add_argument("--query", action="append", required=True, help="Query string (repeatable)")
    parser.add_argument("--context-lines", type=int, default=2, help="Lines of context before/after")
    parser.add_argument("--ignore-case", action="store_true", help="Case-insensitive match")
    parser.add_argument("--output", required=False, help="Output JSON path (default: stdout)")
    args = parser.parse_args()

    text_path = Path(args.input)
    lines = text_path.read_text(encoding="utf-8", errors="replace").splitlines()

    queries = args.query
    if args.ignore_case:
        queries = [q.lower() for q in queries]

    hits = []
    for idx, line in enumerate(lines):
        hay = line.lower() if args.ignore_case else line
        if any(q in hay for q in queries):
            start = max(0, idx - args.context_lines)
            end = min(len(lines), idx + args.context_lines + 1)
            snippet = lines[start:end]
            hits.append({
                "line": idx + 1,
                "match": line,
                "context": snippet,
            })

    result = {
        "input": str(text_path),
        "queries": args.query,
        "context_lines": args.context_lines,
        "hits": hits,
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        print(out)


if __name__ == "__main__":
    main()
