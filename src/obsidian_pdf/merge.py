from __future__ import annotations

import re
from pathlib import Path

import frontmatter

from .obsidian import normalize_obsidian_markdown


WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def collect_markdown_files(folder: Path) -> list[Path]:
    return [p for p in folder.rglob("*.md") if p.is_file()]


def find_note_by_name(folder: Path, note_name: str) -> Path | None:
    note_name = note_name.strip()

    if note_name.endswith(".md"):
        candidates = [note_name]
    else:
        candidates = [f"{note_name}.md", note_name]

    for candidate in candidates:
        direct = folder / candidate
        if direct.exists() and direct.is_file():
            return direct

    for path in folder.rglob("*.md"):
        if path.stem == note_name or path.name == note_name:
            return path

    return None


def extract_index_order(folder: Path, verbose: bool = False) -> list[Path] | None:
    index_file = folder / "index.md"

    if not index_file.exists():
        return None

    text = index_file.read_text(encoding="utf-8")
    note_names = WIKILINK_RE.findall(text)

    ordered_files: list[Path] = []

    for note_name in note_names:
        note_path = find_note_by_name(folder, note_name)
        if note_path is None:
            if verbose:
                print(f"[WARN] index.md references missing note: {note_name}")
            continue

        if note_path.name == "index.md":
            continue

        ordered_files.append(note_path)

    if verbose:
        print("[INFO] Using index.md ordering")
        for file in ordered_files:
            print(f"[INFO]  - {file.relative_to(folder)}")

    return ordered_files


def sort_files_by_frontmatter(md_files: list[Path], folder: Path, verbose: bool) -> list[Path]:
    def get_order(file: Path):
        try:
            post = frontmatter.load(file)
            return post.metadata.get("order", 999)
        except Exception:
            return 999

    sorted_files = sorted(
        md_files,
        key=lambda f: (get_order(f), str(f.relative_to(folder)).lower()),
    )

    if verbose:
        print("[INFO] Using frontmatter/filename ordering")
        for file in sorted_files:
            try:
                post = frontmatter.load(file)
                order = post.metadata.get("order", "N/A")
            except Exception:
                order = "N/A"

            print(f"[INFO]  order={order} -> {file.relative_to(folder)}")

    return sorted_files


def get_ordered_files(folder: Path, verbose: bool = False) -> list[Path]:
    index_order = extract_index_order(folder, verbose)

    if index_order is not None:
        return index_order

    md_files = collect_markdown_files(folder)
    md_files = [file for file in md_files if file.name != "index.md"]

    return sort_files_by_frontmatter(md_files, folder, verbose)


def build_merged_markdown(folder: Path, verbose: bool = False) -> str:
    md_files = get_ordered_files(folder, verbose)

    if verbose:
        print(f"[INFO] Final file count: {len(md_files)}")

    chunks: list[str] = []

    for md_file in md_files:
        if verbose:
            print(f"[INFO] Processing: {md_file.relative_to(folder)}")

        post = frontmatter.load(md_file)

        content = normalize_obsidian_markdown(
            post.content,
            md_file,
            folder,
        )

        title = post.metadata.get(
            "title",
            md_file.stem.replace("-", " ").replace("_", " "),
        )

        chunks.append(f"# {title}\n\n{content.strip()}\n")

    return "\n\n\\newpage\n\n".join(chunks)