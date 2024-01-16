.. _charts:

.. title:: Charts in Lets-Plot

.. meta::
   :description: An overview of the basic building blocks and more complex charts provided by Lets-Plot.
   :keywords: data visualization, charts, visualization of distribution, marginal plots, visualization of errors, smoothing line, visualize time series, images, faceting, coordinate systems, EDA, geopandas, collection of plots, plot themes, plot flavors, cookbooks


Charts
======


|data-icon| Data
------------------------------

.. |data-icon| image:: /_static/images/icons/charts/data.svg


Every layer may have some data associated with it.
The "data" refers to a table of data where each row contains an observation
and each column represents a variable that describes some property of each observation.

Data in this format is sometimes referred to as tidy data, flat data, primary data, atomic data, and unit record data.

You can pass tidy data to Lets-Plot in form of a **Pandas** Dataframe, a **Polars** Dataframe or just a dictionary: |allowed_data_types|.

.. |allowed_data_types| extref:: allowed_data_types
    :type: text
    :text: example notebook


|basic-building-blocks-icon| Basic Building Blocks
--------------------------------------------------

.. |basic-building-blocks-icon| image:: /_static/images/icons/charts/basic-building-blocks.svg


Points:
:py:mod:`points <lets_plot.geom_point>`,
:py:mod:`jittered points <lets_plot.geom_jitter>`


Lines:
:py:mod:`line <lets_plot.geom_line>`,
:py:mod:`path <lets_plot.geom_path>`,
:py:mod:`diagonal line <lets_plot.geom_abline>`,
:py:mod:`horizontal line <lets_plot.geom_hline>`,
:py:mod:`vertical line <lets_plot.geom_vline>`,
:py:mod:`segment <lets_plot.geom_segment>`,
:py:mod:`spoke <lets_plot.geom_spoke>`,
:py:mod:`step-function <lets_plot.geom_step>`


Areas:
:py:mod:`area <lets_plot.geom_area>`,
:py:mod:`ribbon <lets_plot.geom_ribbon>`


Polygons:
:py:mod:`polygon <lets_plot.geom_polygon>`,
:py:mod:`map <lets_plot.geom_map>`


Tiles:
:py:mod:`tiles <lets_plot.geom_tile>`,
:py:mod:`rectangles <lets_plot.geom_rect>`,
:py:mod:`raster plot <lets_plot.geom_raster>`


Text:
:py:mod:`text <lets_plot.geom_text>`,
:py:mod:`label <lets_plot.geom_label>`

Examples:

- .. extref:: covid19_and_mobility
      :type: text
- .. extref:: bayesian_inference
      :type: text
- .. extref:: line_vs_path
      :type: text
- .. extref:: geopandas_kotlin_isl
      :type: text
- .. extref:: formatting_axes_etc
      :type: text
- .. extref:: geom_label
      :type: text
- .. extref:: geom_text_features
      :type: text
- .. extref:: map_use_crs
      :type: text
- .. extref:: aes_size_color_variadic_lines
      :type: text
- .. extref:: geom_spoke
      :type: text


|discrete-icon| Discrete
------------------------

.. |discrete-icon| image:: /_static/images/icons/charts/discrete.svg

:py:mod:`bar <lets_plot.geom_bar>`,
:py:mod:`pie <lets_plot.geom_pie>`,
:py:mod:`lollipop <lets_plot.geom_lollipop>`,
:py:mod:`boxplot <lets_plot.geom_boxplot>`

Examples:

- .. extref:: bar_geometry
      :type: text
- .. extref:: bar_annotations
      :type: text
- .. extref:: geom_pie
      :type: text
- .. extref:: geom_pie_on_map
      :type: text
- .. extref:: annotations_for_pie
      :type: text
- .. extref:: geom_pie_size_unit
      :type: text
- .. extref:: geom_pie_stroke_and_spacers
      :type: text
- .. extref:: stat_boxplot_outlier
      :type: text
- .. extref:: geom_lollipop
      :type: text
- .. extref:: stat_count2d_vars
      :type: text
- .. extref:: geom_count
      :type: text
- .. extref:: discrete_color_scales
      :type: text
      :text: Using scales
- .. extref:: colors_viridis
      :type: text
      :text: Viridis colors


|as_discrete-icon| Ordering Categories, ``as_discrete()``
---------------------------------------------------------

.. |as_discrete-icon| image:: /_static/images/icons/charts/as_discrete.svg

:py:mod:`as_discrete() <lets_plot.mapping.as_discrete>`

Learn more: :ref:`Function as_discrete() <as_discrete>`.

Examples:

- .. extref:: ordering_examples
      :type: text
