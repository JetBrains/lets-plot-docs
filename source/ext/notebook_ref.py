#
# Copyright (c) 2021. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

from docutils import nodes
from docutils.parsers.rst import Directive

class NotebookRefDirective(Directive):
    def run(self):
        node = nodes.raw('', '<span>TODO</span>', format='html')
        return [node]

def config_inited_handler(app, config):
    if not config.notebook_ref_conf:
        raise ValueError("Parameter notebook_ref_conf could not be empty")

def setup(app):
    app.add_config_value('notebook_ref_conf', None, 'html')

    app.add_directive('notebook-ref', NotebookRefDirective)

    app.connect('config-inited', config_inited_handler)

    return {
        'version': '0.1',
    }