.. _whats_new:

:orphan:

.. title:: What is new


What is new in 3.0.0
====================


Added
-----

-  :py:mod:`geom_imshow() <lets_plot.geom_imshow>`:

   -  Improved performance by orders of magnitude.

   -  Transparency of ``NaN`` values in grayscale images
      [`#631 <https://github.com/JetBrains/lets-plot/issues/631>`__].
      See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/image_nan_values.ipynb>`__.

   -  ``alpha`` parameter
      [`#630 <https://github.com/JetBrains/lets-plot/issues/630>`__].
      See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/image_alpha_param.ipynb>`__.

-  :py:mod:`geom_violin() <lets_plot.geom_violin>`:

   -  ``tails_cutoff`` parameter. See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/violin_tails_cutoff.ipynb>`__.

-  New 'bistro' plot - :py:mod:`residual_plot() <lets_plot.bistro.residual.residual_plot>`.

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/residual_plot.ipynb>`__.

-  New geometry :py:mod:`geom_area_ridges() <lets_plot.geom_area_ridges>`.

   See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/ridgeline_plot.ipynb>`__.

-  New geometry :py:mod:`geom_pie() <lets_plot.geom_pie>`.

   See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/geom_pie.ipynb>`__.

-  Annotations for pie chart:

   See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/annotations_for_pie.ipynb>`__.

-  New variables computed by ``'count'`` and ``'count2d'`` statistics:
   ``'..sum..'``, ``'..prop..'``, ``'..proppct..'``.

   See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/stat_count(2d)_vars.ipynb>`__.

-  Static maps:

   -  The value ``"provided"`` for ``use_crs`` parameter.

      See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/projection_provided.ipynb>`__.


Changed
-------

- [BREAKING] Dropped support for Python 3.6 as it is in the [`"end-of-life" <https://devguide.python.org/versions/>`__] of its release cycle.

- :py:mod:`geom_livemap() <lets_plot.geom_livemap>` itself no longer draws geometry, so the following options are no longer used:
  ``'symbol'``, ``'data'``, ``'mapping'``, ``'map'``, ``'map_join'``, ``'ontop'``, ``'stat'``, ``'position'``, ``'show_legend'``, ``'sampling'``, ``'tooltips'``.
  If you need to render points or pies, please, use :py:mod:`geom_point() <lets_plot.geom_point>` and :py:mod:`geom_pie() <lets_plot.geom_pie>` functions.

- Java/Swing platf.: Apache Batik upgraded to v.1.16 [`#624 <https://github.com/JetBrains/lets-plot/issues/624>`__], [`LPK #140 <https://github.com/JetBrains/lets-plot-kotlin/issues/140>`__].

- The default size is increased for the plot title and decreased for the caption.

- Upgraded Kotlin version to 1.7.21 (was 1.7.20).


Fixed
-----

-  Themes: can’t change plot background after applying a ``"flavor"``
   [`#623 <https://github.com/JetBrains/lets-plot/issues/623>`__].

-  Layout: uneven ``left``/``right``, ``top``/``bottom`` plot margins
   [`#625 <https://github.com/JetBrains/lets-plot/issues/625>`__].

-  A plot building error with empty data on various geoms.

-  Precision error in gradient
   [`#634 <https://github.com/JetBrains/lets-plot/issues/634>`__].

-  :py:mod:`geom_livemap <lets_plot.geom_livemap>`: wrong position when datapoints geodesic line goes close
   to the N.P.
   [`#645 <https://github.com/JetBrains/lets-plot/issues/645>`__].


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.