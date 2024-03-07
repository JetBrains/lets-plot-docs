#!/usr/bin/env python

import os
import codecs
import warnings

import pytest
import requests
from bs4 import BeautifulSoup

from .generator import generate_pages

BUILD_DIR = "docs"
SKIP = ["http://my.tile.com"]
REPLACE_LP_TO_FORK = True
REPLACE_TO_BRANCH = "dev"
REPLACES = {
    "lets-plot.org": "asmirnov-horis.github.io/lets-plot-docs",
    "nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples": "nbviewer.org/github/ASmirnov-HORIS/lets-plot-docs/blob/{0}/source/examples".format(REPLACE_TO_BRANCH),
}

checked_external_links = set()

def generate_links():
    for page in generate_pages(BUILD_DIR):
        with codecs.open(page, 'r', 'utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            for a in soup.find_all('a'):
                yield page, a

@pytest.mark.parametrize(('page', 'a'), generate_links())
def test_link(page, a):
    classes = a['class'] if a.has_attr('class') else []
    href = a['href']
    assert href, "Wrong 'href' attribute"
    assert href != "", "Wrong 'href' attribute"
    if href == "#": # Not a link actually
        return
    if href[0] == "#":
        if classes == ["headerlink"]: # Headerlink
            return
        if classes == ["skip-link"]: # Skip link
            return
    if not classes: # Bad case for checking
        return
    if "internal" in classes or "nav-internal" in classes:
        check_section(page, href) if href[0] == "#" else check_page(page, href)
    elif "external" in classes or "nav-external" in classes:
        check_external_link(href)
    else: # Home or header link
        assert "navbar-brand" in classes or "nav-link" in classes, "Wrong 'class' attribute"

def check_section(page, href):
    with codecs.open(page, 'r', 'utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        assert soup.find(id=href[1:])

def check_page(page, href):
    assert os.path.isfile(os.path.join(os.path.dirname(page), href.split("#")[0]))

def check_external_link(href):
    if href in checked_external_links:
        return
    checked_external_links.add(href)
    response = get_response(href)
    if response is None:
        return
    assert response.status_code != 404
    if response.status_code == 200:
        return
    warnings.warn(UserWarning("Status code {0} for href={1}".format(response.status_code, href)))

def get_response(href, first_query=True):
    try:
        response = requests.get(href)
        if response.status_code == 404 and REPLACE_LP_TO_FORK and first_query:
            for replace_from, replace_to in REPLACES.items():
                href = href.replace(replace_from, replace_to)
            response = get_response(href, False)
        return response
    except requests.exceptions.ConnectionError:
        assert href in SKIP
        return None