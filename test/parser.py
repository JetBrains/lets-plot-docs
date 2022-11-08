#!/usr/bin/env python

import os
import subprocess
import codecs
import warnings

from bs4 import BeautifulSoup
from selenium import webdriver

TIMEOUT = 3 * 60 # per subprocess in seconds

class page_parser():

    def __init__(self, page):
        self.page = page

    def __enter__(self):
        self.driver = None
        try:
            self.driver = webdriver.Chrome()
            self.driver.get("file:///{0}".format(os.path.abspath(self.page)))
            return self.driver, 'driver'
        except Exception as e:
            self._close_driver()
            warnings.warn(UserWarning(e))
            with codecs.open(self.page, 'r', 'utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                return soup, 'soup'

    def __exit__(self, type, value, traceback):
        self._close_driver()

    def _close_driver(self):
        if self.driver:
            self.driver.close()

class notebook_parser(page_parser):

    def __init__(self, notebook):
        self.notebook = notebook
        self.page = notebook.replace(".ipynb", ".html")

    def __enter__(self):
        subprocess.check_output("jupyter nbconvert --to notebook --inplace --execute {0}".format(self.notebook), \
                                shell=True, timeout=TIMEOUT)
        subprocess.check_output("jupyter nbconvert --to html {0}".format(self.notebook), \
                                shell=True, timeout=TIMEOUT)
        return super().__enter__()

    def __exit__(self, type, value, traceback):
        super().__exit__(type, value, traceback)
        os.remove(self.page)