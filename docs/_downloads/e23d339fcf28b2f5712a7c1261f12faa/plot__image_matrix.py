"""
Image Matrix
============

The ``image_matrix()`` function arranges a set of images in a grid.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_features\_image_matrix.png"

from PIL import Image
import numpy as np

from lets_plot import *

LetsPlot.setup_html()

# %%

img = np.asarray(Image.open('rock_formation.png'))

# %%

ggplot() + geom_image(image_data=img)