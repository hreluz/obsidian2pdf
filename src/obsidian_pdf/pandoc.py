from __future__ import annotations

import subprocess
from pathlib import Path


def render_pdf(input_md: Path, output_pdf: Path, resource_root: Path) -> None:
    cmd = [
        "pandoc",
        str(input_md),
        "-o",
        str(output_pdf),
        "--resource-path",
        str(resource_root),
        "--toc",
    ]
    subprocess.run(cmd, check=True)