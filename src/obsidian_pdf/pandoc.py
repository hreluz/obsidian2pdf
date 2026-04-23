from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def render_pdf(
    input_md: Path,
    output_pdf: Path,
    resource_root: Path,
    toc: bool = False,
    pdf_engine: str = "pdflatex",
) -> None:
    pandoc_bin = shutil.which("pandoc")
    if pandoc_bin is None:
        raise SystemExit(
            "Pandoc is not installed or not in PATH. Install it first, for example: brew install pandoc"
        )
    
    if shutil.which(pdf_engine) is None:
        fallback = "pdflatex"
        if shutil.which(fallback):
            print(f"Warning: {pdf_engine} not found, using {fallback}")
            pdf_engine = fallback
        else:
            raise SystemExit(f"No PDF engine found. Install pdflatex or tectonic.")

    cmd = [
        pandoc_bin,
        str(input_md),
        "-o",
        str(output_pdf),
        "--resource-path",
        str(resource_root),
        f"--pdf-engine={pdf_engine}",
    ]

    if toc:
        cmd.append("--toc")

    subprocess.run(cmd, check=True)