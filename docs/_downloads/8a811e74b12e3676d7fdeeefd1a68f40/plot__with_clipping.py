"""
With Clipping
=============

Removes unseen data points.

Look at the examples below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_zooming\_with_clipping.png"

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
p2 = p + scale_x_continuous(limits=[-92, -82]) + ylim(36, 43) + ggtitle('Zoom With Clipping')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch