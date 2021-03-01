import pandas as pd
import numpy as pd
import matplotlib.pyplot as plt

filename= 'winequality-red.csv'
data = pd.read_csv(filename)
print(data.head())
data_array=data.values   # get the corresponding numpy array
print(data_array[1])

# Assign the filename: file
file = 'digits.txt'

# Read the first 5 rows of the file into a DataFrame: data, with no header
data=pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array=data.values
print(data_array)
# Print the datatype of data_array to the shell
print(type(data_array))

# Import corrupted Titanic file and apply extra functions of read_csv

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='NA NaN')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

#  example of how to set the dtype for a particular column if there are issues with merging tables

cal = pd.read_csv("cal.txt")
ridership = pd.read_csv("ridership.txt",dtype={"station_id":object,"year":np.int64,"month":np.int64,"day":np.int64,"rides":np.int64})
