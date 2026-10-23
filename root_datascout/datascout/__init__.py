"""datascout: a small package for taking a first look at a CSV file of numbers."""

from .explore import load_data, summarise, find_outliers, correlation
from .plots import plot_histogram, plot_boxplot, plot_scatter
