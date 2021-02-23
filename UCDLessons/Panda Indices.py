import pandas as pd
filename= 'temperatures.csv'
temperatures = pd.read_csv(filename)
print(temperatures.head())
# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
#print(temperatures_ind.reset_index(drop=True))

cities = ["Moscow", "Saint Petersburgh"]

# Subset temperatures using square brackets - index is purely numbers
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[] - use .loc where an index uses the city name
print(temperatures_ind.loc[cities])

#############################################
#############################################
# now for multiple index list
# Index temperatures by country & city

temperatures_ind1  = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore

rows_to_keep = [("Russia","Saint Petersburgh"),("Ireland","Dublin")]

# Subset for rows to keep

print(temperatures_ind1.loc[rows_to_keep])

#############################################
############################################
# Now sort these

# Sort temperatures_ind by index values, ie country then city
print(temperatures_ind1.sort_index())

# Sort temperatures_ind by index values at the city level. Sort by the city
print(temperatures_ind1.sort_index(level=["city"]))

# Sort temperatures_ind by country then descending city
print(temperatures_ind1.sort_index(level=["country","city"],ascending=[True,False]))

#################################################
###################################################
# now slice with loc and iloc

print("-========================")
temp_ind=temperatures_ind1.sort_index()
print(temp_ind)

# Subset rows from Pakistan to Russia
print(temp_ind.loc["Ireland":"Scotland"])

# Subset rows from Ireland, Dublin to Wales, Cardiff
print(temp_ind.loc[("Ireland","Dublin"):("Wales","Cardiff")])

#########################
# now from rows and columns
# Subset rows from India, Hyderabad to Iraq, Baghdad
print("-========================")
print(temp_ind.loc[("Ireland","Dublin"):("Wales","Cardiff")])

# Subset columns from date to avg_temp_c
print(temp_ind.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temp_ind.loc[("Ireland","Dublin"):("Wales","Cardiff"),"date":"avg_temp_c"])

#==========================================================
#############################################################
# sort by date

print("Date Sort ===============================")
print(temperatures)
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2000-01-01") & (temperatures["date"] <= "2000-12-31")]
print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2000":"2001"])

# Use .loc[] to subset temperatures_ind for rows from Jan 2000 to 1st Feb 2001
print(temperatures_ind.loc["2000-01":"2000-02-01"])