- .. extref:: factor_levels
      :type: text
- .. extref:: geom_smooth_matrix
      :type: text


|contours-icon| Contours
------------------------

.. |contours-icon| image:: /_static/images/icons/charts/contours.svg

:py:mod:`contours <lets_plot.geom_contour>`,
:py:mod:`filled contours <lets_plot.geom_contourf>`

Examples:

- .. extref:: contours
      :type: text
- .. extref:: how_to_draw_curve
      :type: text


|visualization-of-distribution-icon| Visualization of Distribution
------------------------------------------------------------------

.. |visualization-of-distribution-icon| image:: /_static/images/icons/charts/visualization-of-distribution.svg

:py:mod:`histogram <lets_plot.geom_histogram>`,
:py:mod:`density <lets_plot.geom_density>`,
:py:mod:`dotplot <lets_plot.geom_dotplot>`,
:py:mod:`ydotplot <lets_plot.geom_ydotplot>`,
:py:mod:`violin <lets_plot.geom_violin>`,
:py:mod:`ridgeline <lets_plot.geom_area_ridges>`,
:py:mod:`frequency polygon <lets_plot.geom_freqpoly>`

Examples:

- .. extref:: histogram_geometry
      :type: text
- .. extref:: distributions
      :type: text
- .. extref:: dot_plots
      :type: text
- .. extref:: geom_violin
      :type: text
- .. extref:: ridgeline_plot
      :type: text
- .. extref:: netflix_movies
      :type: text
- .. extref:: y_orientation
      :type: text
- .. extref:: continuous_color_scales
      :type: text
      :text: Using scales


|stats-icon| Stats
------------------

.. |stats-icon| image:: /_static/images/icons/charts/stats.svg

:py:mod:`stat_ecdf() <lets_plot.stat_ecdf>`,
:py:mod:`stat_summary() <lets_plot.stat_summary>`,
:py:mod:`stat_summary_bin() <lets_plot.stat_summary_bin>`

Examples:

- .. extref:: stat_ecdf
      :type: text
- .. extref:: stat_summary
      :type: text
- .. extref:: stat_summary_bin
      :type: text


|function-icon| Function
------------------------

.. |function-icon| image:: /_static/images/icons/charts/function.svg

:py:mod:`function <lets_plot.geom_function>`

Examples:

- .. extref:: geom_function
      :type: text


|marginal-icon| Marginal Plots
------------------------------

.. |marginal-icon| image:: /_static/images/icons/charts/marginal.svg

:py:mod:`ggmarginal <lets_plot.ggmarginal>`

See also: :ref:`Joint Plot <bistro_joint_plot>`, :ref:`Residual Plot <bistro_residual_plot>`.

Examples:

- .. extref:: marginal_layers
      :type: text


|visualization-of-errors-icon| Visualization of Errors
------------------------------------------------------

.. |visualization-of-errors-icon| image:: /_static/images/icons/charts/visualization-of-errors.svg

:py:mod:`crossbar <lets_plot.geom_crossbar>`,
:py:mod:`errorbar <lets_plot.geom_errorbar>`,
:py:mod:`linerange <lets_plot.geom_linerange>`,
:py:mod:`pointrange <lets_plot.geom_pointrange>`

Examples:

- .. extref:: error_bars
      :type: text
- .. extref:: horizontal_geoms
      :type: text
- .. extref:: horizontal_error_bars
      :type: text


|smoothing-icon| Smoothing
--------------------------

.. |smoothing-icon| image:: /_static/images/icons/charts/smoothing.svg

:py:mod:`smoothing line <lets_plot.geom_smooth>`

Examples:

- .. extref:: scatter_plot
      :type: text
- .. extref:: geom_smooth_matrix
      :type: text


|bivariate-distribution-icon| Bivariate Distribution
----------------------------------------------------

.. |bivariate-distribution-icon| image:: /_static/images/icons/charts/bivariate-distribution.svg

:py:mod:`2d bins <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`

Examples:

- .. extref:: density_2d
      :type: text


|time_series-icon| Time Series
------------------------------

.. |time_series-icon| image:: /_static/images/icons/charts/time-series.svg

:py:mod:`scale_x_datetime() <lets_plot.scale_x_datetime>`,
:py:mod:`scale_y_datetime() <lets_plot.scale_y_datetime>`,
:py:mod:`scale_x_time() <lets_plot.scale_x_time>`,
:py:mod:`scale_y_time() <lets_plot.scale_y_time>`

Examples:

- .. extref:: scale_time
      :type: text
- .. extref:: delhi_climate
      :type: text
      :text: Time series visualizations


|images-icon| Images
--------------------

.. |images-icon| image:: /_static/images/icons/charts/images.svg

