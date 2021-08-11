.. _geocoding:

.. include:: /shared/previews.rst

Geocoding
=========


Administrative Levels
---------------------

:py:mod:`geocode() <lets_plot.geo_data.geocode>`

Country
~~~~~~~

:py:mod:`geocode_countries() <lets_plot.geo_data.geocode_countries>`

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

:py:mod:`geocode_states() <lets_plot.geo_data.geocode_states>`

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

:py:mod:`geocode_counties() <lets_plot.geo_data.geocode_counties>`

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

:py:mod:`geocode_cities() <lets_plot.geo_data.geocode_cities>`

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

:py:mod:`geom_map() <lets_plot.geom_map>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_geometries_map_brazil-nbviewer|

    Brazil

    ---
    |geocoding_geometries_map_nigeria-nbviewer|

    Nigeria states

    ---
    |geocoding_geometries_map_greece-nbviewer|

    Greece counties

Points
~~~~~~

:py:mod:`geom_point() <lets_plot.geom_point>`

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

:py:mod:`geom_rect() <lets_plot.geom_rect>`

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

Often geocoding can find multiple objects for a name or do not find anything.

Read :ref:`the doc about geocoding ambiguity <ambiguity>` to explore many ways to solve the problem.


Reverse Geocoding
-----------------

:py:mod:`reverse_geocode() <lets_plot.geo_data.reverse_geocode>`

Reverse geocoding is the process of converting geographic coordinates into a :py:mod:`Geocoder <lets_plot.geo_data.ReverseGeocoder>` object.


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