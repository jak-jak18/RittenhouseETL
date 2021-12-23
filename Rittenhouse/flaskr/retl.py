import mysql.connector
import petl as etl
from mysql.connector import errorcode

# etl extract function
def extract():
    query = 'SELECT * FROM rittenhouse.books'
    table = etl.fromdb(get_cnx(), query)
    # sort by author name
    return etl.sort(table, 'author')


def get_cnx():
    try:
        cnx = mysql.connector.connect(user='user', password='',
                                      host='127.0.0.1',
                                      database='rittenhouse')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        return cnx
