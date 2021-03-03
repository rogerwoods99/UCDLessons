import pandas as pd
import matplotlib.pyplot as plt

fig,ax=plt.subplots()
# load Seattle and Austin weather data
filename1= 'GBvideos.csv'
data = pd.read_csv(filename1)

x = data['channel_title'].head(5)
y1 = data['views'].head(5)
y2 = data['likes'].head(5)

ax.plot(x,y1)
ax.plot(x,y2)

plt.show()
