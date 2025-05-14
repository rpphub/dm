from bs4 import BeautifulSoup
from .base_scrapper import BaseScraper
from product.product import Product
import re
from datetime import datetime
import requests

class Partedli_Scraper(BaseScraper):
  def __init__(self,name,url):
    self.name = name
    self.url = url

  def fetch_html(self):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0'
    }

    r = requests.get(url=self.url, headers=headers)

    return r
  
  def parse_products(self,r):
    soup = BeautifulSoup(r.content, 'html5lib')
    weekMenu = soup.find('div', class_='vc_tta-panels') 
    product = []
    dayIndex = datetime.today().weekday() #Heti lista van ezért kell.
    
    try:
      dayMenuDiv = weekMenu.find_all('div', class_='vc_tta-panel')[dayIndex]
      dayMenu = dayMenuDiv.find("div", class_="standard-arrow list-divider")
      for elem in dayMenu.find_all('li'):
        span = elem.find("span")

        price = 0
        match = re.search(r'\d+', span.text) #Termék ára
        if match:
            price = int(match.group())
        span.extract() #Könnyebb így a domot manpiulálva, mert hülyén van meg csinálva
        
        food = elem.text
        product.append(Product(food,self.name,price))

    except Exception as e: print(e)
       
    return product