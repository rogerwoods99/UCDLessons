import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

height=[62,64,69,75,66,68,65,71,76,73]
weight=[120,136,148,175,137,165,154,172,200,187]


######################
# scatter plot

#sns.scatterplot(x=height, y=weight)
#plt.show()

###############################
# count plot

gender=["Female","Female","Female","Female","Male","Male","Male","Male","Male","Male"]
#sns.countplot(y=gender)
#plt.show()

################################
# adding third variable, hue
hue_colours={"Yes":"black","No":"red"}   # sets the colours of Yes and NO
                                        # can use hex code for colour #EF0000 for example
tips=sns.load_dataset("tips")
#print(tips.head())
#sns.scatterplot(x="total_bill", y="tip", data=tips,
#                hue="smoker", hue_order=["No","Yes"],
#                palette=hue_colours)
#plt.show()

sns.countplot(x="smoker", data=tips, hue="sex")  # shows data beside each other
plt.show()
