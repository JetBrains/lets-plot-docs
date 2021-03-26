"""
Jitter Position
===============

Position adjustments determine how to arrange geoms that would otherwise
occupy the same space.

Add random noise to ``X`` and ``Y`` position of each element to avoid
overplot using position jitter.

See
`position_jitter() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.position_jitter.html#lets_plot.position_jitter>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_position_adjustments\_jitter_position.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('cty', 'hwy'))
p1 = p + geom_point() + ggtitle('Default')
p2 = p + geom_point(position='jitter') + ggtitle("With Jitter Position")

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch