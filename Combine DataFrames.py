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

auto_df4 = pd.read_csv("E:\_Python_Projects_Data\Combine_DataSets\Imported_Autos\Auto_DataSet_4.csv")
print(auto_df4)
print()
