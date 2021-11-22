#!/usr/bin/env python

import os

def generate_pages(dir, extensions=['html'], kotlin=False):
    for root, directories, filenames in os.walk(dir):
        for filename in filenames:
            if not kotlin and os.path.join(dir, 'kotlin') in root:
                continue
            if filename.split('.')[-1] in extensions:
                yield os.path.join(root, filename)