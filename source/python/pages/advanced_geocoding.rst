.. _advanced_geocoding:

:orphan:

.. title:: Advanced Geocoding

.. meta::
   :description: Lets-Plot offers geocoding API that allows a user to execute a single and batch geocoding queries to convert names of places into geographic coordinates.
   :keywords: geocoding, administrative levels, geopandas, GeoDataFrame


Advanced Geocoding
==================

- :ref:`Overview <geocoding_overview>`
- :ref:`Examples <geocoding_examples>`
- :ref:`Reference <geocoding_reference>`

  - :ref:`Levels <geocoding_levels>`
  - :ref:`Parents <geocoding_parents>`
  - :ref:`Scope <geocoding_scope>`
  - :ref:`Fetch All <geocoding_fetch_all>`
  - :ref:`US-48 <geocoding_us_48>`
  - :ref:`Ambiguity <geocoding_ambiguity>`

    - :ref:`allow_ambiguous() <geocoding_allow_ambiguous>`
    - :ref:`ignore_not_found() <geocoding_ignore_not_found>`
    - :ref:`ignore_all_errors() <geocoding_ignore_all_errors>`
    - :ref:`where() <geocoding_where>`

      - :ref:`closest_to <geocoding_where_closest_to>`
      - :ref:`scope <geocoding_where_scope>`

  - :ref:`Working with Plots <geocoding_working_with_plot>`

    - :ref:`Plotting a GeoDataFrame <geocoding_plot_gdf>`
    - :ref:`Plotting a Geocoder <geocoding_plot_geocoder>`
    - :ref:`map and map_join <geocoding_join>`

      - :ref:`Join with GeoDataFrame <geocoding_join_gdf>`
      - :ref:`Join with Geocoder <geocoding_join_geocoder>`


.. _geocoding_overview:

Overview
--------

Geocoding is the process of converting names of places into geographic coordinates.

*Lets-Plot* now offers geocoding API covering the following administrative levels:

- country
- state
- county
- city

*Lets-Plot* geocoding API allows a user to execute a single and batch geocoding queries, and handle possible names ambiguity.

The core class is ``Geocoder``. There is a function's family for constructing the ``Geocoder`` object - ``geocode_cities()``, ``geocode_counties()``, ``geocode_states()``, ``geocode_countries()`` and ``geocode()``. For example:

.. jupyter-execute::
    :linenos:

    from lets_plot.geo_data import *
    countries = geocode_countries(['usa', 'canada'])

| Note that actual geocoding process is not executing here, it starts when any ``get_xxx()`` function is called. We will use in examples function ``get_geocodes()`` which returns ``DataFrame`` with metadata.

Let us geocode countries. This code returns the ``DataFrame`` object containing internal IDs for Canada and the US:

.. jupyter-execute::
    :linenos:

    countries.get_geocodes()

| More complex queries can be created in order to specify how to handle geocoding ambiguities.

For example, this sample returns the ``DataFrame`` object containing IDs of all cities matching "warwick":

.. jupyter-execute::
    :linenos:

    geocode_cities('warwick')  \
        .allow_ambiguous()  \
        .get_geocodes()

| This example returns the ``DataFrame`` object containing the ID of one particular "warwick" closest to Boston (US):

.. jupyter-execute::
    :linenos:

    boston_us = geocode_cities('boston').scope('us')
    geocode_cities('warwick') \
        .where('warwick', closest_to=boston_us) \
        .get_geocodes()

| Once the ``Geocoder`` object is available, it can be passed to any *Lets-Plot* geom supporting the ``map`` parameter. ``map`` parameter can be used to simply :ref:`draw a GeoDataFrame <geocoding_plot_gdf>` or to :ref:`draw a Geocoder <geocoding_plot_geocoder>`. For more complex plots parameter :ref:`map_join <geocoding_join>` can be used to map data to geometries.

If necessary, the ``Geocoder`` object can be transformed to a geopandas ``GeoDataFrame`` using one of ``get_centroids()``, ``get_boundaries()``, or ``get_limits()`` methods.

All coordinates are in the EPSG:4326 coordinate reference system (CRS).

Note that an internet connection is required to execute geocoding queries.


.. _geocoding_examples:

Examples
--------

-  Various geocoding cases with maps: |geocoding_examples|

.. |geocoding_examples| extref:: geocoding_examples
    :type: logo
    :height: 2rem

-  Mapping US Household Income: |mapping_us_household_income|

.. |mapping_us_household_income| extref:: mapping_us_household_income
    :type: logo
    :height: 2rem

-  Geocoding the US counties: |map_us_household_income|

.. |map_us_household_income| extref:: map_us_household_income
    :type: logo
    :height: 2rem

-  Visualization of the Titanic's voyage: |titanic-datalore| |titanic-kaggle| |titanic-colab|

.. |titanic-datalore| extref:: titanic
    :ref: datalore
    :type: logo
    :height: 2rem
.. |titanic-kaggle| extref:: titanic
    :ref: kaggle
    :type: logo
    :height: 2rem
.. |titanic-colab| extref:: titanic
    :ref: colab
    :type: logo
    :height: 2rem

.. image:: /_static/images/map_titanic.png
    :width: 547px
    :alt: Couldn't load map_titanic.png

-  Visualization of Airport Data on Map: |map_airports|

.. |map_airports| extref:: map_airports
    :type: logo
    :height: 2rem

.. image:: /_static/images/map_airports.png
    :width: 547px
    :alt: Couldn't load map_airports.png


.. _geocoding_reference:

Reference
---------

The |geocoding_reference| notebook contains a demonstration code covering use-cases presented in this section.

.. |geocoding_reference| extref:: geocoding_reference
    :type: text
    :text: geocoding_reference.ipynb


.. _geocoding_levels:

Levels
~~~~~~

Geocoding supports 4 administrative levels:

- city
- county
- state
- country

Function ``geocode()`` with ``level=None`` can try to detect level automatically - it enumerates all levels from country to city and selects best matching level (result without ambiguity and unknown names).
For example:

.. jupyter-execute::
    :linenos:

    geocode(names=['florida', 'tx']).get_geocodes()

| Level auto-detection can be useful, but it is slower and not recommended for large data sets.

Functions ``geocode_cities()``, ``geocode_counties()``, ``geocode_states()``, ``geocode_countries()`` or ``geocode(level=xxx)`` search names only at a given level or return an error.

.. jupyter-execute::
    :linenos:

    geocode_states(['florida', 'tx']).get_geocodes()


.. _geocoding_parents:

Parents
~~~~~~~

``Geocoder`` class provides functions to define parents with administrative level - ``counties()``, ``states()``, ``countries()``.
These functions can handle single or multiple values of type string or ``Geocoder``. The number of values must match the number of names in ``Geocoder`` so that they form a table.

Parents will be present in the result ``DataFrame`` to make it possible to join data and geometry via :ref:`map_join <geocoding_join>`.

.. jupyter-execute::
    :linenos:

    geocode_cities(['warwick', 'worcester'])\
        .counties(['Worth County', 'worcester county'])\
        .states(['georgia', 'massachusetts'])\
        .get_geocodes()

| Parents can contain ``None`` value for countries with different administrative division:

.. jupyter-execute::
    :linenos:

    geocode_cities(['warwick', 'worcester'])\
        .states(['Georgia', None])\
        .countries(['USA', 'United Kingdom'])\
        .get_geocodes()

| Parent can be ``Geocoder`` object. This allows resolving parent's ambiguity:

.. jupyter-execute::
    :linenos:

    s = geocode_states(['vermont', 'georgia']).scope('usa')
    geocode_cities(['worcester', 'warwick']).states(s).get_geocodes()


.. _geocoding_scope:

Scope
~~~~~

``scope()`` is a special kind of parent.
``scope()`` can handle a ``string`` or a single entry ``Geocoder`` object.
``scope()`` is not associated with any administrative level, it acts as parent for any other parents and names.
``scope()`` can not be used with ``countries()`` parents.
Typical use-case: all of names belong to the same parent.

.. jupyter-execute::
    :linenos:

    geocode_counties(['Dakota County', 'Nevada County']).states(['NE', 'AR']).scope('USA').get_geocodes()

| Parents can be modified between searches:

.. jupyter-execute::
    :linenos:

    florida = geocode_states('florida')

    display(florida.countries('usa').get_geocodes())
    display(florida.countries('uruguay').get_geocodes())
    display(florida.countries(None).get_geocodes())


.. _geocoding_fetch_all:

Fetch All
~~~~~~~~~

It is possible to fetch all objects within parent - just do not set the ``names`` parameter.

.. jupyter-execute::
    :linenos:

    geocode_counties().states('massachusetts').get_geocodes()


.. _geocoding_us_48:

US-48
~~~~~

Geocoding supports a special name ``us-48`` for `CONUS <https://en.wikipedia.org/wiki/Contiguous_United_States>`__.
The ``us-48`` can be used as name or parent.

.. jupyter-execute::
    :linenos:

    geocode_states('us-48').get_geocodes()


.. _geocoding_ambiguity:

Ambiguity
~~~~~~~~~

Often geocoding can find multiple objects for a name or do not find anything.
In this case error will be generated:

.. jupyter-execute::
    :linenos:
    :raises: ValueError

    geocode_cities(['warwick', 'worcester']).get_geocodes()

| The ambiguity can be resolved in different ways.


.. _geocoding_allow_ambiguous:

``allow_ambiguous()``
^^^^^^^^^^^^^^^^^^^^^

The best way is to find an object that we search and use its parents.
The function converts error result into success result that can be rendered on a map or verified manually in other way.
Can be combined with :ref:`ignore_not_found() <geocoding_ignore_not_found>` to suppress the "not found" error, which has higher priority.

.. jupyter-execute::
    :linenos:

    geocode_cities(['warwick', 'worcester']).allow_ambiguous().get_geocodes()


.. _geocoding_ignore_not_found:

``ignore_not_found()``
^^^^^^^^^^^^^^^^^^^^^^

Removes unknown names from the result.

.. jupyter-execute::
    :linenos:

    geocode_cities(['paris', 'foo']).ignore_not_found().get_geocodes()


.. _geocoding_ignore_all_errors:

``ignore_all_errors()``
^^^^^^^^^^^^^^^^^^^^^^^

Remove not found names or names with multiple matches.

.. jupyter-execute::
    :linenos:

    geocode_cities(['paris', 'worcester', 'foo']).ignore_all_errors().get_geocodes()


.. _geocoding_where:

``where()``
^^^^^^^^^^^

For resolving an ambiguity geocoding provides a function that can configure names individually.

To configure a name the function ``where(...)`` should be called with the place name and all used parent names.
Parents cannot be changed via ``where()`` function call.
If name and parents do not match with ones from the ``where()`` function an error will be generated.
It is important for cases like this:

.. jupyter-execute::
    :linenos:

    geocode_counties(['Washington', 'Washington']).states(['oregon', 'utah']).get_geocodes()


.. _geocoding_where_closest_to:

| **closest_to**

With parameter ``closest_to`` geocoding will take only the object closest to given place.
Parameter ``closest_to`` can be a single value ``Geocoder``.

.. jupyter-execute::
    :linenos:

    boston = geocode_cities('boston')
    geocode_cities('worcester').where('worcester', closest_to=boston).get_geocodes()

| Or it can be a ``shapely.geometry.Point``.

.. jupyter-execute::
    :linenos:

    import shapely

    geocode_cities('worcester').where('worcester', closest_to=shapely.geometry.Point(-71.088, 42.311)).get_geocodes()


.. _geocoding_where_scope:

| **scope**

With parameter ``scope`` a ``shapely.geometry.Polygon`` can be used for limiting an area of the search (coordinates should be in WGS84 coordinate system).
Note that bbox of the polygon will be used:

.. jupyter-execute::
    :linenos:

    geocode_cities('worcester')\
        .where('worcester', scope=shapely.geometry.box(-71.00, 42.00, -72.00, 43.00))\
        .get_geocodes()

| Also, ``scope`` can be a single value ``Geocoder`` object or a ``string``:

.. jupyter-execute::
    :linenos:

    massachusetts = geocode_states('massachusetts')
    geocode_cities('worcester').where('worcester', scope=massachusetts).get_geocodes()

| ``scope`` does not change parents in the result ``DataFrame``:

.. jupyter-execute::
    :linenos:

    worcester_county=geocode_counties('Worcester County').states('massachusetts').countries('usa')

    geocode_cities(['worcester', 'worcester'])\
        .countries(['USA', 'United Kingdom'])\
        .where('worcester', country='USA', scope=worcester_county)\
        .get_geocodes()


.. _geocoding_working_with_plot:

Working with Plots
~~~~~~~~~~~~~~~~~~


.. _geocoding_plot_gdf:

Plotting a ``GeoDataFrame``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``get_xxx()`` functions return GeoDataFrame which can be used as ``data`` or ``map`` parameter (see |geopandas_naturalearth| or |geopandas_kotlin_isl|).

.. |geopandas_naturalearth| extref:: geopandas_naturalearth
    :type: text
    :text: this
.. |geopandas_kotlin_isl| extref:: geopandas_kotlin_isl
    :type: text
    :text: this

.. jupyter-execute::
    :linenos:

    from lets_plot import *
    LetsPlot.setup_html()

    ggplot() + geom_point(map=geocode_states('us-48').get_centroids())


.. _geocoding_plot_geocoder:

Plotting a ``Geocoder``
^^^^^^^^^^^^^^^^^^^^^^^

Drawing geometries with ``Geocoder`` is a bit easier than using ``GeoDataFrame``.
Just pass a ``Geocoder`` to the ``map`` parameter, and the layer will fetch geometry it supports:

.. jupyter-execute::
    :linenos:

    ggplot() + geom_point(map=geocode_states('us-48'))

| The list of geoms and corresponding fetching functions they support:

.. csv-table::
    :header: "", ""
    :widths: 1, 1

    "geom_point(), geom_text()", "get_centroids()"
    "geom_map(), geom_polygon()", "get_boundaries()"
    "geom_rect()", "get_limits()"


.. _geocoding_join:

``map`` and ``map_join``
^^^^^^^^^^^^^^^^^^^^^^^^

Parameter ``map_join`` is used to join map coordinates with data. Map join is expected to be a ``str``, ``list[str]`` or ``list[list[str]]``.

- first value in a pair is a data_key (column/columns in ``data``),
- second value in a pair is a map_key (column/columns in ``map``).


.. _geocoding_join_gdf:

Join with ``GeoDataFrame``
''''''''''''''''''''''''''
  Explicitly set keys for both data and map.

- ``map_join=['data_column', 'map_column']``:
  same as ``[['data_column'], ['map_column']]``
- ``map_join=[['data_column_1', 'data_column_2'], ['map_column_1', 'map_column_2']]``:
  same as ``[['data_column_1', 'data_column_2'], ['map_column_1', 'map_column_2']]``
- ``map_join=[['City_Name', 'State_Name'], ['city', 'state']]``:

Single string key is not allowed - Lets-Plot can't deduce a map key on a user generated GeoDataFrames.


.. _geocoding_join_geocoder:

Join with ``Geocoder``
''''''''''''''''''''''

``Geocoder`` and ``GeoDataFrame``, returned by a ``Geocoder`` geometries fetching functions, contains metadata so in most cases only data keys have to be provided - Lets-Plot will generate map keys automatically with columns that were used for geocoding.

- ``map_join='State_Name'``:
  same as ``[['State_Name'], ['state']]``
- ``map_join=[['City_Name', 'State_Name']]``:
  same as ``[['City_Name', 'State_Name'], ['city', 'state']]``
- ``map_join=[['City_Name', 'State_Name'], ['city', 'state']]``:
  Explicitly set keys for both data and map.

.. note::

    Generated keys follow this order - ``city``, ``county``, ``state``, ``country``.
    Parents that were not provided will be omitted.
    Data columns should follow the same order or result of join operation will be incorrect.
