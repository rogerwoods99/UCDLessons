import matplotlib.pyplot as plt
import pandas as pd
filename= 'avocados.txt'
data = pd.read_csv(filename)
print(data.head())
print(data.isna().any())
nb_sold_by_size = data.groupby("size")["TotalVolume"].sum()
nb_sold_by_size.plot(kind="bar")
plt.show()

# now plot by size and region
nb_sold_by_size2 = data.groupby(["size","region"])["TotalVolume"].sum()
nb_sold_by_size2.plot(x="Date", y="TotalVolume", kind="line")
plt.show()

##################
# example of grouping and aggregating
# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'],
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant","account","pop_2010"],
                                             ascending=[False,True,True])
