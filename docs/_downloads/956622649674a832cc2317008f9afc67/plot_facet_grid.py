"""
facet_grid()
============

Build a plot with ``facet_grid()``.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_point() + \
    facet_grid(x='fl') + \
    ggsize(800, 300)

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_point() + \
    facet_grid(y='year')

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_point() + \
    facet_grid(x='fl', y='year') + \
    ggsize(800, 600)