"""
Jitterdodge Position
====================

Position adjustments determine how to arrange geoms that would otherwise
occupy the same space.

Simultaneously dodge and jitter in one function:
``position_jitterdodge()``.

See
`position_jitterdodge() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.position_jitterdodge.html#lets_plot.position_jitterdodge>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_position_adjustments\_jitterdodge_position.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes('cyl', 'hwy', group='drv', fill='drv')) + \
    geom_boxplot() + \
    geom_point(position='jitterdodge', shape=21, color='black')