"""
Fixed Coordinates
=================

Cartesian coordinates with fixed aspect ratio between ``x`` and ``y``
units.

See
`coord_fixed() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.coord_fixed.html#lets_plot.coord_fixed>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_coordinate_systems\_fixed_coordinates.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('cty', 'hwy')) + geom_point()
p1 = p + ggtitle('Default')
p2 = p + coord_fixed() + ggtitle('With Fixed Coordinates')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch