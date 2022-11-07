.. _maps:

.. title:: Maps in Lets-Plot


Maps
====

Create beautiful maps just by adding an interactive basemap layer to your plot: :py:mod:`geom_livemap() <lets_plot.geom_livemap>`.


Proportional Symbol Map
-----------------------

.. panels::
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: map_california_housing
        :image: 4x3

    ---
    .. code-block:: python

        ggplot(data) + geom_livemap(aes(..), symbol='point')

    .. raw:: html

        <div class="text-center">or</div>

    .. code-block:: python

        ggplot(data) + geom_livemap() + geom_point(aes(..))


Choropleth Map
--------------

.. panels::
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: covid19_india
        :image: 4x3

    ---
    .. code-block:: python

        ggplot(data) + geom_livemap() + geom_polygon(aes(..))


Combine Layers on Map ``ggplot2`` Style
---------------------------------------

The following ggplot2 geometries can be used with interactive maps:

|layers_primitives-icon| Primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_primitives-icon| image:: /_static/images/icons/maps/layers_primitives.svg

:py:mod:`point <lets_plot.geom_point>`,
:py:mod:`path <lets_plot.geom_path>`,
:py:mod:`tiles <lets_plot.geom_tile>`,
:py:mod:`polygon <lets_plot.geom_polygon>`,
:py:mod:`map <lets_plot.geom_map>`,
:py:mod:`horizontal line <lets_plot.geom_hline>`,
:py:mod:`vertical line <lets_plot.geom_vline>`,
:py:mod:`rectangle <lets_plot.geom_rect>`,
:py:mod:`segment <lets_plot.geom_segment>`,
:py:mod:`text <lets_plot.geom_text>`.

|layers_contours-icon| Contours
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_contours-icon| image:: /_static/images/icons/maps/layers_contours.svg

:py:mod:`contour <lets_plot.geom_contour>`,
:py:mod:`filled contour <lets_plot.geom_contourf>`.

|layers_bivariate-icon| Bivariate Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_bivariate-icon| image:: /_static/images/icons/maps/layers_bivariate.svg

:py:mod:`heatmap of 2d bin counts <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`.

|quickstart-icon| Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |quickstart-icon| image:: /_static/images/icons/maps/quickstart.svg

|map_quickstart|.

.. |map_quickstart| extref:: map_quickstart
    :type: text


Use a Basemap That is Right for You |licenses|
----------------------------------------------

.. |licenses| raw:: html

    <a class="reference internal image-reference" href="licenses.html">
      <img alt="Creative Commons License" src="https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg">
    </a>

Use quality Lets-Plot vector basemaps or choose among many raster map tiles available through 3rd party providers.

Learn more: :ref:`Configuring Basemap Tiles for Interactive Maps <basemap_tiles>`.

.. panels::
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: the_gallery_of_basemaps
        :image: lets_plot_default

    ---
    .. extref:: the_gallery_of_basemaps
        :image: lets_plot_dark

    ---
    .. extref:: the_gallery_of_basemaps
        :image: lets_plot_light

    ---
    .. extref:: the_gallery_of_basemaps
        :image: osm_standard

    ---
    .. extref:: the_gallery_of_basemaps
        :image: open_topo_map

    ---
    .. extref:: the_gallery_of_basemaps
        :image: stamen_design_terrain

    ---
    .. extref:: the_gallery_of_basemaps
        :image: stamen_design_toner

    ---
    .. extref:: the_gallery_of_basemaps
        :image: stamen_design_toner_hybrid

    ---
    .. extref:: the_gallery_of_basemaps
        :image: stamen_design_toner_labels

    ---
    .. extref:: the_gallery_of_basemaps
        :image: stamen_design_watercolor

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_antique

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_dark_matter_no_labels

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_flat_blue

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_midnight_commander

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_positron

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_positron_no_labels

    ---
    .. extref:: the_gallery_of_basemaps
        :image: carto_voyager

    ---
    .. extref:: the_gallery_of_basemaps
        :image: nasa_gibs_blue_marble

    ---
    .. extref:: the_gallery_of_basemaps
        :image: nasa_gibs_color_shaded

    ---
    .. extref:: the_gallery_of_basemaps
        :image: nasa_gibs_greyscale


PyCharm
-------

Create maps in PyCharm with the help of `Lets-Plot in SciView <https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview>`__ plugin.

.. image:: /_static/images/pycharm_map_fr_low_65.gif


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.

Examples:

- .. extref:: soil_pollutants_with_gaussian_processes
      :type: text
- .. extref:: ivindo_river
      :type: text


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: map_quickstart

    ---
    .. extref:: volcanoes_in_japan

    ---
    .. extref:: mapping_us_household_income

    ---
    .. extref:: soil_pollutants_with_gaussian_processes

    ---
    .. extref:: map_airports

    ---
    .. extref:: beijing

    ---
    .. extref:: plotting_airbnb_prices_boston
        :ref: medium

    ---
    .. extref:: covid19_india

    ---
    .. extref:: map_us_household_income

    ---
    .. extref:: map_california_housing

    ---
    .. extref:: bigquery_gis

    ---
    .. extref:: museums

    ---
    .. extref:: titanic

    ---
    .. extref:: minard

    ---
    .. extref:: pushkin

    ---
    .. extref:: spb_bakeries

    ---
    .. extref:: travel_the_world

    ---
    .. extref:: maps_and_geocoding

    ---
    .. extref:: internet_use_and_activities

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst