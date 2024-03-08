.. _basemap_tiles:

:og:description: Lets-Plot provides a variety of constants and functions to configure the basemap tiles.

:orphan:

.. title:: Configuring Basemap Tiles for Interactive Maps in Lets-Plot

.. meta::
   :description: Lets-Plot provides a variety of constants and functions to configure the basemap tiles.
   :keywords: basemap tiles, vector tiles, raster tiles, OpenStreetMap, OSM, OpenTopoMap, CARTO, NASA


Configuring Basemap Tiles for Interactive Maps
==============================================


.. _basemap_tiles_global_cfg:

Configuring Globally
--------------------

You can configure global Lets-Plot options using the :py:mod:`LestPlot.set(dictionary) <lets_plot.LetsPlot>` method.

Where the ``dictionary`` can contain all sorts of Lets-Plot options, including basemap tiles configuration options.

Lets-Plot provides a variety of constants and functions which make configuring of basemap tiles simple:

.. code-block:: python

    from lets_plot import tilesets

    LetsPlot.set(tilesets.LETS_PLOT_DARK)


.. _basemap_tiles_plot_cfg:

Configuring for a Single Plot
-----------------------------

Use ``tiles`` parameter in the :py:mod:`geom_livemap() <lets_plot.geom_livemap>` function:

.. code-block:: python

    from lets_plot import tilesets

    ggplot() + geom_livemap(tiles=tilesets.LETS_PLOT_DARK)


.. _basemap_tiles_vector_tiles:

Vector Tiles
------------

.. note::
  Vector tiles may not work with Safari.
  If the tiles don't load please try disabling the NSURLSession Websocket feature
  (`Develop -> Experimental Features -> NSURLSession Websocket`) or use :ref:`raster tiles <basemap_tiles_raster_tiles>`.

Lets-Plot provides its own vector basemap tiles available in four variants:

- color
- dark
- light
- bw

By default Lets-Plot uses its "color" tiles.

Configure Lets-Plot vector tiles (globally or on the per-plot basis) with the help of the :py:mod:`LetsPlot.maptiles_lets_plot(...) <lets_plot.maptiles_lets_plot>` function:

.. code-block:: python

    ggplot() + geom_livemap(tiles=maptiles_lets_plot(theme='dark'))

or with the help of a constant defined in the ``tilesets`` module:

.. code-block:: python

    from lets_plot import tilesets

    ggplot() + geom_livemap(tiles=tilesets.LETS_PLOT_DARK)


.. _basemap_tiles_blank_tiles:

Blank Tiles
-----------

:py:mod:`Blank tiles <lets_plot.maptiles_solid>` show no other graphics but a solid background color which you can choose (a HEX value is expected):

.. code-block:: python

    ggplot() + geom_livemap(tiles=maptiles_solid(color='#C1C1C1'))

You can also use a constant defined in the ``tilesets`` module (white tiles):

.. code-block:: python

    from lets_plot import tilesets

    ggplot() + geom_livemap(tiles=tilesets.SOLID)

Blank tiles do not require an internet connection.


.. _basemap_tiles_raster_tiles:

Raster Tiles
------------

With Lets-Plot you can use ZXY raster tiles provided by 3rd party maptile services.

.. warning::
  Always read the providers **Terms of Service** before using this provider's tiles in your project.

Some services provide free of charge raster tilesets. The ``tilesets`` module in Lets-Plot contains many such tilesets pre-configured.

Again, you can use these tilesets to configure Lets-Plot globally or on the per-plot basis:

.. code-block:: python

    from lets_plot import tilesets

    ggplot() + geom_livemap(tiles=tilesets.OSM)


.. _basemap_tiles_osm_tiles:

OpenStreetMap
~~~~~~~~~~~~~

`© OpenStreetMap contributors <https://www.openstreetmap.org/copyright>`__

- ``OSM``: OpenStreetMap's Standard tile layer.


.. _basemap_tiles_topo_tiles:

OpenTopoMap
~~~~~~~~~~~

Map data: `© OpenStreetMap contributors <https://www.openstreetmap.org/copyright>`__, `SRTM <http://viewfinderpanoramas.org>`__ | map style: `© OpenTopoMap <https://opentopomap.org>`__ (`CC-BY-SA <https://creativecommons.org/licenses/by-sa/3.0>`__).

- ``OPEN_TOPO_MAP``


