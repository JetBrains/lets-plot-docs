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
    :text: example notebook


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
    :ref: nbviewer-predefined-patterns
    :type: text
    :text: example notebook

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
    :ref: nbviewer-custom-patterns
    :type: text
    :text: example notebook


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
    :ref: nbviewer-font-family
    :type: text
    :text: example notebook

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
    :ref: nbviewer-font-face
    :type: text
    :text: example notebook


.. _aesthetics_color_and_fill:

Color and Fill
--------------

Colors and fills of geometries can be specified in the following ways:

- **RGB**/**RGBA** - e.g. ``"rgb(0, 0, 255)"``, ``"rgba(0, 0, 255, 0.5)"``.

- **HEX** - e.g. ``"#0077ff"`` or shorthand ``"#07f"``.

- **Transparent** - an empty string (``""``) or the aliases ``"blank"`` and ``"transparent"`` for a fully transparent color.

- **Named colors** - see :doc:`the named colors reference </python/pages/named_colors>`.

- **System colors** depending on the current theme :ref:`flavor <charts_presentation_options_flavors>`, one of:

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
    :text: example notebook
