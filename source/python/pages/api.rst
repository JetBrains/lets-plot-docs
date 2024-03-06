.. _api:

:og:description: Basic classes, geometries, stats, themes, geocoding API and other useful features to build beautiful plots.

:orphan:

:tocdepth: 2

.. title:: Lets-Plot Python API Reference: Detailed Documentation

.. meta::
   :description: Basic classes, geometries, stats, themes, geocoding API and other useful features to build beautiful plots.
   :keywords: LetsPlot, ggplot


API Reference
=============


Configuring
-----------

.. currentmodule:: lets_plot

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    LetsPlot


Plotting
--------

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    ggplot
    GGBunch
    gggrid
    ggmarginal
    aes
    ggsave


Geometries
----------

Standard Geometries
~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    geom_point
    geom_path
    geom_line
    geom_smooth
    geom_bar
    geom_count
    geom_pie
    geom_lollipop
    geom_histogram
    geom_dotplot
    geom_bin2d
    geom_tile
    geom_raster
    geom_errorbar
    geom_crossbar
    geom_linerange
    geom_pointrange
    geom_contour
    geom_contourf
    geom_polygon
    geom_map
    geom_abline
    geom_hline
    geom_vline
    geom_boxplot
    geom_violin
    geom_area_ridges
    geom_ydotplot
    geom_ribbon
    geom_area
    geom_density
    geom_density2d
    geom_density2df
    geom_jitter
    geom_freqpoly
    geom_step
    geom_rect
    geom_segment
    geom_curve
    geom_spoke
    geom_text
    geom_label
    geom_qq
    geom_qq2
    geom_qq_line
    geom_qq2_line
    geom_function

Additional Geometries
~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    geom_imshow
    geom_livemap


Stats
-----

.. autosummary::
    :toctree: api
    :nosignatures:

    stat_sum
    stat_summary
    stat_summary_bin
    stat_ecdf


Extras
------

.. autosummary::
    :toctree: api
    :nosignatures:

    arrow

.. currentmodule:: lets_plot.mapping

.. autosummary::
    :toctree: api
    :nosignatures:

    as_discrete

.. currentmodule:: lets_plot

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    layer_labels


Facets
------

.. autosummary::
    :toctree: api
    :nosignatures:

    facet_grid
    facet_wrap


Scales
------

Position Scales
~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_x_discrete
    scale_y_discrete
    scale_x_discrete_reversed
    scale_y_discrete_reversed
    scale_x_continuous
    scale_y_continuous
    scale_x_log10
    scale_y_log10
    scale_x_log2
    scale_y_log2
    scale_x_reverse
    scale_y_reverse

Color Scales
~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_color_manual
    scale_color_gradient
    scale_color_continuous
    scale_color_gradient2
    scale_color_gradientn
    scale_color_hue
    scale_color_discrete
    scale_color_grey
    scale_color_brewer
    scale_color_viridis

Fill Scales
~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_fill_manual
    scale_fill_gradient
    scale_fill_continuous
    scale_fill_gradient2
    scale_fill_gradientn
    scale_fill_hue
    scale_fill_discrete
    scale_fill_grey
    scale_fill_brewer
    scale_fill_viridis

Flexible Color Scales
~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_manual
    scale_gradient
    scale_continuous
    scale_gradient2
    scale_gradientn
    scale_hue
    scale_discrete
    scale_grey
    scale_brewer
    scale_viridis

Shape Scales
~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_shape
    scale_shape_manual

Size Scales
~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_size_manual
    scale_size
    scale_size_area
    scale_linewidth
    scale_stroke

Alpha Scales
~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_alpha_manual
    scale_alpha

Linetype Scales
~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_linetype_manual

Datetime Scales
~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_x_datetime
    scale_y_datetime
    scale_x_time
    scale_y_time

Identity Scales
~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    scale_identity
    scale_color_identity
    scale_fill_identity
    scale_shape_identity
    scale_linetype_identity
    scale_alpha_identity
    scale_size_identity
    scale_linewidth_identity
    scale_stroke_identity

Scale Limits
~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    lims
    xlim
    ylim

Scale Guides
~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    guide_legend
    guide_colorbar
    guides


Positions
---------

.. autosummary::
    :toctree: api
    :nosignatures:

    position_dodge
    position_dodgev
    position_jitter
    position_nudge
    position_jitterdodge
    position_fill
    position_stack


Coordinate Systems
------------------

.. autosummary::
    :toctree: api
    :nosignatures:

    coord_cartesian
    coord_fixed
    coord_polar
    coord_map
    coord_flip


Theme
-----

Base
~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    theme
    element_blank
    element_rect
    element_line
    element_text
    element_geom
    margin
    ggsize

Predefined Themes
~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    theme_none
    theme_void
    theme_bw
    theme_classic
    theme_grey
    theme_light
    theme_minimal
    theme_minimal2

Flavors
~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    flavor_darcula
    flavor_high_contrast_dark
    flavor_high_contrast_light
    flavor_solarized_dark
    flavor_solarized_light

Labels
~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    ggtitle
    labs
    xlab
    ylab

Tooltips
~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    layer_tooltips

Font Features
~~~~~~~~~~~~~

.. autosummary::
    :toctree: api
    :nosignatures:

    font_metrics_adjustment
    font_family_info


Sampling
--------

.. autosummary::
    :toctree: api
    :nosignatures:

    sampling_random
    sampling_random_stratified
    sampling_pick
    sampling_systematic
    sampling_group_random
    sampling_group_systematic
    sampling_vertex_vw
    sampling_vertex_dp


Bistro Module
-------------

.. currentmodule:: lets_plot.bistro.im

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    image_matrix

.. currentmodule:: lets_plot.bistro.corr

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    corr_plot

.. currentmodule:: lets_plot.bistro.qq

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    qq_plot

.. currentmodule:: lets_plot.bistro.joint

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    joint_plot

.. currentmodule:: lets_plot.bistro.residual

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    residual_plot


Geospatial
----------

.. currentmodule:: lets_plot.geo_data

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    NamesGeocoder
    geocode
    geocode_cities
    geocode_counties
    geocode_states
    geocode_countries
    distance

.. currentmodule:: lets_plot

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: base.rst

    maptiles_zxy
    maptiles_lets_plot
    maptiles_solid

.. currentmodule:: lets_plot.tilesets

.. autosummary::
    :toctree: api
    :nosignatures:
    :template: data.rst

    LETS_PLOT_COLOR
    LETS_PLOT_LIGHT
    LETS_PLOT_DARK
    LETS_PLOT_BW
    SOLID
    OSM
    OPEN_TOPO_MAP
    CARTO_POSITRON
    CARTO_POSITRON_HIRES
    CARTO_POSITRON_NO_LABELS
    CARTO_POSITRON_NO_LABELS_HIRES
    CARTO_DARK_MATTER_NO_LABELS
    CARTO_DARK_MATTER_NO_LABELS_HIRES
    CARTO_VOYAGER
    CARTO_VOYAGER_HIRES
    CARTO_MIDNIGHT_COMMANDER
    CARTO_MIDNIGHT_COMMANDER_HIRES
    CARTO_ANTIQUE
    CARTO_ANTIQUE_HIRES
    CARTO_FLAT_BLUE
    CARTO_FLAT_BLUE_HIRES
    NASA_CITYLIGHTS_2012
    NASA_GREYSCALE_SHADED_RELIEF_30M
    NASA_COLOR_SHADED_RELIEF_30M
    NASA_TERRA_TRUECOLOR