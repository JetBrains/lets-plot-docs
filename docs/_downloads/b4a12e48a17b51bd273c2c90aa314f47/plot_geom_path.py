"""
Geometry geom_path()
====================

An example with the geom_path() geometry.

"""

# sphinx_gallery_thumbnail_path = "E:\Projects\DataPad\Subprojects\LetsPlotDocs\MyFork\lets-plot-docs\source\../examples\geom_path.png"

import numpy as np

from lets_plot import *
LetsPlot.setup_html()

# %%

phi = np.linspace(0, 2 * np.pi, 100)
rho = 1 - .9 * np.sin(phi)
data = {'x': rho * np.cos(phi), \
        'y': rho * np.sin(phi)}

# %%

ggplot(data, aes(x='x', y='y')) + \
    geom_path(size=1, color='red') + \
    coord_fixed()