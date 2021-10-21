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

# Missing data functions: isna(), isnull(), notna(), notnull()

print("Missing data functions:")
print('-----------------------')
print(pd.isna(Reliefe_Funds_df), "\n")
print(pd.notna(Reliefe_Funds_df), "\n")

print(pd.isnull(Reliefe_Funds_df), "\n")
print(pd.notnull(Reliefe_Funds_df), "\n")


# Count the rows in the dataframe
print(Reliefe_Funds_df.index, "\n")
print('Number of rows in the dataframe:')
print(len(Reliefe_Funds_df), "\n")

print('-------------------------------')
print('Delete rows with missing values:')
# Delete rows with zero values, first replace the zero values with NaN
Reliefe_Funds_df['Provider Relief Fund'] = Reliefe_Funds_df['Provider Relief Fund'].replace(0,np.nan)
Reliefe_Funds_df['AAP'] = Reliefe_Funds_df['AAP'].replace(0,np.nan)

# now we can drop all NaN values from the dataframe
Reliefe_Funds_df.dropna(subset = ['Provider Relief Fund', 'AAP'], inplace = True)

print(Reliefe_Funds_df, "\n")

# Rename the columns
Reliefe_Funds_df.rename(columns = {"Provider Relief Fund":"Relief_Fund" , 
                                    "Provider Name":"Provider" ,
                                   "State / Territory":"State"} , inplace = True)
print('new columns:')
print(Reliefe_Funds_df.columns , "\n")
print(Reliefe_Funds_df.head(20) , "\n")
print('-----------------------------')



small_df = Reliefe_Funds_df.head(11)
print(small_df, "\n")
print('number of rows in small_df :')
print(len(small_df.index), "\n")

# insert a new column 'ID'
small_df.insert(0, "ID" , [10001,10002,10003,10004,10005,
                            10006,10007,10008,10009,10010,10011])
print('small_df:')
print(small_df , "\n")


# delete columns in DataFrame
small_df_A = small_df.drop(columns = ['Relief_Fund','State','AAP'])
print('small-df_A', "\n")
print(small_df_A , "\n")

small_df_B = small_df.drop(columns = ['Provider','State','AAP'])
print('small_df_B', "\n")
print(small_df_B , "\n")

# delete rows in DataFrame
small_df_C = small_df_A.drop( labels = [4,5,7,18,25,41] , axis = 0)
print("small_df_C :")
print(small_df_C, "\n")

small_df_D = small_df_B.drop( labels = [25,41,43] , axis = 0)
print("small_df_D :")
print(small_df_D , "\n")


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~' , "\n")
# join the DataFrames <small_df_A> and <small_df_B> on index
print('Join twe DataFrames, the output:')
join_df = pd.merge(small_df_A , small_df_B , how = 'left' , on = 'ID')
print(join_df , "\n")

# left join the DataFrames <small_df_C> and <small_df_B> on index
print('Left join on the DataFrames:')
join_df_left = pd.merge(small_df_C, small_df_B , how = 'left', on = 'ID')
print(join_df_left, "\n")

# right join the DataFrames <small_df_C> and <small_df_D>
print('Right join on the DataFrames: ')
join_df_right = pd.merge(small_df_A, small_df_C, how = 'right' , on = 'ID')
print(join_df_right , "\n")
print('-----------------------------------------------------------------------')
# insert a new column
print('small_df :') 
print(small_df, "\n")
print('Insert a new column:')
small_df.insert(0 , "Type", 
                                [1,1,1,1,1,
                                1,1,1,1,1,
                                1], allow_duplicates = True)
print(small_df)


'''
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

print("-- dataframe Reliefe_funds_17_end :")
Reliefe_Funds_df_17_end = Reliefe_Funds_df.tail(17)
print(Reliefe_Funds_df_17_end)
'''
