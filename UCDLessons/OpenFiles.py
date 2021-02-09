# file closes when out of the with statment. Best practice

with open('random text file.txt', 'r') as file:
    print(file.read())

# Shell commands in python

# ! ls - lists all files in a directory

# Open a file: file
file = open("moby_dick.txt", "r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

# Read & print the first 3 lines
with open('moby_dick.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())