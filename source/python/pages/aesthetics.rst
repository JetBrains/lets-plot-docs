.. _tables:

:og:description: A detailed description of the possible values for some aesthetics.

:orphan:

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


Color and Fill
--------------

Colors and fills of geometries can be specified in the following ways:

- RGB/RGBA (e.g. ``"rgb(0, 0, 255)"``).

- HEX (e.g. ``"#0000ff"``).

- A name, one of:

.. jupyter-execute::
   :hide-code:

   def get_cname(name):
       if "_" in name:
           return "{0}\n{1}\n{2}".format(name, name.replace("_", "-"), name.replace("_", ""))
       else:
           return name

   cols = 5
   border = .5
   xcoeff = 1.5
   ycoeff = 1.5
   variant_colors = [
       "dark_blue", "dark_green", "dark_magenta",
       "light_blue", "light_gray", "light_green",
       "light_yellow", "light_magenta", "light_cyan",
       "light_pink", "very_light_gray", "very_light_yellow",
   ]
   colors = [
       "white", "black", "gray",
       "red", "green", "blue",
       "yellow", "magenta", "cyan",
       "orange", "pink",
   ] + variant_colors
   n = len(colors)
   data = dict(
       x = (int(n / cols + 1) * [xcoeff * v for v in range(cols)])[:n],
       y = [ycoeff * int(i / cols) for i in range(n)],
       c = colors,
       cname = [get_cname(name) for name in colors],
   )

   ggplot(data, aes("x", "y", fill="c")) + \
       geom_point(shape=22, size=.75, size_unit='x', tooltips=layer_tooltips().line("@cname")) + \
       geom_text(aes(label="c"), position=position_nudge(y=.6), family='mono') + \
       scale_y_reverse() + \
       scale_fill_identity() + \
       coord_fixed() + \
       xlim(-xcoeff * border, xcoeff * (cols - 1 + border)) + ylim(-border, ycoeff * int((n - 1) / cols) + border) + \
       ggsize(800, 800) + \
       theme_void()

- A system color name, one of:

.. jupyter-execute::
    :hide-code:

    import pandas as pd
    w, h = 360, 270
    th, lh = 50, 75
    df = pd.read_csv("https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv")

.. grid:: 3

    .. grid-item-card::
        :shadow: none

        .. jupyter-execute::
            :hide-code:

            p1_title = ggplot() + \
                geom_label(x=0, label="pen", \
                           size=10, label_size=0, color='white', fill='pen', family='mono') + \
                theme_void()
            p1_label = ggplot() + \
                geom_text(x=0, label='A hight-contrast color\ncommonly used to draw dots and lines', \
                          size=10) + \
                theme_void()
            p1_example = ggplot(df, aes("cty", "hwy")) + \
                geom_point()
            bunch = GGBunch()
            bunch.add_plot(p1_title, 0, 0, w, th)
            bunch.add_plot(p1_label, 0, th, w, lh)
            bunch.add_plot(p1_example, 0, th + lh, w, h)
            bunch.show()

    .. grid-item-card::
        :shadow: none

        .. jupyter-execute::
            :hide-code:

            p2_title = ggplot() + \
                geom_label(x=0, label="brush", \
                           size=10, label_size=0, color='white', fill='brush', family='mono') + \
                theme_void()
            p2_label = ggplot() + \
                geom_text(x=0, label='A color we often use to fill shapes', \
                          size=10) + \
                theme_void()
            p2_example = ggplot(df, aes("fl")) + \
                geom_bar()
            bunch = GGBunch()
            bunch.add_plot(p2_title, 0, 0, w, th)
            bunch.add_plot(p2_label, 0, th, w, lh)
            bunch.add_plot(p2_example, 0, th + lh, w, h)
            bunch.show()

    .. grid-item-card::
        :shadow: none

        .. jupyter-execute::
            :hide-code:

            p3_title = ggplot() + \
                geom_label(x=0, label="paper", \
                           size=10, color='black', fill='paper', family='mono') + \
                theme_void()
            p3_label = ggplot() + \
                geom_text(x=0, label='A "background" color\nwe often use to fill shapes as well', \
                          size=10) + \
                theme_void()
            p3_example = ggplot(df, aes("drv", "cty")) + \
                geom_boxplot()
            bunch = GGBunch()
            bunch.add_plot(p3_title, 0, 0, w, th)
            bunch.add_plot(p3_label, 0, th, w, lh)
            bunch.add_plot(p3_example, 0, th + lh, w, h)
            bunch.show()


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
       geom_text(aes(label='shape'), size=15, fontface='bold', family='mono', position=position_nudge(y=.3)) + \
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
       geom_label(aes(y=linetype_ids, label=linetype_ids), \
                  x=0, hjust=0, size=12, label_size=0, label_format="{d}:", position=position_nudge(y=.3), family='mono') + \
       geom_label(aes(y=linetype_ids, label=linetype_names), \
                  x=.04, hjust=0, size=12, label_size=0, label_format="'{}'", position=position_nudge(y=.3), family='mono') + \
       scale_x_continuous(limits=[0, 1]) + \
       scale_y_reverse() + \
       scale_linetype_identity() + \
       ggsize(800, 600) + \
       theme_void()