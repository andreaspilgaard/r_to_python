# %%
import pandas as pd
from settings import project_settings

# Running project settings
project_settings()

# Read csv from gist

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

# create new column
cars.assign(mean_km_pr_liter=cars.mpg * 1.609344 / 3.78541178)

# create multiple columns
cars.assign(mean_km_pr_liter=cars.mpg * 1.609344 / 3.78541178,
            watts=cars.hp * 745.699872)
# create columns based on other created columns in one chain
cars.assign(mean_km_pr_liter=cars.mpg * 1.609344 / 3.78541178). \
    assign(mean_km_pr_100l=lambda cars: cars.mean_km_pr_liter * 100)

# create new column with lambda
cars.assign(mean_km_pr_liter=lambda x: x.mpg * 1.609344 / 3.78541178,
            mean=lambda x: x.hp * 1.609344 / 3.78541178)
