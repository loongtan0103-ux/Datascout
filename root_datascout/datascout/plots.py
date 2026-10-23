###
## plots.py: tools for plotting different graphs
###

import matplotlib.pyplot as plt


###
## One column
###

# Plotting a histogram
def plot_histogram(name, x):
    """Draw a histogram of one column."""
    # A histogram counts how many values fall in each bar
    plt.figure(figsize = (8, 5))
    plt.hist(x, bins = 30, color = 'white', edgecolor = 'grey')
    plt.title(f'Histogram of {name}')
    plt.xlabel(name)
    plt.ylabel('Frequency')
    plt.show()


# Plotting a boxplot
def plot_boxplot(name, x):
    """Draw a boxplot of one column. Dots mark the unusual values."""
    # The box holds the middle half of the values, the line inside is the median
    plt.figure(figsize = (5, 6))
    plt.boxplot(x)
    plt.title(f'Boxplot of {name}')
    plt.ylabel(name)
    plt.show()


###
## Two columns
###

# Plotting a scatter plot
def plot_scatter(x_name, x, y_name, y):
    """Draw a scatter plot of two columns against each other."""
    # Every dot is one row of the file
    plt.figure(figsize = (8, 5))
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.title(f'{y_name} against {x_name}')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid(True)
    plt.show()
