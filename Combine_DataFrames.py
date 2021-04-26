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

# create subsets of the dataframe <auto_df>
auto1 = auto_df.iloc[:10]
print('auto1')
print(auto1)
print()

auto11 = auto_df.iloc[4:16]
print('auto11')
print(auto11)
print()

auto12 = auto_df.iloc[12:21]
print('auto12')
print(auto12)
print()
print('--------------------------------------')

print()
auto2 = auto_df.iloc[109:130]
print('auto2')
print(auto2)
print()

auto3 = auto_df.iloc[199:]
print('auto3')
print(auto3)
print()
print()





# ----------------------------------------------------------------
# combine/concatenate the dataframes auto1,auto2,auto3
print('combine/concatenate the dataframes auto1,auto2,auto3')
auto123 = pd.concat([auto1 , auto2 , auto3])
print('auto123')
print(auto123)
print()

print('associate specific keys with each of the combined dataframes')
auto123_keys = pd.concat([auto1 , auto2 , auto3] , keys =['auto1' , 'auto2' , 'auto3'])
print('auto123_keys')
print(auto123_keys)
print()
# ----------------------------------------------------------------



# combine/concatenate the dataframes auto1, auto11, auto12
print('combine/concatenate the dataframes auto1, auto11, auto12')
auto1s = pd.concat([auto1 , auto11 , auto12])
print("auto1s")
print(auto1s)

print('associate specific keys with each of the combined dataframes')
auto1s_keys = pd.concat([auto1 , auto11 , auto12] , keys = ['df_1' , 'df_11' , 'df_12'])
print('auto1s_keys')
print(auto1s_keys)
print()
print()

# remane the columns 
print('rename the columns')
print('auto3_col')
auto3_col = auto3.rename(columns = {"Make":"Manufacturer" , "City mpg":"Miliage City" , "Highway mpg":"Mileage Highway"})
print(auto3_col)
print()

# concatenate two dataframes(auto1 and auto3_col) with different columns names
print("! combine two dataframes(auto1 and auto11) with different columns names")
auto_dif_col = pd.concat([auto1 , auto3_col])
print(auto_dif_col)
print()
print()


# concatenate with axis=0
print('concatenate two dataframes(auto1, auto2) when  axis = 0')
auto_ax0 = pd.concat([auto1,auto2], axis=0) 
print('auto_ax0 dataframe, the result of concatenating with axis=0')
print(auto_ax0)
print()
print()

# concatenate with axis=1
print('concatenate two dataframes(auto1, auto2) when  axis = 1')
auto_ax1 = pd.concat([auto1,auto2] , axis=1)
print('auto_ax1 dataframe, the result of concatenating with axis=1')
print(auto_ax1)
print()
print()

# reset the indexes of the concatenated <auto123> dataframe
print('Reset the indexes of the concatenated <auto123> dataframe')
auto123.reset_index(drop = True, inplace = True)
print(auto123)








print('---------------------------------------------------------------------------------')
'''
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
'''