.. _whats_new:

:orphan:

.. title:: What is new


What is new in 3.2.0
====================


Added
-----

-  New geometry :py:mod:`lollipop <lets_plot.geom_lollipop>`.

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23b/geom_lollipop.ipynb>`__.

-  ``stroke`` aesthetic for :py:mod:`geom_point() <lets_plot.geom_point>`, :py:mod:`geom_jitter() <lets_plot.geom_jitter>`, :py:mod:`geom_qq() <lets_plot.geom_qq>`, :py:mod:`geom_qq2() <lets_plot.geom_qq2>`, :py:mod:`geom_pointrange() <lets_plot.geom_pointrange>`, :py:mod:`geom_dotplot() <lets_plot.geom_dotplot>`, :py:mod:`geom_ydotplot() <lets_plot.geom_ydotplot>` and ``outlier_stroke`` parameter for :py:mod:`geom_boxplot() <lets_plot.geom_boxplot>`.

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23b/aes_stroke.ipynb>`__.

-  New aesthetic ``linewidth``. Used only for :py:mod:`geom_lollipop() <lets_plot.geom_lollipop>` at the moment.

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23b/geom_lollipop.ipynb>`__.

-  The 'newline' character (``\n``) now works as ``line break`` in legend text ([`#726 <https://github.com/JetBrains/lets-plot/issues/726>`__])

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23b/legend_text_multiline.ipynb>`__.

-  Horizontal error bars and vertical "dodge" ([`#735 <https://github.com/JetBrains/lets-plot/issues/735>`__]).

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23b/horizontal_error_bars.ipynb>`__.

-  Colorbar in :py:mod:`geom_imshow() <lets_plot.geom_imshow>`. Parameters ``show_legend`` and ``color_by`` [`#717 <https://github.com/JetBrains/lets-plot/issues/717>`__].


Changed
-------

-  [BREAKING] :py:mod:`geom_dotplot() <lets_plot.geom_dotplot>` and :py:mod:`geom_ydotplot() <lets_plot.geom_ydotplot>` no longer supports parameter ``stat``. Only default stats make sense for these geometries.

-  Position adjustment settings:

   -  ``width``, ``height`` parameters of :py:mod:`geom_jitter() <lets_plot.geom_jitter>` have priority over the ``width``, ``height`` parameters of :py:mod:`position_jitter() <lets_plot.position_jitter>` function;
   -  :py:mod:`geom_text() <lets_plot.geom_text>`, :py:mod:`geom_label() <lets_plot.geom_label>` use ``stat='identity'`` by default;
   -  ``nudge_x``, ``nudge_y`` parameters of :py:mod:`geom_text() <lets_plot.geom_text>`, :py:mod:`geom_label() <lets_plot.geom_label>` have priority over ``x``, ``y`` parameters of :py:mod:`position_nudge() <lets_plot.position_jitter>` function.


Fixed
-----

-  livemap: memory leak caused by a document event handler.
-  livemap: flickering when zooming with the buttons.
-  Implement the 'stroke' aesthetic
   [`#320 <https://github.com/JetBrains/lets-plot/issues/320>`__].
-  geom_density2d: Internal error with None values in data
   [`#702 <https://github.com/JetBrains/lets-plot/issues/702>`__].
-  livemap: tooltip text doesn't reflect data under the cursor
   [`#709 <https://github.com/JetBrains/lets-plot/issues/709>`__].
-  Quantile should be shown in tooltip if the variable ``..quantile..``
   is mapped to geom aesthetic.
-  Bad default formatting for stat variables
   [`#654 <https://github.com/JetBrains/lets-plot/issues/654>`__].
-  The scale name does not apply with ``as_discrete()``
   [`#653 <https://github.com/JetBrains/lets-plot/issues/653>`__].
-  Batik: geom_imshow() fail with an error: "The attribute"xlink:href"
   of the element is required"
-  Tooltip is not shown when configured for 'const' value
   [`#610 <https://github.com/JetBrains/lets-plot/issues/610>`__].
-  Fix crash when try to add a constant to a tooltip (e.g.\ ``"^size"``,
   where ``size`` aesthetic is specified with a number).
-  ``geom_segment()`` doesn't take into account the alpha
   [`#748 <https://github.com/JetBrains/lets-plot/issues/748>`__].
-  Batik bug with usage of "&"
   [`#713 <https://github.com/JetBrains/lets-plot/issues/713>`__].
-  HTML export: exclude computation messages from the output
   [`#725 <https://github.com/JetBrains/lets-plot/issues/725>`__].
-  "Variable not found" error in ggmarginal
   [`#681 <https://github.com/JetBrains/lets-plot/issues/681>`__].
-  Image export not working with ``geom_imshow()`` and ``geom_raster()``
   [`LPK-175 <https://github.com/JetBrains/lets-plot-kotlin/issues/175>`__].
-  DateTime metadata is not applied for scales other than X/Y
   [`LPK-174 <https://github.com/JetBrains/lets-plot-kotlin/issues/174>`__].
-  Groups not sorted similarly when using facets
   [`#679 <https://github.com/JetBrains/lets-plot/issues/679>`__].
-  Categorical ordering, it's not respected for Boxplot and violin plot
   [`#746 <https://github.com/JetBrains/lets-plot/issues/746>`__].
-  facet_grid: Internal error
   [`#699 <https://github.com/JetBrains/lets-plot/issues/699>`__].
-  Export to SVG fails if breaks are given by integers
   [`#763 <https://github.com/JetBrains/lets-plot/issues/763>`__].
-  Remove hard IPython dependency
   [`#749 <https://github.com/JetBrains/lets-plot/issues/749>`__].
-  livemap: doesn't work well with gggrid
   [`#750 <https://github.com/JetBrains/lets-plot/issues/750>`__].
-  Tooltips bug
   [`LPK-176 <https://github.com/JetBrains/lets-plot-kotlin/issues/176>`__].


Change Log
----------

See
`CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__
for other changes and fixes.
