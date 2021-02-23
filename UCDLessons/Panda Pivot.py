# Add a year column to temperatures
import pandas as pd

filename= 'temperatures.csv'
temperatures = pd.read_csv(filename)
print(temperatures)
temperatures['date'] = pd.to_datetime(temperatures["date"])
temperatures["year"]=temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c",index=["country","city"],columns="year")

# See the result
print(temp_by_country_city_vs_year)

####################################
#print max and min average temps per year

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])