import pandas as pd

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

# sort using one condition (default = ascending)
cars.sort_values(by=["gear"], ascending=True)

# sort using multiple conditions
cars.sort_values(by=["gear", "hp"], ascending=[False, True])
