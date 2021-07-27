.. _charts:

.. include:: /shared/previews.rst

Charts
======

Basic Building Blocks
---------------------

Points
~~~~~~

Layers:

- :py:mod:`Points <lets_plot.geom_point>`
- :py:mod:`Jittered points <lets_plot.geom_jitter>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |point_geometries-nbviewer|

Demo notebooks:

- `Draw a scatter plot <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__

- `Discover trends with smoothing <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__

Lines
~~~~~

Layers:

.. panels::
    :container: + border-free
    :column: col-lg-1 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/icons/charts/paths.png

    ---
    :column: col-lg-11 col-md-4 col-sm-6 col-xs-12 p-2

    :py:mod:`line <lets_plot.geom_line>`,
    :py:mod:`path <lets_plot.geom_path>`

    ---
    :column: col-lg-1 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/icons/charts/lines.png

    ---
    :column: col-lg-11 col-md-4 col-sm-6 col-xs-12 p-2

    :py:mod:`diagonal line <lets_plot.geom_abline>`,
    :py:mod:`horizontal line <lets_plot.geom_hline>`,
    :py:mod:`vertical line <lets_plot.geom_vline>`

    ---
    :column: col-lg-1 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/icons/charts/segments.png

    ---
    :column: col-lg-11 col-md-4 col-sm-6 col-xs-12 p-2

    :py:mod:`segment <lets_plot.geom_segment>`

    ---
    :column: col-lg-1 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/icons/charts/steps.png

    ---
    :column: col-lg-11 col-md-4 col-sm-6 col-xs-12 p-2

    :py:mod:`step-function <lets_plot.geom_step>`

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_line-nbviewer|

    ---
    |geom_path-nbviewer|

    ---
    |geom_abline-nbviewer|

    ---
    |geom_hline-nbviewer|

    ---
    |geom_vline-nbviewer|

    ---
    |geom_segment-nbviewer|

    ---
    |geom_step-nbviewer|

Demo notebooks:

- `Error bars <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__

- `Line vs. path <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/line_vs_path.ipynb>`__

- `Distributions <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/distributions.ipynb>`__

Areas
~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_area-nbviewer|

    :py:mod:`Area <lets_plot.geom_area>`

    ---
    |geom_ribbon-nbviewer|

    :py:mod:`Ribbon <lets_plot.geom_ribbon>`

Polygons
~~~~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_polygon-nbviewer|

    :py:mod:`Polygon <lets_plot.geom_polygon>`

    ---
    |geom_map-nbviewer|

    :py:mod:`Map <lets_plot.geom_map>`

Demo notebooks:

- `2D density <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/density_2d.ipynb>`__

- `Contours <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__

- `Mapping US household income <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map_US_household_income.ipynb>`__

Tiles
~~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_tile-nbviewer|

    :py:mod:`Tiles <lets_plot.geom_tile>`

    ---
    |geom_rect-nbviewer|

    :py:mod:`Rectangles <lets_plot.geom_rect>`

    ---
    |geom_raster-nbviewer|

    :py:mod:`Raster plot <lets_plot.geom_raster>`

Demo notebooks:

- `Contours <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__

- `"Fisher boat" image <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__

Text
~~~~

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_text-nbviewer|

    :py:mod:`Text <lets_plot.geom_text>`

Demo notebooks:

- `The label_format parameter in geom_text() <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/label_format.ipynb>`__

- `Inset Map of Kotlin Island <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_kotlin_isl.ipynb>`__

- `Formatting labels on plots <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/formatting_axes_etc.ipynb>`__

Discrete
--------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_bar-nbviewer|

    :py:mod:`Bar <lets_plot.geom_bar>`

    ---
    |geom_bar_identity-nbviewer|

    :py:mod:`Bar (stat='identity') <lets_plot.geom_bar>`

    ---
    |geom_boxplot-nbviewer|

    :py:mod:`Boxplot <lets_plot.geom_boxplot>`

Demo notebooks:

- `Bar geometry <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/bar.ipynb>`__

- `Bar on livemap <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/bar_on_livemap.ipynb>`__

- `Error bars <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__

- `Distributions <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/distributions.ipynb>`__

Contours
--------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_contour-nbviewer|

    :py:mod:`Contours <lets_plot.geom_contour>`

    ---
    |geom_contourf-nbviewer|

    :py:mod:`Filled contours <lets_plot.geom_contourf>`

