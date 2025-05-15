import mysql.connector
from product.product import Product
from datetime import date, datetime, timedelta

class Database():
    def __init__(self,host:str, port:int, user:str, passw:str):
        self.host = host
        self.port = port
        self.user = user
        self.passw = passw

    def isRdy(self)->bool:
        try:
            db = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.passw)

            db.close()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0

    def add_product_to_db(self, product:Product):

        db = mysql.connector.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        password=self.passw)

        cursor = db.cursor()
        sql = "INSERT INTO userdb.foods (product, price, restaurant, datetime) VALUES (%s, %s, %s, %s)"

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        values = (product.name, product.price, product.restaurantName, timestamp)

        cursor.execute(sql, values)
        db.commit()

        db.close()
    
