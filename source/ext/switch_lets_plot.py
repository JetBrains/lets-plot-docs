#
# Copyright (c) 2022. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import subprocess
import sys

def todo(app, env, docnames):
    if env.config.switch_lets_plot:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "lets_plot", "--user"])

def setup(app):
    app.add_config_value('switch_lets_plot', False, 'env')
    app.connect('env-before-read-docs', todo)
    return {
        'version': '0.1',
    }