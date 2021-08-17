"""
Graphical Primitives
====================

Use a geom to represent data points. Use the geom’s aesthetic
properties to represent variables. Each function returns a layer.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_geoms\_graphical_primitives.png"

from datetime import datetime

import pandas as pd

from lets_plot import *
from lets_plot.geo_data import *
LetsPlot.setup_html()

# %%

mw_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/midwest.csv')

ec_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/economics.csv', \
                    parse_dates=['date'])
ec_df = ec_df[ec_df.date > datetime(2000, 1, 1)]

# %%

# %% [markdown]
#
# Polygon
# ~~~~~~~

# %%

states = geocode('state', mw_df.state.unique(), scope='US').get_boundaries(9)
states.head(2)

# %%

ggplot() + \
    geom_polygon(data=states, color='white', fill='gray', \
                 tooltips=layer_tooltips().line('@{found name}'))

# %%

# %% [markdown]
#
# Path and Ribbon
# ~~~~~~~~~~~~~~~

# %%

p = ggplot(ec_df, aes('date', 'unemploy'))

# %%

p + geom_path() + scale_x_datetime()

# %%

p + geom_ribbon(aes(ymin=ec_df.unemploy - 900, ymax=ec_df.unemploy + 900))

# %%

# %% [markdown]
#
# Segment and Rectangle
# ~~~~~~~~~~~~~~~~~~~~~

# %%

ggplot() + geom_segment(x=0, y=0, xend=1, yend=1, arrow=arrow())

# %%

ggplot() + geom_rect(xmin=0, xmax=1, ymin=0, ymax=1)