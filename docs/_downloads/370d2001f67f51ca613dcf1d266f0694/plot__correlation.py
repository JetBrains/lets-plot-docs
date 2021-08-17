"""
Correlation
===========

Some plots visualize a transformation of the original data set. Use a
stat parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ..name.. syntax.

Look at the examples below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_correlation.png"

import pandas as pd

from lets_plot import *
from lets_plot.bistro.corr import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p1 = corr_plot(df, flip=False).points().build() + ggtitle('geom="corr_plot" + default stat')
p2 = ggplot(df) + geom_point(aes(size='..corr_abs..'), stat='corr', shape=21, color='black') + \
                  scale_fill_gradient2(name='Corr', low='#ca0020', mid='#f7f7f7', high='#0571b0') + \
                  scale_size_area(name='', max_size=1) + \
                  coord_fixed() + \
                  ggtitle('geom="point" + stat="corr"') + \
                  theme(axis_title='blank')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch