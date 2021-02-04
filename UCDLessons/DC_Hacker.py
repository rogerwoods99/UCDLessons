import numpy as np
x=np.random.rand()
print(x)

# The rand function is pseudo random. It starts with a SEED value and then creates
# random numbers. The same SEED gives the same random sequence.
# This ensures that the random series is reproducable by other people

#np.random.seed(123)

x=np.random.rand()
print(x)

coin=np.random.randint(0,7) # generate random num between 1 and 6
print(coin)

# create a list based on 10 coin tosses

outcomes=[]
for x in range(10):
    coin=np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)

# ======================================================
# create a random walk for 100 rolls of the dice
#====================================================

random_walk=[0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step=random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

#=====================================
# make sure that the result cannot go below 0 using the max function for dice <= 2
# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step= max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

#print(random_walk)

#======= and display this in a plot
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
plt.clf()

#=================================================
# Now show 10 walks on one graph

# initialize and populate all_walks
all_walks = []
for i in range(100) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
            # Implement clumsiness
        if np.random.rand() <= 0.001:  # add some randomness that go to zero 0.1% of time
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw=np.array(all_walks)

# Plot np_aw and show
#plt.plot(np_aw)
#plt.show()

# Clear the figure
#plt.clf()

# Transpose np_aw: np_aw_t

np_aw_t=np.transpose(np_aw)
# Plot np_aw_t and show

plt.plot(np_aw_t)
#plt.xscale('log')
plt.xlabel('Run no.')
plt.ylabel('Step position')
plt.title('Various trajectories')
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#plt.text(1550, 71, 'India')   # add text on graph at particular points
#plt.text(5700, 80, 'China')
#plt.grid(True)   # show grid lines
plt.show()

print(np_aw_t[-1].size)  # the size of the final row in the array
