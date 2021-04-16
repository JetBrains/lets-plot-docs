"""
Map Coordinates
===============

``coord_map()`` projects a portion of the earth, which is approximately
spherical, onto a flat 2D plane.

See
`coord_map <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.coord_map.html#lets_plot.coord_map>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_coordinate_systems\_map_coordinates.png"

from lets_plot import *
from lets_plot.geo_data import *
LetsPlot.setup_html()

# %%

italy = geocode_countries('Italy').get_boundaries(6)

# %%

p = ggplot() + geom_polygon(data=italy)
p1 = p + ggtitle('Default')
p2 = p + coord_map() + ggtitle('With Map Coordinates')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch