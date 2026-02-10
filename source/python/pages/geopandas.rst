.. _geopandas:

:og:description: All GeoPandas shapes are "understood" by Lets-Plot and can be plotted using various geometry layers, depending on the type of the shape.

:orphan:

.. title:: Support Geopandas in Geometry Layers and Interactive Maps

.. meta::
   :description: All GeoPandas shapes are "understood" by Lets-Plot and can be plotted using various geometry layers, depending on the type of the shape.
   :keywords: geopandas, GeoDataFrame, shapes, geometries, coordinate reference system, CRS, interactive maps


GeoPandas Support (`GeoPandas <https://geopandas.org>`__ and `Shapely <https://pypi.org/project/Shapely/>`__)
=============================================================================================================

GeoPandas GeoDataFrame is a tabular data structure that contains a set of shapes (geometry) per each observation.

GeoDataFrame extends pandas DataFrame and as such, aside from the geometry, can contain other data.

GeoPandas supports the following three basic classes of geometric objects (shapes):

- Points / Multi-Points
- Lines / Multi-Lines
- Polygons / Multi-Polygons

All GeoPandas shapes are "understood" by *Lets-Plot* and can be plotted using various geometry layers, depending on the type of the shape.

Use:

- :py:mod:`geom_point() <lets_plot.geom_point>`, :py:mod:`geom_pointdensity() <lets_plot.geom_pointdensity>`, :py:mod:`geom_pie() <lets_plot.geom_pie>`, :py:mod:`geom_text() <lets_plot.geom_text>` with Points / Multi-Points
- :py:mod:`geom_path() <lets_plot.geom_path>` with Lines / Multi-Lines
- :py:mod:`geom_polygon() <lets_plot.geom_polygon>`, :py:mod:`geom_map() <lets_plot.geom_map>` with Polygons / Multi-Polygons
- :py:mod:`geom_rect() <lets_plot.geom_rect>` when used with Polygon shapes will display corresponding bounding boxes


Plot Preliminaries
------------------

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

Depending on the situation, for spatial data we use either parameter ``data`` or ``map`` or both.


Use either ``data`` or ``map`` Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose we have the following data:

.. jupyter-execute::

    gdf

| If you want to draw only shapes, then it makes no difference which parameter is used:

.. grid:: 2

    .. grid-item-card::

        .. jupyter-execute::

            ggplot() + geom_map(data=gdf)

    .. grid-item-card::

        .. jupyter-execute::

            ggplot() + geom_map(map=gdf)


Use ``data`` Parameter
~~~~~~~~~~~~~~~~~~~~~~

If you want to use aesthetics, the ``data`` parameter is the only choice:

.. jupyter-execute::

    ggplot() + geom_map(aes(fill='state'), color='white', data=gdf)


Use Both: ``data`` and ``map`` Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose you also have a dataframe with population data:

.. jupyter-execute::

    df

| In this situation, in order to link aesthetics to the population numbers you will use:

- ``data`` parameter for the "population" dataframe,
- ``map`` parameter for the state boundaries ``GeoDataframe``.

The 3rd parameter, ``map_join``, will help to combine population values and state boundaries on the same chart:

.. jupyter-execute::

    ggplot() + geom_map(aes(fill='pop_2021'), color='white', data=df, map=gdf, map_join='state')


``use_crs`` Parameter
---------------------

Specify EPSG code of coordinate reference system (CRS). All coordinates in ``GeoDataFrame`` will be projected to this CRS.

.. jupyter-execute::

    ggplot() + geom_map(map=gdf, use_crs="EPSG:32616")

| Value "provided" tells *Lets-Plot* that the input ``GeoDataframes`` already contains coordinates in the desired CRS and should not be reprojected any further.

.. jupyter-execute::

    gdf_utm = gdf.to_crs("EPSG:32616")
    ggplot() + geom_map(map=gdf_utm, use_crs="provided")


Interactive Maps
----------------

Apart from the ``use_crs`` parameter, ``GeoDataFrames`` are fully supported on *Lets-Plot* interactive maps.

When used in combination with :py:mod:`geom_livemap() <lets_plot.geom_livemap>`,
the value of the ``use_crs`` parameter is ignored and all coordinates are reprojected using the Mercator projection.

.. jupyter-execute::

    ggplot() + geom_livemap() + geom_map(aes(fill='state'), data=gdf, alpha=.5)


Examples
--------

- The world map with *Lets-Plot* and *GeoPandas*: |geopandas_naturalearth|

.. |geopandas_naturalearth| extref:: geopandas_naturalearth
    :type: text
    :text: link

- Plotting Airbnb prices Boston: |plotting_airbnb_prices_boston|

.. |plotting_airbnb_prices_boston| extref:: plotting_airbnb_prices_boston
    :type: text
    :text: Datalore link

- Spatial prediction of soil pollutants with multi-output Gaussian processes: |soil_pollutants_with_gaussian_processes| 

.. |soil_pollutants_with_gaussian_processes| extref:: soil_pollutants_with_gaussian_processes
    :type: text
    :text: Nextjournal link

- Using geom_imshow() to draw DEM on map: |ivindo_river|

.. |ivindo_river| extref:: ivindo_river
    :type: text
    :text: link

- ``use_crs`` parameter: |map_use_crs|

.. |map_use_crs| extref:: map_use_crs
    :type: text
    :text: link

- Using exotic map projections: |projection_provided|

.. |projection_provided| extref:: projection_provided
    :type: text
    :text: link

- An **inset map** of Kotlin island: |geopandas_kotlin_isl|

.. |geopandas_kotlin_isl| extref:: geopandas_kotlin_isl
    :type: text
    :text: link

.. image:: /_static/images/kotlin_island.png
    :width: 480px
    :alt: Couldn't load kotlin_island.png