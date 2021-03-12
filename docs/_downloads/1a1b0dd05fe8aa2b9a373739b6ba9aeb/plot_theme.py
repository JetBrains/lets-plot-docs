"""
theme()
=======

Build a plot with custom theme.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/HIL-HK/lets-plot-examples/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl')) + \
    geom_bar() + \
    theme(axis_line='blank', axis_ticks='blank', axis_text_y='blank', axis_title_y='blank')