from __future__ import annotations

from pathlib import Path

from .obsidian import normalize_obsidian_markdown


def collect_markdown_files(folder: Path) -> list[Path]:
    return sorted(
        [p for p in folder.rglob("*.md") if p.is_file()],
        key=lambda p: str(p.relative_to(folder)).lower(),
    )


def build_merged_markdown(folder: Path, verbose: bool = False) -> str:
    md_files = collect_markdown_files(folder)

    if verbose:
        print(f"[INFO] Found {len(md_files)} markdown file(s)")
        for md_file in md_files:
            print(f"[INFO]  - {md_file.relative_to(folder)}")

    chunks: list[str] = []

    for md_file in md_files:
        if verbose:
            print(f"[INFO] Processing: {md_file.relative_to(folder)}")

        raw = md_file.read_text(encoding="utf-8")
        normalized = normalize_obsidian_markdown(raw, md_file, folder)

        title = md_file.stem.replace("-", " ").replace("_", " ")
        chunks.append(f"# {title}\n\n{normalized.strip()}\n")

    return "\n\n\\newpage\n\n".join(chunks)