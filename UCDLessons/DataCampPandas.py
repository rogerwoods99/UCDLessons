# Create DataFrame from 3 lists

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict

my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars. Note that rows are labelled 0, 1, 2 etc. not that intuitive
print(cars)

# Definition of row_labels to replace row labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars

cars.index=row_labels
# Print cars again
print(cars)

#======================================================================
#======================================================================

# import data from CSV file is much better. CSV file has to be in the same directory
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv')

# Print out cars
print(cars)

#======================================================================
#======================================================================

# import data from CSV file is much better. This time assign the first column as he index
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)