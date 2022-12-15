.. _whats_new:

:orphan:

.. title:: What is new


What is new in 3.0.0
====================


Breaking Changes
----------------

- ``Python 3.6`` is no longer supported as it is in the `“end-of-life” <https://devguide.python.org/versions/>`__ release cycle stage.

- :py:mod:`geom_livemap() <lets_plot.geom_livemap>` is now a pure basemap layer. The following options are no longer supported: ``symbol``, ``data``, ``mapping``, ``map``, ``map_join``, ``ontop``, ``stat``, ``position``, ``show_legend``, ``sampling``, ``tooltips``, ``geodesic``.

..

   To draw **point** and **pie** markers on map, please, use the :py:mod:`geom_point() <lets_plot.geom_point>` and :py:mod:`geom_pie() <lets_plot.geom_pie>` geometry layers.

   See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/titanic.ipynb>`__.

   In place of the former ``geodetic`` parameter in :py:mod:`geom_livemap <lets_plot.geom_livemap>` please use the new parameter ``flat`` in **path** and **segment** geometry layers.

   See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/param_flat.ipynb>`__.


New Features
------------

- .. rubric:: :py:mod:`residual_plot() <lets_plot.bistro.residual.residual_plot>`
     :name: residual_plot

  |image-residual-light| |image-residual-dark|

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/residual_plot.ipynb>`__.

.. |image-residual-light| image:: /_static/images/changelog/3.0.0/residual-light.png
   :width: 200
.. |image-residual-dark| image:: /_static/images/changelog/3.0.0/residual-dark.png
   :width: 200

- .. rubric:: :py:mod:`geom_area_ridges() <lets_plot.geom_area_ridges>`
     :name: geom_area_ridges

  |image-ridges-dark|

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/ridgeline_plot.ipynb>`__.

.. |image-ridges-dark| image:: /_static/images/changelog/3.0.0/ridges-dark.png
   :width: 400

- .. rubric:: :py:mod:`geom_pie() <lets_plot.geom_pie>`
     :name: geom_pie

  |image-pie|

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/geom_pie.ipynb>`__.

.. |image-pie| image:: /_static/images/changelog/3.0.0/pie.png
   :width: 379

- .. rubric:: Annotation Labels on Pie-Chart
     :name: annotation-labels-on-pie-chart

  |image-pie-labels-explode| |image-pie-labels-titanic|

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/annotations_for_pie.ipynb>`__.

.. |image-pie-labels-explode| image:: /_static/images/changelog/3.0.0/pie-labels-explode.png
   :height: 133
.. |image-pie-labels-titanic| image:: /_static/images/changelog/3.0.0/pie-labels-titanic.png
   :height: 133

- .. rubric:: Spatial Pies
     :name: spatial-pies

  |image-spatial_pies_titanic|

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/titanic.ipynb>`__.

.. |image-spatial_pies_titanic| image:: /_static/images/changelog/3.0.0/spatial_pies_titanic.png
   :height: 133

- .. rubric:: New Parameters in :py:mod:`geom_imshow() <lets_plot.geom_imshow>`:
     :name: new-parameters-in-geom_imshow

  |image-imshow-alpha-jp|

  -  Transparency of ``NaN`` values in grayscale images: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/image_nan_values.ipynb>`__.

  -  ``alpha`` parameter: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-22e/image_alpha_param.ipynb>`__.

.. |image-imshow-alpha-jp| image:: /_static/images/changelog/3.0.0/imshow-alpha-jp.png
   :width: 180


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.