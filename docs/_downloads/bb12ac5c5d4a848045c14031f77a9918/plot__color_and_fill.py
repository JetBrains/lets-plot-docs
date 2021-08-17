"""
Color and Fill Scales
=====================

Scales control how a plot maps data values to the visual values of an
aesthetic.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_scales\_color_and_fill.png"

from datetime import datetime

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

mpg_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

ec_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/economics.csv', \
                    parse_dates=['date'])
ec_df = ec_df[ec_df.date > datetime(2000, 1, 1)]

# %%

# %% [markdown]
#
# Discrete
# ~~~~~~~~

# %%

p = ggplot(mpg_df, aes(x='fl')) + geom_bar(aes(color='fl', fill='fl'), alpha=.5)
p

# %%

p + scale_color_brewer(type='seq', palette='Blues') + \
    scale_fill_brewer(type='seq', palette='Blues')

# %%

p + scale_color_grey(start=0, end=.7) + \
    scale_fill_grey(start=0, end=.7)

# %%

# %% [markdown]
#
# Continuous
# ~~~~~~~~~~

# %%

p = ggplot(ec_df, aes(x='psavert')) + geom_histogram(aes(fill='psavert'))
p

# %%

p + scale_fill_gradient(low='#2c7fb8', high='#edf8b1')

# %%

p + scale_fill_gradient2(low='#1a9641', mid='#ffffbf', high='#d7191c')

# %%

p + scale_fill_hue(l=80, c=150)