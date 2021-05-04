#!/usr/bin/env python

import argparse
import os
import re

import pypandoc

DEFAULT_OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', 'source', '_shared', 'index_body.rst'
)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Path to the README_PYTHON.md document.')
parser.add_argument('-o', '--output', required=False, default=DEFAULT_OUTPUT_PATH, help='Path to the index_body.rst document that included into the main page - index.rst.')
args = parser.parse_args()

input_text = ''
with open(args.input, encoding='utf8') as f:
    input_text = f.read()
    input_text = re.sub(r'\n<table>.+</table>\n', '', input_text, flags=re.DOTALL)
    input_text = re.sub(r'\n-\s*\[License\]\(#license\)', '', input_text, flags=re.DOTALL)
    input_text = re.sub(r'\n<a id="license">.+', '', input_text, flags=re.DOTALL)

assert pypandoc.convert_text(input_text, format='gfm', to='rst', outputfile=args.output) == ''