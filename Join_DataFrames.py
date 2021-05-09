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

# *******   create <price_df> DataFrame from the columns <CarID>,<Price> of <auto> DataFrame
print('<price> DataFrame')
price_df = auto[['CarID' , 'Price']].copy()
print(price_df)


# remove <Price> column from <auto> DataFrame
auto.pop('Price')
print(auto)

# now the DataFrames <auto> and <price_df> have the common column <CarID>
# join/merge these two DataFrames on the column <CarID>
auto_df = pd.merge(auto , price_df , how = 'left' ,on = 'CarID')
print(auto_df)
print(auto_df.shape)
print()

# ******* read the file <country> and create the dataframe <make_country>
country = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Car_Country.csv")
# have the values at the column 'Car Model' at lowercase
country['Car Model'] = country['Car Model'].str.lower()
print('<country> DataFrame')
print(country)
print()

# rename the column "Car Model" into "Make"
country.rename(columns ={'Car Model':'Make'} , inplace = True )
print(country)
print('****')
print()


# ---  LEFT JOIN  ---
print(' ---  LEFT JOIN  ---')
# merge/join the DataFrames <auto> and <country> on the key column <Car Make>
auto_country = pd.merge(auto_df , country , how = 'left' , on  = 'Make')
print('<auto_country> DataFrame')
print(auto_country)


# place the column <Country> after the column <Make> at the auto_country DataFrame
country_column = auto_country.pop('Country')
# insert the column to the third position
auto_country.insert( 2 , 'Country' , country_column)
print()
print(auto_country.head())
print()
print()

# read the file 'Continent.csv' into the dataframe <continent>
continent = pd.read_csv("E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Continent.csv")
print()
print('<continent> DataFrame')
print(continent)
print()

# merhe/join the dataframes <auto_country> and <continent>
auto_country_continent = pd.merge( auto_country , continent , how = 'left' , on = 'Country')
print('<auto_country_continent> DataFrame')
print(auto)

# place the column 'Continent' after the column 'Country'
continent_column = auto_country_continent.pop('Continent')
auto_country_continent.insert( 3 , 'Continent' , continent_column)
print(auto_country_continent.head())
print()
print('-----------------------------------')
print()
print()

# --- INNER JOIN ---
# drop non numeric values from <price_df> DataFrame
price_df = price_df[pd.to_numeric(price_df['Price'] , errors = 'coerce').  notna()]

print()
print(price_df.dtypes) # the column "Price" is object data type, but it should be the numeric/integer data type

price_df['Price'] = pd.to_numeric(price_df['Price'])
print(price_df.dtypes)
print()
print()

# sort the dataframe <price> the descending order by the column 'Price'
price_df.sort_values( by = ['Price']  , inplace = True , ascending = False)
print('sorted <price_df>')
print(price_df.head(10))
print('*******')



# create <price_10_top> DataFrame
price_10_top = price_df.head(10)
print('<price_10_top> DataFrame ')
print(price_10_top)
print()
print('lenght of <price_10_top> DataFrame : ' + str(len(price_10_top)) )

# inner join of the dataframes <auto> and <price_10_top> on the kay column 'CarID'
auto_10_top_price = pd.merge( price_10_top , auto , how = 'inner' , on = 'CarID')
print()
print('auto_10_top_price')
print(auto_10_top_price)
print()

# and one more inner join
auto_10_top = pd.merge( auto_10_top_price , country , how = 'left' , on  = 'Make')
print(auto_10_top)

# create the dataframe with 20 rows
auto_20 = auto.head(20)
print('auto_20')
print(auto_20)

# inner join
auto_10_20_inner_join = pd.merge(auto_10 , auto_20 , how = 'inner' , on = 'CarID')
print(auto_10_20_inner_join)
