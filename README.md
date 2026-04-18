# Kindle Series Manager — Documentation

[![Documentation Status](https://readthedocs.org/projects/kindle-series-manager/badge/?version=latest)](https://kindle-series-manager.readthedocs.io/en/latest/?badge=latest)

This repository contains the [Sphinx](https://www.sphinx-doc.org/) source files for the [Kindle Series Manager](https://github.com/mlapaglia/kindle-series-manager) documentation, hosted on [Read the Docs](https://kindle-series-manager.readthedocs.io/).

## Building Locally

Create a virtual environment and install dependencies:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r docs/requirements.txt
```

Build the HTML docs:

```bash
sphinx-build -b html docs/source docs/build/html
```

Then open `docs/build/html/index.html` in your browser.

## Project Structure

```
├── .readthedocs.yaml          # Read the Docs build configuration
├── docs/
│   ├── requirements.txt       # Python dependencies for RTD
│   └── source/
│       ├── conf.py            # Sphinx configuration
│       ├── index.md           # Landing page
│       ├── quickstart.md      # Installation & getting started
│       ├── series.md          # Series management
│       ├── goodreads.md       # Goodreads progress sync
│       ├── screensavers.md    # Custom screensavers
│       ├── cli.md             # Standalone CLI tool
│       └── backup.md          # Database backup/restore
```

## Contributing

Edit or add Markdown (`.md`) files in `docs/source/`. The docs use [MyST-Parser](https://myst-parser.readthedocs.io/) so you can use standard Markdown with Sphinx directives when needed. Build locally to preview, then open a pull request.

## License

This documentation is licensed under the same [Apache 2.0 License](https://github.com/mlapaglia/kindle-series-manager/blob/main/LICENSE) as the main project.
