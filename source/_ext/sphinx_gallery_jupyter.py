#
# Copyright (c) 2020. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#
# Based on converter written by Sasank Chilamkurthy (sasankchilamkurthy@gmail.com).
#
# https://gist.github.com/chsasank/7218ca16f8d022e02a9c0deb94a310fe
#

'''
An Extension for translating Jupyter notebooks to appropriate python scripts for
Sphinx-Gallery.

To use it, you need to enable and configure the extension.


First, enable extension in the Sphinx conf.py file with:

extensions = [
    ...,
    'sphinx_gallery_jupyter',
]


Next, create your configuration dictionary sphinx_gallery_jupyter_conf.
Available parameters:

notebooks_dirs (str): Path to the directory with examples. Consists of
.ipynb and .py fileas along with previews with the same names in PNG format.

examples_dirs (str): Path to the directory with generated examples. It should
coinside with the value of examples_dirs parameter of Spihnx-Gallery.
'''

import os
from pathlib import Path
from shutil import copytree, rmtree, ignore_patterns
from json import load as json_load

from pypandoc import convert_text

def convert_ipynb_to_gallery(file_name, examples_dirs):
    '''
    Replace *.ipynb file by *.py that is compatible with sphinx_gallery extension.

    Based on converter written by Sasank Chilamkurthy (sasankchilamkurthy@gmail.com).
    '''
    python_file = ''
    nb_dict = json_load(open(file_name))
    cells = nb_dict['cells']
    for i, cell in enumerate(cells):
        if i == 0:
            if cell['cell_type'] == 'markdown':
                rst_source = convert_text(''.join(cell['source']), 'rst', 'md')
                python_file = '"""\n' + rst_source + '\n"""'
            else:
                name = os.path.splitext(os.path.basename(file_name))[0]
                name = name.replace('_', ' ').title()
                md_source = '# {0}\n\n'.format(name)
                rst_source = convert_text(md_source, 'rst', 'md')
                python_file = '"""\n' + rst_source + '\n"""' + \
                              '\n' * 2 + ''.join(cell['source']) + '\n\n#%%'
            preview_file = file_name.replace('.ipynb', '.png')
            if os.path.isfile(preview_file):
                preview_filename = examples_dirs + preview_file.split(examples_dirs)[-1]
                python_file += '\n\n# sphinx_gallery_thumbnail_path = "{0}"'.format(preview_filename)
        else:
            if cell['cell_type'] == 'markdown':
                if 'This page is available as' in ''.join(cell['source']):
                    continue
                rst_source = convert_text(''.join(cell['source']), 'rst', 'md')
                commented_source = '\n'.join(['# ' + x for x in rst_source.split('\n') if any(x)])
                python_file += '\n\n' + '# %% [markdown]\n#\n' + commented_source
            elif cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                python_file += '\n' * 2 + source
        if 0 < i and i < len(cells) - 1:
            python_file += '\n\n# %%'
    python_file = python_file.replace("\n%", "\n# %")
    file_path = Path(file_name)
    open('{0}/plot_{1}.py'.format(file_path.parent, file_path.stem), 'w').write(python_file)
    os.remove(file_name)

def prepare_sources(app, conf):
    '''
    Walk through notebooks_dirs and copy all files to examples_dirs as is except
    *.ipynb processed by convert_ipynb_to_gallery() function.
    '''
    src = os.path.join(app.confdir, conf['notebooks_dirs'])
    dst = os.path.join(app.confdir, conf['examples_dirs'])
    if os.path.isdir(dst):
        rmtree(dst)
    copytree(src, dst, ignore=ignore_patterns('.*'))
    for root, dirs, files in os.walk(dst):
        for filename in files:
            if filename.split('.')[-1] == 'ipynb':
                convert_ipynb_to_gallery(os.path.join(root, filename), conf['examples_dirs'])

def config_inited_handler(app, config):
    '''
    Read the extension configuration and run source preparation.
    '''
    DEFAULT_CONF = {
        'notebooks_dirs': '',
        'examples_dirs': '',
    }
    conf = {**DEFAULT_CONF, **config.sphinx_gallery_jupyter_conf}
    prepare_sources(app, conf)

def setup(app):
    app.add_config_value('sphinx_gallery_jupyter_conf', {}, 'html')
    app.connect('config-inited', config_inited_handler)
    return {
        'version': '0.2',
    }