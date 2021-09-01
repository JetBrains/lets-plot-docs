.. _charts:

.. include:: /shared/previews.rst


Charts
======


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
:py:mod:`text <lets_plot.geom_text>`

Examples:

- `Population mobility and COVID-19 <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/demo/covid-19_and_mobility.ipynb>`__
- `Time series visualizations <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/demo/delhi_climate.ipynb>`__
- `Bayesian inference <https://nbviewer.jupyter.org/github/denisvstepanov/lets-plot-examples/blob/master/Bayesian%20inference.ipynb>`__
- `Line vs. path <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/line_vs_path.ipynb>`__
- `Inset Map of Kotlin Island <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_kotlin_isl.ipynb>`__
- `Formatting labels on plots <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/formatting_axes_etc.ipynb>`__


|discrete-icon| Discrete
------------------------

.. |discrete-icon| image:: /_static/images/icons/charts/discrete.svg

:py:mod:`Bar <lets_plot.geom_bar>`,
:py:mod:`boxplot <lets_plot.geom_boxplot>`

Examples:

- `Bar geometry <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/bar.ipynb>`__
- `Identity stat <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/geom_bar_identity.ipynb>`__
- `Comparisons <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/comparisons.ipynb>`__
- `General purpose stats <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/general_purpose_stats.ipynb>`__
- Using scales: `continuous <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/continuous_scales.ipynb>`__, `discrete <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/discrete_scales.ipynb>`__, `identity <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/identity_scales.ipynb>`__, `manual <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/manual_scales.ipynb>`__, `brewer colors <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/brewer_scale.ipynb>`__, `grey-scale colors <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/grey_scale.ipynb>`__
- `Dodge position <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/dodge_position.ipynb>`__


|as_discrete-icon| Ordering categories, ``as_discrete()``
---------------------------------------------------------

.. |as_discrete-icon| image:: /_static/images/icons/charts/as_discrete.svg

:py:mod:`as_discrete() <lets_plot.mapping.as_discrete>`

Learn more: :ref:`Function as_discrete() <as_discrete>`.

Examples:

- `Guide to ordering <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/cookbook/ordering_examples.ipynb>`__
- `Discover trends with smoothing <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__


|contours-icon| Contours
------------------------

.. |contours-icon| image:: /_static/images/icons/charts/contours.svg

:py:mod:`Contours <lets_plot.geom_contour>`,
:py:mod:`filled contours <lets_plot.geom_contourf>`

Examples:

- `Contours <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__
- `How to draw curve fast <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/demo/contours.ipynb>`__
- `3d distributions <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/3_variables.ipynb>`__


|visualization-of-distribution-icon| Visualization of Distribution
------------------------------------------------------------------

.. |visualization-of-distribution-icon| image:: /_static/images/icons/charts/visualization-of-distribution.svg

:py:mod:`Histogram <lets_plot.geom_histogram>`,
:py:mod:`density <lets_plot.geom_density>`,
:py:mod:`frequency polygon <lets_plot.geom_freqpoly>`

Examples:

- `Histogram <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/features/histogram.ipynb>`__
- `Distributions <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/distributions.ipynb>`__
- `1d Distributions <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/1d_distributions.ipynb>`__
- Using scales: `continuous <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/gradient_scale.ipynb>`__, `diverging <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/gradient2_scale.ipynb>`__, `qualitative <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/hue_scale.ipynb>`__


|visualization-of-errors-icon| Visualization of Errors
------------------------------------------------------

.. |visualization-of-errors-icon| image:: /_static/images/icons/charts/visualization-of-errors.svg

:py:mod:`Crossbar <lets_plot.geom_crossbar>`,
:py:mod:`errorbar <lets_plot.geom_errorbar>`,
:py:mod:`linerange <lets_plot.geom_linerange>`,
:py:mod:`pointrange <lets_plot.geom_pointrange>`

Examples:

- `Error bars <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__
- `Comparisons <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/comparisons.ipynb>`__


|smoothing-icon| Smoothing
--------------------------

.. |smoothing-icon| image:: /_static/images/icons/charts/smoothing.svg

:py:mod:`Smoothing line <lets_plot.geom_smooth>`

Examples:

- `Simple linear smoothing <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/simple_linear_smoothing.ipynb>`__
- `Draw a scatter plot <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__
- `Discover trends with smoothing <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__


|bivariate-distribution-icon| Bivariate Distribution
----------------------------------------------------

.. |bivariate-distribution-icon| image:: /_static/images/icons/charts/bivariate-distribution.svg

:py:mod:`Heatmap of 2d bin counts <lets_plot.geom_bin2d>`,
:py:mod:`2d density <lets_plot.geom_density2d>`,
:py:mod:`filled 2d density <lets_plot.geom_density2df>`

Examples:

- `2d density <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/density_2d.ipynb>`__
- `General purpose stats <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/general_purpose_stats.ipynb>`__
- `2d distributions <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/2d_distributions.ipynb>`__


|images-icon| Images
--------------------

.. |images-icon| image:: /_static/images/icons/charts/images.svg

:py:mod:`Image <lets_plot.geom_image>`,
:py:mod:`matrix of images <lets_plot.bistro.im.image_matrix>`

Examples:

- `"Fisher boat" image <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__
- `Simple image matrix <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/basic_image_matrix.ipynb>`__
- `Image matrix <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_matrix.ipynb>`__