Demo notebooks:

- `Contours <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__

- `How to draw curve fast <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/demo/contours.ipynb>`__

Visualization of Distribution
-----------------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_histogram-nbviewer|

    :py:mod:`Histogram <lets_plot.geom_histogram>`

    ---
    |geom_density-nbviewer|

    :py:mod:`Density <lets_plot.geom_density>`

    ---
    |geom_freqpoly-nbviewer|

    :py:mod:`Frequency polygon <lets_plot.geom_freqpoly>`

Demo notebooks:

- `Histogram <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/histogram.ipynb>`__

- `Distributions <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/distributions.ipynb>`__

Visualization of Errors
-----------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_crossbar-nbviewer|

    :py:mod:`Crossbar <lets_plot.geom_crossbar>`

    ---
    |geom_errorbar-nbviewer|

    :py:mod:`Errorbar <lets_plot.geom_errorbar>`

    ---
    |geom_linerange-nbviewer|

    :py:mod:`Linerange <lets_plot.geom_linerange>`

    ---
    |geom_pointrange-nbviewer|

    :py:mod:`Pointrange <lets_plot.geom_pointrange>`

Demo notebooks:

- `Error bars <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__

Smoothing
---------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_smooth-nbviewer|

    :py:mod:`Smoothing line <lets_plot.geom_smooth>`

Demo notebooks:

- `Draw a scatter plot <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__

- `Discover trends with smoothing <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__

``as_discrete()``
-----------------

Demo notebooks:

- `Discover trends with smoothing <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__

Bivariate Distribution
----------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geom_bin2d-nbviewer|

    :py:mod:`Heatmap of 2d bin counts <lets_plot.geom_bin2d>`

    ---
    |geom_density2d-nbviewer|

    :py:mod:`2D density <lets_plot.geom_density2d>`

    ---
    |geom_density2df-nbviewer|

    :py:mod:`Filled 2D density <lets_plot.geom_density2df>`

Demo notebooks:

- `2D density <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/density_2d.ipynb>`__

Images
------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |image_101-nbviewer|

    :py:mod:`Image <lets_plot.geom_image>`

    ---
    |basic_image_matrix-nbviewer|

    :py:mod:`Matrix of images <lets_plot.bistro.im.image_matrix>`

Demo notebooks:

- `"Fisher boat" image <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__

- `Image matrix <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_matrix.ipynb>`__

Facets
------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |facet_grid-nbviewer|

    :py:mod:`Lay out panels in a grid <lets_plot.facet_grid>`

    ---
    |facet_wrapping-nbviewer|

    :py:mod:`Wrap a 1d ribbon of panels into 2d <lets_plot.facet_wrap>`

Demo notebooks:

- `Facets <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/facets.ipynb>`__

Correlation Plot
----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |corr_plot-nbviewer|

    :py:mod:`Correlation plot <lets_plot.bistro.corr.corr_plot>`

Demo notebooks:

- `Correlation plot <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/correlation_plot.ipynb>`__

Presentation Options
--------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |default_theme-nbviewer|

    :py:mod:`Theme <lets_plot.theme>`

    ---
    |guide_legend-nbviewer|

    :py:mod:`Legend guide <lets_plot.guide_legend>`

    ---
    |guide_colorbar-nbviewer|

    :py:mod:`Continuous colour bar guide <lets_plot.guide_colorbar>`

Demo notebooks:

- `Legend and axis <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/legend_and_axis.ipynb>`__

- `Tooltip customization <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/tooltip_config.ipynb>`__

More Examples
-------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |2020-nbviewer|

    ---
    |adversarial_attack-nbviewer|

    ---
    |bayesian_inference-nbviewer|

    ---
    |covid19_and_mobility-nbviewer|

    ---
    |delhi_climate-nbviewer|

    ---
    |google_play_store-nbviewer|

    ---
    |google_suggestions-nbviewer|

    ---
    |kernels_visualization-nbviewer|

    ---
    |klein_bottle-nbviewer|

    ---
    |malnutrition-nbviewer|

    ---
    |mandelbulbs-nbviewer|

    ---
    |mosaic_image-nbviewer|

    ---
    |nobel-nbviewer|

    ---
    |nyc_metro-nbviewer|

    ---
    |torus-nbviewer|

    ---
    |world_coloring-nbviewer|

.. include:: /shared/features.rst