"""
position_dodge()
================

Build a plot with ``position_dodge()``.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl', fill='drv')) + \
    geom_bar(position='dodge')

# %%

ggplot(df, aes(x='fl', fill='drv')) + \
    geom_bar(position=position_dodge())