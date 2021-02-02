# This looks at the use of square brackets for import data and print out a subset
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

#==================================================================
#==================================================================

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
print("")

#==================================================================
#==================================================================
print(cars.loc['RU'])  # this will provide data in rows
print(cars.iloc[4])
print(cars.loc[['RU']])  # this in a single row
print(cars.iloc[[4]])
print(cars.loc[['RU','AUS']])  # this returns info for 2 rows
print(cars.iloc[[4,1]])
print()
print(cars.loc['IN','cars_per_cap'])
print(cars.loc[['IN','RU'],'cars_per_cap'])
print(cars.iloc[[3,4],0])

#================================================================
#==================================================================


# Print out drives_right value of Morocco

print(cars.loc['MOR', 'drives_right'])
# Print sub-DataFrame of Russia and Morocco and drive right value
print(cars.loc[['RU','MOR'],['country','drives_right']])

# Print out drives_right column as Series for all countries

print(cars.loc[:,'drives_right'])
# Print out drives_right column as DataFrame

print(cars.iloc[:,[2]])
# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:,['cars_per_cap','drives_right']])