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

#===========================================================
#===========================================================

# add 2 new countries to the capitals list for Europe

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy']='rome'

# Print out italy in europe. This verifies that Italy is in the list
print('italy' in europe)

# Add poland to europe
europe["poland"]='warsaw'

# Print europe
print(europe)

#===========================================================
#===========================================================

# add and edit items in a dictionary

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany

europe.update({'germany':'berlin'})

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

#===========================================================
#===========================================================

# this is about dictionaries within dictionaries

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data={'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy']=data

# Print europe
print(europe)
