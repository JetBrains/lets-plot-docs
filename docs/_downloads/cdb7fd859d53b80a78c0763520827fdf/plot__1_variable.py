"""
One Variable
============

Use a geom to represent data points. Use the geom’s aesthetic
properties to represent variables. Each function returns a layer.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_geoms\_1_variable.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

# %% [markdown]
#
# Continuous Variable
# -------------------

# %%

p = ggplot(df, aes(x='hwy'))

# %%

p + geom_area(stat='bin')

# %%

p + geom_density()

# %%

p + geom_freqpoly()

# %%

p + geom_histogram()

# %%

# %% [markdown]
#
# Discrete Variable
# -----------------

# %%

ggplot(df, aes(x='fl')) + geom_bar()