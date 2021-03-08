import json
import requests
import pandas as pd

# get Golf World ranking from https://developer.sportradar.com/docs/read/golf/Golf_v2#official-world-golf-ranking

url = 'https://services6.arcgis.com/uWTLlTypaM5QTKd2/arcgis/rest/services/Administrative_Areas_OSi_National_Statutory_Boundaries_Ungeneralised/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
r = requests.get(url)
#print(r.text)    # prints out the text that has been returned
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

# determine the key of the players (players)
# convert the data to a dataframe

df=pd.json_normalize(json_data["players"])
#print(df.columns)
#print(df)

# save json file to HDD for future analysis and to minimise calling too many APIs

#with open("jsonPlayerProfile2014.txt","w") as outfile:
#    json.dump(json_data["players"], outfile)


