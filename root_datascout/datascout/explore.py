###
## explore.py: tools for taking a first look at a CSV file of numbers
###

import numpy as np


###
## Reading the file
###

def load_data(filename):
    """Read a CSV file and return the data.

    The first line of the file holds the column names, so a column can be
    picked by its name, for example data['height'].
    """
    data = np.genfromtxt(filename, delimiter = ',', names = True,
                         dtype = None, encoding = None)
    return data


###
## Describing a column of numbers
###

def summarise(name, x):
    """Print the main numbers for one column."""
    # The mean is the average, std is how spread out the values are,
    # and n is how many values there are.
    print(f'{name}: mean={np.mean(x):.3f}, std={np.std(x, ddof=1):.3f}, n={len(x)}')


def find_outliers(x):
    """Return the values that are more than 3 standard deviations away from the mean."""
    m = np.mean(x)
    s = np.std(x)
    # Keep a value if it is below the lower limit OR above the upper limit
    return x[(x < m - 3 * s) | (x > m + 3 * s)]


def correlation(x, y):
    """Return how strongly 2 columns move together, from -1 to 1."""
    # Distance of every value from its own average
    dx = x - np.mean(x)
    dy = y - np.mean(y)
    # Close to 1: they rise together. Close to -1: one rises as the other falls.
    return np.mean(dx * dy) / (np.std(x) * np.std(y))
