"""
X and Y Location Scales
=======================

Use with x or y aesthetics (x shown here).

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_scales\_x_and_y.png"

from datetime import datetime

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

mw_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/midwest.csv')

ec_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/economics.csv', \
                    parse_dates=['date'])
ec_df = ec_df[ec_df.date > datetime(2000, 1, 1)]

# %%

# %% [markdown]
#
# Log10 Scale
# ~~~~~~~~~~~

# %%

p = ggplot(mw_df, aes('poptotal', 'state')) + geom_jitter(aes(color='state'), height=.2)

p1 = p + ggtitle('Default')
p2 = p + scale_x_log10() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

# %% [markdown]
#
# Reversed Scale
# ~~~~~~~~~~~~~~

# %%

p = ggplot(ec_df, aes('pop', 'unemploy')) + geom_line()

p1 = p + ggtitle('Default')
p2 = p + scale_x_reverse() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

# %% [markdown]
#
# Datetime Scale
# ~~~~~~~~~~~~~~

# %%

p = ggplot(ec_df, aes('date', 'pce')) + geom_line()

p1 = p + ggtitle('Default')
p2 = p + scale_x_datetime() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch