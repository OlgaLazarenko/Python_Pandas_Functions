# Dataframe index
#!/bin/python3


import pandas as pd
import numpy as np
import random

print()

print("Python Pandas DataFrame Functions" , "\n\n")
print("Read csv file", "\n")

Reliefe_Funds_df = pd.read_csv('E:\_Python_Projects_Data\Provider_Relief_Fund\Funds.csv')
print(Reliefe_Funds_df.head(), "\n")

print('dataframe index:')
print(Reliefe_Funds_df.index , "\n")

# set the index stars from 100 with the step=1
print('dataframe columns:')
print(Reliefe_Funds_df.columns , "\n")

print('dataframe data types:')
print(Reliefe_Funds_df.dtypes, "\n")

print('dataframe info:')
print(Reliefe_Funds_df, "\n")

print('Is the dataframe empty ?')
print(Reliefe_Funds_df.empty , "\n")

print('Print the first five rows of the dataframe:')
print(Reliefe_Funds_df.head(), "\n")


print('create new dataframes as  subsets of the initial dataframe:')
print("-- dataframe Reliefe_Funds_df_5 : ")
Reliefe_Funds_df_5 = Reliefe_Funds_df.head()
print(Reliefe_Funds_df_5, "\n")

print("-- dataframe Reliefe_Funds_df_12 :")
Reliefe_Funds_df_12 = Reliefe_Funds_df.head(12)
print(Reliefe_Funds_df_12)

