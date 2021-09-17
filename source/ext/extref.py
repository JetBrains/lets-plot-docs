#
# Copyright (c) 2021. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import os
import json
import shutil
from urllib.parse import urlparse

from docutils import nodes
from docutils.parsers.rst import Directive, directives

REF_TYPES = ('image', 'logo', 'text')
IMAGES_DIR = "_extref_images"
LOGO_DIR = "logo"
LOGO_SIZE = 20

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
            '<a class="{0}" href="{1}">{2}</a>'.format(self._class(), self._href(), self._content()),
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
        conf_ref = self._conf()['ref']
        if 'ref' in self.options.keys():
            return conf_ref[self.options['ref']]
        if 'extref_default_ref' in self._env().config and \
           self._env().config['extref_default_ref'] in conf_ref:
            return conf_ref[self._env().config['extref_default_ref']]
        return conf_ref[list(conf_ref)[0]]

    def _class(self):
        if self._type() in ['image', 'logo']:
            return "reference {0} image-reference".format(self._url_type())
        return "reference {0}".format(self._url_type())

    def _url_type(self):
        return "external" if urlparse(self._href()).netloc else "internal"

    def _content(self):
        if self._type() == 'image':
            return self._image_tag()
        if self._type() == 'logo':
            return self._logo_tag()
        return self._text()

    def _image_tag(self):
        image_src_path = self._image_src()
        image_src_fullpath = os.path.join(self._env().app.srcdir, image_src_path)
        image_doc_path = os.path.join(self._env().config['extref_images_dir'], os.path.basename(image_src_path))
        image_doc_fullpath = os.path.join(self._env().app.outdir, image_doc_path)
        if not os.path.isfile(image_doc_fullpath):
            shutil.copy(image_src_fullpath, image_doc_fullpath)
        doc_dir = os.path.dirname(self.state.document.attributes['source'].replace(self._env().app.srcdir, ''))[1:]
        return '<img alt="{0}" src="{1}"/>'.format(self._alt(), os.path.relpath(image_doc_path, doc_dir))

    def _image_src(self):
        conf_image = self._conf()['image']
        if 'image' in self.options.keys():
            return conf_image[self.options['image']]
        if 'extref_default_image' in self._env().config and \
           self._env().config['extref_default_image'] in conf_image:
            return conf_image[self._env().config['extref_default_image']]
        return conf_image[list(conf_image)[0]]

    def _alt(self):
        return self._text()

    def _logo_tag(self):
        logo_fullpath = next((path for name, path in self._env().config['extref_logo_images'].items() if name in self._href()), None)
        if not logo_fullpath:
            raise ValueError("There is no appropriate logo for url {0}".format(self._href()))
        logo_path = logo_fullpath.replace(self._env().app.outdir, '')[1:]
        doc_dir = os.path.dirname(self.state.document.attributes['source'].replace(self._env().app.srcdir, ''))[1:]
        return '<img alt="{0}" src="{1}" width="{2}" height="{2}"/>'.format(
            self._alt(), os.path.relpath(logo_path, doc_dir), LOGO_SIZE
        )

    def _text(self):
        if 'text' in self.options.keys():
            return self.options['text']
        if 'text' in self._conf():
            return self._conf()['text']
        return self._href()

def config_inited_handler(app, config):
    if config.extref_default_type and not config.extref_default_type in REF_TYPES:
        raise ValueError("Parameter extref_default_type should be in {0}".format(REF_TYPES))
    prepare_conf_json(app, config)
    prepare_images(app, config)

def prepare_conf_json(app, config):
    if not config.extref_conf:
        raise ValueError("Parameter extref_conf could not be empty")
    with open(os.path.join(app.srcdir, config.extref_conf)) as f:
        try:
            config.extref_conf = json.loads(f.read())
        except json.decoder.JSONDecodeError as e:
            msg = "Decode error in {0}. {1}".format(config.extref_conf, e.msg)
            raise json.decoder.JSONDecodeError(msg, e.doc, e.pos) from e

def prepare_images(app, config):
    extref_images_dir = os.path.join(app.outdir, config.extref_images_dir)
    if not os.path.isdir(extref_images_dir):
        os.makedirs(extref_images_dir)
    prepare_logo(app, config)

def prepare_logo(app, config):
    extref_logo_dir = os.path.join(app.outdir, config.extref_images_dir, LOGO_DIR)
    if not os.path.isdir(extref_logo_dir):
        os.makedirs(extref_logo_dir)
    if config.extref_logo_images:
        extref_logo_images = {}
        for logo_name, logo_src_path in config.extref_logo_images.items():
            logo_src_fullpath = os.path.join(app.srcdir, logo_src_path)
            logo_doc_fullpath = os.path.join(extref_logo_dir, "{0}{1}".format(logo_name, os.path.splitext(logo_src_path)[1]))
            extref_logo_images[logo_name] = logo_doc_fullpath
            if not os.path.isfile(logo_doc_fullpath):
                shutil.copy(logo_src_fullpath, logo_doc_fullpath)
        config.extref_logo_images = extref_logo_images

def setup(app):
    app.add_config_value('extref_conf', None, 'html') # Path to JSON file with references
    app.add_config_value('extref_logo_images', None, 'html') # Dict of the correspondences between logo names and logo images
    app.add_config_value('extref_images_dir', IMAGES_DIR, 'html') # Name of the directory with images in the builded documentation
    app.add_config_value('extref_default_type', REF_TYPES[0], 'html') # Type of the reference by default (if :type: parameter is not specified)
    app.add_config_value('extref_default_ref', None, 'html') # Name of the reference by default (if :url: and :ref: parameters are not specified)
    app.add_config_value('extref_default_image', None, 'html') # Name of the image by default (if :image: parameter is not specified)

    app.add_directive('extref', ExtRefDirective)

    app.connect('config-inited', config_inited_handler)

    return {
        'version': '0.1',
    }