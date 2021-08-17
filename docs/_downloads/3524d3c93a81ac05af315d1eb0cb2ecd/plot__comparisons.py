"""
Comparisons
===========

Some plots visualize a transformation of the original data set. Use a
stat parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ..name.. syntax.

Look at the examples below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_comparisons.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('class', 'hwy'))
p1 = p + geom_boxplot(aes(color='class', outlier_color='class'), show_legend=False) + \
         scale_color_brewer(type='qual', palette='Dark2') + \
         ggtitle('geom="boxplot" + default stat')
p2 = p + geom_crossbar(aes(color='class'), stat='boxplot') + \
         geom_point(aes(color='class'), stat='boxplot') + \
         scale_color_brewer(type='qual', palette='Dark2') + \
         ggtitle('geoms=["crossbar", "point"] + stat="boxplot"') + \
         theme(legend_position='none')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch