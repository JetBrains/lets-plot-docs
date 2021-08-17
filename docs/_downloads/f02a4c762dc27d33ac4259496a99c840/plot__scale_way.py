"""
Scale Way
=========

Set legend title and labels with a scale function.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_legends\_scale_way.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

labels = ['premium', 'regular', 'ethanol', 'diesel', 'natural gas']
ggplot(df, aes(x='fl')) + \
    geom_bar(aes(fill='fl')) + \
    scale_fill_discrete(name='fuel type', labels=labels)