.. _basemap_tiles_carto_tiles:

CARTO
~~~~~

`© OpenStreetMap contributors <https://www.openstreetmap.org/copyright>`__, `© CARTO <https://carto.com/attributions#basemaps>`__, `© CARTO <https://carto.com/attributions>`__.

Free for none-commercial services only (see `Limitations <https://github.com/CartoDB/basemap-styles#1-web-raster-basemaps>`__, `License <https://github.com/CartoDB/basemap-styles/blob/master/LICENSE.md>`__).

- ``CARTO_POSITRON``, ``CARTO_POSITRON_HIRES`` : Positron
- ``CARTO_POSITRON_NO_LABELS``, ``CARTO_POSITRON_NO_LABELS_HIRES`` : Positron (no labels)
- ``CARTO_DARK_MATTER_NO_LABELS``, ``CARTO_DARK_MATTER_NO_LABELS_HIRES`` : Dark Matter (no labels)
- ``CARTO_VOYAGER``, ``CARTO_VOYAGER_HIRES`` : Voyager
- ``CARTO_FLAT_BLUE``, ``CARTO_FLAT_BLUE_HIRES`` : Flat Blue
- ``CARTO_MIDNIGHT_COMMANDER``, ``CARTO_MIDNIGHT_COMMANDER_HIRES`` : Midnight commander
- ``CARTO_ANTIQUE``, ``CARTO_ANTIQUE_HIRES`` : Antique


.. _basemap_tiles_nasa_tiles:

NASA's Global Imagery Browse Services (GIBS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Imagery provided by services from NASA's Global Imagery Browse Services (`GIBS <https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs>`__), part of NASA's Earth Observing System Data and Information System (`EOSDIS <https://earthdata.nasa.gov>`__).

`NASA's Global Imagery Browse Services (GIBS) <https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs>`__.

Global Imagery Browse Services (GIBS) - `API for Developers <https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers>`__.

Global Imagery Browse Services (GIBS) API - `Generic XYZ Tile Access <https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+API+for+Developers#GIBSAPIforDevelopers-GenericXYZTileAccess>`__.

`GIBS Available Imagery Products <https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+Products>`__.

- ``NASA_CITYLIGHTS_2012`` : CityLights 2012
- ``NASA_GREYSCALE_SHADED_RELIEF_30M`` : Greyscale Shaded Relief (30m)
- ``NASA_COLOR_SHADED_RELIEF_30M`` : Color Shaded Relief (30m)
- ``NASA_TERRA_TRUECOLOR`` : Terra TrueColor


.. _basemap_tiles_examples:

Examples
--------

.. image:: /_static/images/basemaps.jpg

Check out `this notebook <https://datalore.jetbrains.com/view/notebook/05NSsbcsOYZMBN9n4JfKzL>`__ to see examples of various tilesets.


.. _basemap_tiles_raster_tiles_man:

Configuring Raster Tiles Manually
---------------------------------

In addition to pre-configured tilesets you can configure and use almost any other raster tilesets provided in ``ZXY`` format.

You can do it with the help of the :py:mod:`LetsPlot.maptiles_zxy() <lets_plot.maptiles_zxy>` function.

The following code will configure 'NASA, CityLights 2012' tiles:

.. code-block:: python

    settings = dict(
        url = "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/VIIRS_CityLights_2012/default/GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg",
        attribution = '<a href="https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs">© NASA Global Imagery Browse Services (GIBS)</a>',
        max_zoom=8
    )

    ggplot() + geom_livemap(tiles=maptiles_zxy(**settings))

**Raster tiles configuration options**:

- ``url`` : ZXY tiles URL , e.g. ``"https://{s}.tile.com/{z}/{x}/{y}.png"``.
  Where ``{z}``, ``{x}``, ``{y}`` and ``{s}`` are placeholders for zoom, coordinates and subdomain. 
- ``attribution`` : An attribution or a copyright notice. 
- ``min_zoom`` : Minimal zoom limit.
- ``max_zoom`` : Maximal zoom limit.
- ``subdomains`` : A list of characters where each character is interpreted as a subdomain in the times URL.   

You can also provide other key-value pairs to include into the tile URL as parameters:

.. code-block:: python

    maptiles_zxy(url='http://maps.example.com/{z}/{x}/{y}.png?access_key={key}', key='MY_ACCESS_KEY')