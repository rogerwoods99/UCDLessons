area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")

if(area>9 and area <11):
    print("between 9 and 11")

#===============================
import numpy as np


# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area>15:
    print("big place!")

    # Import cars data
import pandas as pd

cars = pd.read_csv('cars.txt', index_col=0)

# Extract drives_right column as Series: dr

dr = cars['drives_right']

# Use dr to subset cars: sel

sel = cars[dr]
# Print sel
print(sel)

# you can put the code into one for simplicity

sel = cars[cars['drives_right']]
# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
import numpy as np
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)

#=================================================================
#=================================================================


# WHILE LOOPS

error = 50.0
while error > 1 :
    error = error / 4
    print(error)

    # Initialize offset

offset = 8
    # Code the while loop

while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

# =================================================================
# =================================================================

# FOR LOOPS
print('')
print('FOR LOOPS')
print("")
# areas list. Print each item separately
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for x in areas:
    print(x)

# NOw enumerate with the index position

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print('room ' + str(index) + ": " + str(a) )

# use the house list to print information from a list
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# print(house[1][0])
for index, a in enumerate(house):
    print('the ' + house[index][0] + ' is ' + str(house[index][1]) + ' sqm')

# =================================================================
# =================================================================

# FOR LOOPS in Dictionaries
# to loop over all values use "for key, val in my_dict.items()"

# FOR LOOPS in 2D Numpy arrays
# to loop over all values use "for val in np.nditer(my_array)"

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'austria':'vienna' }
print('')
print('FOR LOOPS IN DICTIONARIES')
print("")

world={"afghanistan":30.55,
       "albania":2.77,
       "algeria":39.21}
print(world)

np_height=np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

#  DICTIONARIES
# Iterate over europe to print name of country and its capital
for key, value in europe.items():
    print("the capital of " + key + " is " + str(value))

# For loop over np_height
for x in np_height:
    print(str(x) + " m")

np_baseball = np.array([[1,2,3,4,5],[45,56,34,45,56]])


# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

# =================================================================
# =================================================================

# FOR LOOPS in Pandas, we need th iterrows function

import pandas as pd

brics=pd.read_csv("brics.txt",index_col=0)

# print each row as set of data. This includes all data in the dataset
for lab, row in brics.iterrows():
    print(lab)
    print(row)

# print only the capital
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])

# create a function to add a new column with the length of the country name
#  this will happen on each iteration and is not the most efficient way of doing things

for lab, row in brics.iterrows():
    brics.loc[lab,"name_length"]=len(row["country"])
print(brics)

# create a function to add a new column with a capitalized version of the country name
#  this will happen on each iteration and is not the most efficient way of doing things
# need to use the str.upper command

for lab, row in brics.iterrows():
    brics.loc[lab,"COUNTRY"]=str.upper(row["country"])
print(brics)

# can do the above with the "apply" function which doesn't require a loop
brics["name_length"] = brics["country"].apply(len)
print(brics)
