from lets_plot import *

def docs_dark_theme():
    bg_color = "#14181e"
    return theme(
        plot_background=element_rect(fill=bg_color),
        geom=element_geom(pen="white", paper=bg_color)
    ) + flavor_high_contrast_dark()