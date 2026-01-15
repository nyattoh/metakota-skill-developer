#!/usr/bin/env python3
"""
Extract text from a PDF.

Usage:
  python extract_pdf_text.py --input file.pdf --output out.txt
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF")
    parser.add_argument("--input", required=True, help="Input PDF path")
    parser.add_argument("--output", required=True, help="Output text path")
    args = parser.parse_args()

    pdf_path = Path(args.input)
    out_path = Path(args.output)

    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path), strict=False)
    chunks = []
    for i, page in enumerate(reader.pages):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text.strip():
            chunks.append(f"\n--- page {i+1} ---\n" + text)
    out_path.write_text("\n".join(chunks), encoding="utf-8")


if __name__ == "__main__":
    main()
