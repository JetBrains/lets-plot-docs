"""
Two Variables
=============

Use a geom to represent data points. Use the geom’s aesthetic
properties to represent variables. Each function returns a layer.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_geoms\_2_variables.png"

from datetime import datetime

import pandas as pd

from lets_plot import *
from lets_plot.geo_data import *
LetsPlot.setup_html()

# %%

mpg_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

mw_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/midwest.csv')

ec_df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/economics.csv', \
                    parse_dates=['date'])
ec_df = ec_df[ec_df.date > datetime(2000, 1, 1)]

# %%

# %% [markdown]
#
# Continuous X, Continuous Y
# --------------------------

# %%

p = ggplot(mpg_df, aes('cty', 'hwy'))

# %%

p + geom_point()

# %%

p + geom_jitter()

# %%

p + geom_smooth()

# %%

p + geom_text(aes(label='fl'))

# %%

# %% [markdown]
#
# Discrete X, Continuous Y
# ------------------------

# %%

hwy_df = mpg_df.groupby('class').hwy.sum().to_frame('count').reset_index()
hwy_df.head(2)

# %%

ggplot(hwy_df, aes('class', 'count')) + geom_bar(stat='identity')

# %%

ggplot(mpg_df, aes('class', 'hwy')) + geom_boxplot()

# %%

# %% [markdown]
#
# Discrete X, Discrete Y
# ----------------------

# %%

ggplot(mpg_df, aes('fl', 'drv')) + geom_jitter(width=.3, height=.3)

# %%

# %% [markdown]
#
# Continuous Bivariate Distribution
# ---------------------------------

# %%

p = ggplot(mpg_df, aes('cty', 'hwy'))

# %%

p + geom_bin2d(binwidth=(2, 2))

# %%

p + geom_density2d(aes(color='..group..'))

# %%

p + geom_density2df(aes(fill='..group..'), color='white', size=.5)

# %%

# %% [markdown]
#
# Continuous Function
# -------------------

# %%

p = ggplot(ec_df, aes('date', 'unemploy')) + scale_x_datetime()

# %%

p + geom_area()

# %%

p + geom_line()

# %%

p + geom_step()

# %%

# %% [markdown]
#
# Visualizing Error
# -----------------

# %%

class_df = mpg_df.groupby('class').hwy.agg(['min', 'median', 'max']).reset_index()
class_df.head(2)

# %%

p = ggplot(class_df, aes(x='class'))

# %%

p + geom_crossbar(aes(ymin='min', middle='median', ymax='max'))

# %%

p + geom_errorbar(aes(ymin='min', ymax='max'))

# %%

p + geom_linerange(aes(ymin='min', ymax='max'))

# %%

p + geom_pointrange(aes(ymin='min', y='median', ymax='max'))

# %%

# %% [markdown]
#
# Maps
# ----

# %%

states = geocode('state', mw_df.state.unique(), scope='US').get_boundaries(9)
states.head(2)

# %%

ggplot() + geom_map(data=states, tooltips=layer_tooltips().line('@{found name}'))