.. _geocoding:

.. title:: Geocoding in Lets-Plot


Geocoding |licenses|
====================

.. |licenses| raw:: html

    <a class="reference internal image-reference" href="licenses.html">
      <img alt="Creative Commons License" src="https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg">
    </a>


Administrative Levels
---------------------

Country
~~~~~~~

:py:mod:`geocode_countries() <lets_plot.geo_data.geocode_countries>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_level_country_world

    World countries

    ---
    .. extref:: geocoding_level_country_canada

    Canada

    ---
    .. extref:: geocoding_level_country_india

    India

State
~~~~~

:py:mod:`geocode_states() <lets_plot.geo_data.geocode_states>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_level_state_us

    US states

    ---
    .. extref:: geocoding_level_state_australia

    Australia states

    ---
    .. extref:: geocoding_level_state_russia

    Russia states

County
~~~~~~

:py:mod:`geocode_counties() <lets_plot.geo_data.geocode_counties>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_level_county_us

    US counties

    ---
    .. extref:: geocoding_level_county_italy

    Italy counties

    ---
    .. extref:: geocoding_level_county_poland

    Poland counties

City
~~~~

:py:mod:`geocode_cities() <lets_plot.geo_data.geocode_cities>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_level_city_nyc

    New York

    ---
    .. extref:: geocoding_level_city_helsinki

    Helsinki

    ---
    .. extref:: geocoding_level_city_london

    London


Geometries
----------

Polygons
~~~~~~~~

:py:mod:`geom_map() <lets_plot.geom_map>`,
:py:mod:`geom_polygon() <lets_plot.geom_polygon>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_geometries_map_brazil

    Brazil

    ---
    .. extref:: geocoding_geometries_map_nigeria

    Nigeria states

    ---
    .. extref:: geocoding_geometries_map_greece

    Greece counties

Points
~~~~~~

:py:mod:`geom_point() <lets_plot.geom_point>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_geometries_point_kazakhstan

    Kazakhstan state centroids

    ---
    .. extref:: geocoding_geometries_point_georgia

    Georgia county centroids

    ---
    .. extref:: geocoding_geometries_point_greenland

    Greenland cities

Rectangles
~~~~~~~~~~

:py:mod:`geom_rect() <lets_plot.geom_rect>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_geometries_rectangle_japan

    Japan bounding box with states

    ---
    .. extref:: geocoding_geometries_rectangle_ireland

    Ireland county bounding boxes

    ---
    .. extref:: geocoding_geometries_rectangle_cuba

    Cuba bounding box with cities


Guides to Geocoding
-------------------

Documentation: :ref:`The Geocoding Reference Guide <advanced_geocoding>`.

An example notebook covering various geocoding use-cases: |geocoding_reference|.

.. |geocoding_reference| extref:: geocoding_reference
    :type: text
    :text: geocoding_reference.ipynb


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: geocoding_examples

    ---
    .. extref:: travel_the_world

    ---
    .. extref:: map_us_household_income

    ---
    .. extref:: covid19_india

    ---
    .. extref:: tourist_cities

    ---
    .. extref:: geocoding_levels

    ---
    .. extref:: map_airports

    ---
    .. extref:: mapping_us_household_income

    ---
    .. extref:: museums

    ---
    .. extref:: titanic

    ---
    .. extref:: internet_use_and_activities

    ---
    .. extref:: with_clipping

    ---
    .. extref:: without_clipping

    ---
    .. extref:: maps_and_geocoding

    ---
    .. extref:: geom_map

    ---
    .. extref:: geom_polygon

    ---
    .. extref:: map_coordinates

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst