# Join_DataFrames
#!/bin/python3

# import Matplotlib library
import matplotlib.pyplot as plt
import pandas as pd

# create <auto> DataFrame by reading the data file
auto = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv" , 
                  usecols = ['Make' ,
                              'Body Style' , 
                              'City mpg' ,
                              'Highway mpg',  
                              'Price'])
print('<auto> DataFrame')
print(auto)

# insert a new column <CarID> at the DataFrame <auto>
print()
column_name = "CarID"
first_column = auto_df.pop(column_name)
print(auto.head())
print()
# use the function insert() to insert the columns saved in the variable <first_column>
auto.insert(0,"CarID",first_column) 
print('auto with CarID at the first position')
print(auto)
print()

# remove some columns from <auto> DataFrame
del auto['Price'] # delete the column 'Price'
auto.pop('Body Style') # remove/pop the column 'Body Style' from the DataFrame <auto>
auto.drop(['City mpg', 'Highway mpg'] , inplace = True , axis = 1 )

# print create <country> DataFrame by reading the data file
country = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Car_Country.csv")
print('<country> DataFrame')
print(country)
print()