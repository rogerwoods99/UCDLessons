import numpy as np
filename = 'titanic.csv'

data = np.genfromtxt(filename, delimiter=',', names=True, dtype=None)
print(np.shape(data))
print(data[1])

# Now use the recfromcsv format which assumes delimiter=,, names=True and dtype=None
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])