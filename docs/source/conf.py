# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import shutil
import glob

def skip(app, what, name, obj, would_skip, options):
    if name in ( '__init__',):
        return False
    return would_skip
def setup(app):
    app.connect('autodoc-skip-member', skip)

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sarathmenon.me'
copyright = '2022, Sarath Menon'
author = 'Sarath Menon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'm2r2',
    'sphinx_markdown_tables',
    'nbsphinx',
]

html_theme = 'furo'

#html_logo = "../_static/calphy_logo.png"
#html_theme_options = {
#    'logo_only' : True,
#    'canonical_url' : 'https://calphy.readthedocs.io/',
#}

html_extra_path = ['../_static' ]
source_suffix = ['.rst', '.md']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
