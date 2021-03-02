"""
ggtitle()
=========

Build a plot with
`ggtitle() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.ggtitle.html#lets_plot.ggtitle>`__.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_point() + \
    ggtitle('New Plot Title')