"""
Correlation Plot
================

The ``corr_plot()`` function creates a fluent builder object offering a
set of methods for configuring of beautiful correlation plots.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_features\_correlation_plot.png"

import pandas as pd

from lets_plot import *
from lets_plot.bistro.corr import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

corr_plot(data=df, threshold=.5).points().labels().palette_gradient(low='#d7191c', mid='#ffffbf', high='#1a9641').build()