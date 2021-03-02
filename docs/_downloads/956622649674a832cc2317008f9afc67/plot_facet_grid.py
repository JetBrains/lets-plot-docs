"""
facet_grid()
============

Build a plot with
`facet_grid() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.facet_grid.html#lets_plot.facet_grid>`__.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

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