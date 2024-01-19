.. _geocoding:

.. title:: Geocoding in Lets-Plot

.. meta::
   :description: Lets-Plot offers geocoding API that allows a user to execute a single and batch geocoding queries to convert names of places into geographic coordinates.
   :keywords: geocoding, administrative levels


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

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_level_country_world

        World countries

    .. grid-item-card::

        .. extref:: geocoding_level_country_canada

        Canada

    .. grid-item-card::

        .. extref:: geocoding_level_country_india

        India


State
~~~~~

:py:mod:`geocode_states() <lets_plot.geo_data.geocode_states>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_level_state_us

        US states

    .. grid-item-card::

        .. extref:: geocoding_level_state_australia

        Australia states

    .. grid-item-card::

        .. extref:: geocoding_level_state_russia

        Russia states


County
~~~~~~

:py:mod:`geocode_counties() <lets_plot.geo_data.geocode_counties>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_level_county_us

        US counties

    .. grid-item-card::

        .. extref:: geocoding_level_county_italy

        Italy counties

    .. grid-item-card::

        .. extref:: geocoding_level_county_poland

        Poland counties


City
~~~~

:py:mod:`geocode_cities() <lets_plot.geo_data.geocode_cities>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_level_city_nyc

        New York

    .. grid-item-card::

        .. extref:: geocoding_level_city_helsinki

        Helsinki

    .. grid-item-card::

        .. extref:: geocoding_level_city_london

        London


Geometries
----------

Polygons
~~~~~~~~

:py:mod:`geom_map() <lets_plot.geom_map>`,
:py:mod:`geom_polygon() <lets_plot.geom_polygon>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_geometries_map_brazil

        Brazil

    .. grid-item-card::

        .. extref:: geocoding_geometries_map_nigeria

        Nigeria states

    .. grid-item-card::

        .. extref:: geocoding_geometries_map_greece

        Greece counties


Points
~~~~~~

:py:mod:`geom_point() <lets_plot.geom_point>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_geometries_point_kazakhstan

        Kazakhstan state centroids

    .. grid-item-card::

        .. extref:: geocoding_geometries_point_georgia

        Georgia county centroids

    .. grid-item-card::

        .. extref:: geocoding_geometries_point_greenland

        Greenland cities


Rectangles
~~~~~~~~~~

:py:mod:`geom_rect() <lets_plot.geom_rect>`

.. grid:: 3

    .. grid-item-card::

        .. extref:: geocoding_geometries_rectangle_japan

        Japan bounding box with states

    .. grid-item-card::

        .. extref:: geocoding_geometries_rectangle_ireland

        Ireland county bounding boxes

    .. grid-item-card::

        .. extref:: geocoding_geometries_rectangle_cuba

        Cuba bounding box with cities


Guides to Geocoding
-------------------

Documentation: :ref:`The Geocoding Reference Guide <advanced_geocoding>`.

An example notebook covering various geocoding use-cases: |geocoding_reference|.

.. |geocoding_reference| extref:: geocoding_reference
    :type: text
    :text: geocoding_reference.ipynb


.. include:: /python/shared/features.rst