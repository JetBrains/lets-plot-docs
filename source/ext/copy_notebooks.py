#
# Copyright (c) 2026. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import os
import shutil

NOTEBOOKS_SRC_DIR = "examples"
NOTEBOOKS_DST_DIR = "download"


def copy_notebooks(app, exception):
    if exception is not None:
        return

    mode = getattr(app.config, "copy_notebooks_mode", "all")
    if mode == "off":
        return

    src_dir = os.path.join(app.srcdir, NOTEBOOKS_SRC_DIR)
    dst_dir = os.path.join(app.outdir, NOTEBOOKS_DST_DIR, NOTEBOOKS_SRC_DIR)

    if not os.path.isdir(src_dir):
        return

    for root, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d != ".ipynb_checkpoints"]
        rel = os.path.relpath(root, src_dir)
        dst_root = os.path.join(dst_dir, rel)

        for name in files:
            if not name.endswith(".ipynb"):
                continue

            src_path = os.path.join(root, name)
            dst_path = os.path.join(dst_root, name)

            if mode == "missing" and os.path.exists(dst_path):
                continue

            if not os.path.isdir(dst_root):
                os.makedirs(dst_root, exist_ok=True)
            shutil.copy2(src_path, dst_path)


def setup(app):
    app.add_config_value("copy_notebooks_mode", "all", "env")
    app.connect("build-finished", copy_notebooks)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }