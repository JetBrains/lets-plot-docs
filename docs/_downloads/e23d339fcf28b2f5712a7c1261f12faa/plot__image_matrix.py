"""
Image Matrix
============

The ``image_matrix()`` function arranges a set of images in a grid.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_features\_image_matrix.png"

from PIL import Image
import requests
from io import BytesIO
import numpy as np

from lets_plot import *

LetsPlot.setup_html()

# %%

response = requests.get('https://www.stevensegallery.com/640/480')
img = np.asarray(Image.open(BytesIO(response.content)))

# %%

ggplot() + geom_image(image_data=img)