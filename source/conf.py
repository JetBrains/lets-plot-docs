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
import json
sys.path.insert(0, os.path.abspath('./ext'))


# -- Project information -----------------------------------------------------

project = 'lets-plot'
author = 'JetBrains'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # built in extensions
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    # installed extensions
    "jupyter_sphinx",
    "notfound.extension",
    "numpydoc",
    "sphinxext.opengraph",
    "sphinx_design",
    "sphinx_reredirects",
    # custom extensions
    "create_cname",
    "extref",
    "switch_lets_plot",
]

# -- Sphinx own configuration ------------------------------------------------

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

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    'css/colors.css',
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


# ----------------------------------------------------------------------------
# -- Built in extensions -----------------------------------------------------
# ----------------------------------------------------------------------------

# -- Autosummary extension ---------------------------------------------------

autodoc_default_options = {
    'member-order': 'bysource',
}
autosummary_generate = True


# ----------------------------------------------------------------------------
# -- Installed extensions ----------------------------------------------------
# ----------------------------------------------------------------------------

# -- Built in theme and PyData Sphinx theme extension ------------------------

html_theme = "pydata_sphinx_theme"
html_show_sourcelink = False
html_title = ""
html_favicon = "_static/favicon.ico"
html_context = {
    'cur_year': datetime.now().year,
    'python_root_doc': "python/index",
    'python_root_name': "Lets-Plot for Python",
}
html_theme_options = {
    "logo": {
        "alt_text": "Lets-Plot",
        "image_light": "_static/logo-light.svg",
        "image_dark": "_static/logo-dark.svg",
        "version_link": "python/pages/whats_new",
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
            "attributes": {"excluded_from": ["index"]},
        },
    ],
    "show_prev_next": False,
    "navbar_start": ["navbar-logo", "navbar-version"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "article_header_start": [],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-and-theme-version"],
    "footer_end": ["terms"],
    "secondary_sidebar_items": {
        "**": ["page-toc", "sourcelink"],
        "index": [],
    },
}

# -- Not found (404) extension -----------------------------------------------

notfound_context = {
    'title': "Page not found",
    'body': """
<h1>Page not found</h1>
<p>
  Unfortunately we couldn't find the content you were looking for.
</p>
<p>
  <a class="sd-sphinx-override sd-btn sd-text-wrap sd-btn-primary reference internal" href="index.html">Take me back to the homepage</a>
</p>""",
}
notfound_urls_prefix = None

# -- Numpydoc extension ------------------------------------------------------

numpydoc_show_class_members = False

# -- OpenGraph extension -----------------------------------------------------

ogp_site_url = "https://lets-plot.org/"
ogp_site_name = "Lets-Plot"
ogp_image = "_static/images/open-graph.png"

# -- Sphinx redirects extension ----------------------------------------------

redirects_conf = open("redirects.json")
redirects = dict(json.load(redirects_conf))
redirect_html_template_file = "_templates/redirect.html.template"


# ----------------------------------------------------------------------------
# -- Custom extensions -------------------------------------------------------
# ----------------------------------------------------------------------------

# -- CNAME generator (extension) ---------------------------------------------

cname_url = "lets-plot.org"

# -- Examples references manager (extension) ---------------------------------

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
extref_class = "extref"