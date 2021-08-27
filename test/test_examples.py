#!/usr/bin/env python

import os
import codecs
import warnings

from bs4 import BeautifulSoup

def test_examples():
    EXAMPLES_DIR = "source/examples"
    for root, directories, filenames in os.walk(EXAMPLES_DIR):
        if root[0] == "." or "/." in root or "\\." in root: # Skip hidden files
            continue
        for filename in filenames:
            if filename[0] == "." or not filename.split('.')[-1] == "ipynb":
                continue
            nb = os.path.join(root, filename)
            assert os.system("jupyter nbconvert --to notebook --inplace --execute {0}".format(nb)) == 0, \
                   "Notebook {0} could not be executed".format(nb)
            assert os.system("jupyter nbconvert --to html {0}".format(nb)) == 0, \
                   "Notebook {0} could not be converted into html format".format(nb)
            nb_html = nb.replace(".ipynb", ".html")
            check_plot_errors(nb, nb_html) # Check errors, but not all of them. Better way is to run JS, but in this case we need Selenium.
            os.remove(nb_html)

def check_plot_errors(nb, nb_html):
    with codecs.open(nb_html, 'r', 'utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        if next((s for s in soup.select('script[data-lets-plot-script="plot"]') if "__error_message" in str(s)), False):
            warnings.warn(UserWarning("Plot displaying error in {0}".format(nb)))