"""
Default Theme
=============

White background with no gridlines.

See
`theme() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.theme.html#lets_plot.theme>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_themes\_default_theme.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes(x='fl')) + \
    geom_bar() + \
    theme(axis_line='blank', axis_ticks='blank', axis_text_y='blank', axis_title_y='blank')