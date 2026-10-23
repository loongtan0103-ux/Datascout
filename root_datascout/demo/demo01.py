"""
demo01.py: a first look at the penguin measurements.

What this demo shows:
    1. loading a CSV file
    2. summarising the measurement columns
    3. checking a column for outliers
    4. measuring how two columns move together
    5. drawing a histogram and a scatter plot

How to run it:
    1. Install the package once, from the root directory:
           python -m pip install -e .
    2. Run the demo from the root directory, so that the data folder is found:
           python demo/demo01.py

Each plot opens in its own window. Close a window to see the next one.
"""

import datascout as ds


###
## 1. Load the data
###

# 333 penguins, one row each. Columns are picked by name, like data['body_mass_g'].
data = ds.load_data('data/penguins.csv')
print('Columns:', data.dtype.names)
print('Number of penguins:', len(data))


###
## 2. Summarise the measurement columns
###

# Each line shows the average, the spread and the number of values
ds.summarise('bill_length_mm', data['bill_length_mm'])
ds.summarise('bill_depth_mm', data['bill_depth_mm'])
ds.summarise('flipper_length_mm', data['flipper_length_mm'])
ds.summarise('body_mass_g', data['body_mass_g'])


###
## 3. Look for outliers
###

# An empty list means no value is more than 3 standard deviations from the mean
print('Outliers in body_mass_g:', ds.find_outliers(data['body_mass_g']))


###
## 4. Do two columns move together?
###

# Close to 1 means heavier penguins also have longer flippers
print('Flipper length and body mass:',
      ds.correlation(data['flipper_length_mm'], data['body_mass_g']))
# A value near 0 or below means the two columns do not rise together
print('Bill length and bill depth:',
      ds.correlation(data['bill_length_mm'], data['bill_depth_mm']))


###
## 5. Draw the plots
###

# The histogram has two clumps because the file mixes three species
ds.plot_histogram('bill_length_mm', data['bill_length_mm'])

# Every dot is one penguin: heavier penguins have longer flippers
ds.plot_scatter('flipper_length_mm', data['flipper_length_mm'],
                'body_mass_g', data['body_mass_g'])
