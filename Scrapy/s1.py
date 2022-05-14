from gc import callbacks
from pickle import TRUE
import scrapy


## Boolean which is used to limit number of hotels scraped to 100.
b=TRUE


## creation of the spider

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'links'
    
    allowed_domains = ['https://hotels.ng/']

## Boolean effect: if the b==TRUE only 10 pages each containing 10 hotels (100 hotels total) are scraped. 
    start_urls=[]
    if b==TRUE:
        pages = list(range(1,11))
        for i in range(len(pages)):
            start_urls.append('https://hotels.ng/hotels-in-lagos/' + str(pages[i]))
    else: 
        pages = list(range(1,333))
        for i in range(len(pages)):
            start_urls.append('https://hotels.ng/hotels-in-lagos/' + str(pages[i]))
            
            
## Xpath method used to extract direct links to hotel subpages

    def parse(self, response):
        xpath = '//*[@id="topPicks"]/div[*]/div/div[2]/div[1]/div[1]/a//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
