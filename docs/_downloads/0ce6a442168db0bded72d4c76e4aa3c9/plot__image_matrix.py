"""
Image Matrix
============

The ``image_matrix()`` function arranges a set of images in a grid.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_features\_image_matrix.png"

from PIL import Image
import numpy as np

from lets_plot import *
from lets_plot.bistro.im import *

LetsPlot.setup_html()

# %%

img = Image.open('rock_formation.png')

# %%

rows, cols = 3, 3
matrix = np.empty((rows, cols), dtype=object)
for r in range(rows):
    for c in range(cols):
        w, h = 128 + 64 * c, 128 + 64 * r
        matrix[r][c] = np.asarray(img.resize((w, h)))
image_matrix(matrix, norm=False, scale=.5)

# %%

# %% [markdown]
#
# ``geom_image()``
# ~~~~~~~~~~~~~~~~
# 
# The ``image_matrix()`` function uses ``geom_image()`` under the hood, so
# you might want to look at the following example.

# %%

ggplot() + geom_image(image_data=np.asarray(img))