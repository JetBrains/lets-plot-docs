.. _geocoding:

.. include:: /shared/previews.rst

Geocoding
=========


Standard Imports
----------------

.. jupyter-execute::

    import shapely

    from lets_plot.geo_data import *
    from lets_plot import *
    LetsPlot.setup_html()


Administrative Levels
---------------------

Country
~~~~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 1

    gdf = geocode_countries().get_boundaries(2)

    ggplot() + \
        geom_map(data=gdf, color='white', fill='black', \
                 tooltips=layer_tooltips().line('@{found name}')) + \
        ggtitle('World')

State
~~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 1

    gdf = geocode_states().countries('US-48').get_boundaries(4)

    ggplot() + \
        geom_map(data=gdf, color='white', fill='black', \
                 tooltips=layer_tooltips().line('@{found name}')) + \
        ggtitle('US States')

County
~~~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 1

    gdf = geocode_counties().countries('US-48').get_boundaries(4)

    ggplot() + \
        geom_map(data=gdf, color='white', fill='black', \
                 tooltips=layer_tooltips().line('@{found name}')) + \
        ggtitle('US Counties')

City
~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 1

    gdf = geocode_cities(names='New York').get_boundaries()

    ggplot() + \
        geom_map(data=gdf, color='white', fill='black', \
                 tooltips=layer_tooltips().line('@{found name}')) + \
        ggtitle('New York City')


Geometries
----------

Map
~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 4-5

    gdf = geocode(level='county').scope('US-ME').get_boundaries()

    ggplot() + \
        geom_map(data=gdf, color='white', fill='black', \
                 tooltips=layer_tooltips().line('@{found name}')) + \
        ggtitle('Map Geometry')

Points
~~~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 4-5

    gdf = geocode(level='county').scope('US-ME').get_centroids()

    ggplot() + \
        geom_point(data=gdf, shape=1, color='black', \
                   tooltips=layer_tooltips().line('@{found name}')) + \
        coord_map() + \
        ggtitle('Point Geometry')

Rectangles
~~~~~~~~~~

.. jupyter-execute::
    :linenos:
    :emphasize-lines: 4-5

    gdf = geocode(level='county').scope('US-ME').get_boundaries()

    ggplot() + \
        geom_rect(data=gdf, color='black', alpha=0, \
                  tooltips=layer_tooltips().line('@{found name}').color('black')) + \
        coord_map() + \
        ggtitle('Rectangle Geometry')


Ambiguity
---------

Problem
~~~~~~~

Often geocoding can find multiple objects for a name or do not find anything. In this case error will be generated:

.. jupyter-execute::
    :raises: ValueError

    geocode_cities(['worcester']).get_geocodes()

Solutions
~~~~~~~~~

.. tabbed:: allow_ambiguous()

    .. jupyter-execute::

        geocode_cities(['worcester']).allow_ambiguous().get_geocodes()

.. tabbed:: ignore_not_found()

    .. jupyter-execute::

        geocode_cities(['paris', 'foo']).ignore_not_found().get_geocodes()

.. tabbed:: ignore_all_errors()

    .. jupyter-execute::

        geocode_cities(['paris', 'worcester', 'foo']).ignore_all_errors().get_geocodes()

.. tabbed:: parents

    .. jupyter-execute::

        geocode_cities('worcester').states('massachusetts').get_geocodes()

    .. raw:: html

        <br/>

    .. jupyter-execute::

        states = geocode_states('US-MA')
        geocode_cities('worcester').states(states).get_geocodes()

.. tabbed:: scope

    .. jupyter-execute::

        geocode_cities(['worcester', 'warwick']).scope('UK').get_geocodes()

.. tabbed:: where(..., scope=...)

    .. jupyter-execute::

        bbox = shapely.geometry.box(-71.00, 42.00, -72.00, 43.00)
        geocode_cities('worcester').where('worcester', scope=bbox).get_geocodes()

    .. raw:: html

        <br/>

    .. jupyter-execute::

        massachusetts = geocode_states('massachusetts')
        geocode_cities('worcester').where('worcester', scope=massachusetts).get_geocodes()

.. tabbed:: where(..., closest_to=...)

    .. jupyter-execute::

        boston = geocode_cities('boston')
        geocode_cities('worcester').where('worcester', closest_to=boston).get_geocodes()

    .. raw:: html

        <br/>

    .. jupyter-execute::

        boston = shapely.geometry.Point(-71.088, 42.311)
        geocode_cities('worcester').where('worcester', closest_to=boston).get_geocodes()


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`geom_polygon() <lets_plot.geom_polygon>`, :py:mod:`geom_map() <lets_plot.geom_map>`, :py:mod:`geom_point() <lets_plot.geom_point>`, :py:mod:`geom_text() <lets_plot.geom_text>`, :py:mod:`geom_path() <lets_plot.geom_path>`, :py:mod:`geom_rect() <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.

|geopandas_kotlin_isl_4x3-nbviewer|


Demo Examples
-------------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_reference-nbviewer|

    ---
    |geocoding_levels-nbviewer|

    ---
    |geocoding_examples-nbviewer|

    ---
    |maps_and_geocoding-nbviewer|

    ---
    |geom_map-nbviewer|

    ---
    |geom_polygon-nbviewer|

    ---
    |map_coordinates-nbviewer|

    ---
    |with_clipping-nbviewer|

    ---
    |without_clipping-nbviewer|

    ---
    |map_US_household_income-nbviewer|

    ---
    |covid19_india-kaggle|

    ---
    |internet_use_and_activities-nbviewer|

    ---
    |map_airports-kaggle|

    ---
    |mapping_US_household_income-kaggle|

    ---
    |museums-nbviewer|

    ---
    |titanic-kaggle|

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>

.. include:: /shared/features.rst