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

#####################################################
#  Beautiful soup part 2

print('#################################################')
print('Beautiful Soup part 2')
print('#################################################')
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, features="html.parser")
print(soup.title)    # print the title of the document
#guido_text=soup.get_text()
#print(guido_text)  # print the text of the document
a_tags =soup.find_all("a")   # find
for link in a_tags:    # loop through and print the links
    print(link.get('href'))
