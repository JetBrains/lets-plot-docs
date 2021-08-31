#!/usr/bin/env python

import os
import codecs
import warnings

import pytest
import requests
from bs4 import BeautifulSoup

external_links = set()

def generate_pages():
    BUILD_DIR = "docs"
    for root, directories, filenames in os.walk(BUILD_DIR):
        for filename in filenames:
            if filename.split('.')[-1] == "html":
                yield root, filename

@pytest.mark.parametrize(('root', 'filename'), generate_pages())
def test_links(root, filename):
    page = os.path.join(root, filename)
    with codecs.open(page, 'r', 'utf-8') as index:
        soup = BeautifulSoup(index, 'html.parser')
        for a in soup.find_all('a'):
            classes = a['class'] if a.has_attr('class') else []
            href = a['href']
            message = "\nPage: {0}\nHREF: {1}".format(page, href)
            assert href, "Wrong 'href' attribute"
            assert href != "", "Wrong 'href' attribute"
            if href == "#": # Not a link actually
                continue
            if not classes: # Bad case for checking
                continue
            if "internal" in classes:
                if href[0] == "#": # Link to a section
                    assert soup.find(id=href[1:]), message
                else: # Link to another page of the documentation
                    assert os.path.isfile(os.path.join(root, href.split("#")[0])), message
            elif "external" in classes: # Link to an external resource
                check_external_link(href, message)
            else: # Home or header link
                assert "headerlink" in classes or "navbar-brand" in classes, "Wrong 'class' attribute"

def check_external_link(href, message):
    SKIP = ["http://my.tile.com"]
    if href in external_links:
        return
    external_links.add(href)
    try:
        response = requests.get(href)
    except requests.exceptions.ConnectionError:
        assert href in SKIP
        return
    assert response.status_code != 404, message
    if response.status_code == 200:
        return
    warnings.warn(UserWarning("{0}\nStatus code: {1}".format(message, response.status_code)))