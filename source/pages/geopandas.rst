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


Hidden Preliminaries
--------------------

.. jupyter-execute::

    import pandas as pd

    from lets_plot.geo_data import *
    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.DataFrame({
        'state': ['IL', 'IN', 'MI', 'OH', 'WI'],
        'pop_2021': [12_569_321, 6_805_663, 9_992_427, 11_714_618, 5_852_490],
    })
    gdf = geocode_states(names=df.state).scope('US').get_boundaries()[['state', 'geometry']]


Use Cases
---------

Depending on the situation, for data mapping we use parameters ``data``, ``map`` or both.


No Difference
~~~~~~~~~~~~~

Suppose we have the following data:

.. jupyter-execute::

    gdf

If you want to draw only shapes, there is no difference which parameter is used:

.. panels::
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    .. jupyter-execute::

        ggplot() + geom_map(data=gdf)

    ---
    .. jupyter-execute::

        ggplot() + geom_map(map=gdf)


Only ``data``
~~~~~~~~~~~~~

If you want to use aesthetics, the ``data`` parameter is the only choice:

.. jupyter-execute::

    ggplot() + geom_map(aes(fill='state'), color='white', data=gdf)


``data`` & ``map``
~~~~~~~~~~~~~~~~~~

Suppose we also have a dataframe with population data:

.. jupyter-execute::

    df

To combine this with geospatial data, you can use the ``map_join`` parameter:

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

.. image:: /_static/images/kotlin_island.png
    :width: 480px
    :alt: Couldn't load kotlin_island.png