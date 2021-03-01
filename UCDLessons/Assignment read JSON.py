import json
import requests
import pandas as pd

# open the JSON file that I saved in Assignment.py file
with open("jsonGolfOut.txt") as json_file:
    json_data = json.load(json_file)

# get Golf World ranking from https://developer.sportradar.com/docs/read/golf/Golf_v2#official-world-golf-ranking


# determine the key of the players (players)

# convert the data to a dataframe

df=pd.json_normalize(json_data)
print(df.columns)
print(df)

# save json file to HDD for future analysis and to minimise calling too many APIs





