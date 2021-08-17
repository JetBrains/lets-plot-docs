"""
Graph Building
==============

``ggplot()`` function begins a plot that you finish by adding layers.

See
`ggplot() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.ggplot.html#lets_plot.ggplot>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_basics\_graph_building.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes('cty', 'hwy')) + \
    geom_point(aes(color='cyl')) + \
    geom_smooth(method='lm') + \
    coord_cartesian() + \
    scale_color_brewer(type='div', palette='Spectral')