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

# filter using logical operaters
cars.query("mpg > 20 & hp > 100")

cars.query("mpg > 24 | hp > 240")

cars.query("gear in (3, 4)")

# filter using regex
cars.query("model.str.contains('Maz')", engine='python')

# call variable within query
selected_gears=[1, 2, 3]
cars.query("gear in @selected_gears")



