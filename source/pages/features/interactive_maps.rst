.. _features_interactive_maps:

Interactive Maps
################

*Lets-Plot* supports interactive maps via the `geom_livemap()` geom layer which enables a researcher to visualize geospatial information on a zoomable and paneble map. 

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/map_path.png
    :width: 480px
    :alt: Couldn't load map_path.png

When building interactive geospatial visualizations with *Lets-Plot* the visualisation workflow remains the same as when building a regular ``ggplot2`` plot.

However, ``geom_livemap()`` creates an interactive base-map super-layer and certain limitations do apply comparing to a regular ``ggplot2`` geom-layer:

* ``geom_livemap()`` must be added as a 1-st layer in plot;
* Maximum one ``geom_livemap()`` layer is alloed per plot;
* Not any type of *geometry* can be combined with interactive map layer in one plot;
* Internet connection to *map tiles provider* is required.

The following ``ggplot2`` geometry can be used with interactive maps:

- ``geom_point``
- ``geom_rect``
- ``geom_path``
- ``geom_polygon``
- ``geom_segment``
- ``geom_text``
- ``geom_tile``
- ``geom_vline``, ``geon_hline``
- ``geom_bin2d``
- ``geom_contour``, ``geom_contourf``
- ``geom_density2d``, ``geom_density2df``

Examples
--------

- `map_quickstart.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map_quickstart.ipynb>`_

- `map_california_housing.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map-california-housing/map_california_housing.ipynb>`_

- Visualization of the Titanic's Voyage: |titanic_voyage_datalore| |titanic_voyage_kaggle| |titanic_voyage_colab|

.. |titanic_voyage_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://view.datalore.jetbrains.com/notebook/1h4h0HMctRKJLY64PBe63a?force_sso=true
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

.. |airport_data_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/visualization-of-airport-data-on-map

- The Gallery of Base-maps: |basemaps_kaggle| |basemaps_colab|

.. |basemaps_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/the-gallery-of-basemaps
.. |basemaps_colab| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg
    :width: 20px
    :height: 20px
    :alt: View at Colab
    :target: https://colab.research.google.com/drive/1lwOyQx0UMBHFiLtXQZhXQpv5Z3M2XJI4?usp=sharing