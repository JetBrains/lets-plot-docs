.. _features_geocoding_api:

Geocoding API
#############

Geocoding is the process of converting names of places into geographic coordinates.

*Lets-Plot* now offers geocoding API covering the following administrative levels:

- country
- state
- county
- city

*Lets-Plot* geocoding API allows a user to execute a single and batch geocoding queries, and handle possible names ambiguity.

Relatively simple geocoding queries are executed using the ``regions_xxx()`` functions family. For example:

.. code-block:: python

    from lets_plot.geo_data import *
    regions_country(['usa', 'canada'])

returns the ``Regions`` object containing internal IDs for Canada and the US:

.. csv-table::
    :header: "", "request", "id", "found name"
    :widths: 1, 5, 5, 10

    0, "usa", "297677", "United States of America"
    1, "canada", "2856251", "Canada"

More complex geocoding queries can be created with the help of the ``regions_builder()`` function that returns the ``RegionsBuilder`` object and allows chaining its various methods in order to specify how to handle geocoding ambiguities.

For example:

.. code-block:: python

    regions_builder(request='warwick', level='city') \
        .allow_ambiguous() \
        .build()

This sample returns the ``Regions`` object containing IDs of all cities matching "warwick":

.. csv-table::
    :header: "", "request", "id", "found name"
    :widths: 1, 5, 5, 10

    0, "warwick", "785807", "Warwick"
    1, "warwick", "363189", "Warwick"
    2, "warwick", "352173", "Warwick"
    3, "warwick", "15994531", "Warwick"
    4, "warwick", "368499", "Warwick"
    5, "warwick", "239553", "Warwick"
    6, "warwick", "352897", "Warwick"
    7, "warwick", "3679247", "Warwick"
    8, "warwick", "8144841", "Warwick"
    9, "warwick", "382429", "West Warwick"
    10, "warwick", "7042961", "Warwick Township"
    11, "warwick", "6098747", "Warwick Township"
    12, "warwick", "15994533", "Sainte-Élizabeth-de-Warwick"

.. code-block:: python

    boston_us = regions(request='boston', within='us')
    regions_builder(request='warwick', level='city') \
        .where('warwick', near=boston_us) \
        .build()

This example returns the ``Regions`` object containing the ID of one particular "warwick" near Boston (US):

.. csv-table::
    :header: "", "request", "id", "found name"
    :widths: 1, 5, 5, 10

    0, "warwick", "785807", "Warwick"

Once the ``Regions`` object is available, it can be passed to any *Lets-Plot* geom supporting the ``map`` parameter.

If necessary, the ``Regions`` object can be transformed into a regular pandas ``DataFrame`` using ``to_data_frame()`` method or to a geopandas ``GeoDataFrame`` using one of ``centroids()``, ``boundaries()``, or ``limits()`` methods.

All coordinates are in the EPSG:4326 coordinate reference system (CRS). 

Note what executing geocoding queries requires an internet connection.

Examples
--------

- Visualization of the Titanic's Voyage: |titanic_voyage_nbviewer| |titanic_voyage_datalore| |titanic_voyage_kaggle| |titanic_voyage_colab|

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/map_titanic.png
    :width: 547px
    :height: 197px
    :alt: Couldn't load map_titanic.png

.. |titanic_voyage_nbviewer| image:: https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png
    :width: 109px
    :height: 20px
    :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map_titanic.ipynb
.. |titanic_voyage_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://view.datalore.io/notebook/1h4h0HMctRKJLY64PBe63a
.. |titanic_voyage_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/visualization-of-the-titanic-s-voyage
.. |titanic_voyage_colab| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg
    :width: 20px
    :height: 20px
    :alt: View at Colab
    :target: https://colab.research.google.com/drive/1PerUfSCyStcbnlXnxBj-JVI25-cXB_N5?usp=sharing

- Visualization of Airport Data on Map: |airport_data_kaggle|

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/map_airports.png
    :width: 547px
    :height: 311px
    :alt: Couldn't load map_airports.png

.. |airport_data_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/visualization-of-airport-data-on-map