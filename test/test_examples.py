#!/usr/bin/env python

import os
import codecs
import warnings

import pytest
from bs4 import BeautifulSoup
from selenium import webdriver

def generate_notebooks():
    EXAMPLES_DIR = "source/examples"
    for root, directories, filenames in os.walk(EXAMPLES_DIR):
        if root[0] == "." or "/." in root or "\\." in root: # Skip hidden files
            continue
        for filename in filenames:
            if filename[0] != "." and filename.split('.')[-1] == "ipynb":
                yield os.path.join(root, filename)

class notebook_parser():

    def __init__(self, notebook):
        self.notebook = notebook
        self.page = notebook.replace(".ipynb", ".html")

    def __enter__(self):
        assert os.system("jupyter nbconvert --to notebook --inplace --execute {0}".format(self.notebook)) == 0, \
               "Notebook {0} could not be executed".format(self.notebook)
        assert os.system("jupyter nbconvert --to html {0}".format(self.notebook)) == 0, \
               "Notebook {0} could not be converted into html format".format(self.notebook)
        self.driver = None
        try:
            self.driver = webdriver.Chrome()
            self.driver.get("file:///{0}".format(os.path.abspath(self.page)))
            return self.driver, 'driver'
        except Exception:
            warnings.warn(UserWarning("Something went wrong with chromedriver. Please check https://chromedriver.chromium.org"))
            with codecs.open(self.page, 'r', 'utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                return soup, 'soup'

    def __exit__(self, type, value, traceback):
        if self.driver:
            self.driver.close()
        os.remove(self.page)

@pytest.mark.parametrize('notebook', generate_notebooks())
def test_notebook(notebook):
    with notebook_parser(notebook) as (parser, parser_type):
        if parser_type == 'driver':
            if len(parser.find_elements_by_css_selector('.lets-plot-message-error')) > 0:
                warnings.warn(UserWarning("Plot displaying error in {0}".format(notebook)))
        else:
            assert parser_type == 'soup'
            if next((s for s in parser.select('script[data-lets-plot-script="plot"]') if "__error_message" in str(s)), False):
                warnings.warn(UserWarning("Plot displaying error in {0}".format(notebook)))