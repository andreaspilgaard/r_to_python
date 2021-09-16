import seaborn as sns
import pandas as pd
from utilities.settings import project_settings

project_settings()

cars = pd.read_csv("https://gist.githubusercontent.com/noamross/"
                   "e5d3e859aa0c794be10b/raw/b999fb4425b54c63cab088c0ce2c0d6ce961a563/cars.csv", index_col=0)

# reset_index sets index column as first column - default name is index
cars = cars.reset_index().rename(columns={"index": "model"})

sns.relplot(data=cars, x="mpg", y="hp", hue="vs", kind="scatter")
