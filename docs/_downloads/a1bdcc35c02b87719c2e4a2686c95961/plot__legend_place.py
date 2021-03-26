"""
Legend Place
============

Place legend at ``bottom``, ``top``, ``left`` or ``right``.

See
`theme() <https://jetbrains.github.io/lets-plot-docs/pages/api/lets_plot.theme.html#lets_plot.theme>`__.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_legends\_legend_place.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

ggplot(df, aes('class', 'hwy')) + \
    geom_jitter(aes(color='fl'), width=.3, height=0) + \
    theme(legend_position='top')