"""
Geom Boxplot
============

"""

import numpy as np

from lets_plot import *
LetsPlot.setup_html()

#%%

# sphinx_gallery_thumbnail_path = "/Users/vdovidaytis/Projects/lets-plot-docs/source/examples/geom_boxplot.png"

np.random.seed(42)
n = 100
data = {'y': np.random.normal(size=n), \
        'class': np.random.randint(5, size=n)}

# %%

ggplot(data, aes(x='class', y='y')) + \
    geom_boxplot(aes(fill='class', color='class'), alpha=.5) + \
    scale_color_discrete() + scale_fill_discrete()