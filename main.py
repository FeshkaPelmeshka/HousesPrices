# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import numpy as np
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100
df = pd.read_csv('/Users/fesha/PycharmProjects/HousesPrices/house-prices-advanced-regression-techniques/train.csv')

# print(df.isna().sum().sort_values(ascending=False))
# print(df.head())
# What is the shape of your data i.e. number of rows and columns?
print("--------------------------------Shape of DF--------------------------------")
print(df.shape)
# How many of the columns (or features) are numerical and how many are categorical?
print("--------------------------------Data Types--------------------------------")
data_types_dic = {dtype: len(columns) for dtype, columns in df.columns.to_series().groupby(df.dtypes).groups.items()}
print(data_types_dic)
# possible_categories = [col for col in df.columns if df[col].nunique() < 10]
# print("Possibly categories: {}".format(len(possible_categories)))

# For the numerical columns, what does the distributions look like?
print("--------------------------------Distributions--------------------------------")

# What is the name of the column to be predicted?
# How are the various attributes correlated to the outcome variable?
# For the numerical columns, how many missing values are there for each column?
# For the categorical columns, how many missing values are there for each column?
# What visualizations can you use to highlight outliers in the data?


