.. _interactive_maps:

.. include:: /shared/previews.rst

Build an Interactive Maps with Lets-Plot
========================================

.. panels::
    :container: + page-demo
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    :body: text-center

    Try the demo notebook with interactive maps right now:

    .. image:: https://mybinder.org/badge_logo.svg
        :target: https://mybinder.org/v2/gh/HIL-HK/lets-plot-examples/master?filepath=demo%2Fmuseums.ipynb
        :width: 100%

    (it's free and no need to sign-up)

    ---
    :column: col-lg-8 col-md-4 col-sm-6 col-xs-12 p-2

    |museums_4x3-nbviewer|


Livemap Geometry
----------------

Lets-Plot supports interactive maps via the ``geom_livemap()`` geom layer which enables a researcher to visualize geospatial information on a zoomable and paneble map.

When building interactive geospatial visualizations with Lets-Plot the visualisation workflow remains the same as when building a regular ggplot2 plot.

.. panels::
    :container: + previews-picker-window id-1
    :column: col-lg-12 p-2

    |maps_and_geocoding_4x3-nbviewer|

.. panels::
    :container: + previews-picker-content id-1
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |maps_and_geocoding-nbviewer|

    ---
    |bigquery_gis-kaggle|

    ---
    |map_california_housing-nbviewer|

    ---
    |museums-nbviewer|


Built-In Geocoding
------------------

Geocoding is the process of converting names of places into geographic coordinates.

The Lets-Plot has built-in geocoding capabilities covering the folloing administrative levels: *countries*, *states* (US and non-US equivalents), *counties* (and equivalents), *cities* (and towns).

Learn more: :ref:`Geocoding <geocoding>`.

.. panels::
    :container: + previews-picker-window id-2
    :column: col-lg-12 p-2

    |geocoding_examples_4x3-nbviewer|

.. panels::
    :container: + previews-picker-content id-2
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_examples-nbviewer|

    ---
    |map_US_household_income-nbviewer|

    ---
    |titanic-kaggle|


Joining Map Coordinates with Data
---------------------------------

Use ``map_join`` parameter to join map coordinates with data.

.. panels::
    :container: + previews-picker-window id-3
    :column: col-lg-12 p-2

    |internet_use_and_activities_4x3-nbviewer|

.. panels::
    :container: + previews-picker-content id-3
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |internet_use_and_activities-nbviewer|

    ---
    |plotting_airbnb_prices_boston-datalore|

    ---
    |map_US_household_income-nbviewer|


Combining Maps with Geometries
------------------------------

``geom_livemap()`` has built-in markers used for displaying the data. Besides you can append as many additional layers with various geometries as you need.

.. panels::
    :container: + previews-picker-window id-4
    :column: col-lg-12 p-2

    |bar_on_livemap_4x3-nbviewer|

.. panels::
    :container: + previews-picker-content id-4
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |bar_on_livemap-nbviewer|

    ---
    |minard-nbviewer|

    ---
    |spb_bakeries-nbviewer|

    ---
    |pushkin-nbviewer|


Built-In and 3d-Party Tiles
---------------------------

Change themes and use external tile services to diversify your maps.

.. panels::
    :container: + previews-picker-window id-5
    :column: col-lg-12 p-2

    |the_gallery_of_basemaps_4x3-kaggle|

.. panels::
    :container: + previews-picker-content id-5
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |the_gallery_of_basemaps-kaggle|

    ---
    |beijing-kaggle|

    ---
    |map_airports-kaggle|

    ---
    |titanic-kaggle|


GeoPandas Support
-----------------

All GeoPandas shapes are "undersood" by Lets-Plot and can be plotted using various geometry layers, depending on the type of the shape.

.. panels::
    :container: + previews-picker-window id-6
    :column: col-lg-12 p-2

    |plotting_airbnb_prices_boston_4x3-datalore|

.. panels::
    :container: + previews-picker-content id-6
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |plotting_airbnb_prices_boston-datalore|

    ---
    |bigquery_gis-kaggle|

    ---
    |spb_bakeries-nbviewer|

    ---
    |beijing-kaggle|