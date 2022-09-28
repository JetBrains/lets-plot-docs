.. _whats_new:

:orphan:

.. title:: What's new


What's New
==========

Added
-----

-  New theme: :py:mod:`theme_bw() <lets_plot.theme_bw>`
   [`#554 <https://github.com/JetBrains/lets-plot/issues/554>`__].

   See: |theme_bw-demo|.

-  Color schemes (flavors) applicable to existing themes:

   - :py:mod:`flavor_darcula() <lets_plot.flavor_darcula>`;

   - :py:mod:`flavor_solarized_light() <lets_plot.flavor_solarized_light>`;

   - :py:mod:`flavor_solarized_dark() <lets_plot.flavor_solarized_dark>`;

   - :py:mod:`flavor_high_contrast_light() <lets_plot.flavor_high_contrast_light>`;

   - :py:mod:`flavor_high_contrast_dark() <lets_plot.flavor_high_contrast_dark>`.

   See: |theme_flavors-demo|.

-  Viridis color scales: :py:mod:`scale_color_viridis() <lets_plot.scale_color_viridis>`,
   :py:mod:`scale_fill_viridis() <lets_plot.scale_fill_viridis>`.

   See: |colors_viridis-demo|.

-  New parameters in :py:mod:`element_text() <lets_plot.element_text>`
   [`#562 <https://github.com/JetBrains/lets-plot/issues/562>`__]:

   -  ``size``, ``family`` (|font_size_and_family-demo|)
   -  ``hjust``, ``vjust`` for plot title, subtitle, caption, legend and
      axis titles (|hjust_vjust-demo|)
   -  ``margin`` for plot title, subtitle, caption, axis titles and tick
      labels (|text_margins-demo|)

-  The ‘newline’ character (``\n``) now works as ``line break`` in axis
   title.

   See: |text_margins-demo|.

-  Parameter ``whisker_width`` in :py:mod:`geom_boxplot() <lets_plot.geom_boxplot>`
   [`#549 <https://github.com/JetBrains/lets-plot/issues/549>`__].

   See: |boxplot_whisker_width-demo|.

-  New geometry :py:mod:`geom_label() <lets_plot.geom_label>`
   [`#557 <https://github.com/JetBrains/lets-plot/issues/557>`__].

   See: |geom_label-demo|.

-  Auto-detection of **Databricks** and **NextJournal** environments
   [`#602 <https://github.com/JetBrains/lets-plot/issues/602>`__].

Changed
-------

-  New tooltip style after applying :py:mod:`coord_flip() <lets_plot.coord_flip>`
   [`#580 <https://github.com/JetBrains/lets-plot/issues/580>`__].

   See: |tooltips_after_coord_flip-demo|.

Fixed
-----

-  Density and area geoms: preserve the z-order when grouping
   [`#552 <https://github.com/JetBrains/lets-plot/issues/552>`__].
-  Allow to import all ‘bistro’ functions just by ’*’
   [`#551 <https://github.com/JetBrains/lets-plot/issues/551>`__].
-  Boxplot, violin, crossbar: position dodge width=0.95 should be used
   by default
   [`#553 <https://github.com/JetBrains/lets-plot/issues/553>`__].
-  Tooltip is shown not for the nearest object
   [`#574 <https://github.com/JetBrains/lets-plot/issues/574>`__].
-  Tooltip is not displayed for the object on the plots border
   [`#575 <https://github.com/JetBrains/lets-plot/issues/575>`__].
-  The plot caption overlaps with the legend
   [`#587 <https://github.com/JetBrains/lets-plot/issues/587>`__].
-  Unclear size unit of width
   [`#589 <https://github.com/JetBrains/lets-plot/issues/589>`__].
-  Specify size units in docstrings
   [`#597 <https://github.com/JetBrains/lets-plot/issues/597>`__].
-  No tooltips for geom_boxplot with zero height
   [`#563 <https://github.com/JetBrains/lets-plot/issues/563>`__].
-  geom_text: wrong label alignment with ``hjust`` 0 and 1
   [`#592 <https://github.com/JetBrains/lets-plot/issues/592>`__].
-  Error when using lets-plot in streamlit
   [`#595 <https://github.com/JetBrains/lets-plot/issues/595>`__].

.. |boxplot_whisker_width-demo| extref:: boxplot_whisker_width
  :type: text
  :text: example notebook

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

.. |tooltips_after_coord_flip-demo| extref:: tooltips_after_coord_flip
  :type: text
  :text: example notebook