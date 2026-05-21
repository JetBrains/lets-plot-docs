.. _aesthetics:

:og:description: A detailed description of the possible values for some aesthetics.

:orphan:

.. title:: Aesthetic Specifications in Lets-Plot

.. meta::
   :description: A detailed description of the possible values for some aesthetics.
   :keywords: ggplot aesthetics, point shape, line type, linetype


Aesthetics
==========


.. _aesthetics_point_shapes:

Point Shapes
------------

.. image:: /_static/images/pages/aesthetics/aesthetics_shape.png
    :class: only-light
    :width: 800
    :alt: Point shapes

.. image:: /_static/images/pages/aesthetics/aesthetics_shape_dark.png
    :class: only-dark
    :width: 800
    :alt: Point shapes (dark)

See |point_shapes|.

.. |point_shapes| extref:: aesthetics_point_shapes
    :type: text
    :text: example


.. _aesthetics_line_types:

Line Types
----------

Predefined Patterns
~~~~~~~~~~~~~~~~~~~

.. image:: /_static/images/pages/aesthetics/aesthetics_linetype.png
    :class: only-light
    :width: 800
    :alt: Predefined line types

.. image:: /_static/images/pages/aesthetics/aesthetics_linetype_dark.png
    :class: only-dark
    :width: 800
    :alt: Predefined line types (dark)

See |line_types-predefined-patterns|.

.. |line_types-predefined-patterns| extref:: aesthetics_line_types
    :type: text
    :target-id: predefined-patterns
    :text: example

Custom Patterns
~~~~~~~~~~~~~~~

Ways to specify the ``linetype``:

- list, defining the pattern of dashes and gaps used to draw the line: ``[dash, gap, ...]``;
- list with specified offset: ``[offset, [dash, gap, ...]]``;
- string of an even number (up to eight) of hexadecimal digits which give the lengths in consecutive positions in the string.

.. image:: /_static/images/pages/aesthetics/aesthetics_custom_linetype.png
    :class: only-light
    :width: 800
    :alt: Custom line types

.. image:: /_static/images/pages/aesthetics/aesthetics_custom_linetype_dark.png
    :class: only-dark
    :width: 800
    :alt: Custom line types (dark)

See |line_types-custom-patterns|.

.. |line_types-custom-patterns| extref:: aesthetics_line_types
    :type: text
    :target-id: custom-patterns
    :text: example


.. _aesthetics_text:

Text
----

Font Family
~~~~~~~~~~~

Universal font names:

.. image:: /_static/images/pages/aesthetics/aesthetics_font_family.png
    :class: only-light
    :width: 200
    :alt: Font families

.. image:: /_static/images/pages/aesthetics/aesthetics_font_family_dark.png
    :class: only-dark
    :width: 200
    :alt: Font families (dark)

The default font family is ``'sans'``.

You can also use the name of any other font installed on your system (e.g. ``"Times New Roman"``).

See |text-font-family|.

.. |text-font-family| extref:: aesthetics_text_style
    :type: text
    :target-id: font-family
    :text: example

Font Face
~~~~~~~~~

.. image:: /_static/images/pages/aesthetics/aesthetics_font_face.png
    :class: only-light
    :width: 300
    :alt: Font faces

.. image:: /_static/images/pages/aesthetics/aesthetics_font_face_dark.png
    :class: only-dark
    :width: 300
    :alt: Font faces (dark)

The default font face is ``'plain'``.

See |text-font-face|.

.. |text-font-face| extref:: aesthetics_text_style
    :type: text
    :target-id: font-face
    :text: example


.. _aesthetics_color_and_fill:

Color and Fill
--------------

Colors can be specified using :doc:`named colors </python/pages/named_colors>`, RGB/RGBA strings, HEX values,
or ``color(...)``. Named colors are case-insensitive;
hyphens and underscores are ignored, and ``grey`` is treated the same as ``gray``
(``"dark_orange"``, ``"light-blue"``, and ``"DARK-GREY"`` are valid).
In addition to the named colors listed in the :doc:`Named colors reference </python/pages/named_colors>`,
grayscale names from ``"gray0"`` to ``"gray100"`` are supported.
Transparency can be included directly in the color value by using an alpha-enabled format
or by appending opacity to a named color, for example ``"steelblue / 0.35"``.

.. list-table::
   :header-rows: 1

   * - Type
     - Format
     - Example
   * - Named color
     - ``name``
     - ``"steelblue"``
   * - Named color with opacity
     - ``name / a``
     - ``"steelblue / 0.35"``
   * - RGB
     - ``rgb(r, g, b)``
     - ``"rgb(70, 130, 180)"``
   * - RGBA
     - ``rgba(r, g, b, a)``
     - ``"rgba(70, 130, 180, 0.35)"``
   * - Color function
     - ``color(r, g, b)``
     - ``"color(70, 130, 180)"``
   * - Color function with opacity
     - ``color(r, g, b, a)``
     - ``"color(70, 130, 180, 0.35)"``
   * - HEX RGB
     - ``#RRGGBB``, ``#RGB``
     - ``"#4682B4"``, ``"#48B"``
   * - HEX RGBA
     - ``#RRGGBBAA``, ``#RGBA``
     - ``"#4682B459"``, ``"#48B6"``
   * - Transparent
     - ``transparent``, ``blank``, empty string
     - ``"transparent"``

For opacity values, ``0`` means fully transparent and ``1`` means fully opaque;
percentage values such as ``"steelblue/35%"`` are not supported. See also an |color_alpha|.

.. grid:: 3

    .. grid-item-card::
        :shadow: none
        :class-item: system-color-pen

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_pen.png
            :class: only-light
            :alt: System color pen

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_pen_dark.png
            :class: only-dark
            :alt: System color pen (dark)

    .. grid-item-card::
        :shadow: none
        :class-item: system-color-brush

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_brush.png
            :class: only-light
            :alt: System color brush

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_brush_dark.png
            :class: only-dark
            :alt: System color brush (dark)

    .. grid-item-card::
        :shadow: none
        :class-item: system-color-paper

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_paper.png
            :class: only-light
            :alt: System color paper

        .. image:: /_static/images/pages/aesthetics/aesthetics_color_paper_dark.png
            :class: only-dark
            :alt: System color paper (dark)

See |system_colors|.

.. |system_colors| extref:: aesthetics_system_colors
    :type: text
    :text: example

.. |color_alpha| extref:: color_alpha
    :type: text
    :text: example