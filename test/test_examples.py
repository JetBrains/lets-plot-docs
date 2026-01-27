#!/usr/bin/env python

import os
import codecs
import json
import re

import pytest
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import lets_plot as lp

from .parser import notebook_parser
from .generator import generate_pages, generate_notebooks
from .lets_plot_errors import check_lets_plot_message_errors, check_warnings, check_copy_spec
from .test_links import check_url

EXCLUDED_PYTHON_NOTEBOOKS = []

BUILD_DIR = "docs"
SOURCE_DIR = "source"
PYTHON_NOTEBOOKS_DIR = "source/examples"
KOTLIN_NOTEBOOKS_DIR = "source/kotlin_examples"
EXTREF_CONF = "source/extref_conf.json"

LPK_DESCRIPTOR = os.getenv("lpk_descriptor")

python_notebook_paths = list(generate_notebooks(PYTHON_NOTEBOOKS_DIR, excluded_names=EXCLUDED_PYTHON_NOTEBOOKS))
kotlin_notebook_paths = list(generate_notebooks(KOTLIN_NOTEBOOKS_DIR))
notebook_paths = python_notebook_paths + kotlin_notebook_paths
extref_json = None
with open(EXTREF_CONF, 'r') as f:
    extref_json = json.load(f)

def paths_contains_name(paths, name):
    for path in paths:
        if path.endswith(name):
            return True
    return False

def generate_local_notebook_links(excluded_names=[]):
    for page in generate_pages(BUILD_DIR, excluded_names=excluded_names):
        with codecs.open(page, 'r', 'utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            for a in soup.find_all('a'):
                if not a.has_attr('href'):
                    continue
                href = a['href']
                if href.startswith("https://nbviewer.org/github/JetBrains") and href.split(".")[-1] == "ipynb":
                    yield page, a

def generate_local_notebook_refs():
    for page in generate_pages(SOURCE_DIR, extensions=["rst"]):
        with open(page, 'r', errors='ignore') as f:
            for nb_ref in re.findall(r' extref:: (.+)', f.read(), re.M):
                yield page, nb_ref

@pytest.mark.parametrize('notebook', notebook_paths)
def test_notebook_has_no_errors(notebook):
    check_version(notebook)
    lpk_descriptor = None if LPK_DESCRIPTOR == "" else LPK_DESCRIPTOR
    with notebook_parser(notebook, _to_html(notebook), lpk_descriptor) as (parser, parser_type):
        check_lets_plot_message_errors(parser, parser_type, notebook)
        check_copy_spec(parser, parser_type, notebook)
        check_warnings(parser, parser_type, notebook)

@pytest.mark.parametrize(('page', 'a'), generate_local_notebook_links(excluded_names=["whats_new"]))
def test_notebook_has_file(page, a):
    nb_name = a['href'].split('/')[-1]
    if nb_name.replace(".ipynb", "") in EXCLUDED_PYTHON_NOTEBOOKS:
        return
    assert paths_contains_name(python_notebook_paths, nb_name), "Notebook {1} from page {0} isn't presented in files".format(page, nb_name)

@pytest.mark.parametrize(('page', 'nb_ref'), generate_local_notebook_refs())
def test_notebook_ref_has_origin(page, nb_ref):
    assert nb_ref in extref_json.keys(), "Notebook {1} from page {0} isn't presented in extref conf".format(page, nb_name)
    nb_data = extref_json[nb_ref]
    nbv_ref = nb_data['ref'].get('nbviewer', None)
    if nbv_ref is not None and nbv_ref.startswith("https://nbviewer.org/github/JetBrains/lets-plot-docs"):
        nb_name = nbv_ref.split('/')[-1]
        if nb_name.replace(".ipynb", "") in EXCLUDED_PYTHON_NOTEBOOKS:
            return
        assert paths_contains_name(python_notebook_paths, nb_name), "Notebook {1} from page {0} isn't presented in files".format(page, nb_name)

def check_version(notebook):
    with open(notebook) as file:
        for line in file:
            if "%use lets-plot" in line:
                return
            if "from lets_plot import" in line:
                break
        for line in file:
            if "https://cdn.jsdelivr.net/gh/JetBrains/lets-plot" in line:
                match = re.search(r'lets-plot@v([0-9.]+)', line)
                version = match.group(1)
                assert lp.__version__ == version, "Version of Lets-Plot from the notebook {0} is too old: {1} instead of {2}".format(notebook, version, lp.__version__)
                return

def _to_html(path):
    html_path = None
    if path.startswith("source/examples/") and path.endswith(".ipynb"):
        html_path = "docs/{0}.html".format(path[7:-6])
        if not os.path.isfile(html_path):
            html_path = None
    return html_path