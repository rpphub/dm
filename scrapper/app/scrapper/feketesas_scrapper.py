from bs4 import BeautifulSoup
from .base_scrapper import BaseScraper
from product.product import Product
import re
import requests

class FeketeSas_Scraper(BaseScraper):
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
    menu_table = soup.find('td', class_='fm_text') 
    product = []
    for table_rows in menu_table.find_all('tr', class_='bgrow'):
        if(len(table_rows.find_all('td', class_='fm_text')) >= 4):

          food = table_rows.find_all('td', class_='fm_text')[1].a.text #Étel neve
          
          price = 0
          match = re.search(r'\d+', table_rows.find_all('td', class_='fm_text')[4].text) #Termék ára
          if match:
              price = int(match.group())

          product.append(Product(food,self.name,price))

    return product