import json
with open ('test JSON.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json_data)

for key, value in json_data.items():
    print(key + ':', value)

for k in json_data.keys():
    print(k + ': ', json_data[k])

print('###########################')
# get movie data using API
import requests
#url = 'http://www.omdbapi.com/?apikey=cc7d7678&t=hackers'  # need API key for this
url = 'http://www.omdbapi.com/?apikey=cc7d7678&t=social+network'
r = requests.get(url)
print(r.text)    # prints out the text that has been returned
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

print('###################################')
print('###################################')

# now the same for WIKI, but print out part of the page
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()
print(json_data)
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)