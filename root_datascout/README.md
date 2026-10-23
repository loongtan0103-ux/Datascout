# datascout

`datascout` is a small Python package for taking a **first look at a CSV file of numbers**.

When you receive a new dataset, the first questions are usually the same:

- What is a typical value in each column, and how spread out are the values?
- Are there values that look wrong, such as impossible measurements?
- Which columns move together?
- What does each column look like?

`datascout` answers these questions with a handful of short functions. It uses only the
Python Standard Library, NumPy and Matplotlib.

## What is in this repository

```
root_datascout/
|-- README.md
|-- pyproject.toml
|-- datascout/
|   |-- __init__.py
|   |-- explore.py      (loading and describing the data)
|   |-- plots.py        (drawing the data)
|-- demo/
|   |-- demo01.py       (penguin measurements)
|   |-- demo02.py       (abalone measurements)
|-- data/
|   |-- penguins.csv
|   |-- abalone.csv
```

## Installation

You need Python 3.10 or newer. From inside the root directory, install the package in
editable mode:

```sh
python -m pip install -e .
```

The dependencies (NumPy and Matplotlib) are listed in `pyproject.toml` and are installed
automatically if they are missing. The first install needs an internet connection.

## How to use it

Import the package and load a CSV file. The first line of the file must hold the column
names, and the columns you analyse must contain numbers only.

```python
import datascout as ds

data = ds.load_data('data/penguins.csv')
print('Columns:', data.dtype.names)
```

A column is picked by its name, for example `data['body_mass_g']`.

### Main functions

| Function | What it does |
|---|---|
| `load_data(filename)` | Reads a CSV file and returns the data. Columns are picked by name. |
| `summarise(name, x)` | Prints the mean, the standard deviation and the number of values of one column. |
| `find_outliers(x)` | Returns the values that are more than 3 standard deviations from the mean. An empty result means none were found. |
| `correlation(x, y)` | Returns a number from -1 to 1 showing how strongly two columns move together. |
| `plot_histogram(name, x)` | Draws a histogram of one column. |
| `plot_boxplot(name, x)` | Draws a boxplot of one column. Dots mark the unusual values. |
| `plot_scatter(x_name, x, y_name, y)` | Draws a scatter plot of two columns against each other. |

### Short example

```python
import datascout as ds

penguins = ds.load_data('data/penguins.csv')

ds.summarise('body_mass_g', penguins['body_mass_g'])
print('Outliers:', ds.find_outliers(penguins['body_mass_g']))
print('Correlation:', ds.correlation(penguins['flipper_length_mm'], penguins['body_mass_g']))

ds.plot_histogram('body_mass_g', penguins['body_mass_g'])
```

## Running the demonstration scripts

Run the demos from the root directory, so that the `data` folder is found. Install the
package first (see above). The demos do not need any change to the package's code.

```sh
python demo/demo01.py
python demo/demo02.py
```

- `demo01.py` explores the penguin measurements: summaries, a correlation check, a
  histogram with two clumps (the file mixes three species) and a scatter plot.
- `demo02.py` explores the abalone measurements and finds real recording errors: two
  shells with a height of 0 and one with a height of 1.13.

Each plot opens in its own window. Close a window to see the next one.

## The data

Both datasets are real, openly licensed data.

**`data/penguins.csv`**: measurements of 333 penguins from the Palmer Archipelago,
Antarctica. The data were collected by Dr. Kristen Gorman and the Palmer Station,
Antarctica LTER. The file comes from the `palmerpenguins` package by Allison Horst,
Alison Hill and Kristen Gorman (2020), doi: 10.5281/zenodo.3960218. Licence: CC0 (public
domain). **Change made:** the 11 rows that contained missing values (`NA`) were removed,
leaving 333 of the original 344 rows.

**`data/abalone.csv`**: physical measurements of 4,177 abalone. Nash, W., Sellers, T.,
Talbot, S., Cawthorn, A., & Ford, W. (1994). *Abalone* [Dataset]. UCI Machine Learning
Repository. https://doi.org/10.24432/C55C7W. Licence: CC BY 4.0. **Change made:** a header
row with column names was added. **Note:** the publishers divided the measurements by
200, so a length of 0.455 means about 91 mm.

## Limitations

- Columns must hold numbers. Text columns, such as `species`, cannot be summarised.
- Missing values are not handled. Remove or fill them before loading a file.
- Outliers are detected with a simple rule (3 standard deviations from the mean), which
  works best for data that is roughly bell-shaped.
