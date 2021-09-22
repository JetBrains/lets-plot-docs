#!/usr/bin/env python

import os

def generate_pages(dir, extensions=['html']):
    for root, directories, filenames in os.walk(dir):
        for filename in filenames:
            if filename.split('.')[-1] in extensions:
                yield os.path.join(root, filename)