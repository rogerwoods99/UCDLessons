import json
import requests
import pandas as pd

# get Golf World ranking from https://developer.sportradar.com/docs/read/golf/Golf_v2#official-world-golf-ranking

url = 'https://api.sportradar.us/golf-t2/players/wgr/2019/rankings.json?api_key=t36r4j5286dv8utdbc4r8ufb'
r = requests.get(url)
print(r.text)    # prints out the text that has been returned
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

# determine the key of the players (players)
# convert the data to a dataframe

df=pd.json_normalize(json_data["players"])
print(df.columns)
print(df)

# save json file to HDD for future analysis and to minimise calling too many APIs

with open("jsonGolfOut.txt","w") as outfile:
    json.dump(json_data["players"], outfile)


