.. _charts:

:og:description: An overview of the basic building blocks and more complex charts provided by Lets-Plot.

.. title:: Lets-Plot Charts: From Basics to Advanced Visualizations

.. meta::
   :description: An overview of the basic building blocks and more complex charts provided by Lets-Plot.
   :keywords: data visualization, charts, visualization of distribution, marginal plots, visualization of errors, smoothing line, visualize time series, images, faceting, coordinate systems, EDA, pandas DataFrame, polars DataFrame, geopandas GeoDataFrame, collection of plots, plot themes, plot flavors, cookbooks


Charts
======


|l1| |d1| Data
--------------

.. |l1| image:: /_static/images/icons/charts/data-light.svg
    :class: only-light

.. |d1| image:: /_static/images/icons/charts/data-dark.svg
    :class: only-dark


Every layer may have some data associated with it.
The "data" refers to a table of data where each row contains an observation
and each column represents a variable that describes some property of each observation.

Data in this format is sometimes referred to as tidy data, flat data, primary data, atomic data, and unit record data.

You can pass tidy data to *Lets-Plot* in form of a **Pandas** Dataframe, a **Polars** Dataframe or just a dictionary: |allowed_data_types|.

.. |allowed_data_types| extref:: allowed_data_types
    :type: text
    :text: example notebook


|l2| |d2| Basic Building Blocks
-------------------------------

.. |l2| image:: /_static/images/icons/charts/basic-building-blocks-light.svg
    :class: only-light

.. |d2| image:: /_static/images/icons/charts/basic-building-blocks-dark.svg
    :class: only-dark


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
:py:mod:`curve <lets_plot.geom_curve>`,
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
- .. extref:: graph_edges
      :type: text
- .. extref:: formatting_axes_etc
      :type: text
- .. extref:: text_geoms
      :type: text
- .. extref:: map_use_crs
      :type: text
- .. extref:: aes_size_color_variadic_lines
      :type: text
- .. extref:: geom_spoke
      :type: text
- .. extref:: geom_curve
      :type: text


|l3| |d3| Discrete
------------------

.. |l3| image:: /_static/images/icons/charts/discrete-light.svg
    :class: only-light

.. |d3| image:: /_static/images/icons/charts/discrete-dark.svg
    :class: only-dark

:py:mod:`bar <lets_plot.geom_bar>`,
:py:mod:`pie <lets_plot.geom_pie>`,
:py:mod:`lollipop <lets_plot.geom_lollipop>`,
:py:mod:`boxplot <lets_plot.geom_boxplot>`,
:py:mod:`count <lets_plot.geom_count>`/:py:mod:`sum <lets_plot.stat_sum>`

.. raw:: html

  <p>
    Learn more:
    <a class="reference internal" href="as_discrete.html">Working with Categorical Variables and the <strong class="code-like">as_discrete()</strong> Function</a>.
  </p>

Examples:

- .. extref:: bar_geometry
      :type: text
- .. extref:: geom_pie
      :type: text
- .. extref:: annotations_page
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
- .. extref:: ordering_examples
      :type: text


|l4| |d4| Contours
------------------

.. |l4| image:: /_static/images/icons/charts/contours-light.svg
    :class: only-light

.. |d4| image:: /_static/images/icons/charts/contours-dark.svg
    :class: only-dark

:py:mod:`contours <lets_plot.geom_contour>`,
:py:mod:`filled contours <lets_plot.geom_contourf>`

Examples:

- .. extref:: contours
      :type: text
- .. extref:: how_to_draw_curve
      :type: text


|l5| |d5| Visualization of Distribution
---------------------------------------

.. |l5| image:: /_static/images/icons/charts/visualization-of-distribution-light.svg
    :class: only-light

.. |d5| image:: /_static/images/icons/charts/visualization-of-distribution-dark.svg
    :class: only-dark

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


|l6| |d6| Stats
---------------

.. |l6| image:: /_static/images/icons/charts/stats-light.svg
    :class: only-light

.. |d6| image:: /_static/images/icons/charts/stats-dark.svg
    :class: only-dark

:py:mod:`stat_ecdf() <lets_plot.stat_ecdf>`,
:py:mod:`stat_summary() <lets_plot.stat_summary>`,
:py:mod:`stat_summary_bin() <lets_plot.stat_summary_bin>`

Examples:

- .. extref:: stats
      :type: text
- .. extref:: stat_ecdf
      :type: text
- .. extref:: stat_summary
      :type: text
- .. extref:: stat_summary_bin
      :type: text


|l7| |d7| Function
------------------

.. |l7| image:: /_static/images/icons/charts/function-light.svg
    :class: only-light

.. |d7| image:: /_static/images/icons/charts/function-dark.svg
    :class: only-dark

:py:mod:`function <lets_plot.geom_function>`

Examples:

- .. extref:: geom_function
      :type: text


|l8| |d8| Visualization of Errors
---------------------------------

.. |l8| image:: /_static/images/icons/charts/visualization-of-errors-light.svg
    :class: only-light

