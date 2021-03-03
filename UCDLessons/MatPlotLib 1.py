import pandas as pd
import matplotlib.pyplot as plt

# load Seattle and Austin weather data
filename1= 'austin_weather2014.csv'
austin = pd.read_csv(filename1)

filename2= 'seattle-weather 2014.csv'
seattle = pd.read_csv(filename2)
print(austin.columns)
print(seattle)

# define an array of 1 column and 2 rows and share the y axis limits
fig, ax = plt.subplots(2,1,sharey=True)

ax[0].plot(seattle["date"],seattle["temp_maxF"],marker="o",linestyle="--")
ax[1].plot(austin["date"],austin["TempHighF"],marker="^",linestyle="dotted")
ax[1].set_xlabel("Day of year")
ax[0].set_ylabel("Max Temperature (F)")
ax[1].set_ylabel("Max Temperature (F)")
ax[0].set_title("Max Temps in Austin and Seattle")
#plt.show()

######################
# repeat the above but this time use the indexing function

# load Seattle and Austin weather data
filename1= 'austin_weather2014.csv'
austin_id = pd.read_csv(filename1,parse_dates=["date"],index_col=["date"])

filename2= 'seattle-weather 2014.csv'
seattle_id = pd.read_csv(filename2,parse_dates=["date"],index_col=["date"])
print(austin.columns)
print(seattle_id)

fig, ax = plt.subplots()

#seattleJan=seattle_id["01-01-2014":"31-01-2014"]

# showthe max temp and precipitation as two lines on the same graph
ax.plot(seattle_id.index,seattle_id["temp_maxF"], color="r")
ax.set_xlabel('Time')
ax.set_ylabel("Max Temp", color="r")
ax.tick_params("y",colors="g")
ax.tick_params("x",colors="yellow")
ax2=ax.twinx()
ax2.plot(seattle_id.index,seattle_id["precipitation"], color="b")
ax2.set_ylabel("Precip", color="b")
ax2.tick_params("y",colors="orange")

# do the same as above but using the plot_timeseries function

def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y,color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel,color=color)
    axes.tick_params("y",color=color)

fig, ax = plt.subplots()

# showthe max temp and precipitation as two lines on the same graph
plot_timeseries(ax,seattle_id.index, seattle_id["temp_maxF"],"blue","Time","Max Temp")
ax2=ax.twinx()
plot_timeseries(ax2,seattle_id.index, seattle_id["precipitation"],"red","Time","Precipitation")
ax.annotate(">24 deg", xy=[seattle_id.TimeStamp("2014-02-02"),24])

plt.show()