.. _geopandas:

GeoPandas Support (`GeoPandas <https://geopandas.org>`__ and `Shapely <https://pypi.org/project/Shapely/>`__)
=============================================================================================================

GeoPandas GeoDataFrame is a tabular data structure that contains a set of shapes (geometry) per each observation.

GeoDataFrame extends pandas DataFrame and as such, aside from the geometry, can contain other data.

GeoPandas supports the following three basic classes of geometric objects (shapes):

- Points / Multi-Points
- Lines / Multi-Lines
- Polygons / Multi-Polygons

All GeoPandas shapes are "undersood" by Lets-Plot and can be plotted using various geometry layers, depending on the type of the shape.

Use:

- ``geom_point()``, ``geom_text()`` with Points / Multi-Points
- ``geom_path()`` with Lines / Multi-Lines
- ``geom_polygon()``, ``geom_map()`` with Polygons / Multi-Polygons
- ``geom_rect()`` when used with Polygon shapes will display corresponding bounding boxes

Examples
^^^^^^^^

- The world map with *Lets-Plot* and *GeoPandas*: `geopandas_naturalearth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_naturalearth.ipynb>`__

- Plotting Airbnb prices Boston: |plotting_airbnb_prices_boston_datalore| |plotting_airbnb_prices_boston_medium|

.. |plotting_airbnb_prices_boston_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://datalore.jetbrains.com/view/notebook/eifzdh96VYuNrcjuOpYPYr

.. |plotting_airbnb_prices_boston_medium| image:: https://raw.githubusercontent.com/Medium/medium-logos/master/01_Logo/01_Black/SVG/Medium-Logo-Black-RGB.svg
    :height: 25px
    :alt: View in Medium
    :target: https://csboutique.medium.com/lets-plot-948ee80cfa5c

- An **inset map** of Kotlin island: `geopandas_kotlin_isl.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_kotlin_isl.ipynb>`__

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/kotlin_island.png
    :width: 480px
    :alt: Couldn't load kotlin_island.png