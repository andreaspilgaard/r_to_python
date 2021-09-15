import numpy as np
import pandas as pd
from settings import project_settings

# Running project settings
project_settings()

# Read csv from gist

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

# Numpy's na's
na_data_type1 = cars.assign(na_col=lambda df: np.where(df.mpg > 20, np.NaN, 1))

na_data_type1.filter(['model', 'na_col']).query("na_col.isnull()", engine="python")

# Python default na's
na_data_type1 = cars.assign(na_col=lambda df: np.where(df.mpg > 20, None, 1))

na_data_type1.filter(['model', 'na_col']).query("na_col.isnull()", engine="python")
