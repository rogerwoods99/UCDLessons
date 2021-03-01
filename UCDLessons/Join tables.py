import pandas as pd
import numpy as np
wards=pd.read_csv("Ward_Offices.csv")
#print(wards.head())
#print(wards.shape)

census=pd.read_csv("Ward_Census.csv")
#print(census.head())

# this is a one to one relationship as only one WARD record per dataframe
wards_census = wards.merge(census, on="Ward", suffixes=["_ward","_census"])
#print(wards.columns)
#print(census.columns)
#print(wards_census.columns)

##########################################
## merge Chicago data tables

# ridership example of how to set the dtype

cal = pd.read_csv("cal.txt")
ridership = pd.read_csv("ridership.txt",dtype={"station_id":object,"year":np.int64,"month":np.int64,"day":np.int64,"rides":np.int64})
stations = pd.read_csv("stations.txt",dtype={"station_id":object,"station_name":str,"location":str})

ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
                    .merge(stations, on='station_id')

print(ridership_cal_stations)

#################################################
## now merge using LEFT JOIN
## all rows from left table will be shown. Any data from right table with same station_id is included
## If no data then we get NaN. If there are multiple rows in the right table, then multiple rows will be
## created in the resulting table
###########################################

stations_new=stations.merge(ridership, on="station_id", how="left")
print(stations_new)

#################################################
## now merge using RIGHT JOIN
## all rows from right table will be shown. Any data from left table with same station_id is included
## If no data then we get NaN. If there are multiple rows in the left table, then multiple rows will be
## created in the resulting table
## Also show that can do this with different column names
###########################################

ridership_r = pd.read_csv("ridership_right.txt",dtype={"id":object,"year":np.int64,"month":np.int64,"day":np.int64,"rides":np.int64})
stations_r = pd.read_csv("stations_right.txt",dtype={"station_id":object,"station_name":str,"location":str})

stations_new_r=ridership_r.merge(stations_r,how="right",left_on="id", right_on="station_id")
print(stations_new_r)

#######################
# this code uses an index to find null values. It has been xed out as won't work as there is no dataset
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes

#iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                #     how="outer",
                              #       on="id",
                              #       suffixes=["_1","_2"])

# Create an index that returns true if name_1 or name_2 are null
#m = ((iron_1_and_2['name_1'].isnull()) |
    # (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
#print(iron_1_and_2[m].head())

#############################
# Join to oneself

sequel = pd.read_csv("sequel.txt")
orig_sequels=sequel.merge(sequel, left_on="sequel", right_on="id",suffixes=("_org","_seq"))
print(orig_sequels)

################################
# more code about selecting

# Merge sequels and financials on index id
#sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
#orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                          #   right_on='id', right_index=True,
                          #   suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
#orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff NOTE THIS CODE####################################
#titles_diff = orig_seq[['title_org','title_seq','diff']]