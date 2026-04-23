from __future__ import annotations

import re
from pathlib import Path


EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def normalize_obsidian_markdown(text: str, current_file: Path, root_folder: Path) -> str:
    text = _replace_embeds(text, current_file, root_folder)
    text = _replace_wikilinks(text)
    return text


def _replace_embeds(text: str, current_file: Path, root_folder: Path) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()

        # Ignore size hints like image.png|300 if present
        target = target.split("|", 1)[0].strip()

        resolved = _find_asset(target, current_file, root_folder)
        if resolved is None:
            return f"**[Missing embed: {target}]**"

        rel = resolved.relative_to(root_folder).as_posix()
        return f"![]({rel})"

    return EMBED_RE.sub(repl, text)


def _replace_wikilinks(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        alias = match.group(2)
        return alias.strip() if alias else target

    return WIKILINK_RE.sub(repl, text)


def _find_asset(target: str, current_file: Path, root_folder: Path) -> Path | None:
    current_candidate = current_file.parent / target
    if current_candidate.exists():
        return current_candidate.resolve()

    for path in root_folder.rglob(target):
        if path.is_file():
            return path.resolve()

    return None