"""
coord_cartesian()
=================

Build a bar plot with
`coord_cartesian() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.coord_cartesian.html#lets_plot.coord_cartesian>`__
coordinate system.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl')) + \
    geom_bar() + \
    coord_cartesian(ylim=[0, 200])