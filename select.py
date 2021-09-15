# %%
import pandas as pd
from settings import project_settings
import numpy as np

# Running project settings
project_settings()

# Read csv from gist

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

# selecting values and hp
cars.filter(["gear", "hp"])

# selecting values based on regex
cars.filter(regex="^m")

cars.filter(regex="^m")

# reorganizing columns using equivilent to everything

# 1
first_cols = ["mpg", "hp"]
rest = list(set(cars.columns).difference(set(first_cols)))
cars.filter(first_cols + rest)

# 2
first_cols = ["model", "mpg", "hp", "gear", "am"]
rest = [item for item in cars.columns if item not in first_cols]
cars.filter(first_cols + list(cars.columns))
