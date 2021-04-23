# Python Pandas Combine DataFrames
#!/bin/python3

# import Matplotlib library
import matplotlib.pyplot as plt
import pandas as pd

print('Here I will combine dataframes')

# read imported auto datsets
print('auto_df1')
auto_df1 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_1.csv")
print(auto_df1)
print()

print('auto_df2')
auto_df2 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_2.csv")
print(auto_df2)
print()

print('auto_df3')
auto_df3 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_3.csv")
print(auto_df3)
print()

print('auto_df4')
auto_df4 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_4.csv")
print(auto_df4)
print()

print('auto_df5')
auto_df5 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_5.csv")
print(auto_df5)
print()

print('auto_df')
auto_df = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv" , 
                                 usecols = [
                                    'Make' ,
                                    'Body Style' , 
                                    'City mpg' ,
                                    'Highway mpg',  
                                    'Price'])
print(auto_df.head())
print()

# create a new column at the dataframe auto_df
auto_df['CarID'] = range(1,len(auto_df) + 1,1)
print()
print('auto_df with new column CarID')
print(auto_df.head())
print()


# move the new column at auto_df to the first position
# first: remove the new column by unsing the function pop() and save this column in a variable
column_name = "CarID"
first_column = auto_df.pop(column_name)
print(auto_df.head())
print()
# use the function insert() to insert the columns saved in the variable <first_column>
auto_df.insert(0,"CarID",first_column)
print('auto_df with CarID at the first position')
print(auto_df)



print('---------------------------------------------------------------------------------')

# read Pennsylvania Briges datasets
print('brige_df1')
brige_df1 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Pennsylvania_Briges\Briges_1.csv")
print(brige_df1)
print()

print('brige_df2')
brige_df2 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Pennsylvania_Briges\Briges_2.csv")
print(brige_df2)
print()

print('brige_df3')
brige_df3 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Pennsylvania_Briges\Briges_3.csv")
print(brige_df3)
print()

print('brige_df4')
brige_df4 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Pennsylvania_Briges\Briges_4.csv")
print(brige_df4)
print()

print('brige_df5')
brige_df5 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Pennsylvania_Briges\Briges_5.csv")
print(brige_df5)
print()


print('-------------------------------------------------------------------------------------')

# *** Concatenating DataFrames
print('Concatenating DataFrames')
auto_result = pd.concat([auto_df1 , auto_df2 , auto_df3])
print('auto_result')
print(auto_result)