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

- :py:mod:`geom_point() <lets_plot.geom_point>`, :py:mod:`geom_text() <lets_plot.geom_text>` with Points / Multi-Points
- :py:mod:`geom_path() <lets_plot.geom_path>` with Lines / Multi-Lines
- :py:mod:`geom_polygon() <lets_plot.geom_polygon>`, :py:mod:`geom_map() <lets_plot.geom_map>` with Polygons / Multi-Polygons
- :py:mod:`geom_rect() <lets_plot.geom_rect>` when used with Polygon shapes will display corresponding bounding boxes

Standard Imports
----------------

.. jupyter-execute::

    import pandas as pd

    from lets_plot.geo_data import *
    from lets_plot import *
    LetsPlot.setup_html()

Use cases
---------

Suppose we have the following data:

.. jupyter-execute::

    df = pd.DataFrame({
        'state': ['IL', 'IN', 'MI', 'OH', 'WI'],
        'pop_2021': [12_569_321, 6_805_663, 9_992_427, 11_714_618, 5_852_490],
    })
    gdf = geocode_states(names=df.state).scope('US').get_boundaries()

We can just draw the shapes from ``gdf``:

.. jupyter-execute::

    ggplot() + geom_map(map=gdf)

If we want to use aesthetics, we need to use the ``data`` parameter:

.. jupyter-execute::

    ggplot() + geom_map(aes(fill='found name'), color='white', data=gdf)

If we need both: dataframe with data and geodataframe with geometries, we use ``map_join`` parameter:

.. jupyter-execute::

    ggplot() + geom_map(aes(fill='pop_2021'), color='white', data=df, map=gdf, map_join='state')

Examples
--------

- The world map with *Lets-Plot* and *GeoPandas*: `geopandas_naturalearth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_naturalearth.ipynb>`__

- Plotting Airbnb prices Boston: |plotting_airbnb_prices_boston_datalore|

.. |plotting_airbnb_prices_boston_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://datalore.jetbrains.com/view/notebook/eifzdh96VYuNrcjuOpYPYr

- An **inset map** of Kotlin island: `geopandas_kotlin_isl.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_kotlin_isl.ipynb>`__

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/kotlin_island.png
    :width: 480px
    :alt: Couldn't load kotlin_island.png