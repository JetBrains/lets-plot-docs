"""
Without Clipping
================

Preferred type of zooming.

See
`coord_cartesian() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.coord_cartesian.html#lets_plot.coord_cartesian>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_zooming\_without_clipping.png"

import pandas as pd

from lets_plot import *
from lets_plot.geo_data import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/midwest.csv')

# %%

states = geocode('state', df.state.unique(), scope='US').get_boundaries(9)
states.head(2)

# %%

p = ggplot() + geom_map(data=states, tooltips=layer_tooltips().line('@{found name}'))
p1 = p + ggtitle('Default')
p2 = p + coord_map(ylim=[36, 43]) + ggtitle('Zoom Witouth Clipping')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch