import mysql.connector
from product.product import Product
from datetime import date, datetime, timedelta

def add_product_to_db(product:Product):

  db = mysql.connector.connect(
      host="mysqldb",
      port=3306,
      user="dm",
      password="dmpass")
  
  '''
  db = mysql.connector.connect(
      host="127.0.0.1",
      port=3306,
      user="dm",
      password="dmpass")
  '''

  cursor = db.cursor()
  sql = "INSERT INTO userdb.foods (product, price, restaurant, datetime) VALUES (%s, %s, %s, %s)"
  
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  values = (product.name, product.price, product.restaurantName, timestamp)

  cursor.execute(sql, values)
  db.commit()

  db.close()