:py:mod:`geom_imshow() <lets_plot.geom_imshow>`,
:py:mod:`matrix of images <lets_plot.bistro.im.image_matrix>`

Examples:

- .. extref:: image_101
      :type: text
- .. extref:: image_extent
      :type: text
- .. extref:: image_grayscale
      :type: text
- .. extref:: image_alpha_param
      :type: text
- .. extref:: image_nan_values
      :type: text
- .. extref:: image_fisher_boat
      :type: text
      :text: "Fisher boat": 'geom_imshow()' and 'geom_raster()'
- .. extref:: ivindo_river
      :type: text
- .. extref:: map_use_crs
      :type: text
- .. extref:: image_matrix
      :type: text


|facets-icon| Facets
--------------------

.. |facets-icon| image:: /_static/images/icons/charts/facets.svg

:py:mod:`facet_grid() <lets_plot.facet_grid>`,
:py:mod:`facet_wrap() <lets_plot.facet_wrap>`

Examples:

- .. extref:: facets
      :type: text
- .. extref:: facets_free_scales
      :type: text
- .. extref:: covid19_and_mobility
      :type: text


|coordinate-systems-icon| Coordinate Systems
--------------------------------------------

.. |coordinate-systems-icon| image:: /_static/images/icons/charts/coordinate-systems.svg

:py:mod:`coord_cartesian() <lets_plot.coord_cartesian>`,
:py:mod:`coord_fixed() <lets_plot.coord_fixed>`,
:py:mod:`coord_flip() <lets_plot.coord_flip>`,
:py:mod:`coord_map() <lets_plot.coord_map>`

Examples:

- .. extref:: coordinate_systems
      :type: text
- .. extref:: flip_coordinates
      :type: text


|bistro-icon| 'bistro' Plots
----------------------------

.. |bistro-icon| image:: /_static/images/icons/charts/bistro.svg

Exploratory Data Analysis (EDA) is an open-ended, highly interactive, iterative process, whose actual steps are segments of a stubbily branching, tree-like pattern of possible actions.

Learn more about instruments for EDA in Lets-Plot: :ref:`'bistro' Plots <bistro>`.


|geopandas-icon| GeoPandas Shapes
---------------------------------

