from googlesearch import search   

# to search 
def getLinks(query):
  links = []
  print(query)
  for j in search(query, num_results=10, lang="vi"): 
      links.append(j) 
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

def getTitle(url):
  http = urllib3.PoolManager()
  response = http.request('GET', url)

  #can't get url pdf file
  soup = BeautifulSoup(response.data)

  return soup.title.string