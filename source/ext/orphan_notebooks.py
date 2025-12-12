#
# Copyright (c) 2025. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

NOTEBOOKS_DIR = "examples/"

def mark_notebooks_as_orphan(app, env):
    for docname in env.found_docs:
        if not docname.startswith(NOTEBOOKS_DIR):
            continue
        meta = env.metadata.setdefault(docname, {})
        meta['orphan'] = True

def setup(app):
    app.connect('env-updated', mark_notebooks_as_orphan)
    return {
        'version': "0.1",
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }