import pickle

# the first few lines create a Pickle file
# take user input to take the amount of data
number_of_data = int(input('Enter the number of data : '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# open a file, where you ant to store the data
file = open('important.pkl', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()

# now open this file and view contents

with open('important.pkl', 'rb') as file:  # read only and binary
    data = pickle.load(file)
print(data)
print(type(data))   # the type of the data