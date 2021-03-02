"""
position_dodge()
================

Build a plot with
`position_dodge() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.position_dodge.html#lets_plot.position_dodge>`__.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl', fill='drv')) + \
    geom_bar(position='dodge')

# %%

ggplot(df, aes(x='fl', fill='drv')) + \
    geom_bar(position=position_dodge())