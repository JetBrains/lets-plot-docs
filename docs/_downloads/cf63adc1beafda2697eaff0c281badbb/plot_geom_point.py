"""
Geometry geom_point()
=====================

An example with the geom_point() geometry.

"""

# sphinx_gallery_thumbnail_path = "E:\Projects\DataPad\Subprojects\LetsPlotDocs\MyFork\lets-plot-docs\source\gallery_py\geoms\geom_point.png"

import numpy as np

from lets_plot import *
LetsPlot.setup_html()

# %%

np.random.seed(42)
n = 100
x = np.random.uniform(-5, 5, size=n)
y = x ** 2 + np.random.normal(size=n)
data = {'x': x, 'y': y}

# %%

ggplot(data, aes(x='x', y='y')) + geom_point()