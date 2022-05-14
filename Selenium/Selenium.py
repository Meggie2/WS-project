#### IMPORT LIBRARY 
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

#### WEB DRIVER PATH
driver = webdriver.Chrome(executable_path=r'/Users/macbookpro/Downloads/chromedriver-2')



####SCRAPE OF HOTELS AND OTHER DETAILS
def scrap(page, db, count):
    driver.get(page)
    box = driver.find_elements_by_class_name('listing-hotels-details-box')
    for i in box:
        name = i.find_element_by_class_name('listing-hotels-name').text
        price = i.find_element_by_class_name('listing-hotels-prices-discount').text.replace('\n', '')
        try:
            rating = i.find_element_by_class_name('listing-hotels-rating').text
        except:
            rating = ''
        a = {
            'name': name,
            'price': price,
            'rating': rating
        }
        db.append(a)
        print(count)
        if int(count) > 100:
            print(db)
            print(len(db))
            quit()
        else:
            count += 1


count = 0
page_urls = []
db = []

for i in range(1, 15):
    page = i
    base_url = 'https://hotels.ng/hotels-in-lagos/' + str(page)
    page_urls.append(base_url)

for i in page_urls:
    scrap(i, db, count)

# save the data to a csv file
with open('hotels_selenium', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'price', 'rating'])
    writer.writerows(db)
