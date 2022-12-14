#!/usr/bin/env python

import re
import codecs
import warnings

import pytest
from bs4 import BeautifulSoup

from .generator import generate_pages

BUILD_DIR = "docs"

EXCEPTIONS = {
    'role': [
        "lets_plot.bistro.residual.residual_plot.html",
    ],
}

def _is_exception(exception, page):
    for p in EXCEPTIONS[exception]:
        if p in page:
            warnings.warn(UserWarning("Could be bad {0} in {1}".format(exception, page)))
            return True
    return False

@pytest.mark.parametrize(('page'), generate_pages(BUILD_DIR))
def test_source_footprints(page):
    with codecs.open(page, 'r', 'utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        for script in soup.select('script'):
            script.extract()
        body = str(soup.body)
        assert not re.search(r'\|([a-z]|-|_)+\|', body) # Bad substitutions
        assert not re.search(r'\. ([a-z]|-|_)+:', body) # Bad directives
        if not _is_exception('role', page):
            assert not re.search(r':([a-z]|-|_)+:', body) # Bad roles
        assert not re.search(r'&lt;http', body) # Bad external links
        for ref in soup.select('.std-ref'):
            assert ref.parent.name == 'a' # Bad internal link
        assert not re.search(r':mod:', body) # Bad internal links
        for ref in soup.select('code.py-mod'):
            if ref.parent.name != 'a':
                warnings.warn(UserWarning("Bad API reference in {0}".format(page))) # Bad API link
                break