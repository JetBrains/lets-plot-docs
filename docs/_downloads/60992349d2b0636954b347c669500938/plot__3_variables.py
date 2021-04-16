"""
3 Variables
===========

Some plots visualize a transformation of the original data set. Use a
stat parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ..name.. syntax.

Look at the examples below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_3_variables.png"

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

p = ggplot(data, aes(x='x', y='y', z='z', color='..level..'))
p1 = p + geom_contour() + ggtitle('geom="contour" + default stat')
p2 = p + geom_tile(stat='contour', size=2) + ggtitle('geom="tile" + stat="contour"')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch