"""
Facet Wrapping
==============

Facets divide a plot into subplots based on the values of one or more
discrete variable.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_faceting\_facet_wrapping.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('cty', 'hwy')) + geom_point()
p

# %%

p + facet_wrap(facets='fl', ncol=3)