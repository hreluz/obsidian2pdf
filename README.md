# Obsidian to PDF (obsidian2pdf)

Convert an Obsidian folder (vault or subfolder) into a single PDF using
Python + Pandoc.

------------------------------------------------------------------------

## ✨ Features

-   Convert a folder of `.md` notes into one PDF
-   Supports basic Obsidian syntax:
    -   `![[image.png]]`
    -   `[[Wiki Links]]`
-   Automatic merging of notes
-   Optional table of contents (`--toc`)
-   Configurable PDF engine (`--engine`)
-   Verbose debugging mode (`--verbose`)
-   Frontmatter-based ordering (`order`)
-   Index-based ordering (`index.md`)
-   Works as a CLI tool

------------------------------------------------------------------------

## 🚀 Requirements

-   Python 3.13+
-   Pandoc
-   A PDF engine:
    -   macOS: BasicTeX (`pdflatex`)
    -   or alternatives like `tectonic`

------------------------------------------------------------------------

## 📦 Installation

``` bash
git clone <your-repo-url>
cd obsidian2pdf

python3.13 -m venv .env
source .env/bin/activate
pip install --upgrade pip

brew install pandoc
brew install --cask basictex

pip install python-frontmatter
pip install -e .
```

------------------------------------------------------------------------

## 🧪 Usage

### Basic

``` bash
obsidian-pdf ./MyBook ./book.pdf
```

### With Table of Contents

``` bash
obsidian-pdf ./MyBook ./book.pdf --toc
```

### With PDF engine

``` bash
obsidian-pdf ./MyBook ./book.pdf --engine pdflatex
```

or

``` bash
obsidian-pdf ./MyBook ./book.pdf --engine tectonic
```
### Verbose (debug mode)

``` bash
obsidian-pdf ./MyBook ./book.pdf --verbose
```

### Combined

``` bash
obsidian-pdf ./MyBook ./book.pdf --toc --engine tectonic --verbose
```

------------------------------------------------------------------------

## ⚙️ CLI Options

| Option      | Description                                      |
|-------------|--------------------------------------------------|
| `--toc`     | Generate a table of contents                     |
| `--engine`  | Choose PDF engine (`pdflatex`, `tectonic`)       |
| `--verbose` | Show detailed logs and debug information         |

------------------------------------------------------------------------

## 📁 Example Structure

```
    MyBook/
    ├─ index.md
    ├─ intro.md
    ├─ chapter.md
    ├─ summary.md
    └─ images/
        └─ cover.png

```

------------------------------------------------------------------------

## 📑 Ordering Notes

The order of your notes in the final PDF is determined using the following priority:

1. index.md (highest priority)
2. frontmatter (order)
3. filename (fallback)

---

### 🥇 1. Using index.md (Recommended)

If a file named `index.md` exists, it completely controls the order and content.

Example:

```md
# My Book

[[intro]]
[[chapter]]
[[summary]]
```

What happens:
- Notes appear in the exact order listed
- Only referenced notes are included
- Missing notes show warnings in verbose mode

---

### 🥈 2. Using frontmatter (order)

If index.md does not exist, ordering falls back to frontmatter.

```md
---
order: 1
title: Chapter One
---

Content here.
```

Rules:
- Lower number = earlier
- Missing order = goes last
- Same order = fallback to filename
- title overrides PDF heading

---

### 🥉 3. Filename ordering

If neither index.md nor frontmatter is used:

01-intro.md  
02-chapter.md  

Files are sorted alphabetically.

---

### 💡 Summary

index.md → full control (recommended)  
order → flexible control  
filename → simple fallback  

------------------------------------------------------------------------

## 🧠 How it works

Obsidian folder → Python → Pandoc → PDF

------------------------------------------------------------------------

## 🛠 Development

``` bash
PYTHONPATH=src python -m obsidian_pdf.cli ./MyBook ./book.pdf
```

------------------------------------------------------------------------

## 🐞 Troubleshooting

Install pandoc:

``` bash
brew install pandoc
```

Install PDF engine:

``` bash
brew install --cask basictex
```

or

``` bash
brew install tectonic
```

Reinstall project:

``` bash
pip install -e .
```

------------------------------------------------------------------------

## 📦 .gitignore

    __pycache__/
    *.py[cod]
    .venv/
    *.egg-info/
    build/
    dist/
    .DS_Store
    *.pdf

------------------------------------------------------------------------

## License

MIT
