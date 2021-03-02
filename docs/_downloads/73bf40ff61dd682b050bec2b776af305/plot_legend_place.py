"""
Legend Place
============

Place legend at ``bottom``, ``top``, ``left`` or ``right``.

"""

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes(x='cty', y='hwy')) + \
    geom_jitter(aes(color='fl'), width=.2, height=.2) + \
    theme(legend_position='bottom')