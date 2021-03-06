
####IMPORT NECESSARY LIBRARY####
from bs4 import BeautifulSoup as bs
import requests
import csv


####PREPARATION OF LNIKS
page_urls=[]
for i in range(1,11):
  page=i
  base_url='https://hotels.ng/hotels-in-lagos/'+str(page)
  page_urls.append(base_url)


links=[]

def get_links(url,links):
  html=requests.get(url).text
  soup=bs(html,'html.parser')

  header=soup.find_all('div',class_='listing-hotels-details-property')

  for i in header:
    try:
      link=i.a['href']
      links.append(link)
    except:
      pass

for i in page_urls:
  get_links(i,links)


#####SCRAPING OF HOTELS AND OTHER NECESSARY INFO####
db=[]
def extract(link,db):
  html=requests.get(link).text
  soup=bs(html,'html.parser')

  try:
      rating=soup.find('div',class_='sph-reviews-overview-rating header-section bkgrnd-excellent').text
  except:
      rating=''

  try:
      name=soup.find('h1',class_='sph-header-name').text
  except:
      name=''
  
  try:
    price=soup.find('p', class_='sph-room-price sph-range').text
  except:
      price=''    

  data={
      'name':name,
      'rating':rating,
      'price': price
  }
  db.append(data)


for i in links:
    extract(i,db)


####TO SAVE DATA TO CSV####
field=['name','price','rating']

with open ('hotels_BS.csv', 'w') as csvfile:
  writer=csv.DictWriter(csvfile, fieldnames=field)
  writer.writeheader()
  writer.writerows(db)
