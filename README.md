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
-   Table of contents support
-   Works as a CLI tool
-   Extensible (ordering, styling, metadata)

------------------------------------------------------------------------

## 🚀 Requirements

-   Python 3.13+
-   Pandoc
-   A PDF engine (BasicTeX recommended on macOS)

------------------------------------------------------------------------

## 📦 Installation

### Clone the repo

``` bash
git clone <your-repo-url>
cd obsidian2pdf
```

### Setup environment

``` bash
python3.13 -m venv .env
source .env/bin/activate
pip install --upgrade pip
```

### Install dependencies

``` bash
brew install pandoc
brew install --cask basictex
pip install python-frontmatter
pip install -e .
```

------------------------------------------------------------------------

## 🧪 Usage

``` bash
obsidian-pdf ./MyBook ./book.pdf
```

With options:

``` bash
obsidian-pdf ./MyBook ./book.pdf --toc --engine tectonic
```

------------------------------------------------------------------------

## 📁 Example Structure

```
    MyBook/ 
        ├─ 01-intro.md 
        ├─ 02-chapter.md 
        └─ images/ 
            └─ cover.png
```

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

-   Install pandoc if missing: brew install pandoc
-   Install pdflatex: brew install --cask basictex
-   Reinstall package: pip install -e .

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
