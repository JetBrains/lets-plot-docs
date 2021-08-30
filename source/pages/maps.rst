.. _maps:

.. include:: /shared/previews.rst


Maps
====

Create beautiful maps just by adding an interactive basemap layer to your plot: :py:mod:`geom_livemap() <lets_plot.geom_livemap>`.


Proportional Symbol Map
-----------------------

.. panels::
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    |map_california_housing_4x3-datalore|

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

    |covid19_india_4x3-kaggle|

    ---
    .. code-block:: python

        ggplot(data) + geom_livemap() + geom_polygon(aes(..))


Combine Layers on Map ``ggplot2`` Style
---------------------------------------

The following ggplot2 geometries can be used with interactive maps:

|layers_primitives-icon| Primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_primitives-icon| image:: /_static/images/icons/maps/layers_primitives.png

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

.. |layers_contours-icon| image:: /_static/images/icons/maps/layers_contours.png

:py:mod:`contour <lets_plot.geom_contour>`,
:py:mod:`filled contour <lets_plot.geom_contourf>`.

|layers_bivariate-icon| Bivariate Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |layers_bivariate-icon| image:: /_static/images/icons/maps/layers_bivariate.png

:py:mod:`heatmap of 2d bin counts <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`.

|quickstart-icon| Quickstart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |quickstart-icon| image:: /_static/images/icons/maps/quickstart.png

`Quickstart guide to maps <https://datalore.jetbrains.com/view/notebook/9dzGjTQay4ENqj7GTEIvBU>`__.


Use a Basemap That is Right for You
-----------------------------------

Use quality Lets-Plot vector basemaps or choose among many raster map tiles available through 3rd party providers.

Learn more: :ref:`Configuring Basemap Tiles for Interactive Maps <basemap_tiles>`.

.. panels::
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    |the_gallery_of_basemaps-lets_plot_default-datalore|

    ---
    |the_gallery_of_basemaps-lets_plot_dark-datalore|

    ---
    |the_gallery_of_basemaps-lets_plot_light-datalore|

    ---
    |the_gallery_of_basemaps-osm_standard-datalore|

    ---
    |the_gallery_of_basemaps-open_topo_map-datalore|

    ---
    |the_gallery_of_basemaps-stamen_design_terrain-datalore|

    ---
    |the_gallery_of_basemaps-stamen_design_toner-datalore|

    ---
    |the_gallery_of_basemaps-stamen_design_toner_hybrid-datalore|

    ---
    |the_gallery_of_basemaps-stamen_design_toner_labels-datalore|

    ---
    |the_gallery_of_basemaps-stamen_design_watercolor-datalore|

    ---
    |the_gallery_of_basemaps-carto_antique-datalore|

    ---
    |the_gallery_of_basemaps-carto_dark_matter_no_labels-datalore|

    ---
    |the_gallery_of_basemaps-carto_flat_blue-datalore|

    ---
    |the_gallery_of_basemaps-carto_midnight_commander-datalore|

    ---
    |the_gallery_of_basemaps-carto_positron-datalore|

    ---
    |the_gallery_of_basemaps-carto_positron_no_labels-datalore|

    ---
    |the_gallery_of_basemaps-carto_voyager-datalore|

    ---
    |the_gallery_of_basemaps-nasa_gibs_blue_marble-datalore|

    ---
    |the_gallery_of_basemaps-nasa_gibs_color_shaded-datalore|

    ---
    |the_gallery_of_basemaps-nasa_gibs_greyscale-datalore|

PyCharm
-------

Create maps in PyCharm with the help of `Lets-Plot in SciView <https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview>`__ plugin.

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/pycharm_map_fr_low_65.gif


GeoPandas Shapes
----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |map_quickstart-datalore|

    ---
    |volcanoes_in_japan-kaggle|

    ---
    |mapping_US_household_income-kaggle|

    ---
    |map_airports-kaggle|

    ---
    |beijing-kaggle|

    ---
    |plotting_airbnb_prices_boston-medium|

    ---
    |covid19_india-kaggle|

    ---
    |map_US_household_income-datalore|

    ---
    |map_california_housing-nbviewer|

    ---
    |bigquery_gis-kaggle|

    ---
    |museums-nbviewer|

    ---
    |bar_on_livemap-nbviewer|

    ---
    |titanic-kaggle|

    ---
    |minard-nbviewer|

    ---
    |pushkin-nbviewer|

    ---
    |spb_bakeries-nbviewer|

    ---
    |maps_and_geocoding-nbviewer|

    ---
    |internet_use_and_activities-nbviewer|

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst