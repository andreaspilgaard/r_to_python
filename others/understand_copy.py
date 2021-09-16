import pandas as pd

df = pd.DataFrame({'x': [1, 2]})

# This way of copying a dataframe causes df and df2 to refer the same dataframe object.
# This means that changing one of the two dataframes will cause the other frame to change as well.
df2 = df

df2["x"] = df2["x"] - 2

# Notice that both dataframes are the same even though we only made changes to df2.
print(df)
print(df2)

# Using copy to mitigate this issue.

df = pd.DataFrame({'x': [1, 2]})

df2 = df.copy()

df2["x"] = df2["x"] - 2

# Notice that the dataframes are now different.
print(df)
print(df2)

# What about assign?
df = pd.DataFrame({'x': [1, 2]})

df2 = df.assign(
    x=lambda x: x.x - 2
)

# Notice that assign automatically creates a copy of the dataframe leaving df unchanged.
print(df)
print(df2)

# What about assign - with inplace = True?
df = pd.DataFrame({'x': [1, 2]})

df2 = df.assign(
    x=lambda x: x.x - 2
)

# Notice that assign automatically creates a copy of the dataframe leaving df unchanged.
print(df)
print(df2)
