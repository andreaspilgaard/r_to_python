# %%
import pandas as pd
from settings import project_settings
import numpy as np

# Running project settings
project_settings()

# Read csv from gist

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# Convert column names to lower case.

cars = cars.rename(str.lower, axis='columns')

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

# Counting models. Ways to get nice headers that are easy to work with.

# 1 No control of output names
cars.groupby(["gear"], as_index=False)[["model"]].count()

# 2 No control of output names
cars.groupby(["gear"], as_index=False)[["model"]].agg('count')

# 3 Control of output names
cars.groupby(["gear"], as_index=False). \
    agg(observations=pd.NamedAgg(column="model",
                                 aggfunc="count"))

# 4 Control of output names (F)
cars.groupby(["gear"], as_index=False). \
    agg(rows=("model", "count"),
        mean=("mpg", np.mean)
        )


