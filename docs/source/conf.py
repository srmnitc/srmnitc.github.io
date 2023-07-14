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
    #'m2r2',
    #'sphinx_markdown_tables',
    #'nbsphinx',
    #"html_image", 
    #"html_admonition", 
    #"colon_fence", 
    "sphinx.ext.extlinks", 
    "sphinx.ext.intersphinx", 
    "sphinx.ext.todo", 
    "sphinx.ext.viewcode", 
    #"furo.sphinxext", 
    "myst_parser", 
    "sphinx_copybutton", 
    "sphinx_design", 
    "sphinx_inline_tabs"
]

#html_theme = 'furo'
html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False

#html_theme_options = {
#    'logo_only' : True,
#    'canonical_url' : 'https://calphy.readthedocs.io/',
#}

html_extra_path = ['_static/']
html_logo = "_static/logo_light.png"

source_suffix = ['.rst', '.md']
exclude_patterns = []
templates_path = ["_templates"]


html_theme_options = {
    # Disable showing the sidebar. Defaults to 'false'
    'nosidebar': True,
    "sidebar_hide_name": True,
    "show_prev_next": False,
    #"light_logo": "logo_light.png",
    #"dark_logo": "logo_dark.png",
}


#html_logo = "_static/logo.png"


