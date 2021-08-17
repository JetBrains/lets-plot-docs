"""
Labels
======

Use ``xlab()``, ``ylab()`` and ``labs()`` functions to set plot labels.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_labels\_labels.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

# %% [markdown]
#
# ``xlab()`` and ``ylab()``
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# %%

ggplot(df, aes('cty', 'hwy')) + \
    geom_point() + \
    xlab('city miles per gallon') + ylab('highway miles per gallon')

# %%

# %% [markdown]
#
# ``labs()``
# ~~~~~~~~~~

# %%

ggplot(df, aes('cty', 'hwy')) + \
    geom_point() + \
    labs(x='city miles per gallon', y='highway miles per gallon')