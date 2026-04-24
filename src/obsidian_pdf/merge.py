from __future__ import annotations

from pathlib import Path
import frontmatter

from .obsidian import normalize_obsidian_markdown


def collect_markdown_files(folder: Path) -> list[Path]:
    return [p for p in folder.rglob("*.md") if p.is_file()]


def sort_files(md_files: list[Path], folder: Path, verbose: bool) -> list[Path]:
    def get_order(file: Path):
        try:
            post = frontmatter.load(file)
            order = post.metadata.get("order", 999)
            return order
        except Exception:
            return 999

    sorted_files = sorted(md_files, key=lambda f: (get_order(f), str(f)))

    if verbose:
        print("[INFO] File order after frontmatter sorting:")
        for f in sorted_files:
            try:
                post = frontmatter.load(f)
                order = post.metadata.get("order", "N/A")
            except Exception:
                order = "N/A"

            print(f"[INFO]  order={order} → {f.relative_to(folder)}")

    return sorted_files


def build_merged_markdown(folder: Path, verbose: bool = False) -> str:
    md_files = collect_markdown_files(folder)

    if verbose:
        print(f"[INFO] Found {len(md_files)} markdown file(s)")

    md_files = sort_files(md_files, folder, verbose)

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