.. |d8| image:: /_static/images/icons/charts/visualization-of-errors-dark.svg
    :class: only-dark

:py:mod:`crossbar <lets_plot.geom_crossbar>`,
:py:mod:`errorbar <lets_plot.geom_errorbar>`,
:py:mod:`linerange <lets_plot.geom_linerange>`,
:py:mod:`pointrange <lets_plot.geom_pointrange>`

Examples:

- .. extref:: vertical_intervals
      :type: text


|l9| |d9| Smoothing
-------------------

.. |l9| image:: /_static/images/icons/charts/smoothing-light.svg
    :class: only-light

.. |d9| image:: /_static/images/icons/charts/smoothing-dark.svg
    :class: only-dark

:py:mod:`smoothing line <lets_plot.geom_smooth>`

Examples:

- .. extref:: scatter_plot
      :type: text
- .. extref:: geom_smooth_matrix
      :type: text


|l10| |d10| Bivariate Distribution
----------------------------------

.. |l10| image:: /_static/images/icons/charts/bivariate-distribution-light.svg
    :class: only-light

.. |d10| image:: /_static/images/icons/charts/bivariate-distribution-dark.svg
    :class: only-dark

:py:mod:`2d bins <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`

Examples:

- .. extref:: density_2d
      :type: text


|l11| |d11| Marginal Plots
--------------------------

.. |l11| image:: /_static/images/icons/charts/marginal-light.svg
    :class: only-light

.. |d11| image:: /_static/images/icons/charts/marginal-dark.svg
    :class: only-dark

:py:mod:`ggmarginal <lets_plot.ggmarginal>`

See also: :ref:`Joint Plot <bistro_joint_plot>`, :ref:`Residual Plot <bistro_residual_plot>`.

Examples:

- .. extref:: marginal_layers
      :type: text


|l12| |d12| Time Series
-----------------------

.. |l12| image:: /_static/images/icons/charts/time-series-light.svg
    :class: only-light

.. |d12| image:: /_static/images/icons/charts/time-series-dark.svg
    :class: only-dark

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


|l13| |d13| Images
------------------

.. |l13| image:: /_static/images/icons/charts/images-light.svg
    :class: only-light

.. |d13| image:: /_static/images/icons/charts/images-dark.svg
    :class: only-dark

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


|l14| |d14| Facets
------------------

.. |l14| image:: /_static/images/icons/charts/facets-light.svg
    :class: only-light

.. |d14| image:: /_static/images/icons/charts/facets-dark.svg
    :class: only-dark

:py:mod:`facet_grid() <lets_plot.facet_grid>`,
:py:mod:`facet_wrap() <lets_plot.facet_wrap>`

Examples:

- .. extref:: facets
      :type: text
- .. extref:: covid19_and_mobility
      :type: text


|l15| |d15| Coordinate Systems
------------------------------

.. |l15| image:: /_static/images/icons/charts/coordinate-systems-light.svg
    :class: only-light

.. |d15| image:: /_static/images/icons/charts/coordinate-systems-dark.svg
    :class: only-dark

:py:mod:`coord_cartesian() <lets_plot.coord_cartesian>`,
:py:mod:`coord_fixed() <lets_plot.coord_fixed>`,
:py:mod:`coord_polar() <lets_plot.coord_polar>`,
:py:mod:`coord_flip() <lets_plot.coord_flip>`,
:py:mod:`coord_map() <lets_plot.coord_map>`

Examples:

- .. extref:: coordinate_systems
      :type: text
- .. extref:: flip_coordinates
      :type: text
- .. extref:: coord_polar
      :type: text


|l16| |d16| 'bistro' Plots
--------------------------

.. |l16| image:: /_static/images/icons/charts/bistro-light.svg
    :class: only-light

.. |d16| image:: /_static/images/icons/charts/bistro-dark.svg
    :class: only-dark

:py:mod:`corr_plot() <lets_plot.bistro.corr.corr_plot>`,
:py:mod:`qq_plot() <lets_plot.bistro.qq.qq_plot>`,
:py:mod:`joint_plot() <lets_plot.bistro.joint.joint_plot>`,
:py:mod:`residual_plot() <lets_plot.bistro.residual.residual_plot>`

"Bistro" plots is a collection of "compound plots" allowing users to generate intricate charts without the need for extensive coding.

With these high-level functions you can create visualizations like correlation matrices, quantile-quantile plots, and joint distribution plots using single function calls.

Learn more: :doc:`'bistro' Plots </python/pages/bistro>`.


|l17| |d17| GeoPandas Shapes
----------------------------

.. |l17| image:: /_static/images/icons/charts/geopandas-light.svg
    :class: only-light

.. |d17| image:: /_static/images/icons/charts/geopandas-dark.svg
    :class: only-dark

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`pie <lets_plot.geom_pie>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`label <lets_plot.geom_label>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :doc:`GeoPandas Support </python/pages/geopandas>`.

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


|l18| |d18| Grouping Plots
--------------------------

