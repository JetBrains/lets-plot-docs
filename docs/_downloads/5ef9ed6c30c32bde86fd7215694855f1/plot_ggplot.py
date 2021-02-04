"""
ggplot()
========

Build a graph with ``ggplot()``.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_point(aes(color='cyl')) + \
    geom_smooth(method='lm') + \
    coord_cartesian() + \
    scale_color_brewer(type='div', palette='Spectral')