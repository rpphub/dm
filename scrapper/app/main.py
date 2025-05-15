from bs4 import BeautifulSoup
from scrapper.feketesas_scrapper import FeketeSas_Scraper
from scrapper.partedli_scrapper import Partedli_Scraper
from sql.sql import Database
import time

def main():
    print("App Started.")

    db = Database("mysqldb",3306,"dm","dmpass")
    #db = Database("127.0.0.1",3306,"dm","dmpass")
    feketeSas = FeketeSas_Scraper("Fekete Sas","https://www.fekete-sas.hu/index.php?page=food_menu")
    partedli = Partedli_Scraper("Partedli","https://partedli-etterem.hu/etlap")
    
    while db.isRdy() == 0:
          print("Waiting for database to become available...")
          time.sleep(5)


    feketeSasMenu = feketeSas.parse_products(feketeSas.fetch_html())
    partedliMenu = partedli.parse_products(partedli.fetch_html())
    

    for food in partedliMenu:
        db.add_product_to_db(food)

    for food in feketeSasMenu:
        db.add_product_to_db(food)

if __name__ == "__main__":
    main()