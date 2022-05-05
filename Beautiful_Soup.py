from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

# Hotel links

Hotel_links = []

url = 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaLYBiAEBmAEeuAEHyAEM2AED6AEBiAIBqAIDuALgh9CTBsACAdICJDA3ZWNiN2JkLTc2MjktNDQzZS04ZmQ3LTdlODBmOTJmMzQ3YdgCBOACAQ&sid=521953b71ac73a73e253104282cff91f&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaLYBiAEBmAEeuAEHyAEM2AED6AEBiAIBqAIDuALgh9CTBsACAdICJDA3ZWNiN2JkLTc2MjktNDQzZS04ZmQ3LTdlODBmOTJmMzQ3YdgCBOACAQ%3Bsid%3D521953b71ac73a73e253104282cff91f%3Bsb_price_type%3Dtotal%26%3B&ss=Gda%C5%84sk&is_ski_area=0&ssne=Gda%C5%84sk&ssne_untouched=Gda%C5%84sk&dest_id=-501400&dest_type=city&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'class':re.compile('e6e585da68')})


links = [tag.a['href'] for tag in tags]

Hotel_links.extend(links)

for link in Hotel_links:
    print(link)
