#!/usr/bin/env python

import os

def _is_hidden_path(path):
    return path[0] == "." or "/." in path or "\\." in path

def _is_hidden_file(filename):
    return filename[0] == "."

def generate_notebooks(path, included_names=None, excluded_names=[]):
    for root, directories, filenames in os.walk(path):
        if _is_hidden_path(root):
            continue
        for filename in filenames:
            visible = not _is_hidden_file(filename)
            is_notebook = filename.split('.')[-1] == "ipynb"
            pass_filters = included_names is None or os.path.splitext(filename)[0] in included_names and \
                           os.path.splitext(filename)[0] not in excluded_names
            if visible and is_notebook and pass_filters:
                yield os.path.join(root, filename)

def generate_pages(path, extensions=['html'], included_names=None, excluded_names=[], kotlin=False):
    for root, directories, filenames in os.walk(path):
        if _is_hidden_path(root):
            continue
        if not kotlin and os.path.join(path, 'kotlin') in root:
            continue
        for filename in filenames:
            pass_filters = (included_names is None or os.path.splitext(filename)[0] in included_names) and \
                           os.path.splitext(filename)[0] not in excluded_names
            if not _is_hidden_file(filename) and filename.split('.')[-1] in extensions and pass_filters:
                yield os.path.join(root, filename)