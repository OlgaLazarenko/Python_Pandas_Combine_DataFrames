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
print(auto.head())
print()


# generate a list of number of a specific range(for CarID column)
def create_CarID_list(firstID , lastID):
    return list(range(firstID , lastID))


N1 = 10001
N2 = (len(auto)+1)+10000
create_CarID_list(N1,N2) # call the function 
print()
print('The values for the column CarID:')
print(create_CarID_list(N1,N2))
print()

CarID_list = create_CarID_list(N1,N2) # these values will be instered as 'CarID' values into the auto DataFrame
# insert a new column <CarID> at the DataFrame <auto> at the first position
auto.insert( 0 , "CarID" , CarID_list)
print(auto)
print()

# create <price_df> DataFrame from the columns <CarID>,<Price> of <auto> DataFrame
print('<price> DataFrame')
price_df = auto[['CarID' , 'Price']].copy()
print(price_df)


print()
'''
column_name = 'CarID'
first_column = auto.pop(column_name)
print(auto.head())
print()
# use the function insert() to insert the columns saved in the variable <first_column>
auto.insert(0,"CarID",first_column) 
print('auto with CarID at the first position')
print(auto)
print()
'''

# remove some columns from <auto> DataFrame
del auto['Price'] # delete the column 'Price'
auto.pop('Body Style') # remove/pop the column 'Body Style' from the DataFrame <auto>
auto.drop(['City mpg', 'Highway mpg'] , inplace = True , axis = 1 )
print('<auto> DataFrame')
print(auto.head())

# print create <country> DataFrame by reading the data file
country = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Car_Country.csv")
print('<country> DataFrame')
# have the values at the column 'Car Model' at lowercase
country['Car Model'] = country['Car Model'].str.lower()
print('<country> DataFrame')
print(country)
print()