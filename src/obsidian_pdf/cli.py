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
    parser.add_argument(
        "input_folder",
        type=Path,
        help="Folder containing Obsidian notes",
    )
    parser.add_argument(
        "output_pdf",
        type=Path,
        help="Target PDF file",
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Include a table of contents",
    )
    parser.add_argument(
        "--engine",
        default="pdflatex",
        help="PDF engine to use (example: pdflatex, tectonic)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed progress output",
    )

    args = parser.parse_args()

    folder = args.input_folder.resolve()
    output_pdf = args.output_pdf.resolve()

    if not folder.exists() or not folder.is_dir():
        raise SystemExit(f"Input folder does not exist or is not a directory: {folder}")

    if args.verbose:
        print(f"[INFO] Input folder: {folder}")
        print(f"[INFO] Output PDF: {output_pdf}")
        print(f"[INFO] TOC enabled: {args.toc}")
        print(f"[INFO] PDF engine: {args.engine}")

    merged = build_merged_markdown(folder, verbose=args.verbose)

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_md = Path(tmpdir) / "merged.md"
        temp_md.write_text(merged, encoding="utf-8")

        if args.verbose:
            print(f"[INFO] Temporary merged markdown: {temp_md}")

        render_pdf(
            input_md=temp_md,
            output_pdf=output_pdf,
            resource_root=folder,
            toc=args.toc,
            pdf_engine=args.engine,
            verbose=args.verbose,
        )

    print(f"Created: {output_pdf}")