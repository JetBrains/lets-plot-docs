"""
Facet Grid
==========

Facets divide a plot into subplots based on the values of one or more
discrete variable.

See
`facet_grid() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.facet_grid.html#lets_plot.facet_grid>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_faceting\_facet_grid.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('cty', 'hwy')) + geom_point()
p

# %%

# %% [markdown]
#
# Columns Based Facet
# -------------------

# %%

p + facet_grid(x='fl')

# %%

# %% [markdown]
#
# Rows Based Facet
# ----------------

# %%

p + facet_grid(y='year')

# %%

# %% [markdown]
#
# Facet Into Rows and Columns
# ---------------------------

# %%

p + facet_grid(x='fl', y='year')