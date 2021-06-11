.. _interactive_maps:

Interactive Maps
================

*Lets-Plot* supports interactive maps via the ``geom_livemap()`` geom layer which enables a researcher to visualize geospatial information on a zoomable and paneble map.

.. image:: /_static/images/map_path.png
    :width: 480px
    :alt: Couldn't load map_path.png

When building interactive geospatial visualizations with *Lets-Plot* the visualisation workflow remains the same as when building a regular ``ggplot2`` plot.

However, ``geom_livemap()`` creates an interactive base-map super-layer and certain limitations do apply comparing to a regular ``ggplot2`` geom-layer:

- ``geom_livemap()`` must be added as a 1-st layer in plot;
- Maximum one ``geom_livemap()`` layer is alloed per plot;
- Not any type of *geometry* can be combined with interactive map layer in one plot;
- Internet connection to *map tiles provider* is required.

The following ``ggplot2`` geometry can be used with interactive maps:

- ``geom_point``,
- ``geom_rect``,
- ``geom_path``,
- ``geom_polygon``,
- ``geom_segment``,
- ``geom_text``,
- ``geom_tile``,
- ``geom_vline``, ``geon_hline``,
- ``geom_bin2d``,
- ``geom_contour``, ``geom_contourf``,
- ``geom_density2d``, ``geom_density2df``.

Examples:

- Interactive maps: quick start: |interactive_maps_quickstart_datalore|

.. |interactive_maps_quickstart_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://datalore.jetbrains.com/view/notebook/cwDq8gX5UGidzo65RY85yP

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

- Mapping US Household Income: |us_household_income_kaggle|

.. |us_household_income_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/mapping-us-household-income

- Plotting Airbnb prices Boston: |plotting_airbnb_prices_boston_datalore| |plotting_airbnb_prices_boston_medium|

.. |plotting_airbnb_prices_boston_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://datalore.jetbrains.com/view/notebook/eifzdh96VYuNrcjuOpYPYr

.. |plotting_airbnb_prices_boston_medium| image:: https://raw.githubusercontent.com/Medium/medium-logos/master/01_Logo/01_Black/SVG/Medium-Logo-Black-RGB.svg
    :height: 25px
    :alt: View in Medium
    :target: https://csboutique.medium.com/lets-plot-948ee80cfa5c

- Beijing housing prices on a map: |beijing_housing_prices_kaggle|

.. |beijing_housing_prices_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/beijing-housing-prices-on-a-map-with-spatial-join

- `map_california_housing.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map-california-housing/map_california_housing.ipynb>`__
