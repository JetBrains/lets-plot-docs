.. _whats_new:

:orphan:

.. title:: What is new


What is new in 3.1.0
====================

Breaking Changes
----------------

- ``geom_violin()``: parameter ``draw_quantiles`` renamed to ``quantiles`` - and now it works as in the ``geom_area_ridges()`` geometry.


New Features
------------

-  ``gggrid()`` function.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/plot_grid.ipynb>`__.

-  ``position`` parameter in position scales
   ``scale_x_*(), scale_y_*()``.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/axis_position.ipynb>`__.

-  ``angle`` parameter in ``element_text()`` for
   ``axis_text, axis_text_x, axis_text_y`` in a ``theme()`` (i.e. to
   axis labels).

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/axis_text_angle.ipynb>`__.

-  ``geodesic`` parameter for ``geom_segment()`` and ``geom_path()``.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/param_geodesic.ipynb>`__.

-  New scale functions with parameter ``aesthetic`` to define aesthetics
   that this scale works with:

   -  ``scale_identity(aesthetic, *, ...)``
   -  ``scale_manual(aesthetic, values, *, ...)``
   -  ``scale_continuous(aesthetic, *, ...)``
   -  ``scale_gradient(aesthetic, *, ...)``
   -  ``scale_gradient2(aesthetic, *, ...)``
   -  ``scale_gradientn(aesthetic, *, ...)``
   -  ``scale_hue(aesthetic, *, ...)``
   -  ``scale_discrete(aesthetic, *, ...)``
   -  ``scale_grey(aesthetic, *, ...)``
   -  ``scale_brewer(aesthetic, *, ...)``
   -  ``scale_viridis(aesthetic, *, ...)``

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/scale_functions.ipynb>`__.

-  ``joint_plot()`` - new function in the ``bistro`` module.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/joint_plot.ipynb>`__.

-  PNG support for ``ggsave()``
   [`#596 <https://github.com/JetBrains/lets-plot/issues/596>`__].
   Requires the `CairoSVG <https://pypi.org/project/CairoSVG>`__ library

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/export_to_png.ipynb>`__.

-  ``color_by`` and ``fill_by`` layer parameters to support more than
   one mapping for color and fill. New color aesthetics:
   ``paint_a, paint_b, paint_c``.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/multiple_color_scales.ipynb>`__.

-  ``quantile_lines`` parameter for ``geom_violin()`` - as in the
   ``geom_area_ridges()`` geometry. Also, it was added a
   ``..quantile..`` statistic variable.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/quantile_parameters.ipynb>`__.

-  ``quantiles`` and ``quantile_lines`` parameters for
   ``geom_density()`` - as in the ``geom_area_ridges()`` geometry. Also,
   it was added a ``..quantile..`` statistic variable.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/quantile_parameters.ipynb>`__.

-  ``mode`` parameter for ``position_stack()`` and ``position_fill()``.
   When ``mode='groups'`` (default) the position adjustment shifts
   objects only if their groups are distinct.

   See: `example
   notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23a/position_stack.ipynb>`__.

-  ``residual_plot()``: added ``'density2d'`` and ``'density2df'``
   geometry types, changed some defaults for color parameters.

-  ``pandas`` library was added to dependencies of the
   ``residual_plot()`` function.

-  Python packages for ``Windows`` no longer require ``MinGW`` tools to
   run.

-  Parameter ``flat=True`` turns off lines re-projection, keeping the
   original number of points.


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.