from __future__ import annotations

from pathlib import Path

from .obsidian import normalize_obsidian_markdown


def collect_markdown_files(folder: Path) -> list[Path]:
    return sorted(
        [p for p in folder.rglob("*.md") if p.is_file()],
        key=lambda p: str(p.relative_to(folder)).lower(),
    )


def build_merged_markdown(folder: Path) -> str:
    chunks: list[str] = []

    for md_file in collect_markdown_files(folder):
        raw = md_file.read_text(encoding="utf-8")
        normalized = normalize_obsidian_markdown(raw, md_file, folder)

        title = md_file.stem.replace("-", " ").replace("_", " ")
        chunks.append(f"# {title}\n\n{normalized.strip()}\n")

    return "\n\n\\newpage\n\n".join(chunks)