.. _maps:

:og:description: Lets-Plot allows you to create beautiful maps just by adding an interactive basemap layer to your plot.

.. title:: Lets-Plot Maps: Interactive Basemaps for Enhanced Data Visualization

.. meta::
   :description: Lets-Plot allows you to create beautiful maps just by adding an interactive basemap layer to your plot.
   :keywords: geospatial visualization, interactive maps, ggplot2, geopandas, GeoDataFrame, basemap tiles, Lets-Plot in SciView


.. raw:: html

    <div id="maps-page">


Maps
====

Create beautiful maps just by adding an interactive basemap layer to your plot: :py:func:`geom_livemap() <lets_plot.geom_livemap>`.


Proportional Symbol Map
-----------------------

.. grid:: 2
    :class-container: wide-grid

    .. grid-item-card::

        .. extref:: map_california_housing
            :image: 4x3

    .. grid-item-card::

        .. code-block:: python

            ggplot(data) + geom_livemap() + geom_point(aes(..))


Choropleth Map
--------------

.. grid:: 2
    :class-container: wide-grid

    .. grid-item-card::

        .. extref:: covid19_india
            :image: 4x3

    .. grid-item-card::

        .. code-block:: python

            ggplot(data) + geom_livemap() + geom_polygon(aes(..))


Combine Layers on Map ``ggplot2`` Style
---------------------------------------

Quick Start
~~~~~~~~~~~

|map_quickstart|.

.. |map_quickstart| extref:: map_quickstart
    :type: text

Primitives
~~~~~~~~~~

:py:func:`point <lets_plot.geom_point>`,
:py:func:`pie <lets_plot.geom_pie>`,
:py:func:`path <lets_plot.geom_path>`,
:py:func:`tiles <lets_plot.geom_tile>`,
:py:func:`polygon <lets_plot.geom_polygon>`,
:py:func:`map <lets_plot.geom_map>`,
:py:func:`horizontal line <lets_plot.geom_hline>`,
:py:func:`vertical line <lets_plot.geom_vline>`,
:py:func:`rectangle <lets_plot.geom_rect>`,
:py:func:`segment <lets_plot.geom_segment>`,
:py:func:`curve <lets_plot.geom_curve>`,
:py:func:`text <lets_plot.geom_text>`,
:py:func:`label <lets_plot.geom_label>`,
:py:func:`pointdensity <lets_plot.geom_pointdensity>`.

|param_geodesic|.

.. |param_geodesic| extref:: param_geodesic
      :type: text

Contours
~~~~~~~~

:py:func:`contour <lets_plot.geom_contour>`,
:py:func:`filled contour <lets_plot.geom_contourf>`.

Bivariate Distribution
~~~~~~~~~~~~~~~~~~~~~~

:py:func:`2d bins <lets_plot.geom_bin2d>`,
:py:func:`2d hexagonal bins <lets_plot.geom_hex>`,
:py:func:`2d density <lets_plot.geom_density2d>`,
:py:func:`filled 2d density <lets_plot.geom_density2df>`.


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:func:`polygon <lets_plot.geom_polygon>`, :py:func:`map <lets_plot.geom_map>`, :py:func:`point <lets_plot.geom_point>`, :py:func:`pointdensity <lets_plot.geom_pointdensity>`, :py:func:`pie <lets_plot.geom_pie>`, :py:func:`text <lets_plot.geom_text>`, :py:func:`path <lets_plot.geom_path>`, :py:func:`rect <lets_plot.geom_rect>`.

Learn more: :doc:`GeoPandas Support </python/pages/geopandas>`.


Use a Basemap That is Right for You |licenses|
----------------------------------------------

.. |licenses| raw:: html

    <a class="reference internal image-reference" href="licenses.html">
      <img alt="Creative Commons License" src="https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg">
    </a>

Use quality *Lets-Plot* vector basemaps or choose among many raster map tiles available through 3rd party providers.

Learn more: :doc:`Configuring Basemap Tiles for Interactive Maps </python/pages/basemap_tiles>`.

.. grid:: 6
    :class-container: preview-gallery wide-grid

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
            :image: lets_plot_bw

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: osm_standard

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: open_topo_map

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
            :image: nasa_gibs_color_shaded

    .. grid-item-card::

        .. extref:: the_gallery_of_basemaps
            :image: nasa_gibs_greyscale


PyCharm
-------

Create maps in PyCharm with the help of `Lets-Plot in SciView <https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview>`__ plugin.

.. image:: /_static/images/pycharm_map_fr_low_65.gif


Example Notebooks
-----------------

Cookbooks:

- .. extref:: geom_livemap_interactive
    :type: text
- .. extref:: param_flat
    :type: text

Demos:

- .. extref:: titanic
    :type: text
- .. extref:: pushkin
    :type: text
- .. extref:: map_airports
    :type: text
- .. extref:: beijing
    :type: text
- .. extref:: plotting_airbnb_prices_boston
    :type: text
- .. extref:: soil_pollutants_with_gaussian_processes
    :type: text
- .. extref:: covid19_india
    :type: text
- .. extref:: cities_density
    :type: text
- .. extref:: map_california_housing
    :type: text
- .. extref:: minard
    :type: text
- .. extref:: montenegrin_independence_referendum
    :type: text


.. include:: /python/shared/features.rst


.. raw:: html

    </div>