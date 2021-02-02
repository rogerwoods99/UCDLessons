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
