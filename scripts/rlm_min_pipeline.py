#!/usr/bin/env python3
"""
Minimal RLM-style pipeline: search -> extract -> verify.

Usage:
  python rlm_min_pipeline.py --input file.txt --query "term1" --query "term2" --output out.json
  python rlm_min_pipeline.py --input file.txt --query "term" --verify-query "except" --verify-query "ただし"
"""

import argparse
import json
from pathlib import Path

DEFAULT_VERIFY_QUERIES = [
    "ただし",
    "例外",
    "禁止",
    "定義",
    "除外",
    "not",
    "except",
    "unless",
    "definition",
]


def find_hits(lines, queries, context_lines=2, ignore_case=False):
    if ignore_case:
        q_norm = [q.lower() for q in queries]
    else:
        q_norm = queries

    hits = []
    for idx, line in enumerate(lines):
        hay = line.lower() if ignore_case else line
        if any(q in hay for q in q_norm):
            start = max(0, idx - context_lines)
            end = min(len(lines), idx + context_lines + 1)
            hits.append({
                "line": idx + 1,
                "match": line,
                "context": lines[start:end],
            })
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(description="Minimal RLM-style pipeline")
    parser.add_argument("--input", required=True, help="Input text file")
    parser.add_argument("--query", action="append", required=True, help="Query string (repeatable)")
    parser.add_argument("--verify-query", action="append", help="Verification query (repeatable)")
    parser.add_argument("--context-lines", type=int, default=2, help="Lines of context before/after")
    parser.add_argument("--ignore-case", action="store_true", help="Case-insensitive match")
    parser.add_argument("--output", required=False, help="Output JSON path (default: stdout)")
    args = parser.parse_args()

    text_path = Path(args.input)
    lines = text_path.read_text(encoding="utf-8", errors="replace").splitlines()

    primary_hits = find_hits(lines, args.query, args.context_lines, args.ignore_case)

    verify_queries = args.verify_query or DEFAULT_VERIFY_QUERIES
    verify_hits = find_hits(lines, verify_queries, args.context_lines, args.ignore_case)

    result = {
        "input": str(text_path),
        "queries": args.query,
        "verify_queries": verify_queries,
        "context_lines": args.context_lines,
        "primary_hits": primary_hits,
        "verify_hits": verify_hits,
        "counts": {
            "primary": len(primary_hits),
            "verify": len(verify_hits),
        },
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        print(out)


if __name__ == "__main__":
    main()
