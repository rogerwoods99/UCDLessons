import numpy as np
filename = 'MNIST.txt'

# loadtxt is good for basic datasets, but not so good for datasets with mixed datatypes

# load a CSV file
data = np.loadtxt(filename, delimiter=',')

# load a TAB file
data = np.loadtxt(filename, delimiter='\t')

# data = np.loadtxt(filename, delimiter=',', skiprows=1)  # this will skip the first row
# this will skip the first row and select only the 1st and 3rd columns
# data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2])

# this will skip the first row and select only the 1st and 3rd columns and set the datatype to float
# data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float, usecols=[0,2])

data

print(data.shape[0])   # print number of rows in a NP array
print(data.shape[1])   # print number of columns in a NP array
