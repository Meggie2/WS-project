from gc import callbacks
from pickle import TRUE
import scrapy

b=TRUE


class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'links'
    
    allowed_domains = ['https://hotels.ng/']
    
    start_urls=[]
    if b==TRUE:
        pages = list(range(1,11))
        for i in range(len(pages)):
            start_urls.append('https://hotels.ng/hotels-in-lagos/' + str(pages[i]))
    else: 
        pages = list(range(1,333))
        for i in range(len(pages)):
            start_urls.append('https://hotels.ng/hotels-in-lagos/' + str(pages[i]))

    def parse(self, response):
        xpath = '//*[@id="topPicks"]/div[*]/div/div[2]/div[1]/div[1]/a//@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
