#
# Copyright (c) 2024. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import os
import sys; sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from utils.sitemap import generate_sitemap

def build_finished_handler(app, exception):
    generate_sitemap(html_dir="docs", sitemap_filename="docs/sitemap.xml")

def setup(app):
    # A list of all core events can be found here: https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html#core-events-overview
    app.connect('build-finished', build_finished_handler)
    return {
        'version': '0.1',
    }