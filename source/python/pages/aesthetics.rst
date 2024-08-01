.. _tables:

:og:description: A detailed description of the possible values for some aesthetics.

.. title:: Aesthetic Specifications in Lets-Plot

.. meta::
   :description: A detailed description of the possible values for some aesthetics.
   :keywords: ggplot aesthetics, point shape, line type, linetype


Aesthetics
==========

.. jupyter-execute::
   :hide-code:

   from lets_plot import *
   LetsPlot.setup_html()


Point Shapes
------------

.. jupyter-execute::
   :hide-code:

   n = 26
   points_data = {
       'x': (list(range(7)) * 4)[:n],
       'y': ([3] * 7 + [2] * 7 + [1] * 7 + [0] * 7)[:n],
       'shape': list(range(n)),
   }

   ggplot(points_data, aes('x', 'y')) + scale_shape_identity() + \
       geom_text(aes(label='shape'), size=15, fontface='bold', position=position_nudge(y=.3)) + \
       geom_point(aes(shape='shape'), size=10, fill="#fa9fb5", tooltips='none') + \
       xlim(0, 6) + ylim(0, 3) + \
       ggsize(800, 600) + \
       theme_void()


Line Types
----------

.. jupyter-execute::
   :hide-code:

   linetype_names = ['blank', 'solid', 'dashed', 'dotted', 'dotdash', 'longdash', 'twodash']
   linetype_ids = list(range(len(linetype_names)))

   ggplot() + \
       geom_spoke(aes(y=linetype_ids), x=0, angle=0, radius=1, size=4, color="#fa9fb5", alpha=.25) + \
       geom_spoke(aes(y=linetype_ids, linetype=linetype_ids), x=0, angle=0, radius=1, size=2, show_legend=False) + \
       geom_label(aes(y=linetype_ids, label=linetype_ids), x=0, hjust=0, size=12, label_size=0, label_format="{d}:", position=position_nudge(y=.3)) + \
       geom_label(aes(y=linetype_ids, label=linetype_names), x=.04, hjust=0, size=12, label_size=0, label_format="'{}'", position=position_nudge(y=.3)) + \
       scale_x_continuous(limits=[0, 1]) + \
       scale_y_reverse() + \
       scale_linetype_identity() + \
       ggsize(800, 600) + \
       theme_void()