.. _whats_new:

:orphan:

.. title:: What is new


What is new in 4.0.0
====================

| The major version was bumped to 4 due to a major package refactoring that the project has undergone.
| This refactoring doesn’t affect the Python API, however, as a result of package names changed,
| Lets-Plot v4.0.0 is partially incompatible with Lets-Plot Kotlin API versions 4.4.1 and earlier.

A Number of Geometry Defaults Changed
-------------------------------------

-  The default qualitative color palette is now
   `Color Brewer "Set1" <https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=9>`__
   (was `"Set2" <https://colorbrewer2.org/#type=qualitative&scheme=Set2&n=8>`__).
-  Slightly bigger default size of points and width of lines.
-  Flavor-aware default colors for points, lines etc.
   |geom_defaults-img|
   |flavor_geom_colors-img|
   See: |geom_theme_colors|.

.. |geom_defaults-img| image:: /_static/images/changelog/4.0.0/geom_defaults.png
   :width: 504

.. |flavor_geom_colors-img| image:: /_static/images/changelog/4.0.0/flavor_geom_colors.png
   :width: 1024

.. |geom_theme_colors| extref:: geom_theme_colors
    :type: text
    :text: example notebook
-  Size of points is slightly adjusted to match the width of a line of the same "size".
   |point_vs_line-img|

.. |point_vs_line-img| image:: /_static/images/changelog/4.0.0/point_vs_line.png
   :width: 170

Support for Variadic Line Width and/or Color in :py:mod:`geom_line() <lets_plot.geom_line>` and :py:mod:`geom_path() <lets_plot.geom_path>`
-------------------------------------------------------------------------------------------------------------------------------------------

.. image:: /_static/images/changelog/4.0.0/variadic_width.png
    :width: 455

See: |aes_size_color_variadic_lines|.

.. |aes_size_color_variadic_lines| extref:: aes_size_color_variadic_lines
    :type: text
    :text: example notebook

Parameter ``"size_unit"`` in :py:mod:`geom_pie() <lets_plot.geom_pie>`
----------------------------------------------------------------------

A way to specify size of the pie in units relative to the plot size.

See: |geom_pie_size_unit|.

.. |geom_pie_size_unit| extref:: geom_pie_size_unit
    :type: text
    :text: example notebook

Stroke and Spacers in :py:mod:`geom_pie() <lets_plot.geom_pie>`
---------------------------------------------------------------

.. image:: /_static/images/changelog/4.0.0/pie_stroke.png
    :width: 162

See: |geom_pie_stroke_and_spacers|.

.. |geom_pie_stroke_and_spacers| extref:: geom_pie_stroke_and_spacers
    :type: text
    :text: example notebook

New :py:mod:`theme_void() <lets_plot.theme_void>`, Geometries and Statistics
----------------------------------------------------------------------------

-  :py:mod:`theme_void() <lets_plot.theme_void>`:
   `example <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23c/theme_void.ipynb>`__.
-  :py:mod:`geom_function() <lets_plot.geom_function>`: |geom_function|.
-  :py:mod:`stat_ecdf() <lets_plot.stat_ecdf>`: |stat_ecdf|.
-  :py:mod:`stat_summary() <lets_plot.stat_summary>`: |stat_summary|.
-  :py:mod:`stat_summary_bin() <lets_plot.stat_summary_bin>`: |stat_summary_bin|.
-  ``"sum"`` statistic: |param_stat_sum|.
-  ``"boxplot_outlier"`` statistic: |stat_boxplot_outlier|.

.. |geom_function| extref:: geom_function
    :type: text
    :text: example
.. |stat_ecdf| extref:: stat_ecdf
    :type: text
    :text: example
.. |stat_summary| extref:: stat_summary
    :type: text
    :text: example
.. |stat_summary_bin| extref:: stat_summary_bin
    :type: text
    :text: example
.. |param_stat_sum| extref:: param_stat_sum
    :type: text
    :text: example
.. |stat_boxplot_outlier| extref:: stat_boxplot_outlier
    :type: text
    :text: example

Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.