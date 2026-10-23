"""
demo02.py: finding unusual values in the abalone measurements.

What this demo shows:
    1. loading a second CSV file
    2. finding outliers, which in this data are real recording errors
    3. checking how strongly the measurements are related
    4. drawing a boxplot and a scatter plot

Note: the abalone measurements were divided by 200 by the people who
published them, so a length of 0.455 means about 91 mm.

How to run it:
    1. Install the package once, from the root directory:
           python -m pip install -e .
    2. Run the demo from the root directory, so that the data folder is found:
           python demo/demo02.py

Each plot opens in its own window. Close a window to see the next one.
"""

import datascout as ds


###
## 1. Load the data
###

# 4177 abalone (a sea snail), one row each
abalone = ds.load_data('data/abalone.csv')
print('Columns:', abalone.dtype.names)
print('Number of abalone:', len(abalone))


###
## 2. Look for outliers
###

# A height of 0 is impossible, and 1.13 is far above all the others
print('Outliers in height:', ds.find_outliers(abalone['height']))

# The summary shows that the average height is small, so these values stand out
ds.summarise('height', abalone['height'])
ds.summarise('shell_weight', abalone['shell_weight'])


###
## 3. Do the measurements move together?
###

# Close to 1: a longer shell is almost always a wider shell
print('Length and diameter:', ds.correlation(abalone['length'], abalone['diameter']))
# Lower: a heavier shell tends to have more rings, but less strongly
print('Shell weight and rings:', ds.correlation(abalone['shell_weight'], abalone['rings']))


###
## 4. Draw the plots
###

# The dots beyond the whiskers are the unusual heights
ds.plot_boxplot('height', abalone['height'])

# One dot per abalone, lying close to a straight line
ds.plot_scatter('length', abalone['length'], 'diameter', abalone['diameter'])
