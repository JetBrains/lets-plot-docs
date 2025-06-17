.. _tables:

:og:description: A detailed description of the possible values for some aesthetics.

:orphan:

.. title:: Aesthetic Specifications in Lets-Plot

.. meta::
   :description: A detailed description of the possible values for some aesthetics.
   :keywords: ggplot aesthetics, point shape, line type, linetype


Aesthetics
==========


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


Color and Fill
--------------

Colors and fills of geometries can be specified in the following ways:

- **RGB**/**RGBA** - e.g. ``"rgb(0, 0, 255)"``, ``"rgba(0, 0, 255, 0.5)"``.

- **HEX** - e.g. ``"#0077ff"`` or shorthand ``"#07f"``.

- **Transparent** - an empty string (``""``) or the aliases ``"blank"`` and ``"transparent"`` for a fully transparent color.

- **Named colors** - a predefined list of color names.

  .. note::

    Named colors are case-insensitive and can be written in various formats: ``LightGreen``, ``lightgreen``, ``light green``, or ``light-green`` are all accepted and treated equivalently. You can also use either ``"gray"`` or ``"grey"`` spelling for grayscale colors.

  .. tab-set::

      .. tab-item:: By color

          .. raw:: html

            <table class="named-colors-table">
            <thead><tr><td colspan="3">Gray colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#000000;color:white;">black</td>
            <td class="light-text" style="background-color:#000000;color:white;">#000000</td>
            <td class="light-text" style="background-color:#000000;color:white;">0,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">gray10</td>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">#1A1A1A</td>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">26,26,26</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#333333;color:white;">gray20</td>
            <td class="light-text" style="background-color:#333333;color:white;">#333333</td>
            <td class="light-text" style="background-color:#333333;color:white;">51,51,51</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">dark_slate_gray</td>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">#2F4F4F</td>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">47,79,79</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">gray30</td>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">#4D4D4D</td>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">77,77,77</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#555555;color:white;">dark_gray</td>
            <td class="light-text" style="background-color:#555555;color:white;">#555555</td>
            <td class="light-text" style="background-color:#555555;color:white;">85,85,85</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#666666;color:white;">gray40</td>
            <td class="light-text" style="background-color:#666666;color:white;">#666666</td>
            <td class="light-text" style="background-color:#666666;color:white;">102,102,102</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#696969;color:white;">dim_gray</td>
            <td class="light-text" style="background-color:#696969;color:white;">#696969</td>
            <td class="light-text" style="background-color:#696969;color:white;">105,105,105</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#708090;color:white;">slate_gray</td>
            <td class="light-text" style="background-color:#708090;color:white;">#708090</td>
            <td class="light-text" style="background-color:#708090;color:white;">112,128,144</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#808080;color:white;">gray</td>
            <td class="light-text" style="background-color:#808080;color:white;">#808080</td>
            <td class="light-text" style="background-color:#808080;color:white;">128,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#808080;color:white;">gray50</td>
            <td class="light-text" style="background-color:#808080;color:white;">#808080</td>
            <td class="light-text" style="background-color:#808080;color:white;">128,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#778899;color:white;">light_slate_gray</td>
            <td class="light-text" style="background-color:#778899;color:white;">#778899</td>
            <td class="light-text" style="background-color:#778899;color:white;">119,136,153</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#999999;color:white;">gray60</td>
            <td class="light-text" style="background-color:#999999;color:white;">#999999</td>
            <td class="light-text" style="background-color:#999999;color:white;">153,153,153</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">gray70</td>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">#B3B3B3</td>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">179,179,179</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">silver</td>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">#C0C0C0</td>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">192,192,192</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">gray80</td>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">#CCCCCC</td>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">204,204,204</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">light_gray</td>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">#D3D3D3</td>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">211,211,211</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">gainsboro</td>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">#DCDCDC</td>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">220,220,220</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">gray90</td>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">#E6E6E6</td>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">230,230,230</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">lavender</td>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">#E6E6FA</td>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">230,230,250</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Brown colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#800000;color:white;">maroon</td>
            <td class="light-text" style="background-color:#800000;color:white;">#800000</td>
            <td class="light-text" style="background-color:#800000;color:white;">128,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B0000;color:white;">dark_red</td>
            <td class="light-text" style="background-color:#8B0000;color:white;">#8B0000</td>
            <td class="light-text" style="background-color:#8B0000;color:white;">139,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B4513;color:white;">saddle_brown</td>
            <td class="light-text" style="background-color:#8B4513;color:white;">#8B4513</td>
            <td class="light-text" style="background-color:#8B4513;color:white;">139,69,19</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A52A2A;color:white;">brown</td>
            <td class="light-text" style="background-color:#A52A2A;color:white;">#A52A2A</td>
            <td class="light-text" style="background-color:#A52A2A;color:white;">165,42,42</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B22222;color:white;">firebrick</td>
            <td class="light-text" style="background-color:#B22222;color:white;">#B22222</td>
            <td class="light-text" style="background-color:#B22222;color:white;">178,34,34</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A0522D;color:white;">sienna</td>
            <td class="light-text" style="background-color:#A0522D;color:white;">#A0522D</td>
            <td class="light-text" style="background-color:#A0522D;color:white;">160,82,45</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">indian_red</td>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">#CD5C5C</td>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">205,92,92</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D2691E;color:white;">chocolate</td>
            <td class="light-text" style="background-color:#D2691E;color:white;">#D2691E</td>
            <td class="light-text" style="background-color:#D2691E;color:white;">210,105,30</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#CD853F;color:white;">peru</td>
            <td class="light-text" style="background-color:#CD853F;color:white;">#CD853F</td>
            <td class="light-text" style="background-color:#CD853F;color:white;">205,133,63</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">rosy_brown</td>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">#BC8F8F</td>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">188,143,143</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D2B48C;color:white;">tan</td>
            <td class="light-text" style="background-color:#D2B48C;color:white;">#D2B48C</td>
            <td class="light-text" style="background-color:#D2B48C;color:white;">210,180,140</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DEB887;color:black;">burly_wood</td>
            <td class="dark-text" style="background-color:#DEB887;color:black;">#DEB887</td>
            <td class="dark-text" style="background-color:#DEB887;color:black;">222,184,135</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Red colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#FF0000;color:white;">red</td>
            <td class="light-text" style="background-color:#FF0000;color:white;">#FF0000</td>
            <td class="light-text" style="background-color:#FF0000;color:white;">255,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF4500;color:white;">orange_red</td>
            <td class="light-text" style="background-color:#FF4500;color:white;">#FF4500</td>
            <td class="light-text" style="background-color:#FF4500;color:white;">255,69,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF6347;color:white;">tomato</td>
            <td class="light-text" style="background-color:#FF6347;color:white;">#FF6347</td>
            <td class="light-text" style="background-color:#FF6347;color:white;">255,99,71</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#F08080;color:white;">light_coral</td>
            <td class="light-text" style="background-color:#F08080;color:white;">#F08080</td>
            <td class="light-text" style="background-color:#F08080;color:white;">240,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FA8072;color:white;">salmon</td>
            <td class="light-text" style="background-color:#FA8072;color:white;">#FA8072</td>
            <td class="light-text" style="background-color:#FA8072;color:white;">250,128,114</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF7F50;color:white;">coral</td>
            <td class="light-text" style="background-color:#FF7F50;color:white;">#FF7F50</td>
            <td class="light-text" style="background-color:#FF7F50;color:white;">255,127,80</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#E9967A;color:white;">dark_salmon</td>
            <td class="light-text" style="background-color:#E9967A;color:white;">#E9967A</td>
            <td class="light-text" style="background-color:#E9967A;color:white;">233,150,122</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">light_salmon</td>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">#FFA07A</td>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">255,160,122</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Orange colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#B8860B;color:white;">dark_goldenrod</td>
            <td class="light-text" style="background-color:#B8860B;color:white;">#B8860B</td>
            <td class="light-text" style="background-color:#B8860B;color:white;">184,134,11</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF8C00;color:white;">dark_orange</td>
            <td class="light-text" style="background-color:#FF8C00;color:white;">#FF8C00</td>
            <td class="light-text" style="background-color:#FF8C00;color:white;">255,140,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DAA520;color:white;">goldenrod</td>
            <td class="light-text" style="background-color:#DAA520;color:white;">#DAA520</td>
            <td class="light-text" style="background-color:#DAA520;color:white;">218,165,32</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F4A460;color:black;">sandy_brown</td>
            <td class="dark-text" style="background-color:#F4A460;color:black;">#F4A460</td>
            <td class="dark-text" style="background-color:#F4A460;color:black;">244,164,96</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFA500;color:black;">orange</td>
            <td class="dark-text" style="background-color:#FFA500;color:black;">#FFA500</td>
            <td class="dark-text" style="background-color:#FFA500;color:black;">255,165,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">peach_puff</td>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">#FFDAB9</td>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">255,218,185</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">wheat</td>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">#F5DEB3</td>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">245,222,179</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">navajo_white</td>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">#FFDEAD</td>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">255,222,173</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">moccasin</td>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">#FFE4B5</td>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">255,228,181</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">bisque</td>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">#FFE4C4</td>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">255,228,196</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Yellow colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#808000;color:white;">olive</td>
            <td class="light-text" style="background-color:#808000;color:white;">#808000</td>
            <td class="light-text" style="background-color:#808000;color:white;">128,128,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BDB76B;color:white;">dark_khaki</td>
            <td class="light-text" style="background-color:#BDB76B;color:white;">#BDB76B</td>
            <td class="light-text" style="background-color:#BDB76B;color:white;">189,183,107</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFD700;color:black;">gold</td>
            <td class="dark-text" style="background-color:#FFD700;color:black;">#FFD700</td>
            <td class="dark-text" style="background-color:#FFD700;color:black;">255,215,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">light_goldenrod</td>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">#EEDD82</td>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">238,221,130</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">khaki</td>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">#F0E68C</td>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">240,230,140</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">pale_goldenrod</td>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">#EEE8AA</td>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">238,232,170</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">yellow</td>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">#FFFF00</td>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">255,255,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">lemon_chiffon</td>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">#FFFACD</td>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">255,250,205</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Green colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#006400;color:white;">dark_green</td>
            <td class="light-text" style="background-color:#006400;color:white;">#006400</td>
            <td class="light-text" style="background-color:#006400;color:white;">0,100,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#556B2F;color:white;">dark_olive_green</td>
            <td class="light-text" style="background-color:#556B2F;color:white;">#556B2F</td>
            <td class="light-text" style="background-color:#556B2F;color:white;">85,107,47</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#008000;color:white;">green</td>
            <td class="light-text" style="background-color:#008000;color:white;">#008000</td>
            <td class="light-text" style="background-color:#008000;color:white;">0,128,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#228B22;color:white;">forest_green</td>
            <td class="light-text" style="background-color:#228B22;color:white;">#228B22</td>
            <td class="light-text" style="background-color:#228B22;color:white;">34,139,34</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2E8B57;color:white;">sea_green</td>
            <td class="light-text" style="background-color:#2E8B57;color:white;">#2E8B57</td>
            <td class="light-text" style="background-color:#2E8B57;color:white;">46,139,87</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6B8E23;color:white;">olive_drab</td>
            <td class="light-text" style="background-color:#6B8E23;color:white;">#6B8E23</td>
            <td class="light-text" style="background-color:#6B8E23;color:white;">107,142,35</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#3CB371;color:white;">medium_sea_green</td>
            <td class="light-text" style="background-color:#3CB371;color:white;">#3CB371</td>
            <td class="light-text" style="background-color:#3CB371;color:white;">60,179,113</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#32CD32;color:white;">lime_green</td>
            <td class="light-text" style="background-color:#32CD32;color:white;">#32CD32</td>
            <td class="light-text" style="background-color:#32CD32;color:white;">50,205,50</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">dark_sea_green</td>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">#8FBC8F</td>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">143,188,143</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#66CDAA;color:white;">medium_aquamarine</td>
            <td class="light-text" style="background-color:#66CDAA;color:white;">#66CDAA</td>
            <td class="light-text" style="background-color:#66CDAA;color:white;">102,205,170</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9ACD32;color:white;">yellow_green</td>
            <td class="light-text" style="background-color:#9ACD32;color:white;">#9ACD32</td>
            <td class="light-text" style="background-color:#9ACD32;color:white;">154,205,50</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#90EE90;color:black;">light_green</td>
            <td class="dark-text" style="background-color:#90EE90;color:black;">#90EE90</td>
            <td class="dark-text" style="background-color:#90EE90;color:black;">144,238,144</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">medium_spring_green</td>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">#00FA9A</td>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">0,250,154</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FF00;color:black;">lime</td>
            <td class="dark-text" style="background-color:#00FF00;color:black;">#00FF00</td>
            <td class="dark-text" style="background-color:#00FF00;color:black;">0,255,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">spring_green</td>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">#00FF7F</td>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">0,255,127</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">lawn_green</td>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">#7CFC00</td>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">124,252,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">chartreuse</td>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">#7FFF00</td>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">127,255,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#98FB98;color:black;">pale_green</td>
            <td class="dark-text" style="background-color:#98FB98;color:black;">#98FB98</td>
            <td class="dark-text" style="background-color:#98FB98;color:black;">152,251,152</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">aquamarine</td>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">#7FFFD4</td>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">127,255,212</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">green_yellow</td>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">#ADFF2F</td>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">173,255,47</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Cyan colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#008080;color:white;">teal</td>
            <td class="light-text" style="background-color:#008080;color:white;">#008080</td>
            <td class="light-text" style="background-color:#008080;color:white;">0,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#008B8B;color:white;">dark_cyan</td>
            <td class="light-text" style="background-color:#008B8B;color:white;">#008B8B</td>
            <td class="light-text" style="background-color:#008B8B;color:white;">0,139,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">cadet_blue</td>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">#5F9EA0</td>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">95,158,160</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#20B2AA;color:white;">light_sea_green</td>
            <td class="light-text" style="background-color:#20B2AA;color:white;">#20B2AA</td>
            <td class="light-text" style="background-color:#20B2AA;color:white;">32,178,170</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00CED1;color:white;">dark_turquoise</td>
            <td class="light-text" style="background-color:#00CED1;color:white;">#00CED1</td>
            <td class="light-text" style="background-color:#00CED1;color:white;">0,206,209</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#48D1CC;color:white;">medium_turquoise</td>
            <td class="light-text" style="background-color:#48D1CC;color:white;">#48D1CC</td>
            <td class="light-text" style="background-color:#48D1CC;color:white;">72,209,204</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">turquoise</td>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">#40E0D0</td>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">64,224,208</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">powderblue</td>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">#B0E0E6</td>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">176,224,230</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">pale_turquoise</td>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">#AFEEEE</td>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">175,238,238</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">aqua</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">#00FFFF</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">0,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">cyan</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">#00FFFF</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">0,255,255</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Blue colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#000080;color:white;">navy</td>
            <td class="light-text" style="background-color:#000080;color:white;">#000080</td>
            <td class="light-text" style="background-color:#000080;color:white;">0,0,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#191970;color:white;">midnight_blue</td>
            <td class="light-text" style="background-color:#191970;color:white;">#191970</td>
            <td class="light-text" style="background-color:#191970;color:white;">25,25,112</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00008B;color:white;">dark_blue</td>
            <td class="light-text" style="background-color:#00008B;color:white;">#00008B</td>
            <td class="light-text" style="background-color:#00008B;color:white;">0,0,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0000CD;color:white;">medium_blue</td>
            <td class="light-text" style="background-color:#0000CD;color:white;">#0000CD</td>
            <td class="light-text" style="background-color:#0000CD;color:white;">0,0,205</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#483D8B;color:white;">dark_slate_blue</td>
            <td class="light-text" style="background-color:#483D8B;color:white;">#483D8B</td>
            <td class="light-text" style="background-color:#483D8B;color:white;">72,61,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0000FF;color:white;">blue</td>
            <td class="light-text" style="background-color:#0000FF;color:white;">#0000FF</td>
            <td class="light-text" style="background-color:#0000FF;color:white;">0,0,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">slate_blue</td>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">#6A5ACD</td>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">106,90,205</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4169E1;color:white;">royal_blue</td>
            <td class="light-text" style="background-color:#4169E1;color:white;">#4169E1</td>
            <td class="light-text" style="background-color:#4169E1;color:white;">65,105,225</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4682B4;color:white;">steel_blue</td>
            <td class="light-text" style="background-color:#4682B4;color:white;">#4682B4</td>
            <td class="light-text" style="background-color:#4682B4;color:white;">70,130,180</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#7B68EE;color:white;">medium_slate_blue</td>
            <td class="light-text" style="background-color:#7B68EE;color:white;">#7B68EE</td>
            <td class="light-text" style="background-color:#7B68EE;color:white;">123,104,238</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#118ED8;color:white;">pacific_blue</td>
            <td class="light-text" style="background-color:#118ED8;color:white;">#118ED8</td>
            <td class="light-text" style="background-color:#118ED8;color:white;">17,142,216</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8470FF;color:white;">light_slate_blue</td>
            <td class="light-text" style="background-color:#8470FF;color:white;">#8470FF</td>
            <td class="light-text" style="background-color:#8470FF;color:white;">132,112,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1E90FF;color:white;">dodger_blue</td>
            <td class="light-text" style="background-color:#1E90FF;color:white;">#1E90FF</td>
            <td class="light-text" style="background-color:#1E90FF;color:white;">30,144,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6495ED;color:white;">cornflower_blue</td>
            <td class="light-text" style="background-color:#6495ED;color:white;">#6495ED</td>
            <td class="light-text" style="background-color:#6495ED;color:white;">100,149,237</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00BFFF;color:white;">deep_sky_blue</td>
            <td class="light-text" style="background-color:#00BFFF;color:white;">#00BFFF</td>
            <td class="light-text" style="background-color:#00BFFF;color:white;">0,191,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">light_steel_blue</td>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">#B0C4DE</td>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">176,196,222</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">sky_blue</td>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">#87CEEB</td>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">135,206,235</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">light_sky_blue</td>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">#87CEFA</td>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">135,206,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">light_blue</td>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">#ADD8E6</td>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">173,216,230</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Purple/violet colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#4B0082;color:white;">indigo</td>
            <td class="light-text" style="background-color:#4B0082;color:white;">#4B0082</td>
            <td class="light-text" style="background-color:#4B0082;color:white;">75,0,130</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#800080;color:white;">purple</td>
            <td class="light-text" style="background-color:#800080;color:white;">#800080</td>
            <td class="light-text" style="background-color:#800080;color:white;">128,0,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#663399;color:white;">rebeccapurple</td>
            <td class="light-text" style="background-color:#663399;color:white;">#663399</td>
            <td class="light-text" style="background-color:#663399;color:white;">102,51,153</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B008B;color:white;">dark_magenta</td>
            <td class="light-text" style="background-color:#8B008B;color:white;">#8B008B</td>
            <td class="light-text" style="background-color:#8B008B;color:white;">139,0,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9400D3;color:white;">dark_violet</td>
            <td class="light-text" style="background-color:#9400D3;color:white;">#9400D3</td>
            <td class="light-text" style="background-color:#9400D3;color:white;">148,0,211</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">blue_violet</td>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">#8A2BE2</td>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">138,43,226</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9932CC;color:white;">dark_orchid</td>
            <td class="light-text" style="background-color:#9932CC;color:white;">#9932CC</td>
            <td class="light-text" style="background-color:#9932CC;color:white;">153,50,204</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9370DB;color:white;">medium_purple</td>
            <td class="light-text" style="background-color:#9370DB;color:white;">#9370DB</td>
            <td class="light-text" style="background-color:#9370DB;color:white;">147,112,219</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BA55D3;color:white;">medium_orchid</td>
            <td class="light-text" style="background-color:#BA55D3;color:white;">#BA55D3</td>
            <td class="light-text" style="background-color:#BA55D3;color:white;">186,85,211</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DA70D6;color:white;">orchid</td>
            <td class="light-text" style="background-color:#DA70D6;color:white;">#DA70D6</td>
            <td class="light-text" style="background-color:#DA70D6;color:white;">218,112,214</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF00FF;color:white;">fuchsia</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">#FF00FF</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">255,0,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF00FF;color:white;">magenta</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">#FF00FF</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">255,0,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#EE82EE;color:white;">violet</td>
            <td class="light-text" style="background-color:#EE82EE;color:white;">#EE82EE</td>
            <td class="light-text" style="background-color:#EE82EE;color:white;">238,130,238</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">plum</td>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">#DDA0DD</td>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">221,160,221</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">thistle</td>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">#D8BFD8</td>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">216,191,216</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">light_magenta</td>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">#FFD2FF</td>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">255,210,255</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Rose colors</td></tr></thead>
            <tr>
            <td class="light-text" style="background-color:#C71585;color:white;">medium_violet_red</td>
            <td class="light-text" style="background-color:#C71585;color:white;">#C71585</td>
            <td class="light-text" style="background-color:#C71585;color:white;">199,21,133</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DC143C;color:white;">crimson</td>
            <td class="light-text" style="background-color:#DC143C;color:white;">#DC143C</td>
            <td class="light-text" style="background-color:#DC143C;color:white;">220,20,60</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D02090;color:white;">violet_red</td>
            <td class="light-text" style="background-color:#D02090;color:white;">#D02090</td>
            <td class="light-text" style="background-color:#D02090;color:white;">208,32,144</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF1493;color:white;">deep_pink</td>
            <td class="light-text" style="background-color:#FF1493;color:white;">#FF1493</td>
            <td class="light-text" style="background-color:#FF1493;color:white;">255,20,147</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DB7093;color:white;">pale_violet_red</td>
            <td class="light-text" style="background-color:#DB7093;color:white;">#DB7093</td>
            <td class="light-text" style="background-color:#DB7093;color:white;">219,112,147</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF69B4;color:white;">hot_pink</td>
            <td class="light-text" style="background-color:#FF69B4;color:white;">#FF69B4</td>
            <td class="light-text" style="background-color:#FF69B4;color:white;">255,105,180</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">light_pink</td>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">#FFB6C1</td>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">255,182,193</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">pink</td>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">#FFC0CB</td>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">255,192,203</td>
            </tr>
            </table>
            <table class="named-colors-table">
            <thead><tr><td colspan="3">Very light colors</td></tr></thead>
            <tr>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">white</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">#FFFFFF</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">255,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">snow</td>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">#FFFAFA</td>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">255,250,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">white_smoke</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">#F5F5F5</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">245,245,245</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">misty_rose</td>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">#FFE4E1</td>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">255,228,225</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">sea_shell</td>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">#FFF5EE</td>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">255,245,238</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">linen</td>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">#FAF0E6</td>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">250,240,230</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">antique_white</td>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">#FAEBD7</td>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">250,235,215</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">blanched_almond</td>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">#FFEBCD</td>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">255,235,205</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">papaya_whip</td>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">#FFEFD5</td>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">255,239,213</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">floral_white</td>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">#FFFAF0</td>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">255,250,240</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">old_lace</td>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">#FDF5E6</td>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">253,245,230</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">cornsilk</td>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">#FFF8DC</td>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">255,248,220</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">ivory</td>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">#FFFFF0</td>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">255,255,240</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">light_yellow</td>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">#FFFFE0</td>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">255,255,224</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">light_goldenrod_yellow</td>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">#FAFAD2</td>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">250,250,210</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">beige</td>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">#F5F5DC</td>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">245,245,220</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">honey_dew</td>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">#F0FFF0</td>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">240,255,240</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">mint_cream</td>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">#F5FFFA</td>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">245,255,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">azure</td>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">#F0FFFF</td>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">240,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">light_cyan</td>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">#E0FFFF</td>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">224,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">alice_blue</td>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">#F0F8FF</td>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">240,248,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">ghost_white</td>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">#F8F8FF</td>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">248,248,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">lavender_blush</td>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">#FFF0F5</td>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">255,240,245</td>
            </tr>
            </table>

      .. tab-item:: By name

          .. raw:: html

            <table class="named-colors-table by-name">
            <tr>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">alice_blue</td>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">#F0F8FF</td>
            <td class="dark-text" style="background-color:#F0F8FF;color:black;">240,248,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">antique_white</td>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">#FAEBD7</td>
            <td class="dark-text" style="background-color:#FAEBD7;color:black;">250,235,215</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">aqua</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">#00FFFF</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">0,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">aquamarine</td>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">#7FFFD4</td>
            <td class="dark-text" style="background-color:#7FFFD4;color:black;">127,255,212</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">azure</td>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">#F0FFFF</td>
            <td class="dark-text" style="background-color:#F0FFFF;color:black;">240,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">beige</td>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">#F5F5DC</td>
            <td class="dark-text" style="background-color:#F5F5DC;color:black;">245,245,220</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">bisque</td>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">#FFE4C4</td>
            <td class="dark-text" style="background-color:#FFE4C4;color:black;">255,228,196</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#000000;color:white;">black</td>
            <td class="light-text" style="background-color:#000000;color:white;">#000000</td>
            <td class="light-text" style="background-color:#000000;color:white;">0,0,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">blanched_almond</td>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">#FFEBCD</td>
            <td class="dark-text" style="background-color:#FFEBCD;color:black;">255,235,205</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0000FF;color:white;">blue</td>
            <td class="light-text" style="background-color:#0000FF;color:white;">#0000FF</td>
            <td class="light-text" style="background-color:#0000FF;color:white;">0,0,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">blue_violet</td>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">#8A2BE2</td>
            <td class="light-text" style="background-color:#8A2BE2;color:white;">138,43,226</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A52A2A;color:white;">brown</td>
            <td class="light-text" style="background-color:#A52A2A;color:white;">#A52A2A</td>
            <td class="light-text" style="background-color:#A52A2A;color:white;">165,42,42</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DEB887;color:black;">burly_wood</td>
            <td class="dark-text" style="background-color:#DEB887;color:black;">#DEB887</td>
            <td class="dark-text" style="background-color:#DEB887;color:black;">222,184,135</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">cadet_blue</td>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">#5F9EA0</td>
            <td class="light-text" style="background-color:#5F9EA0;color:white;">95,158,160</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">chartreuse</td>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">#7FFF00</td>
            <td class="dark-text" style="background-color:#7FFF00;color:black;">127,255,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D2691E;color:white;">chocolate</td>
            <td class="light-text" style="background-color:#D2691E;color:white;">#D2691E</td>
            <td class="light-text" style="background-color:#D2691E;color:white;">210,105,30</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF7F50;color:white;">coral</td>
            <td class="light-text" style="background-color:#FF7F50;color:white;">#FF7F50</td>
            <td class="light-text" style="background-color:#FF7F50;color:white;">255,127,80</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6495ED;color:white;">cornflower_blue</td>
            <td class="light-text" style="background-color:#6495ED;color:white;">#6495ED</td>
            <td class="light-text" style="background-color:#6495ED;color:white;">100,149,237</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">cornsilk</td>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">#FFF8DC</td>
            <td class="dark-text" style="background-color:#FFF8DC;color:black;">255,248,220</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DC143C;color:white;">crimson</td>
            <td class="light-text" style="background-color:#DC143C;color:white;">#DC143C</td>
            <td class="light-text" style="background-color:#DC143C;color:white;">220,20,60</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">cyan</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">#00FFFF</td>
            <td class="dark-text" style="background-color:#00FFFF;color:black;">0,255,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00008B;color:white;">dark_blue</td>
            <td class="light-text" style="background-color:#00008B;color:white;">#00008B</td>
            <td class="light-text" style="background-color:#00008B;color:white;">0,0,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#008B8B;color:white;">dark_cyan</td>
            <td class="light-text" style="background-color:#008B8B;color:white;">#008B8B</td>
            <td class="light-text" style="background-color:#008B8B;color:white;">0,139,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B8860B;color:white;">dark_goldenrod</td>
            <td class="light-text" style="background-color:#B8860B;color:white;">#B8860B</td>
            <td class="light-text" style="background-color:#B8860B;color:white;">184,134,11</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#555555;color:white;">dark_gray</td>
            <td class="light-text" style="background-color:#555555;color:white;">#555555</td>
            <td class="light-text" style="background-color:#555555;color:white;">85,85,85</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#006400;color:white;">dark_green</td>
            <td class="light-text" style="background-color:#006400;color:white;">#006400</td>
            <td class="light-text" style="background-color:#006400;color:white;">0,100,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BDB76B;color:white;">dark_khaki</td>
            <td class="light-text" style="background-color:#BDB76B;color:white;">#BDB76B</td>
            <td class="light-text" style="background-color:#BDB76B;color:white;">189,183,107</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B008B;color:white;">dark_magenta</td>
            <td class="light-text" style="background-color:#8B008B;color:white;">#8B008B</td>
            <td class="light-text" style="background-color:#8B008B;color:white;">139,0,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#556B2F;color:white;">dark_olive_green</td>
            <td class="light-text" style="background-color:#556B2F;color:white;">#556B2F</td>
            <td class="light-text" style="background-color:#556B2F;color:white;">85,107,47</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF8C00;color:white;">dark_orange</td>
            <td class="light-text" style="background-color:#FF8C00;color:white;">#FF8C00</td>
            <td class="light-text" style="background-color:#FF8C00;color:white;">255,140,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9932CC;color:white;">dark_orchid</td>
            <td class="light-text" style="background-color:#9932CC;color:white;">#9932CC</td>
            <td class="light-text" style="background-color:#9932CC;color:white;">153,50,204</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B0000;color:white;">dark_red</td>
            <td class="light-text" style="background-color:#8B0000;color:white;">#8B0000</td>
            <td class="light-text" style="background-color:#8B0000;color:white;">139,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#E9967A;color:white;">dark_salmon</td>
            <td class="light-text" style="background-color:#E9967A;color:white;">#E9967A</td>
            <td class="light-text" style="background-color:#E9967A;color:white;">233,150,122</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">dark_sea_green</td>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">#8FBC8F</td>
            <td class="light-text" style="background-color:#8FBC8F;color:white;">143,188,143</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#483D8B;color:white;">dark_slate_blue</td>
            <td class="light-text" style="background-color:#483D8B;color:white;">#483D8B</td>
            <td class="light-text" style="background-color:#483D8B;color:white;">72,61,139</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">dark_slate_gray</td>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">#2F4F4F</td>
            <td class="light-text" style="background-color:#2F4F4F;color:white;">47,79,79</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00CED1;color:white;">dark_turquoise</td>
            <td class="light-text" style="background-color:#00CED1;color:white;">#00CED1</td>
            <td class="light-text" style="background-color:#00CED1;color:white;">0,206,209</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9400D3;color:white;">dark_violet</td>
            <td class="light-text" style="background-color:#9400D3;color:white;">#9400D3</td>
            <td class="light-text" style="background-color:#9400D3;color:white;">148,0,211</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF1493;color:white;">deep_pink</td>
            <td class="light-text" style="background-color:#FF1493;color:white;">#FF1493</td>
            <td class="light-text" style="background-color:#FF1493;color:white;">255,20,147</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#00BFFF;color:white;">deep_sky_blue</td>
            <td class="light-text" style="background-color:#00BFFF;color:white;">#00BFFF</td>
            <td class="light-text" style="background-color:#00BFFF;color:white;">0,191,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#696969;color:white;">dim_gray</td>
            <td class="light-text" style="background-color:#696969;color:white;">#696969</td>
            <td class="light-text" style="background-color:#696969;color:white;">105,105,105</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1E90FF;color:white;">dodger_blue</td>
            <td class="light-text" style="background-color:#1E90FF;color:white;">#1E90FF</td>
            <td class="light-text" style="background-color:#1E90FF;color:white;">30,144,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B22222;color:white;">firebrick</td>
            <td class="light-text" style="background-color:#B22222;color:white;">#B22222</td>
            <td class="light-text" style="background-color:#B22222;color:white;">178,34,34</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">floral_white</td>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">#FFFAF0</td>
            <td class="dark-text" style="background-color:#FFFAF0;color:black;">255,250,240</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#228B22;color:white;">forest_green</td>
            <td class="light-text" style="background-color:#228B22;color:white;">#228B22</td>
            <td class="light-text" style="background-color:#228B22;color:white;">34,139,34</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF00FF;color:white;">fuchsia</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">#FF00FF</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">255,0,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">gainsboro</td>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">#DCDCDC</td>
            <td class="dark-text" style="background-color:#DCDCDC;color:black;">220,220,220</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">ghost_white</td>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">#F8F8FF</td>
            <td class="dark-text" style="background-color:#F8F8FF;color:black;">248,248,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFD700;color:black;">gold</td>
            <td class="dark-text" style="background-color:#FFD700;color:black;">#FFD700</td>
            <td class="dark-text" style="background-color:#FFD700;color:black;">255,215,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DAA520;color:white;">goldenrod</td>
            <td class="light-text" style="background-color:#DAA520;color:white;">#DAA520</td>
            <td class="light-text" style="background-color:#DAA520;color:white;">218,165,32</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#808080;color:white;">gray</td>
            <td class="light-text" style="background-color:#808080;color:white;">#808080</td>
            <td class="light-text" style="background-color:#808080;color:white;">128,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#000000;color:white;">gray0</td>
            <td class="light-text" style="background-color:#000000;color:white;">#000000</td>
            <td class="light-text" style="background-color:#000000;color:white;">0,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#030303;color:white;">gray1</td>
            <td class="light-text" style="background-color:#030303;color:white;">#030303</td>
            <td class="light-text" style="background-color:#030303;color:white;">3,3,3</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#050505;color:white;">gray2</td>
            <td class="light-text" style="background-color:#050505;color:white;">#050505</td>
            <td class="light-text" style="background-color:#050505;color:white;">5,5,5</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#080808;color:white;">gray3</td>
            <td class="light-text" style="background-color:#080808;color:white;">#080808</td>
            <td class="light-text" style="background-color:#080808;color:white;">8,8,8</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0A0A0A;color:white;">gray4</td>
            <td class="light-text" style="background-color:#0A0A0A;color:white;">#0A0A0A</td>
            <td class="light-text" style="background-color:#0A0A0A;color:white;">10,10,10</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0D0D0D;color:white;">gray5</td>
            <td class="light-text" style="background-color:#0D0D0D;color:white;">#0D0D0D</td>
            <td class="light-text" style="background-color:#0D0D0D;color:white;">13,13,13</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0F0F0F;color:white;">gray6</td>
            <td class="light-text" style="background-color:#0F0F0F;color:white;">#0F0F0F</td>
            <td class="light-text" style="background-color:#0F0F0F;color:white;">15,15,15</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#121212;color:white;">gray7</td>
            <td class="light-text" style="background-color:#121212;color:white;">#121212</td>
            <td class="light-text" style="background-color:#121212;color:white;">18,18,18</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#141414;color:white;">gray8</td>
            <td class="light-text" style="background-color:#141414;color:white;">#141414</td>
            <td class="light-text" style="background-color:#141414;color:white;">20,20,20</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#171717;color:white;">gray9</td>
            <td class="light-text" style="background-color:#171717;color:white;">#171717</td>
            <td class="light-text" style="background-color:#171717;color:white;">23,23,23</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">gray10</td>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">#1A1A1A</td>
            <td class="light-text" style="background-color:#1A1A1A;color:white;">26,26,26</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1C1C1C;color:white;">gray11</td>
            <td class="light-text" style="background-color:#1C1C1C;color:white;">#1C1C1C</td>
            <td class="light-text" style="background-color:#1C1C1C;color:white;">28,28,28</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#1F1F1F;color:white;">gray12</td>
            <td class="light-text" style="background-color:#1F1F1F;color:white;">#1F1F1F</td>
            <td class="light-text" style="background-color:#1F1F1F;color:white;">31,31,31</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#212121;color:white;">gray13</td>
            <td class="light-text" style="background-color:#212121;color:white;">#212121</td>
            <td class="light-text" style="background-color:#212121;color:white;">33,33,33</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#242424;color:white;">gray14</td>
            <td class="light-text" style="background-color:#242424;color:white;">#242424</td>
            <td class="light-text" style="background-color:#242424;color:white;">36,36,36</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#262626;color:white;">gray15</td>
            <td class="light-text" style="background-color:#262626;color:white;">#262626</td>
            <td class="light-text" style="background-color:#262626;color:white;">38,38,38</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#292929;color:white;">gray16</td>
            <td class="light-text" style="background-color:#292929;color:white;">#292929</td>
            <td class="light-text" style="background-color:#292929;color:white;">41,41,41</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2B2B2B;color:white;">gray17</td>
            <td class="light-text" style="background-color:#2B2B2B;color:white;">#2B2B2B</td>
            <td class="light-text" style="background-color:#2B2B2B;color:white;">43,43,43</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2E2E2E;color:white;">gray18</td>
            <td class="light-text" style="background-color:#2E2E2E;color:white;">#2E2E2E</td>
            <td class="light-text" style="background-color:#2E2E2E;color:white;">46,46,46</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#303030;color:white;">gray19</td>
            <td class="light-text" style="background-color:#303030;color:white;">#303030</td>
            <td class="light-text" style="background-color:#303030;color:white;">48,48,48</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#333333;color:white;">gray20</td>
            <td class="light-text" style="background-color:#333333;color:white;">#333333</td>
            <td class="light-text" style="background-color:#333333;color:white;">51,51,51</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#363636;color:white;">gray21</td>
            <td class="light-text" style="background-color:#363636;color:white;">#363636</td>
            <td class="light-text" style="background-color:#363636;color:white;">54,54,54</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#383838;color:white;">gray22</td>
            <td class="light-text" style="background-color:#383838;color:white;">#383838</td>
            <td class="light-text" style="background-color:#383838;color:white;">56,56,56</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#3B3B3B;color:white;">gray23</td>
            <td class="light-text" style="background-color:#3B3B3B;color:white;">#3B3B3B</td>
            <td class="light-text" style="background-color:#3B3B3B;color:white;">59,59,59</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#3D3D3D;color:white;">gray24</td>
            <td class="light-text" style="background-color:#3D3D3D;color:white;">#3D3D3D</td>
            <td class="light-text" style="background-color:#3D3D3D;color:white;">61,61,61</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#404040;color:white;">gray25</td>
            <td class="light-text" style="background-color:#404040;color:white;">#404040</td>
            <td class="light-text" style="background-color:#404040;color:white;">64,64,64</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#424242;color:white;">gray26</td>
            <td class="light-text" style="background-color:#424242;color:white;">#424242</td>
            <td class="light-text" style="background-color:#424242;color:white;">66,66,66</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#454545;color:white;">gray27</td>
            <td class="light-text" style="background-color:#454545;color:white;">#454545</td>
            <td class="light-text" style="background-color:#454545;color:white;">69,69,69</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#474747;color:white;">gray28</td>
            <td class="light-text" style="background-color:#474747;color:white;">#474747</td>
            <td class="light-text" style="background-color:#474747;color:white;">71,71,71</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4A4A4A;color:white;">gray29</td>
            <td class="light-text" style="background-color:#4A4A4A;color:white;">#4A4A4A</td>
            <td class="light-text" style="background-color:#4A4A4A;color:white;">74,74,74</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">gray30</td>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">#4D4D4D</td>
            <td class="light-text" style="background-color:#4D4D4D;color:white;">77,77,77</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4F4F4F;color:white;">gray31</td>
            <td class="light-text" style="background-color:#4F4F4F;color:white;">#4F4F4F</td>
            <td class="light-text" style="background-color:#4F4F4F;color:white;">79,79,79</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#525252;color:white;">gray32</td>
            <td class="light-text" style="background-color:#525252;color:white;">#525252</td>
            <td class="light-text" style="background-color:#525252;color:white;">82,82,82</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#545454;color:white;">gray33</td>
            <td class="light-text" style="background-color:#545454;color:white;">#545454</td>
            <td class="light-text" style="background-color:#545454;color:white;">84,84,84</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#575757;color:white;">gray34</td>
            <td class="light-text" style="background-color:#575757;color:white;">#575757</td>
            <td class="light-text" style="background-color:#575757;color:white;">87,87,87</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#595959;color:white;">gray35</td>
            <td class="light-text" style="background-color:#595959;color:white;">#595959</td>
            <td class="light-text" style="background-color:#595959;color:white;">89,89,89</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#5C5C5C;color:white;">gray36</td>
            <td class="light-text" style="background-color:#5C5C5C;color:white;">#5C5C5C</td>
            <td class="light-text" style="background-color:#5C5C5C;color:white;">92,92,92</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#5E5E5E;color:white;">gray37</td>
            <td class="light-text" style="background-color:#5E5E5E;color:white;">#5E5E5E</td>
            <td class="light-text" style="background-color:#5E5E5E;color:white;">94,94,94</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#616161;color:white;">gray38</td>
            <td class="light-text" style="background-color:#616161;color:white;">#616161</td>
            <td class="light-text" style="background-color:#616161;color:white;">97,97,97</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#636363;color:white;">gray39</td>
            <td class="light-text" style="background-color:#636363;color:white;">#636363</td>
            <td class="light-text" style="background-color:#636363;color:white;">99,99,99</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#666666;color:white;">gray40</td>
            <td class="light-text" style="background-color:#666666;color:white;">#666666</td>
            <td class="light-text" style="background-color:#666666;color:white;">102,102,102</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#696969;color:white;">gray41</td>
            <td class="light-text" style="background-color:#696969;color:white;">#696969</td>
            <td class="light-text" style="background-color:#696969;color:white;">105,105,105</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6B6B6B;color:white;">gray42</td>
            <td class="light-text" style="background-color:#6B6B6B;color:white;">#6B6B6B</td>
            <td class="light-text" style="background-color:#6B6B6B;color:white;">107,107,107</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6E6E6E;color:white;">gray43</td>
            <td class="light-text" style="background-color:#6E6E6E;color:white;">#6E6E6E</td>
            <td class="light-text" style="background-color:#6E6E6E;color:white;">110,110,110</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#707070;color:white;">gray44</td>
            <td class="light-text" style="background-color:#707070;color:white;">#707070</td>
            <td class="light-text" style="background-color:#707070;color:white;">112,112,112</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#737373;color:white;">gray45</td>
            <td class="light-text" style="background-color:#737373;color:white;">#737373</td>
            <td class="light-text" style="background-color:#737373;color:white;">115,115,115</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#757575;color:white;">gray46</td>
            <td class="light-text" style="background-color:#757575;color:white;">#757575</td>
            <td class="light-text" style="background-color:#757575;color:white;">117,117,117</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#787878;color:white;">gray47</td>
            <td class="light-text" style="background-color:#787878;color:white;">#787878</td>
            <td class="light-text" style="background-color:#787878;color:white;">120,120,120</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#7A7A7A;color:white;">gray48</td>
            <td class="light-text" style="background-color:#7A7A7A;color:white;">#7A7A7A</td>
            <td class="light-text" style="background-color:#7A7A7A;color:white;">122,122,122</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#7D7D7D;color:white;">gray49</td>
            <td class="light-text" style="background-color:#7D7D7D;color:white;">#7D7D7D</td>
            <td class="light-text" style="background-color:#7D7D7D;color:white;">125,125,125</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#808080;color:white;">gray50</td>
            <td class="light-text" style="background-color:#808080;color:white;">#808080</td>
            <td class="light-text" style="background-color:#808080;color:white;">128,128,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#828282;color:white;">gray51</td>
            <td class="light-text" style="background-color:#828282;color:white;">#828282</td>
            <td class="light-text" style="background-color:#828282;color:white;">130,130,130</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#858585;color:white;">gray52</td>
            <td class="light-text" style="background-color:#858585;color:white;">#858585</td>
            <td class="light-text" style="background-color:#858585;color:white;">133,133,133</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#878787;color:white;">gray53</td>
            <td class="light-text" style="background-color:#878787;color:white;">#878787</td>
            <td class="light-text" style="background-color:#878787;color:white;">135,135,135</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8A8A8A;color:white;">gray54</td>
            <td class="light-text" style="background-color:#8A8A8A;color:white;">#8A8A8A</td>
            <td class="light-text" style="background-color:#8A8A8A;color:white;">138,138,138</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8C8C8C;color:white;">gray55</td>
            <td class="light-text" style="background-color:#8C8C8C;color:white;">#8C8C8C</td>
            <td class="light-text" style="background-color:#8C8C8C;color:white;">140,140,140</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8F8F8F;color:white;">gray56</td>
            <td class="light-text" style="background-color:#8F8F8F;color:white;">#8F8F8F</td>
            <td class="light-text" style="background-color:#8F8F8F;color:white;">143,143,143</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#919191;color:white;">gray57</td>
            <td class="light-text" style="background-color:#919191;color:white;">#919191</td>
            <td class="light-text" style="background-color:#919191;color:white;">145,145,145</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#949494;color:white;">gray58</td>
            <td class="light-text" style="background-color:#949494;color:white;">#949494</td>
            <td class="light-text" style="background-color:#949494;color:white;">148,148,148</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#969696;color:white;">gray59</td>
            <td class="light-text" style="background-color:#969696;color:white;">#969696</td>
            <td class="light-text" style="background-color:#969696;color:white;">150,150,150</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#999999;color:white;">gray60</td>
            <td class="light-text" style="background-color:#999999;color:white;">#999999</td>
            <td class="light-text" style="background-color:#999999;color:white;">153,153,153</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9C9C9C;color:white;">gray61</td>
            <td class="light-text" style="background-color:#9C9C9C;color:white;">#9C9C9C</td>
            <td class="light-text" style="background-color:#9C9C9C;color:white;">156,156,156</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9E9E9E;color:white;">gray62</td>
            <td class="light-text" style="background-color:#9E9E9E;color:white;">#9E9E9E</td>
            <td class="light-text" style="background-color:#9E9E9E;color:white;">158,158,158</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A1A1A1;color:white;">gray63</td>
            <td class="light-text" style="background-color:#A1A1A1;color:white;">#A1A1A1</td>
            <td class="light-text" style="background-color:#A1A1A1;color:white;">161,161,161</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A3A3A3;color:white;">gray64</td>
            <td class="light-text" style="background-color:#A3A3A3;color:white;">#A3A3A3</td>
            <td class="light-text" style="background-color:#A3A3A3;color:white;">163,163,163</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A6A6A6;color:white;">gray65</td>
            <td class="light-text" style="background-color:#A6A6A6;color:white;">#A6A6A6</td>
            <td class="light-text" style="background-color:#A6A6A6;color:white;">166,166,166</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A8A8A8;color:white;">gray66</td>
            <td class="light-text" style="background-color:#A8A8A8;color:white;">#A8A8A8</td>
            <td class="light-text" style="background-color:#A8A8A8;color:white;">168,168,168</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#ABABAB;color:white;">gray67</td>
            <td class="light-text" style="background-color:#ABABAB;color:white;">#ABABAB</td>
            <td class="light-text" style="background-color:#ABABAB;color:white;">171,171,171</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#ADADAD;color:white;">gray68</td>
            <td class="light-text" style="background-color:#ADADAD;color:white;">#ADADAD</td>
            <td class="light-text" style="background-color:#ADADAD;color:white;">173,173,173</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B0B0B0;color:white;">gray69</td>
            <td class="light-text" style="background-color:#B0B0B0;color:white;">#B0B0B0</td>
            <td class="light-text" style="background-color:#B0B0B0;color:white;">176,176,176</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">gray70</td>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">#B3B3B3</td>
            <td class="light-text" style="background-color:#B3B3B3;color:white;">179,179,179</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B5B5B5;color:white;">gray71</td>
            <td class="light-text" style="background-color:#B5B5B5;color:white;">#B5B5B5</td>
            <td class="light-text" style="background-color:#B5B5B5;color:white;">181,181,181</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#B8B8B8;color:white;">gray72</td>
            <td class="light-text" style="background-color:#B8B8B8;color:white;">#B8B8B8</td>
            <td class="light-text" style="background-color:#B8B8B8;color:white;">184,184,184</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BABABA;color:white;">gray73</td>
            <td class="light-text" style="background-color:#BABABA;color:white;">#BABABA</td>
            <td class="light-text" style="background-color:#BABABA;color:white;">186,186,186</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#BDBDBD;color:black;">gray74</td>
            <td class="dark-text" style="background-color:#BDBDBD;color:black;">#BDBDBD</td>
            <td class="dark-text" style="background-color:#BDBDBD;color:black;">189,189,189</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#BFBFBF;color:black;">gray75</td>
            <td class="dark-text" style="background-color:#BFBFBF;color:black;">#BFBFBF</td>
            <td class="dark-text" style="background-color:#BFBFBF;color:black;">191,191,191</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C2C2C2;color:black;">gray76</td>
            <td class="dark-text" style="background-color:#C2C2C2;color:black;">#C2C2C2</td>
            <td class="dark-text" style="background-color:#C2C2C2;color:black;">194,194,194</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C4C4C4;color:black;">gray77</td>
            <td class="dark-text" style="background-color:#C4C4C4;color:black;">#C4C4C4</td>
            <td class="dark-text" style="background-color:#C4C4C4;color:black;">196,196,196</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C7C7C7;color:black;">gray78</td>
            <td class="dark-text" style="background-color:#C7C7C7;color:black;">#C7C7C7</td>
            <td class="dark-text" style="background-color:#C7C7C7;color:black;">199,199,199</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C9C9C9;color:black;">gray79</td>
            <td class="dark-text" style="background-color:#C9C9C9;color:black;">#C9C9C9</td>
            <td class="dark-text" style="background-color:#C9C9C9;color:black;">201,201,201</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">gray80</td>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">#CCCCCC</td>
            <td class="dark-text" style="background-color:#CCCCCC;color:black;">204,204,204</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#CFCFCF;color:black;">gray81</td>
            <td class="dark-text" style="background-color:#CFCFCF;color:black;">#CFCFCF</td>
            <td class="dark-text" style="background-color:#CFCFCF;color:black;">207,207,207</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D1D1D1;color:black;">gray82</td>
            <td class="dark-text" style="background-color:#D1D1D1;color:black;">#D1D1D1</td>
            <td class="dark-text" style="background-color:#D1D1D1;color:black;">209,209,209</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D4D4D4;color:black;">gray83</td>
            <td class="dark-text" style="background-color:#D4D4D4;color:black;">#D4D4D4</td>
            <td class="dark-text" style="background-color:#D4D4D4;color:black;">212,212,212</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D6D6D6;color:black;">gray84</td>
            <td class="dark-text" style="background-color:#D6D6D6;color:black;">#D6D6D6</td>
            <td class="dark-text" style="background-color:#D6D6D6;color:black;">214,214,214</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D9D9D9;color:black;">gray85</td>
            <td class="dark-text" style="background-color:#D9D9D9;color:black;">#D9D9D9</td>
            <td class="dark-text" style="background-color:#D9D9D9;color:black;">217,217,217</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DBDBDB;color:black;">gray86</td>
            <td class="dark-text" style="background-color:#DBDBDB;color:black;">#DBDBDB</td>
            <td class="dark-text" style="background-color:#DBDBDB;color:black;">219,219,219</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DEDEDE;color:black;">gray87</td>
            <td class="dark-text" style="background-color:#DEDEDE;color:black;">#DEDEDE</td>
            <td class="dark-text" style="background-color:#DEDEDE;color:black;">222,222,222</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E0E0E0;color:black;">gray88</td>
            <td class="dark-text" style="background-color:#E0E0E0;color:black;">#E0E0E0</td>
            <td class="dark-text" style="background-color:#E0E0E0;color:black;">224,224,224</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E3E3E3;color:black;">gray89</td>
            <td class="dark-text" style="background-color:#E3E3E3;color:black;">#E3E3E3</td>
            <td class="dark-text" style="background-color:#E3E3E3;color:black;">227,227,227</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">gray90</td>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">#E6E6E6</td>
            <td class="dark-text" style="background-color:#E6E6E6;color:black;">230,230,230</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E8E8E8;color:black;">gray91</td>
            <td class="dark-text" style="background-color:#E8E8E8;color:black;">#E8E8E8</td>
            <td class="dark-text" style="background-color:#E8E8E8;color:black;">232,232,232</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EBEBEB;color:black;">gray92</td>
            <td class="dark-text" style="background-color:#EBEBEB;color:black;">#EBEBEB</td>
            <td class="dark-text" style="background-color:#EBEBEB;color:black;">235,235,235</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EDEDED;color:black;">gray93</td>
            <td class="dark-text" style="background-color:#EDEDED;color:black;">#EDEDED</td>
            <td class="dark-text" style="background-color:#EDEDED;color:black;">237,237,237</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0F0F0;color:black;">gray94</td>
            <td class="dark-text" style="background-color:#F0F0F0;color:black;">#F0F0F0</td>
            <td class="dark-text" style="background-color:#F0F0F0;color:black;">240,240,240</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F2F2F2;color:black;">gray95</td>
            <td class="dark-text" style="background-color:#F2F2F2;color:black;">#F2F2F2</td>
            <td class="dark-text" style="background-color:#F2F2F2;color:black;">242,242,242</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">gray96</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">#F5F5F5</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">245,245,245</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F7F7F7;color:black;">gray97</td>
            <td class="dark-text" style="background-color:#F7F7F7;color:black;">#F7F7F7</td>
            <td class="dark-text" style="background-color:#F7F7F7;color:black;">247,247,247</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAFAFA;color:black;">gray98</td>
            <td class="dark-text" style="background-color:#FAFAFA;color:black;">#FAFAFA</td>
            <td class="dark-text" style="background-color:#FAFAFA;color:black;">250,250,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FCFCFC;color:black;">gray99</td>
            <td class="dark-text" style="background-color:#FCFCFC;color:black;">#FCFCFC</td>
            <td class="dark-text" style="background-color:#FCFCFC;color:black;">252,252,252</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">gray100</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">#FFFFFF</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">255,255,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#008000;color:white;">green</td>
            <td class="light-text" style="background-color:#008000;color:white;">#008000</td>
            <td class="light-text" style="background-color:#008000;color:white;">0,128,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">green_yellow</td>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">#ADFF2F</td>
            <td class="dark-text" style="background-color:#ADFF2F;color:black;">173,255,47</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">honey_dew</td>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">#F0FFF0</td>
            <td class="dark-text" style="background-color:#F0FFF0;color:black;">240,255,240</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF69B4;color:white;">hot_pink</td>
            <td class="light-text" style="background-color:#FF69B4;color:white;">#FF69B4</td>
            <td class="light-text" style="background-color:#FF69B4;color:white;">255,105,180</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">indian_red</td>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">#CD5C5C</td>
            <td class="light-text" style="background-color:#CD5C5C;color:white;">205,92,92</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4B0082;color:white;">indigo</td>
            <td class="light-text" style="background-color:#4B0082;color:white;">#4B0082</td>
            <td class="light-text" style="background-color:#4B0082;color:white;">75,0,130</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">ivory</td>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">#FFFFF0</td>
            <td class="dark-text" style="background-color:#FFFFF0;color:black;">255,255,240</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">khaki</td>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">#F0E68C</td>
            <td class="dark-text" style="background-color:#F0E68C;color:black;">240,230,140</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">lavender</td>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">#E6E6FA</td>
            <td class="dark-text" style="background-color:#E6E6FA;color:black;">230,230,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">lavender_blush</td>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">#FFF0F5</td>
            <td class="dark-text" style="background-color:#FFF0F5;color:black;">255,240,245</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">lawn_green</td>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">#7CFC00</td>
            <td class="dark-text" style="background-color:#7CFC00;color:black;">124,252,0</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">lemon_chiffon</td>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">#FFFACD</td>
            <td class="dark-text" style="background-color:#FFFACD;color:black;">255,250,205</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">light_blue</td>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">#ADD8E6</td>
            <td class="dark-text" style="background-color:#ADD8E6;color:black;">173,216,230</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#F08080;color:white;">light_coral</td>
            <td class="light-text" style="background-color:#F08080;color:white;">#F08080</td>
            <td class="light-text" style="background-color:#F08080;color:white;">240,128,128</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">light_cyan</td>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">#E0FFFF</td>
            <td class="dark-text" style="background-color:#E0FFFF;color:black;">224,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">light_goldenrod</td>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">#EEDD82</td>
            <td class="dark-text" style="background-color:#EEDD82;color:black;">238,221,130</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">light_goldenrod_yellow</td>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">#FAFAD2</td>
            <td class="dark-text" style="background-color:#FAFAD2;color:black;">250,250,210</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">light_gray</td>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">#D3D3D3</td>
            <td class="dark-text" style="background-color:#D3D3D3;color:black;">211,211,211</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#90EE90;color:black;">light_green</td>
            <td class="dark-text" style="background-color:#90EE90;color:black;">#90EE90</td>
            <td class="dark-text" style="background-color:#90EE90;color:black;">144,238,144</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">light_magenta</td>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">#FFD2FF</td>
            <td class="dark-text" style="background-color:#FFD2FF;color:black;">255,210,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">light_pink</td>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">#FFB6C1</td>
            <td class="dark-text" style="background-color:#FFB6C1;color:black;">255,182,193</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">light_salmon</td>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">#FFA07A</td>
            <td class="dark-text" style="background-color:#FFA07A;color:black;">255,160,122</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#20B2AA;color:white;">light_sea_green</td>
            <td class="light-text" style="background-color:#20B2AA;color:white;">#20B2AA</td>
            <td class="light-text" style="background-color:#20B2AA;color:white;">32,178,170</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">light_sky_blue</td>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">#87CEFA</td>
            <td class="dark-text" style="background-color:#87CEFA;color:black;">135,206,250</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8470FF;color:white;">light_slate_blue</td>
            <td class="light-text" style="background-color:#8470FF;color:white;">#8470FF</td>
            <td class="light-text" style="background-color:#8470FF;color:white;">132,112,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#778899;color:white;">light_slate_gray</td>
            <td class="light-text" style="background-color:#778899;color:white;">#778899</td>
            <td class="light-text" style="background-color:#778899;color:white;">119,136,153</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">light_steel_blue</td>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">#B0C4DE</td>
            <td class="dark-text" style="background-color:#B0C4DE;color:black;">176,196,222</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">light_yellow</td>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">#FFFFE0</td>
            <td class="dark-text" style="background-color:#FFFFE0;color:black;">255,255,224</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FF00;color:black;">lime</td>
            <td class="dark-text" style="background-color:#00FF00;color:black;">#00FF00</td>
            <td class="dark-text" style="background-color:#00FF00;color:black;">0,255,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#32CD32;color:white;">lime_green</td>
            <td class="light-text" style="background-color:#32CD32;color:white;">#32CD32</td>
            <td class="light-text" style="background-color:#32CD32;color:white;">50,205,50</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">linen</td>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">#FAF0E6</td>
            <td class="dark-text" style="background-color:#FAF0E6;color:black;">250,240,230</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF00FF;color:white;">magenta</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">#FF00FF</td>
            <td class="light-text" style="background-color:#FF00FF;color:white;">255,0,255</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#800000;color:white;">maroon</td>
            <td class="light-text" style="background-color:#800000;color:white;">#800000</td>
            <td class="light-text" style="background-color:#800000;color:white;">128,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#66CDAA;color:white;">medium_aquamarine</td>
            <td class="light-text" style="background-color:#66CDAA;color:white;">#66CDAA</td>
            <td class="light-text" style="background-color:#66CDAA;color:white;">102,205,170</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#0000CD;color:white;">medium_blue</td>
            <td class="light-text" style="background-color:#0000CD;color:white;">#0000CD</td>
            <td class="light-text" style="background-color:#0000CD;color:white;">0,0,205</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BA55D3;color:white;">medium_orchid</td>
            <td class="light-text" style="background-color:#BA55D3;color:white;">#BA55D3</td>
            <td class="light-text" style="background-color:#BA55D3;color:white;">186,85,211</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9370DB;color:white;">medium_purple</td>
            <td class="light-text" style="background-color:#9370DB;color:white;">#9370DB</td>
            <td class="light-text" style="background-color:#9370DB;color:white;">147,112,219</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#3CB371;color:white;">medium_sea_green</td>
            <td class="light-text" style="background-color:#3CB371;color:white;">#3CB371</td>
            <td class="light-text" style="background-color:#3CB371;color:white;">60,179,113</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#7B68EE;color:white;">medium_slate_blue</td>
            <td class="light-text" style="background-color:#7B68EE;color:white;">#7B68EE</td>
            <td class="light-text" style="background-color:#7B68EE;color:white;">123,104,238</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">medium_spring_green</td>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">#00FA9A</td>
            <td class="dark-text" style="background-color:#00FA9A;color:black;">0,250,154</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#48D1CC;color:white;">medium_turquoise</td>
            <td class="light-text" style="background-color:#48D1CC;color:white;">#48D1CC</td>
            <td class="light-text" style="background-color:#48D1CC;color:white;">72,209,204</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#C71585;color:white;">medium_violet_red</td>
            <td class="light-text" style="background-color:#C71585;color:white;">#C71585</td>
            <td class="light-text" style="background-color:#C71585;color:white;">199,21,133</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#191970;color:white;">midnight_blue</td>
            <td class="light-text" style="background-color:#191970;color:white;">#191970</td>
            <td class="light-text" style="background-color:#191970;color:white;">25,25,112</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">mint_cream</td>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">#F5FFFA</td>
            <td class="dark-text" style="background-color:#F5FFFA;color:black;">245,255,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">misty_rose</td>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">#FFE4E1</td>
            <td class="dark-text" style="background-color:#FFE4E1;color:black;">255,228,225</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">moccasin</td>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">#FFE4B5</td>
            <td class="dark-text" style="background-color:#FFE4B5;color:black;">255,228,181</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">navajo_white</td>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">#FFDEAD</td>
            <td class="dark-text" style="background-color:#FFDEAD;color:black;">255,222,173</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#000080;color:white;">navy</td>
            <td class="light-text" style="background-color:#000080;color:white;">#000080</td>
            <td class="light-text" style="background-color:#000080;color:white;">0,0,128</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">old_lace</td>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">#FDF5E6</td>
            <td class="dark-text" style="background-color:#FDF5E6;color:black;">253,245,230</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#808000;color:white;">olive</td>
            <td class="light-text" style="background-color:#808000;color:white;">#808000</td>
            <td class="light-text" style="background-color:#808000;color:white;">128,128,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6B8E23;color:white;">olive_drab</td>
            <td class="light-text" style="background-color:#6B8E23;color:white;">#6B8E23</td>
            <td class="light-text" style="background-color:#6B8E23;color:white;">107,142,35</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFA500;color:black;">orange</td>
            <td class="dark-text" style="background-color:#FFA500;color:black;">#FFA500</td>
            <td class="dark-text" style="background-color:#FFA500;color:black;">255,165,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF4500;color:white;">orange_red</td>
            <td class="light-text" style="background-color:#FF4500;color:white;">#FF4500</td>
            <td class="light-text" style="background-color:#FF4500;color:white;">255,69,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DA70D6;color:white;">orchid</td>
            <td class="light-text" style="background-color:#DA70D6;color:white;">#DA70D6</td>
            <td class="light-text" style="background-color:#DA70D6;color:white;">218,112,214</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#118ED8;color:white;">pacific_blue</td>
            <td class="light-text" style="background-color:#118ED8;color:white;">#118ED8</td>
            <td class="light-text" style="background-color:#118ED8;color:white;">17,142,216</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">pale_goldenrod</td>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">#EEE8AA</td>
            <td class="dark-text" style="background-color:#EEE8AA;color:black;">238,232,170</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#98FB98;color:black;">pale_green</td>
            <td class="dark-text" style="background-color:#98FB98;color:black;">#98FB98</td>
            <td class="dark-text" style="background-color:#98FB98;color:black;">152,251,152</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">pale_turquoise</td>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">#AFEEEE</td>
            <td class="dark-text" style="background-color:#AFEEEE;color:black;">175,238,238</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#DB7093;color:white;">pale_violet_red</td>
            <td class="light-text" style="background-color:#DB7093;color:white;">#DB7093</td>
            <td class="light-text" style="background-color:#DB7093;color:white;">219,112,147</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">papaya_whip</td>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">#FFEFD5</td>
            <td class="dark-text" style="background-color:#FFEFD5;color:black;">255,239,213</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">peach_puff</td>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">#FFDAB9</td>
            <td class="dark-text" style="background-color:#FFDAB9;color:black;">255,218,185</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#CD853F;color:white;">peru</td>
            <td class="light-text" style="background-color:#CD853F;color:white;">#CD853F</td>
            <td class="light-text" style="background-color:#CD853F;color:white;">205,133,63</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">pink</td>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">#FFC0CB</td>
            <td class="dark-text" style="background-color:#FFC0CB;color:black;">255,192,203</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">plum</td>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">#DDA0DD</td>
            <td class="dark-text" style="background-color:#DDA0DD;color:black;">221,160,221</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">powderblue</td>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">#B0E0E6</td>
            <td class="dark-text" style="background-color:#B0E0E6;color:black;">176,224,230</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#800080;color:white;">purple</td>
            <td class="light-text" style="background-color:#800080;color:white;">#800080</td>
            <td class="light-text" style="background-color:#800080;color:white;">128,0,128</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#663399;color:white;">rebeccapurple</td>
            <td class="light-text" style="background-color:#663399;color:white;">#663399</td>
            <td class="light-text" style="background-color:#663399;color:white;">102,51,153</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF0000;color:white;">red</td>
            <td class="light-text" style="background-color:#FF0000;color:white;">#FF0000</td>
            <td class="light-text" style="background-color:#FF0000;color:white;">255,0,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">rosy_brown</td>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">#BC8F8F</td>
            <td class="light-text" style="background-color:#BC8F8F;color:white;">188,143,143</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4169E1;color:white;">royal_blue</td>
            <td class="light-text" style="background-color:#4169E1;color:white;">#4169E1</td>
            <td class="light-text" style="background-color:#4169E1;color:white;">65,105,225</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#8B4513;color:white;">saddle_brown</td>
            <td class="light-text" style="background-color:#8B4513;color:white;">#8B4513</td>
            <td class="light-text" style="background-color:#8B4513;color:white;">139,69,19</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FA8072;color:white;">salmon</td>
            <td class="light-text" style="background-color:#FA8072;color:white;">#FA8072</td>
            <td class="light-text" style="background-color:#FA8072;color:white;">250,128,114</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F4A460;color:black;">sandy_brown</td>
            <td class="dark-text" style="background-color:#F4A460;color:black;">#F4A460</td>
            <td class="dark-text" style="background-color:#F4A460;color:black;">244,164,96</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#2E8B57;color:white;">sea_green</td>
            <td class="light-text" style="background-color:#2E8B57;color:white;">#2E8B57</td>
            <td class="light-text" style="background-color:#2E8B57;color:white;">46,139,87</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">sea_shell</td>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">#FFF5EE</td>
            <td class="dark-text" style="background-color:#FFF5EE;color:black;">255,245,238</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#A0522D;color:white;">sienna</td>
            <td class="light-text" style="background-color:#A0522D;color:white;">#A0522D</td>
            <td class="light-text" style="background-color:#A0522D;color:white;">160,82,45</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">silver</td>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">#C0C0C0</td>
            <td class="dark-text" style="background-color:#C0C0C0;color:black;">192,192,192</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">sky_blue</td>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">#87CEEB</td>
            <td class="dark-text" style="background-color:#87CEEB;color:black;">135,206,235</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">slate_blue</td>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">#6A5ACD</td>
            <td class="light-text" style="background-color:#6A5ACD;color:white;">106,90,205</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#708090;color:white;">slate_gray</td>
            <td class="light-text" style="background-color:#708090;color:white;">#708090</td>
            <td class="light-text" style="background-color:#708090;color:white;">112,128,144</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">snow</td>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">#FFFAFA</td>
            <td class="dark-text" style="background-color:#FFFAFA;color:black;">255,250,250</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">spring_green</td>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">#00FF7F</td>
            <td class="dark-text" style="background-color:#00FF7F;color:black;">0,255,127</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#4682B4;color:white;">steel_blue</td>
            <td class="light-text" style="background-color:#4682B4;color:white;">#4682B4</td>
            <td class="light-text" style="background-color:#4682B4;color:white;">70,130,180</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D2B48C;color:white;">tan</td>
            <td class="light-text" style="background-color:#D2B48C;color:white;">#D2B48C</td>
            <td class="light-text" style="background-color:#D2B48C;color:white;">210,180,140</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#008080;color:white;">teal</td>
            <td class="light-text" style="background-color:#008080;color:white;">#008080</td>
            <td class="light-text" style="background-color:#008080;color:white;">0,128,128</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">thistle</td>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">#D8BFD8</td>
            <td class="dark-text" style="background-color:#D8BFD8;color:black;">216,191,216</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#FF6347;color:white;">tomato</td>
            <td class="light-text" style="background-color:#FF6347;color:white;">#FF6347</td>
            <td class="light-text" style="background-color:#FF6347;color:white;">255,99,71</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">turquoise</td>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">#40E0D0</td>
            <td class="dark-text" style="background-color:#40E0D0;color:black;">64,224,208</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#EE82EE;color:white;">violet</td>
            <td class="light-text" style="background-color:#EE82EE;color:white;">#EE82EE</td>
            <td class="light-text" style="background-color:#EE82EE;color:white;">238,130,238</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#D02090;color:white;">violet_red</td>
            <td class="light-text" style="background-color:#D02090;color:white;">#D02090</td>
            <td class="light-text" style="background-color:#D02090;color:white;">208,32,144</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">wheat</td>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">#F5DEB3</td>
            <td class="dark-text" style="background-color:#F5DEB3;color:black;">245,222,179</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">white</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">#FFFFFF</td>
            <td class="dark-text" style="background-color:#FFFFFF;color:black;">255,255,255</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">white_smoke</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">#F5F5F5</td>
            <td class="dark-text" style="background-color:#F5F5F5;color:black;">245,245,245</td>
            </tr>
            <tr>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">yellow</td>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">#FFFF00</td>
            <td class="dark-text" style="background-color:#FFFF00;color:black;">255,255,0</td>
            </tr>
            <tr>
            <td class="light-text" style="background-color:#9ACD32;color:white;">yellow_green</td>
            <td class="light-text" style="background-color:#9ACD32;color:white;">#9ACD32</td>
            <td class="light-text" style="background-color:#9ACD32;color:white;">154,205,50</td>
            </tr>
            </table>

- A system color name, one of:

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