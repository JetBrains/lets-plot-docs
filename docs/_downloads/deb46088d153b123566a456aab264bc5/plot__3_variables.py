"""
Three Variables
===============

Use a geom to represent data points. Use the geom’s aesthetic
properties to represent variables. Each function returns a layer.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_geoms\_3_variables.png"

import numpy as np
from scipy.stats import multivariate_normal

from lets_plot import *
LetsPlot.setup_html()

# %%

np.random.seed(42)
n = 25
x = np.linspace(-1, 1, n)
y = np.linspace(-1, 1, n)
X, Y = np.meshgrid(x, y)
mean = np.zeros(2)
cov = [[1, .5],
       [.5, 1]]
rv = multivariate_normal(mean, cov)
Z = rv.pdf(np.dstack((X, Y)))
data = {'x': X.flatten(), 'y': Y.flatten(), 'z': Z.flatten()}

# %%

p = ggplot(data, aes('x', 'y'))

# %%

p + geom_contour(aes(z='z'))

# %%

p + geom_contourf(aes(z='z'), size=.5, color='white')

# %%

p + geom_raster(aes(fill='z'))

# %%

p + geom_tile(aes(fill='z'))