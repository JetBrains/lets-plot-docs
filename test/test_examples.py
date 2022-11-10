#!/usr/bin/env python

import os

import pytest

from .parser import notebook_parser
from .lets_plot_errors import check_lets_plot_message_errors, check_warnings

def generate_notebooks():
    EXAMPLES_DIR = "source/examples"
    for root, directories, filenames in os.walk(EXAMPLES_DIR):
        if root[0] == "." or "/." in root or "\\." in root: # Skip hidden files
            continue
        for filename in filenames:
            if filename[0] != "." and filename.split('.')[-1] == "ipynb":
                yield os.path.join(root, filename)

@pytest.mark.parametrize('notebook', generate_notebooks())
def test_notebook(notebook):
    with notebook_parser(notebook) as (parser, parser_type):
        check_lets_plot_message_errors(parser, parser_type, notebook)
        check_warnings(parser, parser_type, notebook)