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
    verbose: bool = False,
) -> None:
    pandoc_bin = shutil.which("pandoc")
    if pandoc_bin is None:
        raise SystemExit(
            "Pandoc is not installed or not in PATH. Install it first, for example: brew install pandoc"
        )

    if shutil.which(pdf_engine) is None:
        raise SystemExit(
            f"PDF engine '{pdf_engine}' is not installed or not in PATH."
        )

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

    if verbose:
        print("[INFO] Running Pandoc command:")
        print("[INFO] " + " ".join(cmd))

    subprocess.run(cmd, check=True)