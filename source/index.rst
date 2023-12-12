.. title:: Lets-Plot: open-source plotting library for statistical data


.. toctree::
    :glob:
    :hidden:
    :maxdepth: 1

    API <python/pages/api>
    python/pages/charts
    python/pages/maps
    Geocoding <python/pages/geocoding>
    Gallery <python/pages/gallery>
    'bistro' plots <python/pages/bistro>
    What is new <python/pages/whats_new>

.. grid:: 2
    :class-container: landing-content

    .. grid-item-card::

        .. raw:: html

            <h1>Lets-Plot</h1>

        Multiplatform plotting library based on the Grammar of Graphics.

        .. grid:: 3
            :class-container: landing-buttons

            .. grid-item-card::

                .. button-ref:: python/index
                    :color: primary

                    Get started

            .. grid-item-card::

                .. button-ref:: python/pages/user_guide
                    :color: primary
                    :outline:

                    See user guide

            .. grid-item-card::
                :text-align: center

                :ref:`Visit the API <api>`

    .. grid-item-card::

        .. grid:: 3
            :class-container: landing-gallery

            .. grid-item-card::

                .. extref:: geom_violin

            .. grid-item-card::

                .. extref:: world_happiness

            .. grid-item-card::

                .. extref:: bar_annotations

            .. grid-item-card::

                .. extref:: soil_pollutants_with_gaussian_processes

            .. grid-item-card::

                .. extref:: map_california_housing

            .. grid-item-card::

                .. extref:: user_guide


.. grid:: 2
    :class-container: features-list

    .. grid-item-card::

        .. raw:: html

            <h2>Key Features</h2>

    .. grid-item-card::

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/grammar-of-graphics.png

        Grammar of Graphics

        We recommend an excellent book called `"ggplot2: Elegant Graphics for Data Analysis" <https://ggplot2-book.org/index.html>`__. This will be a good prerequisite for further exploration of the Lets-Plot library.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/logo/kotlin.svg

        Multiplatform

        R, Python, what’s next? Right. `Lets-Plot Kotlin API <https://github.com/JetBrains/lets-plot-kotlin>`__ enables data visualization in JVM and Kotlin/JS applications as well as in scientific notebooks like Jupyter and Datalore.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/geospatial-visualization.svg

        Geospatial Visualization

        Find spatial objects with the help of our powerful and easy to use :ref:`Geocoding <geocoding>` module. In case you already have ``GeoDataFrame`` on hand - :ref:`plot it <geopandas>` straight away.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/tooltips.svg

        Customizable Tooltips and Annotations

        You can customize the content, values formatting and appearance of tooltip for any geometry layer in your plot. :ref:`Learn more <tooltips>`.