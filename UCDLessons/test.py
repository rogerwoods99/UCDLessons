import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
np_baseball = np.array([1,2,3,4,5]) #,[45,56,34,45,56])
print(np_baseball[0])
print(a)
# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)