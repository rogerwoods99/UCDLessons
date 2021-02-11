from urllib.request import urlopen, Request
url = "https://www.wikipedia.org"
request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()

#####################################################
# GET requests package
import requests
url = "https://www.wikipedia.org"
r = requests.get(url)
text = r.text
print(text)

#####################################################
#  Beautiful soup
from bs4 import BeautifulSoup
import requests
url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html.parser")
print(soup.prettify())