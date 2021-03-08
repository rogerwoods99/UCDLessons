import pandas as pd
import matplotlib.pyplot as plt

# load Rio 2016 medals
filename1= 'Rio2016Short.csv'
Rio = pd.read_csv(filename1, index_col=0)
print(Rio)

##
# using stacked bar chart so that results on the same bar
# note that the position of the higher bars is the sum of the lower bars
fig, ax = plt.subplots()

ax.bar(Rio.index, Rio["Gold"], label="Gold")
ax.bar(Rio.index, Rio["Silver"], bottom=Rio["Gold"], label= "Silver")
ax.bar(Rio.index, Rio["Bronze"], bottom=Rio["Gold"] + Rio["Silver"], label= "Bronze")
ax.set_xticklabels(Rio.index, rotation=45)
ax.set_ylabel("Number of medals")
ax.legend()
plt.show()

############################################
# now look at the athletes using histograms
#####################################
filename2= 'Rio2016Athletes.csv'
Athletes = pd.read_csv(filename2)
print(Athletes)

# sort into Rowing and Gymnastics
gymnastics=Athletes[Athletes["sport"]=="gymnastics"]
print(gymnastics)
rowing=Athletes[Athletes["sport"]=="rowing"]
print(rowing["height"])

fig, ax = plt.subplots()
ax.hist(rowing["height"], label="Rowing", bins=20)  # sets the number of bins
ax.hist(gymnastics["height"], label="Gymnastics", bins=20)
ax.set_xlabel("Height (m)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()

## show data with fixed boundaries and using the histtype function to "step" so that not coloured in
fig, ax = plt.subplots()
ax.hist(rowing["height"], label="Rowing", bins=[1.5,1.6,1.7,1.8,1.9,2,2.1], histtype="step")  # sets the boundaries of the bins
ax.hist(gymnastics["height"], label="Gymnastics", bins=[1.3,1.4,1.5,1.6,1.7,1.8,1.9],histtype="step")
ax.set_xlabel("Height (m)")
ax.set_ylabel("# of observations")
ax.legend()
plt.show()

#####################################################
# add error bars to bar chart
#####################################################

fig, ax = plt.subplots()

ax.bar("Rowing", rowing["height"].mean(), yerr=rowing["height"].std())
ax.bar("Gymnastics", gymnastics["height"].mean(), yerr=gymnastics["height"].std())
ax.set_ylabel("Height (m)")
plt.show()

################################################
# boxplots. This displays the mean, interquartile range, and any outlying data values
#################################################

fig, ax=plt.subplots()

ax.boxplot([rowing["height"], gymnastics["height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (m)")
plt.show()