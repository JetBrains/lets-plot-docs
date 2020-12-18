"""
Geometry geom_histogram()
=========================

An example with the geom_histogram() geometry.

"""

# sphinx_gallery_thumbnail_path = "/Users/vdovidaytis/Projects/lets-plot-docs/source/examples/geom_histogram.png"

import numpy as np

from lets_plot import *
LetsPlot.setup_html()

# %%

np.random.seed(42)
data = {'x': np.random.normal(0, 1, size=1000)}

# %%

ggplot(data) + \
    geom_histogram(aes(x='x'))