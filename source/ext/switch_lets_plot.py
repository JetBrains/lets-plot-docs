#
# Copyright (c) 2022. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import subprocess
import sys

def replace_lib(app, env, docnames):
    if env.config.switch_lets_plot:
        version_setup = "" if env.config.lets_plot_version is None else "=={0}".format(env.config.lets_plot_version)
        subprocess.check_call([
            sys.executable,
            "-m", "pip", "install", "--force-reinstall", "lets_plot{0}".format(version_setup), "--user"
        ])

def setup(app):
    app.add_config_value('switch_lets_plot', False, 'env')
    app.add_config_value('lets_plot_version', None, 'env')
    app.connect('env-before-read-docs', replace_lib)
    return {
        'version': '0.1',
    }