.. |l18| image:: /_static/images/icons/charts/grouping-plots-light.svg
    :class: only-light

.. |d18| image:: /_static/images/icons/charts/grouping-plots-dark.svg
    :class: only-dark

:py:mod:`GGBunch <lets_plot.GGBunch>` and :py:mod:`gggrid <lets_plot.gggrid>` shows a collection of plots on one figure.

Examples:

- .. extref:: ggbunch
      :type: text
- .. extref:: plot_grid
      :type: text
- .. extref:: gggrid_scale_share
      :type: text
- .. extref:: themes
      :type: text


|l19| |d19| Presentation Options
--------------------------------

.. |l19| image:: /_static/images/icons/charts/presentation-options-light.svg
    :class: only-light

.. |d19| image:: /_static/images/icons/charts/presentation-options-dark.svg
    :class: only-dark

:py:mod:`theme() <lets_plot.theme>`,
:py:mod:`ggtitle() <lets_plot.ggtitle>`,
:py:mod:`ggsize() <lets_plot.ggsize>`,
:py:mod:`xlab() <lets_plot.xlab>`,
:py:mod:`ylab() <lets_plot.ylab>`,
:py:mod:`labs() <lets_plot.labs>`,
:py:mod:`guide_legend() <lets_plot.guide_legend>`,
:py:mod:`guide_colorbar() <lets_plot.guide_colorbar>`,
:py:mod:`guides() <lets_plot.guides>`

Predefined themes
~~~~~~~~~~~~~~~~~

:py:mod:`minimal2 <lets_plot.theme_minimal2>`,
:py:mod:`bw <lets_plot.theme_bw>`,
:py:mod:`grey <lets_plot.theme_grey>`,
:py:mod:`classic <lets_plot.theme_classic>`,
:py:mod:`light <lets_plot.theme_light>`,
:py:mod:`minimal <lets_plot.theme_minimal>`,
:py:mod:`void <lets_plot.theme_void>`,
:py:mod:`none <lets_plot.theme_none>`

.. grid:: 3
    :class-container: wide-grid

    .. grid-item-card::

        .. extref:: complete_themes
            :image: minimal2

    .. grid-item-card::

        .. extref:: complete_themes
            :image: bw

    .. grid-item-card::

        .. extref:: complete_themes
            :image: grey

    .. grid-item-card::

        .. extref:: complete_themes
            :image: classic

    .. grid-item-card::

        .. extref:: complete_themes
            :image: light

    .. grid-item-card::

        .. extref:: complete_themes
            :image: minimal

Color schemes (flavors)
~~~~~~~~~~~~~~~~~~~~~~~

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
- .. extref:: legend
      :type: text
- .. extref:: tooltip_config
      :type: text
- .. extref:: set_font_faces
      :type: text
- .. extref:: axis_position
      :type: text
- .. extref:: axis_text_angle
      :type: text
- .. extref:: superscript_exponent
      :type: text
- .. extref:: annotations_page
      :type: text


Miscellaneous
-------------

Multiple Color Scales
~~~~~~~~~~~~~~~~~~~~~

Use ``color_by``/``fill_by`` parameters and ``paint_a``/``paint_b``/``paint_c`` aesthetics if you need to display two different layers with the same color aesthetic but different color scales.

Examples:

- .. extref:: multiple_color_scales
      :type: text
- .. extref:: mpg_corrgram
      :type: text
- .. extref:: montenegrin_independence_referendum
      :type: text

Scale Functions
~~~~~~~~~~~~~~~

To specify a scale for any group of aesthetics, use the special scale functions: :py:mod:`scale_manual() <lets_plot.scale_manual>`, :py:mod:`scale_continuous() <lets_plot.scale_continuous>`, :py:mod:`scale_gradient() <lets_plot.scale_gradient>`, etc.

Examples:

- .. extref:: scale_functions
      :type: text
- .. extref:: palmer_penguins
      :type: text
- .. extref:: montenegrin_independence_referendum
      :type: text
- .. extref:: google_play_store
      :type: text

Quantiles
~~~~~~~~~

Density-like plots let you show the quantiles by mapping them to a particular colour palette.

Examples:

- .. extref:: quantile_parameters
      :type: text
- .. extref:: ridgeline_plot
      :type: text

Stackable Position Adjustments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure positioning where groups are stacked on top of each other, use the :py:mod:`position_stack() <lets_plot.position_stack>` and :py:mod:`position_fill() <lets_plot.position_fill>` functions.

Examples:

- .. extref:: position_stack
      :type: text
- .. extref:: nobel
      :type: text


Resources
---------

- :doc:`EDA Examples </python/pages/eda>`

- `Picking the Perfect Data Visualization: Line Plots <https://blog.jetbrains.com/dataspell/2023/02/picking-the-perfect-data-visualization-line-plots/>`__

- `Picking the Perfect Data Visualization: Barplots <https://blog.jetbrains.com/dataspell/2023/03/picking-the-perfect-data-visualization-barplots/>`__

.. include:: /python/shared/books.rst


.. include:: /python/shared/features.rst