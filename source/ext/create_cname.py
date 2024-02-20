#
# Copyright (c) 2021. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

def env_updated_handler(app, env):
    if not env.config.cname_url:
        return
    with open('{0}/CNAME'.format(app.outdir), 'w') as f:
        f.write(env.config.cname_url)

def setup(app):
    app.add_config_value('cname_url', None, '')
    # A list of all core events can be found here: https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events
    # If you start creating a CNAME one step earlier (env-merge-info event), it will be deleted
    app.connect('env-updated', env_updated_handler)
    return {
        'version': '0.2',
    }