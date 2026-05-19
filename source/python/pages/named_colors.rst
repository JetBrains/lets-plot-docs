.. _named_colors:

:og:description: List of all named colors.

:orphan:

.. title:: Named Colors in Lets-Plot

.. meta::
   :description: List of all named colors.
   :keywords: named colors


Named Colors Reference
======================

You can specify a color for theme elements and geometries by its name from the table below.

.. raw:: html

   <details>
   <summary><a class="reference internal" target="_blank">Example</a></summary>

.. jupyter-execute::
    :hide-code:

    import numpy as np

    from lets_plot import *
    LetsPlot.setup_html()

.. jupyter-execute::
    :linenos:

    np.random.seed(42)
    data = {"x": np.random.choice(["A", "B", "C"], size=20)}
    ggplot(data, aes(x="x")) + \
        geom_bar(fill="salmon", size=0, tooltips='none') + \
        theme(plot_background=element_rect(fill="navy"),
              text=element_text(color="white"),
              axis=element_line(color="azure"),
              panel_grid=element_line(color="azure"))

.. raw:: html

   </details>

.. note::

  Named colors are case-insensitive and can be written in various formats: ``LightGreen``, ``lightgreen``, ``light green``, or ``light-green`` are all accepted and treated equivalently. You can also use either ``"gray"`` or ``"grey"`` spelling for grayscale colors.

.. note::

  Any named color can carry an opacity suffix: ``"steelblue / 0.35"`` is the named color ``"steelblue"`` at 35% opacity. The opacity value is between ``0.0`` and ``1.0``. See |color_alpha|.

.. tab-set::

  .. tab-item:: By shade

      .. include:: include/aesthetics/named-colors-table_by-shade.rst

  .. tab-item:: By name

      .. include:: include/aesthetics/named-colors-table_by-name.rst

.. |color_alpha| extref:: color_alpha
    :type: text
    :text: example