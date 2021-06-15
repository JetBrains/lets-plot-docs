#
# Copyright (c) 2021. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

def config_inited_handler(app, config):
    if not config.cname_url:
        return
    with open('{0}/CNAME'.format(app.outdir), 'w') as f:
        f.write(config.cname_url)

def setup(app):
    app.add_config_value('cname_url', None, '')
    app.connect('config-inited', config_inited_handler)
    return {
        'version': '0.1',
    }