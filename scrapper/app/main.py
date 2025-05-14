from bs4 import BeautifulSoup
from scrapper.feketesas_scrapper import FeketeSas_Scraper
from scrapper.partedli_scrapper import Partedli_Scraper
from sql.sql import add_product_to_db

def main():
    print("App Started.")
    feketeSas = FeketeSas_Scraper("Fekete Sas","https://www.fekete-sas.hu/index.php?page=food_menu")
    partedli = Partedli_Scraper("Partedli","https://partedli-etterem.hu/etlap")

    feketeSasMenu = feketeSas.parse_products(feketeSas.fetch_html())
    partedliMenu = partedli.parse_products(partedli.fetch_html())
    

    for food in partedliMenu:
        add_product_to_db(food)

    for food in feketeSasMenu:
        add_product_to_db(food)

if __name__ == "__main__":
    main()