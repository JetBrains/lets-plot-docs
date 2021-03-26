"""
Nudge Position
==============

Position adjustments determine how to arrange geoms that would otherwise
occupy the same space.

``position_nudge()`` is generally useful for adjusting the position of
items on discrete scales by a small amount.

See
`position_nudge() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.position_nudge.html#lets_plot.position_nudge>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_position_adjustments\_nudge_position.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot() + \
    geom_point(aes('cty', 'hwy'), data=df[df.year == 1999], \
               color='#ca0020', position=position_nudge(x=-.1, y=-.1)) + \
    geom_point(aes('cty', 'hwy'), data=df[df.year == 2008], \
               color='#0571b0', position=position_nudge(x=.1, y=.1))