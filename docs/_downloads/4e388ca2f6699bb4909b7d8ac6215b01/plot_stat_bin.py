"""
Stat ``bin``
============

Build a plot with ``stat='bin'``.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl')) + \
    geom_point(stat='bin')