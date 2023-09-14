#!/usr/bin/env python

import os

def _is_hidden_path(path):
    return path[0] == "." or "/." in path or "\\." in path

def _is_hidden_file(filename):
    return filename[0] == "."

def generate_notebooks(path):
    for root, directories, filenames in os.walk(path):
        if _is_hidden_path(root):
            continue
        for filename in filenames:
            if not _is_hidden_file(filename) and filename.split('.')[-1] == "ipynb":
                yield os.path.join(root, filename)

def generate_pages(path, extensions=['html'], excluded_names=[], kotlin=False):
    for root, directories, filenames in os.walk(path):
        if _is_hidden_path(root):
            continue
        if not kotlin and os.path.join(path, 'kotlin') in root:
            continue
        for filename in filenames:
            if not _is_hidden_file(filename) and filename.split('.')[-1] in extensions and os.path.splitext(filename)[0] not in excluded_names:
                yield os.path.join(root, filename)