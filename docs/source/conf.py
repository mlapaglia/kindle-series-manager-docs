project = "Kindle Series Manager"
copyright = "2026, Matt LaPaglia"
author = "Matt LaPaglia"

version = "0.2.0"
release = "0.2.0"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = []

language = "en"

html_theme = "furo"
html_static_path = ["_static"]

html_theme_options = {
    "source_repository": "https://github.com/mlapaglia/kindle-series-manager",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
