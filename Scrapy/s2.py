import scrapy

## definition of all element which will be scraped

class hotels(scrapy.Item):
    Name        = scrapy.Field()
    Price = scrapy.Field()
    Rating = scrapy.Field()
    Cleanliness       = scrapy.Field()
    Comfort = scrapy.Field()
    Service_Quality = scrapy.Field()
    Security = scrapy.Field()
    Location = scrapy.Field()
    
## spider creation
class LinkListsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['https://hotels.ng/']
    
## import of links saved using spider s1
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = hotels()

## Xpath method used to extract needed information 
        name_xpath        = '//h1/text()'
        price_xpath = '//*[@id="bookOnline"]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/div/p[1]//text()'
        rating_xpath = '//*[@id="reviews"]/div[2]/div[1]/div/div[1]//text()'
        cleanlines_xpath   = '//*[@id="reviews"]/div[2]/div[2]/div[1]/p[2]//text()'
        comfort_xpath       = '//*[@id="reviews"]/div[2]/div[2]/div[2]/p[2]//text()'
        service_xpath       = '//*[@id="reviews"]/div[2]/div[2]/div[3]/p[2]//text()'
        security_xpath       = '//*[@id="reviews"]/div[2]/div[2]/div[4]/p[2]//text()'
        location_xpath       = '//*[@id="reviews"]/div[2]/div[2]/div[5]/p[2]//text()'

## Extracting all date for each column and row

        p['Name']               = response.xpath(name_xpath).getall()
        p['Price']= response.xpath(price_xpath).getall()
        p['Rating']= response.xpath(rating_xpath).getall()
        p['Cleanliness']       = response.xpath(cleanlines_xpath).getall()
        p['Comfort']       = response.xpath(comfort_xpath).getall()
        p['Service_Quality']       = response.xpath(service_xpath).getall()
        p['Security']       = response.xpath(security_xpath).getall()
        p['Location']       = response.xpath(location_xpath).getall()


        yield p
