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
-   Works as a CLI tool
-   Extensible (ordering, styling, metadata)

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
