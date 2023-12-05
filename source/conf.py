# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('./ext'))


# -- Project information -----------------------------------------------------

project = 'lets-plot'
copyright = '2021, JetBrains'
author = 'JetBrains'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    "sphinx_design",
    'jupyter_sphinx',
    'create_cname',
    'extref',
    'switch_lets_plot',
]

cname_url = "lets-plot.org"

extref_conf = "extref_conf.json"
extref_logo_images = {
    'colab': "_static/images/logo/colab.svg",
    'datalore': "_static/images/logo/datalore.svg",
    'dataspell': "_static/images/logo/dataspell.png",
    'deepnote': "_static/images/logo/deepnote.svg",
    'kaggle': "_static/images/logo/kaggle.svg",
    'nbviewer': "_static/images/logo/jupyter.svg",
    'nextjournal': "_static/images/logo/nextjournal.svg",
    'pycharm': "_static/images/logo/pycharm.svg",
}
extref_default_image = 'square'

autodoc_default_options = {
    'member-order': 'bysource',
}

autosummary_generate = True

numpydoc_show_class_members = False


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import lets_plot
version = lets_plot.__version__
# The full version, including alpha/beta/rc tags.
release = lets_plot.__version__


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_show_sourcelink = False
html_title = ""

html_theme_options = {
    "logo": {
        "text": "Lets-Plot v{0}".format(version),
        "image_light": "_static/lets-plot-light.svg",
        "image_dark": "_static/lets-plot-dark.svg",
    },
    "header_links_before_dropdown": 1,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/JetBrains/lets-plot",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/lets-plot",
            "icon": "_static/images/logo/pypi.svg",
            "type": "local",
        },
    ],
    "show_prev_next": False,
}

html_context = {
    'cur_year': datetime.now().year,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    'css/dataframe.css',
]
html_js_files = [
    'js/custom.js',
    'js/language_data.js',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    # Default to no sidebar
    '**': [],
}