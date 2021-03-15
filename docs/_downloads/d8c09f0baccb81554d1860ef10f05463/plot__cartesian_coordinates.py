"""
Cartesian Coordinates
=====================

The default coordinate system.

See
`coord_cartesian() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.coord_cartesian.html#lets_plot.coord_cartesian>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_coordinate_systems\_cartesian_coordinates.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes(x='fl')) + geom_bar()
p1 = p + ggtitle('Default')
p2 = p + coord_cartesian(ylim=[0, 250]) + ggtitle('With Specified Coordinates')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch