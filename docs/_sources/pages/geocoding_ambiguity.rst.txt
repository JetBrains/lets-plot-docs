.. _ambiguity:

Geocoding Ambiguity
===================


Hidden Preliminaries
--------------------

.. jupyter-execute::

    import shapely

    from lets_plot.geo_data import *
    from lets_plot import *
    LetsPlot.setup_html()


Problem
-------

Often geocoding can find multiple objects for a name or do not find anything. In this case error will be generated:

.. jupyter-execute::
    :raises: ValueError

    geocode_cities(['worcester']).get_geocodes()


Solutions
---------

``allow_ambiguous()``
~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    geocode_cities(['worcester']).allow_ambiguous().get_geocodes()

``ignore_not_found()``
~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    geocode_cities(['paris', 'foo']).ignore_not_found().get_geocodes()

``ignore_all_errors()``
~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    geocode_cities(['paris', 'worcester', 'foo']).ignore_all_errors().get_geocodes()

Parents
~~~~~~~

.. jupyter-execute::

    geocode_cities('worcester').states('massachusetts').get_geocodes()

.. raw:: html

    <br/>

.. jupyter-execute::

    states = geocode_states('US-MA')
    geocode_cities('worcester').states(states).get_geocodes()

Scope
~~~~~

.. jupyter-execute::

    geocode_cities(['worcester', 'warwick']).scope('UK').get_geocodes()

``where(..., scope=...)``
~~~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    bbox = shapely.geometry.box(-71.00, 42.00, -72.00, 43.00)
    geocode_cities('worcester').where('worcester', scope=bbox).get_geocodes()

.. raw:: html

    <br/>

.. jupyter-execute::

    massachusetts = geocode_states('massachusetts')
    geocode_cities('worcester').where('worcester', scope=massachusetts).get_geocodes()

``where(..., closest_to=...)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. jupyter-execute::

    boston = geocode_cities('boston')
    geocode_cities('worcester').where('worcester', closest_to=boston).get_geocodes()

.. raw:: html

    <br/>

.. jupyter-execute::

    boston = shapely.geometry.Point(-71.088, 42.311)
    geocode_cities('worcester').where('worcester', closest_to=boston).get_geocodes()