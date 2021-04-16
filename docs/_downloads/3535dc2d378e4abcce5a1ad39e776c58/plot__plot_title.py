"""
Plot Title
==========

Add a main title above the plot.

See
`ggtitle() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.ggtitle.html#lets_plot.ggtitle>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_labels\_plot_title.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes('cty', 'hwy')) + \
    geom_point() + \
    ggtitle('New Plot Title')