#
# Copyright (c) 2026. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import os
import fnmatch
import subprocess


def _should_exclude(rel_path, patterns):
    for p in patterns:
        if fnmatch.fnmatch(rel_path, p):
            return True
    return False


def execute_notebooks(app):
    if not app.config.execute_notebooks:
        return
    for root, dirs, files in os.walk(app.srcdir):
        dirs[:] = [d for d in dirs if d != ".ipynb_checkpoints"]
        for name in files:
            if not name.endswith(".ipynb"):
                continue
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, app.srcdir)
            rel_posix = rel_path.replace(os.sep, "/")
            if _should_exclude(rel_posix, app.config.execute_notebooks_exclude):
                continue
            print("[execute_notebooks] executing", rel_posix)
            try:
                subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", full_path],
                               check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                               timeout=300)
            except subprocess.CalledProcessError as e:
                print("[execute_notebooks] failed:", rel_posix)
                if app.config.execute_notebooks_fail_on_error:
                    raise e


def setup(app):
    app.add_config_value("execute_notebooks", False, "env")
    app.add_config_value("execute_notebooks_exclude", [], "env")
    app.add_config_value("execute_notebooks_fail_on_error", True, "env")
    app.connect("builder-inited", execute_notebooks)
    return {
        "version": "0.1",
        "parallel_read_safe": False,
        "parallel_write_safe": True,
    }