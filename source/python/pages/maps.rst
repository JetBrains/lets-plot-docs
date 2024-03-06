.. _maps:

:og:description: Lets-Plot allows you to create beautiful maps just by adding an interactive basemap layer to your plot.

.. title:: Lets-Plot Maps: Interactive Basemaps for Enhanced Data Visualization

.. meta::
   :description: Lets-Plot allows you to create beautiful maps just by adding an interactive basemap layer to your plot.
   :keywords: geospatial visualization, interactive maps, ggplot2, geopandas, GeoDataFrame, basemap tiles, Lets-Plot in SciView


Maps
====

Create beautiful maps just by adding an interactive basemap layer to your plot: :py:mod:`geom_livemap() <lets_plot.geom_livemap>`.


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

|quickstart-light| |quickstart-dark| Quick Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |quickstart-light| image:: /_static/images/icons/maps/quickstart-light.svg
    :class: only-light

.. |quickstart-dark| image:: /_static/images/icons/maps/quickstart-dark.svg
    :class: only-dark

|map_quickstart|.

.. |map_quickstart| extref:: map_quickstart
    :type: text

|layers_primitives-light| |layers_primitives-dark| Primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_primitives-light| image:: /_static/images/icons/maps/layers_primitives-light.svg
    :class: only-light

.. |layers_primitives-dark| image:: /_static/images/icons/maps/layers_primitives-dark.svg
    :class: only-dark

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
:py:mod:`curve <lets_plot.geom_curve>`,
:py:mod:`text <lets_plot.geom_text>`,
:py:mod:`label <lets_plot.geom_label>`.

|param_geodesic|.

.. |param_geodesic| extref:: param_geodesic
      :type: text

|layers_contours-light| |layers_contours-dark| Contours
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_contours-light| image:: /_static/images/icons/maps/layers_contours-light.svg
    :class: only-light

.. |layers_contours-dark| image:: /_static/images/icons/maps/layers_contours-dark.svg
    :class: only-dark

:py:mod:`contour <lets_plot.geom_contour>`,
:py:mod:`filled contour <lets_plot.geom_contourf>`.

|layers_bivariate-light| |layers_bivariate-dark| Bivariate Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_bivariate-light| image:: /_static/images/icons/maps/layers_bivariate-light.svg
    :class: only-light

.. |layers_bivariate-dark| image:: /_static/images/icons/maps/layers_bivariate-dark.svg
    :class: only-dark

:py:mod:`2d bins <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`.


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`pie <lets_plot.geom_pie>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :doc:`GeoPandas Support </python/pages/geopandas>`.


Use a Basemap That is Right for You |licenses|
----------------------------------------------

.. |licenses| raw:: html

    <a class="reference internal image-reference" href="licenses.html">
      <img alt="Creative Commons License" src="https://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg">
    </a>

Use quality Lets-Plot vector basemaps or choose among many raster map tiles available through 3rd party providers.

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


.. include:: /python/shared/features.rst