.. |geopandas-icon| image:: /_static/images/icons/charts/geopandas.svg

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`pie <lets_plot.geom_pie>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.

Examples:

- .. extref:: geopandas_kotlin_isl
      :type: text
- .. extref:: geopandas_naturalearth
      :type: text
- .. extref:: plotting_airbnb_prices_boston
      :type: text
- .. extref:: soil_pollutants_with_gaussian_processes
      :type: text
- .. extref:: ivindo_river
      :type: text
- .. extref:: projection_provided
      :type: text


|grouping-plots-icon| Grouping Plots
------------------------------------

.. |grouping-plots-icon| image:: /_static/images/icons/charts/grouping-plots.svg

:py:mod:`GGBunch <lets_plot.GGBunch>` and :py:mod:`gggrid <lets_plot.gggrid>` shows a collection of plots on one figure.

Examples:

- .. extref:: ggbunch
      :type: text
- .. extref:: plot_grid
      :type: text
- .. extref:: gggrid_theme
      :type: text
- .. extref:: gggrid_scale_share
      :type: text


|presentation-options-icon| Presentation Options
------------------------------------------------

.. |presentation-options-icon| image:: /_static/images/icons/charts/presentation-options.svg

:py:mod:`theme() <lets_plot.theme>`,
:py:mod:`ggtitle() <lets_plot.ggtitle>`,
:py:mod:`ggsize() <lets_plot.ggsize>`,
:py:mod:`xlab() <lets_plot.xlab>`,
:py:mod:`ylab() <lets_plot.ylab>`,
:py:mod:`labs() <lets_plot.labs>`,
:py:mod:`guide_legend() <lets_plot.guide_legend>`,
:py:mod:`guide_colorbar() <lets_plot.guide_colorbar>`

Predefined themes:

:py:mod:`minimal2 <lets_plot.theme_minimal2>`,
:py:mod:`bw <lets_plot.theme_bw>`,
:py:mod:`grey <lets_plot.theme_grey>`,
:py:mod:`classic <lets_plot.theme_classic>`,
:py:mod:`light <lets_plot.theme_light>`,
:py:mod:`minimal <lets_plot.theme_minimal>`,
:py:mod:`void <lets_plot.theme_void>`,
:py:mod:`none <lets_plot.theme_none>`

.. panels::
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: complete_themes
        :image: minimal2

    ---
    .. extref:: complete_themes
        :image: bw

    ---
    .. extref:: complete_themes
        :image: grey

    ---
    .. extref:: complete_themes
        :image: classic

    ---
    .. extref:: complete_themes
        :image: light

    ---
    .. extref:: complete_themes
        :image: minimal

Color schemes (flavors):

:py:mod:`darcula <lets_plot.flavor_darcula>`,
:py:mod:`solarized light <lets_plot.flavor_solarized_light>`,
:py:mod:`solarized dark <lets_plot.flavor_solarized_dark>`,
:py:mod:`high contrast light <lets_plot.flavor_high_contrast_light>`,
:py:mod:`high contrast dark <lets_plot.flavor_high_contrast_dark>`

.. extref:: flavors
  :image: common
  :width: 1000
  :height: 117

Examples:

- .. extref:: default_theme
      :type: text
- .. extref:: themes
      :type: text
- .. extref:: geom_theme_colors
      :type: text
- .. extref:: theme_flavors
      :type: text
- .. extref:: gggrid_theme
      :type: text
- .. extref:: legend_and_axis
      :type: text
- .. extref:: margins
      :type: text
- .. extref:: legend_text_multiline
      :type: text
- .. extref:: tooltip_config
      :type: text
- .. extref:: title_subtitle_caption
      :type: text
- .. extref:: tooltips_theme
      :type: text
- .. extref:: set_font_faces
      :type: text
- .. extref:: panel_border
      :type: text
- .. extref:: axis_position
      :type: text
- .. extref:: axis_text_angle
      :type: text
- .. extref:: theme_plot_message
      :type: text
- .. extref:: superscript_exponent
      :type: text
- .. extref:: theme_label_text
      :type: text


Cookbooks
---------

- .. extref:: lets_plot_cheatbook
      :type: text
      :text: Lets-Plot API overview
- .. extref:: multiple_color_scales
      :type: text
- .. extref:: quantile_parameters
      :type: text
- .. extref:: scale_functions
      :type: text
- .. extref:: position_stack
      :type: text


Resources
---------

- :ref:`EDA Examples <eda>`
- `Picking the Perfect Data Visualization: Line Plots <https://blog.jetbrains.com/dataspell/2023/02/picking-the-perfect-data-visualization-line-plots/>`__
- `Picking the Perfect Data Visualization: Barplots <https://blog.jetbrains.com/dataspell/2023/03/picking-the-perfect-data-visualization-barplots/>`__

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/coding_for_economists.png
        :target: https://aeturrell.github.io/coding-for-economists

    ---
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    Coding for Economists is a guide for economists on what programming is, why it’s useful, and how to do it.

    In the `Easy Data Visualisation for Tidy Data with Lets-Plot <https://aeturrell.github.io/coding-for-economists/vis-letsplot.html>`__ section you’ll see how to make plots quickly using the declarative plotting.

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/Python4DS.png
        :target: https://aeturrell.github.io/python4DS/

    ---
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    This book will walk you through the main tools and techniques of data science in Python: importing, cleaning, transforming, and visualizing data.

    In the `visualization chapter <https://aeturrell.github.io/python4DS/data-visualise.html>`__ you will find easy-to-read and comprehensive guides to data visualization using the Lets-Plot package.


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    .. extref:: covid19_and_mobility

    ---
    .. extref:: delhi_climate

    ---
    .. extref:: google_play_store

    ---
    .. extref:: malnutrition

    ---
    .. extref:: netflix

    ---
    .. extref:: geopandas_kotlin_isl

    ---
    .. extref:: geopandas_naturalearth

    ---
    .. extref:: nobel

    ---
    .. extref:: bbc_cookbook

    ---
    .. extref:: bayesian_inference

    ---
    .. extref:: post_punk_remake

    ---
    .. extref:: correlation_plot

    ---
    .. extref:: plotting_airbnb_prices_boston

    ---
    .. extref:: mandelbulbs

    ---
    .. extref:: ivindo_river

    ---
    .. extref:: how_to_draw_curve

    ---
    .. extref:: world_happiness

    ---
    .. extref:: world_coloring

    ---
    .. extref:: kernels_visualization

    ---
    .. extref:: torus

    ---
    .. extref:: klein_bottle

    ---
    .. extref:: nyc_metro

    ---
    .. extref:: google_suggestions

    ---
    .. extref:: mosaic_image

    ---
    .. extref:: marginal_layers

    ---
    .. extref:: map_use_crs

    ---
    .. extref:: new_zealand_dem_remake

    ---
    .. extref:: world_values_survey

    ---
    .. extref:: holidays_2023_eda

    ---
    .. extref:: joyplot

    ---
    .. extref:: scale_params_with_dict


.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst