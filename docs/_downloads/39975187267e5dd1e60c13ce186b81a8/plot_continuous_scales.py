"""
scale_*_continuous()
====================

Build a plot with ``scale_*__continuous()`` scale.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl')) + \
    geom_bar(aes(fill='fl')) + \
    scale_fill_continuous()