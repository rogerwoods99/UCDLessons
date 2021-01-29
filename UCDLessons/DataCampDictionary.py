# find the capital based on index of the country, a slow method
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger

ind_ger=countries.index("germany")
# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

#===========================================================
#===========================================================

# A dictionary has been defined. Find values within it
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe

print(europe.keys())
# Print out value that belongs to key 'norway'
print(europe['norway'])