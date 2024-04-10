#!/usr/bin/env python

import os
import codecs
import json
import re

import pytest
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from .parser import notebook_parser
from .generator import generate_pages, generate_notebooks
from .lets_plot_errors import check_lets_plot_message_errors, check_warnings
from .test_links import check_url

BUILD_DIR = "docs"
SOURCE_DIR = "source"
NOTEBOOKS_DIR = "source/examples"
EXTREF_CONF = "source/extref_conf.json"

notebook_paths = list(generate_notebooks(NOTEBOOKS_DIR))
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
    with notebook_parser(notebook) as (parser, parser_type):
        check_lets_plot_message_errors(parser, parser_type, notebook)
        _check_links(parser, parser_type, notebook)
        check_warnings(parser, parser_type, notebook)

@pytest.mark.parametrize(('page', 'a'), generate_local_notebook_links(excluded_names=["whats_new"]))
def test_notebook_has_file(page, a):
    nb_name = a['href'].split('/')[-1]
    assert paths_contains_name(notebook_paths, nb_name), "Notebook {1} from page {0} isn't presented in files".format(page, nb_name)

@pytest.mark.parametrize(('page', 'nb_ref'), generate_local_notebook_refs())
def test_notebook_ref_has_origin(page, nb_ref):
    assert nb_ref in extref_json.keys(), "Notebook {1} from page {0} isn't presented in extref conf".format(page, nb_name)
    nb_data = extref_json[nb_ref]
    nbv_ref = nb_data['ref'].get('nbviewer', None)
    if nbv_ref is not None and nbv_ref.startswith("https://nbviewer.org/github/JetBrains/lets-plot-docs"):
        nb_name = nbv_ref.split('/')[-1]
        assert paths_contains_name(notebook_paths, nb_name), "Notebook {1} from page {0} isn't presented in files".format(page, nb_name)

def _check_links(parser, parser_type, source):
    if parser_type == 'driver':
        for a in parser.find_elements(By.CSS_SELECTOR, 'a'):
            _check_href(a.get_attribute('href'), source)
    elif parser_type == 'soup':
        for a in parser.find_all('a'):
            _check_href(a['href'], source)
    else:
        raise ValueError("Bad parser type: {0}".format(parser_type))

def _check_href(href, source):
    if href is None or href == "":
        return
    if href.startswith("#") or href.startswith("file:"):
        return
    check_url(href, source)