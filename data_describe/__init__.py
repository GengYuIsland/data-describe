"""data-describe.

data-describe
=============

data-describe is a Python toolkit for Exploratory Data Analysis (EDA).
It aims to accelerate data exploration and analysis by providing automated
and polished analysis widgets.

Main Features
-------------
    - cluster: Clustering and visualization on a 2D plot
    - correlation_matrix: Association measures for both numeric and categorical features
    - data_heatmap: Data variation and missingness heatmap
    - data_summary: Selected summary statistics
    - distribution: Histograms, violin plots, bar charts
    - scatter_plots: Scatterplots
    - importance: Feature ranking
    - plot_time_series: Time series analysis and visualizations

Example:
    ::
        import data_describe as dd
        dd.data_summary(df)
"""
from data_describe.utilities.load_data import load_data  # noqa: F401
from data_describe.core.summary import data_summary  # noqa: F401
from data_describe.core.data_heatmap import data_heatmap  # noqa: F401
from data_describe.core.distributions import distribution  # noqa: F401
from data_describe.core.scatter_plot import scatter_plots  # noqa: F401
from data_describe.core.correlations import correlation_matrix  # noqa: F401
from data_describe.core.importance import importance  # noqa: F401
from data_describe.core.clusters import cluster  # noqa: F401
from data_describe.core.time_series import plot_time_series  # noqa: F401
from data_describe.config._config import options  # noqa: F401
from data_describe.compat import _compat  # noqa: F401
