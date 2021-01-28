# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm Test')

# Import numpy

import numpy as np
import matplotlib.pyplot as plt

year=[1,2,3]
ht=[140,160,155]
plt.plot(year,ht)
plt.show()
# Create a numpy array from height_in: np_height_in
np_height_in = np.array([1,2])

# Print out np_height_in
print(np_height_in)

# Print out type of np_baseball (data type)
#print(type (np_height_in)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
