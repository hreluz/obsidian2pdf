from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from .merge import build_merged_markdown
from .pandoc import render_pdf


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert an Obsidian folder into a single PDF."
    )
    parser.add_argument("input_folder", type=Path, help="Folder containing Obsidian notes")
    parser.add_argument("output_pdf", type=Path, help="Target PDF file")
    args = parser.parse_args()

    folder = args.input_folder.resolve()
    output_pdf = args.output_pdf.resolve()

    if not folder.exists() or not folder.is_dir():
        raise SystemExit(f"Input folder does not exist or is not a directory: {folder}")

    merged = build_merged_markdown(folder)

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_md = Path(tmpdir) / "merged.md"
        temp_md.write_text(merged, encoding="utf-8")
        render_pdf(temp_md, output_pdf, folder)

    print(f"Created: {output_pdf}")