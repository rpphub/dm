import mysql.connector
try:
    sql = mysql.connector.connect(
        host="mysqldb",
        port=3306,
        user="dm",
        password="dmpass")
    
    '''
    sql = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="dm",
        password="dmpass")
    '''
    print("Mysql connected.")
    sql.close()
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))