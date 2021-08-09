.. _geocoding:

.. include:: /shared/previews.rst

Geocoding
=========


Hidden Preliminaries
--------------------

.. jupyter-execute::

    import shapely

    from lets_plot.geo_data import *
    from lets_plot import *
    LetsPlot.setup_html()


Administrative Levels
---------------------

Country
~~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_level_country_world-nbviewer|

    World countries

    ---
    |geocoding_level_country_canada-nbviewer|

    Canada

    ---
    |geocoding_level_country_india-nbviewer|

    India

State
~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_level_state_us-nbviewer|

    US states

    ---
    |geocoding_level_state_china-nbviewer|

    China states

    ---
    |geocoding_level_state_russia-nbviewer|

    Russia states

County
~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_level_county_us-nbviewer|

    US counties

    ---
    |geocoding_level_county_italy-nbviewer|

    Italy counties

    ---
    |geocoding_level_county_poland-nbviewer|

    Poland counties

City
~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_level_city_nyc-nbviewer|

    New York

    ---
    |geocoding_level_city_helsinki-nbviewer|

    Helsinki

    ---
    |geocoding_level_city_london-nbviewer|

    London


Geometries
----------

Polygons
~~~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_geometries_map_brasil-nbviewer|

    Brasil

    ---
    |geocoding_geometries_map_nigeria-nbviewer|

    Nigeria states

    ---
    |geocoding_geometries_map_greece-nbviewer|

    Greece counties

Points
~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_geometries_point_kazakhstan-nbviewer|

    Kazakhstan state centroids

    ---
    |geocoding_geometries_point_georgia-nbviewer|

    Ceorgia county centroids

    ---
    |geocoding_geometries_point_greenland-nbviewer|

    Greenland cities

Rectangles
~~~~~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_geometries_rectangle_japan-nbviewer|

    Japan bounding box with states

    ---
    |geocoding_geometries_rectangle_ireland-nbviewer|

    Ireland county bounding boxes

    ---
    |geocoding_geometries_rectangle_cuba-nbviewer|

    Cuba bounding box with cities


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


Examples
--------

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