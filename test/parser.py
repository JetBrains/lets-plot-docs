#!/usr/bin/env python

import os
import subprocess
import warnings

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HEADLESS = True # for Selenium webdriver
TIMEOUT = 3 * 60 # `jupyter nbconvert` timeout: per subprocess in seconds

class page_parser():

    def __init__(self, page):
        self.page = page

    def __enter__(self):
        self.driver = None
        try:
            driver_options = Options()
            driver_options.add_argument("--start-maximized")
            if HEADLESS:
                driver_options.add_argument("--headless=new")
            self.driver = webdriver.Chrome(options=driver_options)
            self.driver.get("file:///{0}".format(os.path.abspath(self.page)))
            return self.driver, 'driver'
        except Exception as e:
            self._close_driver()
            warnings.warn(UserWarning(e))
            with open(self.page, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                return soup, 'soup'

    def __exit__(self, type, value, traceback):
        self._close_driver()

    def _close_driver(self):
        if self.driver:
            self.driver.close()

class notebook_parser(page_parser):
    import re

    def __init__(self, notebook, page, lpk_descriptor):
        self.notebook = notebook
        self.lpk_descriptor = lpk_descriptor
        self.page = page or notebook.replace(".ipynb", ".html")
        self.prepare_page = page is None

    def __enter__(self):
        if self.prepare_page:
            self._update_descriptors(revert=False)
            subprocess.check_output("jupyter nbconvert --to html --execute {0}".format(self.notebook),
                                    shell=True, timeout=TIMEOUT)
        return super().__enter__()

    def __exit__(self, type, value, traceback):
        super().__exit__(type, value, traceback)
        if self.prepare_page:
            os.remove(self.page)
            self._update_descriptors(revert=True)

    def _update_descriptors(self, *, revert):
        if self.lpk_descriptor is None:
            return

        if revert:
            search_lp_descriptor = '%use lets-plot@.+"'
            from_lp_descriptor = "%use lets-plot@{0}".format(self.lpk_descriptor)
            to_lp_descriptor = "%use lets-plot"
            search_lpgt_descriptor = '%use lets-plot-gt@.+"'
            from_lpgt_descriptor = "%use lets-plot-gt@{0}".format(self.lpk_descriptor.replace("lets-plot.json", "lets-plot-gt.json"))
            to_lpgt_descriptor = "%use lets-plot-gt"
        else:
            search_lp_descriptor = '%use lets-plot[^-]*"'
            from_lp_descriptor = "%use lets-plot"
            to_lp_descriptor = "%use lets-plot@{0}".format(self.lpk_descriptor)
            search_lpgt_descriptor = "%use lets-plot-gt"
            from_lpgt_descriptor = "%use lets-plot-gt"
            to_lpgt_descriptor = "%use lets-plot-gt@{0}".format(self.lpk_descriptor.replace("lets-plot.json", "lets-plot-gt.json"))

        self._replace_descriptors(search_lp_descriptor, from_lp_descriptor, to_lp_descriptor,
                                  search_lpgt_descriptor, from_lpgt_descriptor, to_lpgt_descriptor)

    def _replace_descriptors(self, search_lp_descriptor, from_lp_descriptor, to_lp_descriptor,
                                   search_lpgt_descriptor, from_lpgt_descriptor, to_lpgt_descriptor):
        lp_descriptor_is_replaced = False
        lpgt_descriptor_is_replaced = False
        with open(self.notebook, 'r') as file:
            data = []
            for line in file.readlines():
                line, lp_descriptor_is_replaced = self._update_descriptor_line(line, lp_descriptor_is_replaced, \
                                                                               search_lp_descriptor, \
                                                                               from_lp_descriptor, to_lp_descriptor)
                line, lpgt_descriptor_is_replaced = self._update_descriptor_line(line, lpgt_descriptor_is_replaced, \
                                                                                 search_lpgt_descriptor, \
                                                                                 from_lpgt_descriptor, to_lpgt_descriptor)
                data.append(line)
        with open(self.notebook, 'w') as file:
            file.writelines(data)

    def _update_descriptor_line(self, line, descriptor_is_replaced, search_descriptor, from_descriptor, to_descriptor):
        if descriptor_is_replaced or self.re.search(search_descriptor, line) is None:
            return line, False
        return line.replace(from_descriptor, to_descriptor), True