|facets-icon| Facets
--------------------

.. |facets-icon| image:: /_static/images/icons/charts/facets.svg

:py:mod:`facet_grid() <lets_plot.facet_grid>`,
:py:mod:`facet_wrap() <lets_plot.facet_wrap>`

Examples:

- `Facets <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/facets.ipynb>`__
- `Population mobility and COVID-19 <https://nbviewer.jupyter.org/github/HIL-HK/lets-plot-examples/blob/master/demo/covid-19_and_mobility.ipynb>`__


|correlation-plot-icon| Correlation Plot
----------------------------------------

.. |correlation-plot-icon| image:: /_static/images/icons/charts/correlation-plot.svg

:py:mod:`Correlation plot <lets_plot.bistro.corr.corr_plot>`

Examples:

- `Simple correlation plot <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/corr_plot.ipynb>`__
- `Correlation plot <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/correlation_plot.ipynb>`__


|geopandas-icon| GeoPandas Shapes
---------------------------------

.. |geopandas-icon| image:: /_static/images/icons/charts/geopandas.svg

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: :py:mod:`polygon <lets_plot.geom_polygon>`, :py:mod:`map <lets_plot.geom_map>`, :py:mod:`point <lets_plot.geom_point>`, :py:mod:`text <lets_plot.geom_text>`, :py:mod:`path <lets_plot.geom_path>`, :py:mod:`rect <lets_plot.geom_rect>`.

Learn more: :ref:`GeoPandas Support <geopandas>`.


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

Examples:

- `Default theme <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/default_theme.ipynb>`__
- `Legend and axis <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/legend_and_axis.ipynb>`__
- `Tooltip customization <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/tooltip_config.ipynb>`__
- `Comparisons <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/comparisons.ipynb>`__
- `Legend guide <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/guide_legend.ipynb>`__
- `Legend place <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/legend_place.ipynb>`__
- `Title and labels through a scale <https://nbviewer.jupyter.org/github/ASmirnov-HORIS/lets-plot-docs/blob/redesign/source/examples/basics/gog/scale_way.ipynb>`__


Examples
--------

.. panels::
    :container: + preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |covid19_and_mobility-nbviewer|

    ---
    |delhi_climate-nbviewer|

    ---
    |google_play_store-nbviewer|

    ---
    |bayesian_inference-nbviewer|

    ---
    |nobel-nbviewer|

    ---
    |simple_linear_smoothing-nbviewer|

    ---
    |jitterdodge_position-nbviewer|

    ---
    |stat_corr-nbviewer|

    ---
    |nyc_metro-nbviewer|

    ---
    |google_suggestions-nbviewer|

    ---
    |malnutrition-nbviewer|

    ---
    |world_coloring-nbviewer|

    ---
    |1d_distributions-nbviewer|

    ---
    |general_purpose_stats-nbviewer|

    ---
    |2d_distributions-nbviewer|

    ---
    |3_variables-nbviewer|

    ---
    |kernels_visualization-nbviewer|

    ---
    |torus-nbviewer|

    ---
    |klein_bottle-nbviewer|

    ---
    |mandelbulbs-nbviewer|

    ---
    |2020-nbviewer|

    ---
    |adversarial_attack-nbviewer|

    ---
    |mosaic_image-nbviewer|

    ---
    |map_coordinates-nbviewer|

    ---
    |point_geometries-nbviewer|

    ---
    |jitter_position-nbviewer|

    ---
    |fixed_coordinates-nbviewer|

    ---
    |guide_colorbar-nbviewer|

    ---
    |legend_place-nbviewer|

    ---
    |log10_scale-nbviewer|

    ---
    |shape_manual_scale-nbviewer|

    ---
    |size_area_scale-nbviewer|

    ---
    |reversed_scale-nbviewer|

    ---
    |datetime_scale-nbviewer|

    ---
    |with_clipping-nbviewer|

    ---
    |without_clipping-nbviewer|

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#">Show more</a>
    </div>


.. include:: /shared/features.rst