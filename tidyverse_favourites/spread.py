import pandas as pd
from utilities.settings import project_settings
import numpy as np

project_settings()

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/"
                   "b999fb4425b54c63cab088c0ce2c0d6ce961a563/"
                   "cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

summary = cars.groupby(['gear', 'vs'], as_index=False).agg(mean_mpg=("mpg", np.mean),
                                                           mean_hp=("hp", np.mean)
                                                           )

tidy_data = summary.melt(id_vars=['gear', 'vs'], value_vars=['mean_mpg', 'mean_hp'])

spread_data = tidy_data.pivot(values='value', index=['gear', 'vs'], columns=['variable']). \
    reset_index().rename_axis(
    None, axis=1)

print(spread_data)
