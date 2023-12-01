.. _maps:

.. title:: Maps in Lets-Plot


Maps
====

Create beautiful maps just by adding an interactive basemap layer to your plot: :py:mod:`geom_livemap() <lets_plot.geom_livemap>`.


Proportional Symbol Map
-----------------------

.. grid:: 2

    .. grid-item-card::

        .. extref:: map_california_housing
            :image: 4x3

    .. grid-item-card::

        .. code-block:: python

            ggplot(data) + geom_livemap() + \
                geom_point(aes(..))


Choropleth Map
--------------

.. grid:: 2

    .. grid-item-card::

        .. extref:: covid19_india
            :image: 4x3

    .. grid-item-card::

        .. code-block:: python

            ggplot(data) + geom_livemap() + \
                geom_polygon(aes(..))


Combine Layers on Map ``ggplot2`` Style
---------------------------------------

|quickstart-icon| Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |quickstart-icon| image:: /_static/images/icons/maps/quickstart.svg

|map_quickstart|.

.. |map_quickstart| extref:: map_quickstart
    :type: text

|layers_primitives-icon| Primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_primitives-icon| image:: /_static/images/icons/maps/layers_primitives.svg

:py:mod:`point <lets_plot.geom_point>`,
:py:mod:`pie <lets_plot.geom_pie>`,
:py:mod:`path <lets_plot.geom_path>`,
:py:mod:`tiles <lets_plot.geom_tile>`,
:py:mod:`polygon <lets_plot.geom_polygon>`,
:py:mod:`map <lets_plot.geom_map>`,
:py:mod:`horizontal line <lets_plot.geom_hline>`,
:py:mod:`vertical line <lets_plot.geom_vline>`,
:py:mod:`rectangle <lets_plot.geom_rect>`,
:py:mod:`segment <lets_plot.geom_segment>`,
:py:mod:`text <lets_plot.geom_text>`,
:py:mod:`label <lets_plot.geom_label>`.

|param_geodesic|.

.. |param_geodesic| extref:: param_geodesic
      :type: text

|layers_contours-icon| Contours
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_contours-icon| image:: /_static/images/icons/maps/layers_contours.svg

:py:mod:`contour <lets_plot.geom_contour>`,
:py:mod:`filled contour <lets_plot.geom_contourf>`.

|layers_bivariate-icon| Bivariate Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_bivariate-icon| image:: /_static/images/icons/maps/layers_bivariate.svg

:py:mod:`2d bins <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`.


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`pie <lets_plot.geom_pie>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.


Use a Basemap That is Right for You |licenses|
----------------------------------------------

.. |licenses| raw:: html

    <a class="reference internal image-reference" href="licenses.html">
      <img alt="Creative Commons License" src="https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg">
    </a>

Use quality Lets-Plot vector basemaps or choose among many raster map tiles available through 3rd party providers.

Learn more: :ref:`Configuring Basemap Tiles for Interactive Maps <basemap_tiles>`.

.. grid:: 6

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: lets_plot_default

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: lets_plot_dark

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: lets_plot_light

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: osm_standard

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: open_topo_map

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: stamen_design_terrain

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: stamen_design_toner

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: stamen_design_toner_hybrid

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: stamen_design_toner_labels

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: stamen_design_watercolor

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_antique

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_dark_matter_no_labels

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_flat_blue

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_midnight_commander

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_positron

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_positron_no_labels

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: carto_voyager

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: nasa_gibs_blue_marble

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: nasa_gibs_color_shaded

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: nasa_gibs_greyscale


PyCharm
-------

Create maps in PyCharm with the help of `Lets-Plot in SciView <https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview>`__ plugin.

.. image:: /_static/images/pycharm_map_fr_low_65.gif


Examples
--------

.. grid:: 4
    :class-container: preview-gallery

    .. grid-item-card::

        .. extref:: volcanoes_in_japan

    .. grid-item-card::

        .. extref:: mapping_us_household_income

    .. grid-item-card::

        .. extref:: soil_pollutants_with_gaussian_processes

    .. grid-item-card::

        .. extref:: map_airports

    .. grid-item-card::

        .. extref:: beijing

    .. grid-item-card::

        .. extref:: plotting_airbnb_prices_boston
            :ref: medium

    .. grid-item-card::

        .. extref:: covid19_india

    .. grid-item-card::

        .. extref:: map_us_household_income

    .. grid-item-card::

        .. extref:: map_california_housing

    .. grid-item-card::

        .. extref:: bigquery_gis

    .. grid-item-card::

        .. extref:: museums

    .. grid-item-card::

        .. extref:: titanic

    .. grid-item-card::

        .. extref:: minard

    .. grid-item-card::

        .. extref:: pushkin

    .. grid-item-card::

        .. extref:: spb_bakeries

    .. grid-item-card::

        .. extref:: travel_the_world

    .. grid-item-card::

        .. extref:: map_quickstart

    .. grid-item-card::

        .. extref:: maps_and_geocoding

    .. grid-item-card::

        .. extref:: internet_use_and_activities

    .. grid-item-card::

        .. extref:: param_flat

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst