from googlesearch import search   
import requests
# to search 
def getLinks(query):
  links = []
  for link in search(query, tld='com', num=5, stop=5, pause=2):
      links.append(link) 
  return links


import urllib3
from bs4 import BeautifulSoup

# def getData(links):
#   data = []
#   for url in links:
#     http = urllib3.PoolManager()
#     response = http.request('GET', url)

#     #can't get url pdf file
#     soup = BeautifulSoup(response.data)

#     data.append(soup.body.get_text())
#   return data
def extract_text(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    return 'n'.join([text.get_text().strip() for text in soup.find_all('p')])

def getTitle(url):
  try:
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    #can't get url pdf file
    soup = BeautifulSoup(response.data)
    return soup.title.string
  except:
    return 'Page url'