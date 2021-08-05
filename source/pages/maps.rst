.. _maps:

.. include:: /shared/previews.rst


Maps
====


Livemap
-------

Lets-Plot supports interactive maps via the :py:mod:`geom_livemap() <lets_plot.geom_livemap>` geom layer which enables a researcher to visualize geospatial information on a zoomable and paneble map.

.. panels::
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    |maps_and_geocoding-nbviewer|

    ---
    |bar_on_livemap-nbviewer|

    ---
    |map_california_housing-nbviewer|

    ---
    |map_US_household_income-nbviewer|

    ---
    |the_gallery_of_basemaps-kaggle|

    ---
    |bigquery_gis-kaggle|


Choropleth Map
--------------

Choropleth maps provide an easy way to visualize how a variable varies across a geographic area or show the level of variability within a region.

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |maps_and_geocoding-nbviewer|

    ---
    |map_US_household_income-nbviewer|


Symbol Map
----------

Parameter ``symbol`` of the ``geom_livemap()`` is used to set a marker for displaying the data. There are three types of markers:

- ``"point"`` for circles of different size and color;
- ``"pie"`` for pie charts;
- ``"bar"`` for bar charts.

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |bar_on_livemap-nbviewer|


Integration with Grammar of Graphics
------------------------------------

When building interactive geospatial visualizations with Lets-Plot the visualisation workflow remains the same as when building a regular ggplot2 plot.

However, ``geom_livemap()`` creates an interactive base-map super-layer and certain limitations do apply comparing to a regular ggplot2 geom-layer:

- ``geom_livemap()`` must be added as a 1-st layer in plot;
- Maximum one ``geom_livemap()`` layer is alloed per plot;
- Not any type of geometry can be combined with interactive map layer in one plot;
- Internet connection to map tiles provider is required.

The following ggplot2 geometries can be used with interactive maps: :py:mod:`point <lets_plot.geom_point>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`heatmap of 2d bin counts <lets_plot.geom_bin2d>`, :py:mod:`tiles <lets_plot.geom_tile>`, :py:mod:`contour <lets_plot.geom_contour>`, :py:mod:`filled contour <lets_plot.geom_contourf>`, :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`horizontal line <lets_plot.geom_hline>`, :py:mod:`vertical line <lets_plot.geom_vline>`, :py:mod:`2d density <lets_plot.geom_density2d>`, :py:mod:`filled 2d density <lets_plot.geom_density2df>`, :py:mod:`rectangle <lets_plot.geom_rect>`, :py:mod:`segment <lets_plot.geom_segment>` and :py:mod:`text <lets_plot.geom_text>`.

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |maps_and_geocoding-nbviewer|

    ---
    |map_california_housing-nbviewer|

    ---
    |map_US_household_income-nbviewer|

    ---
    |bigquery_gis-kaggle|


Built-In and 3d-Party Tiles
---------------------------

:py:mod:`maptiles_zxy() <lets_plot.maptiles_zxy>` and :py:mod:`maptiles_lets_plot() <lets_plot.maptiles_lets_plot>` functions are designed to help you to change themes and use external tile services to diversify your maps.

.. panels::
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    |the_gallery_of_basemaps-lets_plot_default-kaggle|

    ---
    |the_gallery_of_basemaps-lets_plot_dark-kaggle|

    ---
    |the_gallery_of_basemaps-lets_plot_light-kaggle|

    ---
    |the_gallery_of_basemaps-osm_standard-kaggle|

    ---
    |the_gallery_of_basemaps-open_topo_map-kaggle|

    ---
    |the_gallery_of_basemaps-stamen_design_terrain-kaggle|

    ---
    |the_gallery_of_basemaps-stamen_design_toner-kaggle|

    ---
    |the_gallery_of_basemaps-stamen_design_toner_hybrid-kaggle|

    ---
    |the_gallery_of_basemaps-stamen_design_toner_labels-kaggle|

    ---
    |the_gallery_of_basemaps-stamen_design_watercolor-kaggle|

    ---
    |the_gallery_of_basemaps-carto_antique-kaggle|

    ---
    |the_gallery_of_basemaps-carto_dark_matter_no_labels-kaggle|

    ---
    |the_gallery_of_basemaps-carto_flat_blue-kaggle|

    ---
    |the_gallery_of_basemaps-carto_midnight_commander-kaggle|

    ---
    |the_gallery_of_basemaps-carto_positron-kaggle|

    ---
    |the_gallery_of_basemaps-carto_positron_no_labels-kaggle|

    ---
    |the_gallery_of_basemaps-carto_voyager-kaggle|

    ---
    |the_gallery_of_basemaps-nasa_gibs_blue_marble-kaggle|

    ---
    |the_gallery_of_basemaps-nasa_gibs_color_shaded-kaggle|

    ---
    |the_gallery_of_basemaps-nasa_gibs_greyscale-kaggle|


PyCharm
-------

Plugin "Lets-Plot in SciView" is available at the JetBrains Plugin Repository.

The plugin adds support for interactive plots in IntelliJ-based IDEs with the enabled `Scientific mode <https://www.jetbrains.com/help/pycharm/matplotlib-support.html>`__.

Through the plugin an interactive map is available in the "Plots" window:

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/pycharm_map_fr_low_65.gif


Geospatial
----------

All GeoPandas shapes are "undersood" by Lets-Plot and can be plotted using various geometry layers, depending on the type of the shape:

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |bigquery_gis-kaggle|

To join map coordinates with data use the ``map_join`` parameter:

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |map_US_household_income-nbviewer|


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |beijing-kaggle|

    ---
    |covid19_india-kaggle|

    ---
    |internet_use_and_activities-nbviewer|

    ---
    |map_airports-kaggle|

    ---
    |mapping_US_household_income-kaggle|

    ---
    |minard-nbviewer|

    ---
    |museums-nbviewer|

    ---
    |plotting_airbnb_prices_boston-datalore|

    ---
    |spb_bakeries-nbviewer|

    ---
    |titanic-kaggle|

    ---
    |pushkin-nbviewer|

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst