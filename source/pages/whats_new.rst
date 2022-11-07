.. _whats_new:

:orphan:

.. title:: What is new


What is new
===========

Version 2.5.1
-------------

Mostly a maintenance release.

Nevertheless, few new features and improvements were added as well, among them:

- New rendering options in :py:mod:`geom_text() <lets_plot.geom_text>`, :py:mod:`geom_label() <lets_plot.geom_label>`.

- :py:mod:`geom_imshow() <lets_plot.geom_imshow>` is now supporting ``cmap`` and ``extent`` parameters (also, ``norm``, ``vmin`` and ``vmax`` were fixed).


Version 2.5.0
-------------

Plot Theme
^^^^^^^^^^

:py:mod:`theme_bw() <lets_plot.theme_bw>`
"""""""""""""""""""""""""""""""""""""""""

See: |theme_bw-demo|.

Theme Flavors
"""""""""""""
    
Theme flavor offers an easy way to change the colors of all elements in a theme to match a specific color scheme.

In this release, we have added the following flavors:

- *darcula*

- *solarized_light*

- *solarized_dark*

- *high_contrast_light*

- *high_contrast_dark*

.. image:: /_static/images/theme_flavors.png
  :alt: _images/theme_flavors.png
  :width: 1000
  :height: 133

See: |theme_flavors-demo|.

New parameters in :py:mod:`element_text() <lets_plot.element_text>`
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

- ``size``, ``family`` (|font_size_and_family-demo|)

- ``hjust``, ``vjust`` for plot title, subtitle, caption, legend and axis titles (|hjust_vjust-demo|)

- ``margin`` for plot title, subtitle, caption, axis titles and tick labels (|text_margins-demo|)

New Plot Types
^^^^^^^^^^^^^^

:py:mod:`geom_label() <lets_plot.geom_label>`.

See: |geom_label-demo|.

Color Scales
^^^^^^^^^^^^

Viridis color scales: :py:mod:`scale_color_viridis() <lets_plot.scale_color_viridis>`, :py:mod:`scale_fill_viridis() <lets_plot.scale_fill_viridis>`.

Supported colormaps:

- *magma*

- *inferno*

- *plasma*

- *viridis*

- *cividis*

- *turbo*

- *twilight*

.. image:: /_static/images/viridis_plasma.png
  :alt: _images/viridis_plasma.png
  :width: 439
  :height: 132

See: |colors_viridis-demo|.


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.


.. |colors_viridis-demo| extref:: colors_viridis
  :type: text
  :text: example notebook

.. |font_size_and_family-demo| extref:: font_size_and_family
  :type: text
  :text: example notebook

.. |geom_label-demo| extref:: geom_label
  :type: text
  :text: example notebook

.. |hjust_vjust-demo| extref:: hjust_vjust
  :type: text
  :text: example notebook

.. |text_margins-demo| extref:: text_margins
  :type: text
  :text: example notebook

.. |theme_bw-demo| extref:: theme_bw
  :type: text
  :text: example notebook

.. |theme_flavors-demo| extref:: theme_flavors
  :type: text
  :text: example notebook