:og:description: A detailed description of the possible values for some aesthetics.

:orphan:

.. title:: Aesthetic Specifications in Lets-Plot

.. meta::
   :description: A detailed description of the possible values for some aesthetics.
   :keywords: ggplot aesthetics, point shape, line type, linetype


Aesthetics
==========


Color and Fill
--------------

Colors and fills of geometries can be specified in the following ways:

- RGB/RGBA (e.g. ``"rgb(0, 0, 255)"``, ``"rgba(0, 0, 255, 0.5)"``).

- HEX (e.g. ``"#0000ff"``, ``"#00f"``).

- Blank string (``""``) or aliases: ``"blank"``, ``"transparent"`` for a fully transparent color.

- A name, one of:

  .. list-table:: Colors
     :header-rows: 1
     :widths: 50 20 40 50

     * - Name
       - Hex
       - RGB
       - Preview
     * - ``alice_blue``
       - ``#F0F8FF``
       - ``240, 248, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F0F8FF;border:1px solid #000;"></div>

     * - ``antique_white``
       - ``#FAEBD7``
       - ``250, 235, 215``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FAEBD7;border:1px solid #000;"></div>

     * - ``aqua``
       - ``#00FFFF``
       - ``0, 255, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00FFFF;border:1px solid #000;"></div>

     * - ``aquamarine``
       - ``#7FFFD4``
       - ``127, 255, 212``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#7FFFD4;border:1px solid #000;"></div>

     * - ``azure``
       - ``#F0FFFF``
       - ``240, 255, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F0FFFF;border:1px solid #000;"></div>

     * - ``beige``
       - ``#F5F5DC``
       - ``245, 245, 220``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F5F5DC;border:1px solid #000;"></div>

     * - ``bisque``
       - ``#FFE4C4``
       - ``255, 228, 196``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFE4C4;border:1px solid #000;"></div>

     * - ``black``
       - ``#000000``
       - ``0, 0, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#000000;border:1px solid #000;"></div>

     * - ``blanched_almond``
       - ``#FFEBCD``
       - ``255, 235, 205``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFEBCD;border:1px solid #000;"></div>

     * - ``blue``
       - ``#0000FF``
       - ``0, 0, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#0000FF;border:1px solid #000;"></div>

     * - ``blue_violet``
       - ``#8A2BE2``
       - ``138, 43, 226``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8A2BE2;border:1px solid #000;"></div>

     * - ``brown``
       - ``#A52A2A``
       - ``165, 42, 42``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#A52A2A;border:1px solid #000;"></div>

     * - ``burly_wood``
       - ``#DEB887``
       - ``222, 184, 135``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DEB887;border:1px solid #000;"></div>

     * - ``cadet_blue``
       - ``#5F9EA0``
       - ``95, 158, 160``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#5F9EA0;border:1px solid #000;"></div>

     * - ``chartreuse``
       - ``#7FFF00``
       - ``127, 255, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#7FFF00;border:1px solid #000;"></div>

     * - ``chocolate``
       - ``#D2691E``
       - ``210, 105, 30``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#D2691E;border:1px solid #000;"></div>

     * - ``coral``
       - ``#FF7F50``
       - ``255, 127, 80``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF7F50;border:1px solid #000;"></div>

     * - ``cornflower_blue``
       - ``#6495ED``
       - ``100, 149, 237``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#6495ED;border:1px solid #000;"></div>

     * - ``cornsilk``
       - ``#FFF8DC``
       - ``255, 248, 220``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFF8DC;border:1px solid #000;"></div>

     * - ``crimson``
       - ``#DC143C``
       - ``220, 20, 60``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DC143C;border:1px solid #000;"></div>

     * - ``cyan``
       - ``#00FFFF``
       - ``0, 255, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00FFFF;border:1px solid #000;"></div>

     * - ``dark_blue``
       - ``#00008B``
       - ``0, 0, 139``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00008B;border:1px solid #000;"></div>

     * - ``dark_cyan``
       - ``#008B8B``
       - ``0, 139, 139``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#008B8B;border:1px solid #000;"></div>

     * - ``dark_goldenrod``
       - ``#B8860B``
       - ``184, 134, 11``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#B8860B;border:1px solid #000;"></div>

     * - ``dark_gray``
       - ``#555555``
       - ``85, 85, 85``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#555555;border:1px solid #000;"></div>

     * - ``dark_green``
       - ``#006400``
       - ``0, 100, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#006400;border:1px solid #000;"></div>

     * - ``dark_khaki``
       - ``#BDB76B``
       - ``189, 183, 107``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#BDB76B;border:1px solid #000;"></div>

     * - ``dark_magenta``
       - ``#8B008B``
       - ``139, 0, 139``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8B008B;border:1px solid #000;"></div>

     * - ``dark_olive_green``
       - ``#556B2F``
       - ``85, 107, 47``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#556B2F;border:1px solid #000;"></div>

     * - ``dark_orange``
       - ``#FF8C00``
       - ``255, 140, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF8C00;border:1px solid #000;"></div>

     * - ``dark_orchid``
       - ``#9932CC``
       - ``153, 50, 204``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#9932CC;border:1px solid #000;"></div>

     * - ``dark_red``
       - ``#8B0000``
       - ``139, 0, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8B0000;border:1px solid #000;"></div>

     * - ``dark_salmon``
       - ``#E9967A``
       - ``233, 150, 122``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#E9967A;border:1px solid #000;"></div>

     * - ``dark_sea_green``
       - ``#8FBC8F``
       - ``143, 188, 143``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8FBC8F;border:1px solid #000;"></div>

     * - ``dark_slate_blue``
       - ``#483D8B``
       - ``72, 61, 139``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#483D8B;border:1px solid #000;"></div>

     * - ``dark_slate_gray``
       - ``#2F4F4F``
       - ``47, 79, 79``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#2F4F4F;border:1px solid #000;"></div>

     * - ``dark_turquoise``
       - ``#00CED1``
       - ``0, 206, 209``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00CED1;border:1px solid #000;"></div>

     * - ``dark_violet``
       - ``#9400D3``
       - ``148, 0, 211``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#9400D3;border:1px solid #000;"></div>

     * - ``deep_pink``
       - ``#FF1493``
       - ``255, 20, 147``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF1493;border:1px solid #000;"></div>

     * - ``deep_sky_blue``
       - ``#00BFFF``
       - ``0, 191, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00BFFF;border:1px solid #000;"></div>

     * - ``dim_gray``
       - ``#696969``
       - ``105, 105, 105``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#696969;border:1px solid #000;"></div>

     * - ``dodger_blue``
       - ``#1E90FF``
       - ``30, 144, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#1E90FF;border:1px solid #000;"></div>

     * - ``firebrick``
       - ``#B22222``
       - ``178, 34, 34``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#B22222;border:1px solid #000;"></div>

     * - ``floral_white``
       - ``#FFFAF0``
       - ``255, 250, 240``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFAF0;border:1px solid #000;"></div>

     * - ``forest_green``
       - ``#228B22``
       - ``34, 139, 34``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#228B22;border:1px solid #000;"></div>

     * - ``fuchsia``
       - ``#FF00FF``
       - ``255, 0, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF00FF;border:1px solid #000;"></div>

     * - ``gainsboro``
       - ``#DCDCDC``
       - ``220, 220, 220``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DCDCDC;border:1px solid #000;"></div>

     * - ``ghost_white``
       - ``#F8F8FF``
       - ``248, 248, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F8F8FF;border:1px solid #000;"></div>

     * - ``gold``
       - ``#FFD700``
       - ``255, 215, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFD700;border:1px solid #000;"></div>

     * - ``goldenrod``
       - ``#DAA520``
       - ``218, 165, 32``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DAA520;border:1px solid #000;"></div>

     * - ``gray``
       - ``#808080``
       - ``128, 128, 128``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#808080;border:1px solid #000;"></div>

     * - ``green``
       - ``#008000``
       - ``0, 128, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#008000;border:1px solid #000;"></div>

     * - ``green_yellow``
       - ``#ADFF2F``
       - ``173, 255, 47``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#ADFF2F;border:1px solid #000;"></div>

     * - ``honey_dew``
       - ``#F0FFF0``
       - ``240, 255, 240``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F0FFF0;border:1px solid #000;"></div>

     * - ``hot_pink``
       - ``#FF69B4``
       - ``255, 105, 180``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF69B4;border:1px solid #000;"></div>

     * - ``indian_red``
       - ``#CD5C5C``
       - ``205, 92, 92``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#CD5C5C;border:1px solid #000;"></div>

     * - ``indigo``
       - ``#4B0082``
       - ``75, 0, 130``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#4B0082;border:1px solid #000;"></div>

     * - ``ivory``
       - ``#FFFFF0``
       - ``255, 255, 240``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFFF0;border:1px solid #000;"></div>

     * - ``khaki``
       - ``#F0E68C``
       - ``240, 230, 140``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F0E68C;border:1px solid #000;"></div>

     * - ``lavender``
       - ``#E6E6FA``
       - ``230, 230, 250``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#E6E6FA;border:1px solid #000;"></div>

     * - ``lavender_blush``
       - ``#FFF0F5``
       - ``255, 240, 245``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFF0F5;border:1px solid #000;"></div>

     * - ``lawn_green``
       - ``#7CFC00``
       - ``124, 252, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#7CFC00;border:1px solid #000;"></div>

     * - ``lemon_chiffon``
       - ``#FFFACD``
       - ``255, 250, 205``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFACD;border:1px solid #000;"></div>

     * - ``light_blue``
       - ``#ADD8E6``
       - ``173, 216, 230``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#ADD8E6;border:1px solid #000;"></div>

     * - ``light_coral``
       - ``#F08080``
       - ``240, 128, 128``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F08080;border:1px solid #000;"></div>

     * - ``light_cyan``
       - ``#E0FFFF``
       - ``224, 255, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#E0FFFF;border:1px solid #000;"></div>

     * - ``light_goldenrod``
       - ``#EEDD82``
       - ``238, 221, 130``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#EEDD82;border:1px solid #000;"></div>

     * - ``light_goldenrod_yellow``
       - ``#FAFAD2``
       - ``250, 250, 210``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FAFAD2;border:1px solid #000;"></div>

     * - ``light_gray``
       - ``#D3D3D3``
       - ``211, 211, 211``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#D3D3D3;border:1px solid #000;"></div>

     * - ``light_green``
       - ``#90EE90``
       - ``144, 238, 144``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#90EE90;border:1px solid #000;"></div>

     * - ``light_magenta``
       - ``#FFD2FF``
       - ``255, 210, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFD2FF;border:1px solid #000;"></div>

     * - ``light_pink``
       - ``#FFB6C1``
       - ``255, 182, 193``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFB6C1;border:1px solid #000;"></div>

     * - ``light_salmon``
       - ``#FFA07A``
       - ``255, 160, 122``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFA07A;border:1px solid #000;"></div>

     * - ``light_sea_green``
       - ``#20B2AA``
       - ``32, 178, 170``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#20B2AA;border:1px solid #000;"></div>

     * - ``light_sky_blue``
       - ``#87CEFA``
       - ``135, 206, 250``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#87CEFA;border:1px solid #000;"></div>

     * - ``light_slate_blue``
       - ``#8470FF``
       - ``132, 112, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8470FF;border:1px solid #000;"></div>

     * - ``light_slate_gray``
       - ``#778899``
       - ``119, 136, 153``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#778899;border:1px solid #000;"></div>

     * - ``light_steel_blue``
       - ``#B0C4DE``
       - ``176, 196, 222``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#B0C4DE;border:1px solid #000;"></div>

     * - ``light_yellow``
       - ``#FFFFE0``
       - ``255, 255, 224``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFFE0;border:1px solid #000;"></div>

     * - ``lime``
       - ``#00FF00``
       - ``0, 255, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00FF00;border:1px solid #000;"></div>

     * - ``lime_green``
       - ``#32CD32``
       - ``50, 205, 50``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#32CD32;border:1px solid #000;"></div>

     * - ``linen``
       - ``#FAF0E6``
       - ``250, 240, 230``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FAF0E6;border:1px solid #000;"></div>

     * - ``magenta``
       - ``#FF00FF``
       - ``255, 0, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF00FF;border:1px solid #000;"></div>

     * - ``maroon``
       - ``#800000``
       - ``128, 0, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#800000;border:1px solid #000;"></div>

     * - ``medium_aquamarine``
       - ``#66CDAA``
       - ``102, 205, 170``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#66CDAA;border:1px solid #000;"></div>

     * - ``medium_blue``
       - ``#0000CD``
       - ``0, 0, 205``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#0000CD;border:1px solid #000;"></div>

     * - ``medium_orchid``
       - ``#BA55D3``
       - ``186, 85, 211``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#BA55D3;border:1px solid #000;"></div>

     * - ``medium_purple``
       - ``#9370DB``
       - ``147, 112, 219``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#9370DB;border:1px solid #000;"></div>

     * - ``medium_sea_green``
       - ``#3CB371``
       - ``60, 179, 113``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#3CB371;border:1px solid #000;"></div>

     * - ``medium_slate_blue``
       - ``#7B68EE``
       - ``123, 104, 238``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#7B68EE;border:1px solid #000;"></div>

     * - ``medium_spring_green``
       - ``#00FA9A``
       - ``0, 250, 154``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00FA9A;border:1px solid #000;"></div>

     * - ``medium_turquoise``
       - ``#48D1CC``
       - ``72, 209, 204``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#48D1CC;border:1px solid #000;"></div>

     * - ``medium_violet_red``
       - ``#C71585``
       - ``199, 21, 133``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#C71585;border:1px solid #000;"></div>

     * - ``midnight_blue``
       - ``#191970``
       - ``25, 25, 112``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#191970;border:1px solid #000;"></div>

     * - ``mint_cream``
       - ``#F5FFFA``
       - ``245, 255, 250``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F5FFFA;border:1px solid #000;"></div>

     * - ``misty_rose``
       - ``#FFE4E1``
       - ``255, 228, 225``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFE4E1;border:1px solid #000;"></div>

     * - ``moccasin``
       - ``#FFE4B5``
       - ``255, 228, 181``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFE4B5;border:1px solid #000;"></div>

     * - ``navajo_white``
       - ``#FFDEAD``
       - ``255, 222, 173``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFDEAD;border:1px solid #000;"></div>

     * - ``navy``
       - ``#000080``
       - ``0, 0, 128``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#000080;border:1px solid #000;"></div>

     * - ``old_lace``
       - ``#FDF5E6``
       - ``253, 245, 230``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FDF5E6;border:1px solid #000;"></div>

     * - ``olive``
       - ``#808000``
       - ``128, 128, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#808000;border:1px solid #000;"></div>

     * - ``olive_drab``
       - ``#6B8E23``
       - ``107, 142, 35``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#6B8E23;border:1px solid #000;"></div>

     * - ``orange``
       - ``#FFA500``
       - ``255, 165, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFA500;border:1px solid #000;"></div>

     * - ``orange_red``
       - ``#FF4500``
       - ``255, 69, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF4500;border:1px solid #000;"></div>

     * - ``orchid``
       - ``#DA70D6``
       - ``218, 112, 214``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DA70D6;border:1px solid #000;"></div>

     * - ``pacific_blue``
       - ``#118ED8``
       - ``17, 142, 216``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#118ED8;border:1px solid #000;"></div>

     * - ``pale_goldenrod``
       - ``#EEE8AA``
       - ``238, 232, 170``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#EEE8AA;border:1px solid #000;"></div>

     * - ``pale_green``
       - ``#98FB98``
       - ``152, 251, 152``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#98FB98;border:1px solid #000;"></div>

     * - ``pale_turquoise``
       - ``#AFEEEE``
       - ``175, 238, 238``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#AFEEEE;border:1px solid #000;"></div>

     * - ``pale_violet_red``
       - ``#DB7093``
       - ``219, 112, 147``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DB7093;border:1px solid #000;"></div>

     * - ``papaya_whip``
       - ``#FFEFD5``
       - ``255, 239, 213``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFEFD5;border:1px solid #000;"></div>

     * - ``peach_puff``
       - ``#FFDAB9``
       - ``255, 218, 185``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFDAB9;border:1px solid #000;"></div>

     * - ``peru``
       - ``#CD853F``
       - ``205, 133, 63``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#CD853F;border:1px solid #000;"></div>

     * - ``pink``
       - ``#FFC0CB``
       - ``255, 192, 203``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFC0CB;border:1px solid #000;"></div>

     * - ``plum``
       - ``#DDA0DD``
       - ``221, 160, 221``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#DDA0DD;border:1px solid #000;"></div>

     * - ``powderblue``
       - ``#B0E0E6``
       - ``176, 224, 230``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#B0E0E6;border:1px solid #000;"></div>

     * - ``purple``
       - ``#800080``
       - ``128, 0, 128``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#800080;border:1px solid #000;"></div>

     * - ``rebeccapurple``
       - ``#663399``
       - ``102, 51, 153``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#663399;border:1px solid #000;"></div>

     * - ``red``
       - ``#FF0000``
       - ``255, 0, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF0000;border:1px solid #000;"></div>

     * - ``rosy_brown``
       - ``#BC8F8F``
       - ``188, 143, 143``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#BC8F8F;border:1px solid #000;"></div>

     * - ``royal_blue``
       - ``#4169E1``
       - ``65, 105, 225``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#4169E1;border:1px solid #000;"></div>

     * - ``saddle_brown``
       - ``#8B4513``
       - ``139, 69, 19``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#8B4513;border:1px solid #000;"></div>

     * - ``salmon``
       - ``#FA8072``
       - ``250, 128, 114``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FA8072;border:1px solid #000;"></div>

     * - ``sandy_brown``
       - ``#F4A460``
       - ``244, 164, 96``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F4A460;border:1px solid #000;"></div>

     * - ``sea_green``
       - ``#2E8B57``
       - ``46, 139, 87``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#2E8B57;border:1px solid #000;"></div>

     * - ``sea_shell``
       - ``#FFF5EE``
       - ``255, 245, 238``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFF5EE;border:1px solid #000;"></div>

     * - ``sienna``
       - ``#A0522D``
       - ``160, 82, 45``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#A0522D;border:1px solid #000;"></div>

     * - ``silver``
       - ``#C0C0C0``
       - ``192, 192, 192``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#C0C0C0;border:1px solid #000;"></div>

     * - ``sky_blue``
       - ``#87CEEB``
       - ``135, 206, 235``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#87CEEB;border:1px solid #000;"></div>

     * - ``slate_blue``
       - ``#6A5ACD``
       - ``106, 90, 205``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#6A5ACD;border:1px solid #000;"></div>

     * - ``slate_gray``
       - ``#708090``
       - ``112, 128, 144``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#708090;border:1px solid #000;"></div>

     * - ``snow``
       - ``#FFFAFA``
       - ``255, 250, 250``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFAFA;border:1px solid #000;"></div>

     * - ``spring_green``
       - ``#00FF7F``
       - ``0, 255, 127``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#00FF7F;border:1px solid #000;"></div>

     * - ``steel_blue``
       - ``#4682B4``
       - ``70, 130, 180``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#4682B4;border:1px solid #000;"></div>

     * - ``tan``
       - ``#D2B48C``
       - ``210, 180, 140``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#D2B48C;border:1px solid #000;"></div>

     * - ``teal``
       - ``#008080``
       - ``0, 128, 128``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#008080;border:1px solid #000;"></div>

     * - ``thistle``
       - ``#D8BFD8``
       - ``216, 191, 216``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#D8BFD8;border:1px solid #000;"></div>

     * - ``tomato``
       - ``#FF6347``
       - ``255, 99, 71``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FF6347;border:1px solid #000;"></div>

     * - ``turquoise``
       - ``#40E0D0``
       - ``64, 224, 208``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#40E0D0;border:1px solid #000;"></div>

     * - ``violet``
       - ``#EE82EE``
       - ``238, 130, 238``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#EE82EE;border:1px solid #000;"></div>

     * - ``violet_red``
       - ``#D02090``
       - ``208, 32, 144``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#D02090;border:1px solid #000;"></div>

     * - ``wheat``
       - ``#F5DEB3``
       - ``245, 222, 179``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F5DEB3;border:1px solid #000;"></div>

     * - ``white``
       - ``#FFFFFF``
       - ``255, 255, 255``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFFFF;border:1px solid #000;"></div>

     * - ``white_smoke``
       - ``#F5F5F5``
       - ``245, 245, 245``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#F5F5F5;border:1px solid #000;"></div>

     * - ``yellow``
       - ``#FFFF00``
       - ``255, 255, 0``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#FFFF00;border:1px solid #000;"></div>

     * - ``yellow_green``
       - ``#9ACD32``
       - ``154, 205, 50``
       - .. raw:: html

            <div style="width:80px;height:30px;background-color:#9ACD32;border:1px solid #000;"></div>

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