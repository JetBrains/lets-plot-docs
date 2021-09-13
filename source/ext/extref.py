#
# Copyright (c) 2021. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import os
import json
import shutil

from docutils import nodes
from docutils.parsers.rst import Directive, directives

REF_TYPES = ('image', 'text')

class ExtRefDirective(Directive):
    has_content = True
    option_spec = {
        'type': lambda t: directives.choice(t, REF_TYPES),
        'ref': directives.unchanged,
        'url': directives.uri,
        'image': directives.unchanged,
        'text': directives.unchanged,
    }

    def run(self):
        return [nodes.raw(
            "",
            '<a class="{0}" href="{1}" target="_blank">{2}</a>'.format(self._class(), self._href(), self._content()),
            format='html'
        )]

    def _env(self):
        return self.state.document.settings.env

    def _conf(self):
        return self._env().config['extref_conf'][self.content[0]]

    def _type(self):
        if 'type' in self.options.keys():
            return self.options['type']
        return self._env().config['extref_default_type']

    def _href(self):
        if 'url' in self.options.keys():
            return self.options['url']
        ref_conf = self._conf()['ref']
        if 'ref' in self.options.keys():
            return ref_conf[self.options['ref']]
        return ref_conf[list(ref_conf)[0]]

    def _class(self):
        if self._type() == 'image':
            return "reference external image-reference"
        else:
            return "reference external"

    def _content(self):
        return self._image_tag() if self._type() == 'image' else self._text()

    def _image_tag(self):
        image_path = self._conf()['image'][self.options['image']] if 'image' in self.options.keys() else \
                     self._conf()['image'][list(self._conf()['image'])[0]]
        src = os.path.join('_extref_images', os.path.basename(image_path))
        file_path = os.path.join(self._env().app.outdir, src)
        if not os.path.isfile(file_path):
            shutil.copy(os.path.join(self._env().app.srcdir, image_path), file_path)
        return '<img alt="{0}" src="{1}"/>'.format(self._alt(), src)

    def _alt(self):
        return self._text()

    def _text(self):
        if 'text' in self.options.keys():
            return self.options['text']
        return self._conf()['text']

def config_inited_handler(app, config):
    if not config.extref_conf:
        raise ValueError("Parameter extref_conf could not be empty")
    if config.extref_default_type and not config.extref_default_type in REF_TYPES:
        raise ValueError("Parameter extref_default_type should be in {0}".format(REF_TYPES))
    with open(os.path.join(app.srcdir, config.extref_conf)) as f:
        config.extref_conf = json.loads(f.read())
    extref_images_dir = os.path.join(app.outdir, '_extref_images')
    if not os.path.isdir(extref_images_dir):
        os.makedirs(extref_images_dir)

def setup(app):
    app.add_config_value('extref_conf', None, 'html')
    app.add_config_value('extref_default_type', 'image', 'html')

    app.add_directive('extref', ExtRefDirective)

    app.connect('config-inited', config_inited_handler)

    return {
        'version': '0.1',
    }