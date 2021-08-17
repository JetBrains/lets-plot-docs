"""
Dodge Position
==============

Position adjustments determine how to arrange geoms that would otherwise
occupy the same space.

Arrange elements side by side using position ``dodge``.

See
`position_dodge() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.position_dodge.html#lets_plot.position_dodge>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_position_adjustments\_dodge_position.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes(x='fl', fill='drv'))
p1 = p + geom_bar() + ggtitle('Default')
p2 = p + geom_bar(position='dodge') + ggtitle("With Dodge Position")

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch