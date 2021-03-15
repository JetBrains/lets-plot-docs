"""
Interactive Maps
================

The ``geom_livemap()`` geom layer enables a researcher to visualize
geospatial information on a zoomable and paneble map.

See
`geom_livemap() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.geom_livemap.html#lets_plot.geom_livemap>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_features\_interactive_maps.png"

import pandas as pd

from lets_plot import *
from lets_plot.geo_data import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/midwest.csv')

# %%

pop_df = df.groupby('state').poptotal.sum().to_frame('population').reset_index()
pop_df.head(2)

# %%

states = geocode('state', pop_df.state, scope='US').get_boundaries(9)
states.head(2)

# %%

ggplot() + \
    geom_livemap() + \
    geom_map(aes(color='population', fill='population'), \
             data=pop_df, map=states, map_join='state', size=1, alpha=.3) + \
    scale_color_gradient(low='#1a9641', high='#d7191c') + \
    scale_fill_gradient(low='#1a9641', high='#d7191c')