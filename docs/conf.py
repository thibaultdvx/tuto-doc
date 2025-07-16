# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "NeuroPlot"
copyright = "2025, ARAMIS Lab"
author = "ARAMIS Lab"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_gallery.gen_gallery",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_inherit_docstrings = False

napoleon_custom_sections = [("Returns", "params_style")]

intersphinx_mapping = {
    "matplotlib": ("https://matplotlib.org/stable/", None),
}

from pathlib import Path

sphinx_gallery_conf = {
    "examples_dirs": "../examples",
    "gallery_dirs": "auto_examples",
    "backreferences_dir": Path("api", "generated"),  # where mini-galleries are stored
    "doc_module": (
        "neuroplot",
    ),  # generate mini-galleries for all the objects in clinicadl
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = "NeuroPlot"
html_logo = "_static/logos/logo_ARAMISLAB_rvb.png"
html_static_path = ["_static"]
