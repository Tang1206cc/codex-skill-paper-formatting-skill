#!/usr/bin/env python3
"""Compare draft text and final text for Word formatting workflows.

This helper is intentionally conservative: it normalizes common whitespace and
Word field artifacts, then reports whether the normalized texts match. When they
do not match, it prints a short diff and likely added/removed snippets so Codex
can inspect whether a difference is an expected layout artifact or a real content
change.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path


FIELD_NOISE_PATTERNS = [
    r"TOC\s+\\o\s+\"[^\"]+\"\s+\\h\s+\\z\s+\\u",
    r"PAGEREF\s+\S+\s+\\h",
    r"HYPERLINK\s+\\l\s+\"[^\"]+\"",
    r"请在\s*Word\s*中更新目录",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def normalize(text: str, *, loose: bool = False) -> str:
    text = text.replace("\ufeff", "")
    text = text.replace("\u00a0", " ")
    text = text.replace("\u3000", " ")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for pattern in FIELD_NOISE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    text = text.strip()
    if loose:
        text = re.sub(r"\s+", "", text)
    return text


def snippets(base: str, other: str, label: str) -> list[str]:
    matcher = difflib.SequenceMatcher(a=base, b=other, autojunk=False)
    out: list[str] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "insert":
            out.append(f"{label}: {other[j1:j2][:160]!r}")
        elif tag == "delete":
            out.append(f"{label}: {base[i1:i2][:160]!r}")
        elif tag == "replace":
            out.append(f"{label}: {base[i1:i2][:80]!r} -> {other[j1:j2][:80]!r}")
        if len(out) >= 12:
            break
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare source draft text with final document text.")
    parser.add_argument("source", type=Path, help="Extracted source draft text file")
    parser.add_argument("final", type=Path, help="Extracted final document text file")
    parser.add_argument("--loose", action="store_true", help="Ignore all whitespace differences")
    parser.add_argument("--show-diff", action="store_true", help="Print unified diff on mismatch")
    args = parser.parse_args()

    source_raw = read_text(args.source)
    final_raw = read_text(args.final)
    source = normalize(source_raw, loose=args.loose)
    final = normalize(final_raw, loose=args.loose)

    if source == final:
        print("PASS: normalized source and final text match.")
        print(f"source_chars={len(source)} final_chars={len(final)} loose={args.loose}")
        return 0

    print("FAIL: normalized source and final text differ.")
    print(f"source_chars={len(source)} final_chars={len(final)} loose={args.loose}")
    for line in snippets(source, final, "difference"):
        print(line)

    if args.show_diff:
        diff = difflib.unified_diff(
            source.splitlines(),
            final.splitlines(),
            fromfile=str(args.source),
            tofile=str(args.final),
            lineterm="",
        )
        for line in list(diff)[:240]:
            print(line)

    return 1


if __name__ == "__main__":
    sys.exit(main())
