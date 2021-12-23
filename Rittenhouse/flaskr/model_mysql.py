import mysql.connector
from mysql.connector import errorcode
import petl as etl

# Book class for populating Jinja template
class Book:
    idBooks = None
    title = None
    author = None
    descrip = None
    pages = None
    rating = None


# create method. takes values provided by submitted form
def create(values: tuple):
    """

    :param values: values for entry
    :type tuple:
    """
    cnx = get_cnx()
    cursor = cnx.cursor()

    insert = ("INSERT INTO rittenhouse.books "
              "(idBooks, title, author, descrip, pages, rating) "
              "VALUES (%s, %s, %s, %s, %s, %s)")

    cursor.execute(insert, values)
    cnx.commit()
    cnx.close()
    cursor.close()


# Read method. Default setting is to return all entries.
# Also used by update method in .crud
def read(sel='all', id=None) -> list:
    """

    :param sel: Toggles if returning all values or specific entry
    :type sel: str
    :param id: Used to update entry. Provides id of entry to be updated.
    :type id: None or int
    :return books: Book(s) to be updated.
    :rtype: Book
    """
    cnx = get_cnx()
    cursor = cnx.cursor()
    if sel == 'all':
        query = "SELECT * FROM rittenhouse.books"
    else:
        query = ("SELECT * "
                 "FROM rittenhouse.books "
                 "WHERE idBooks = %s") % id
    cursor.execute(query)

    books = []
    for (idBooks, title, author, descrip, pages, rating) in cursor:
        book = Book()
        book.idBooks = idBooks
        book.title = title
        book.author = author
        book.descrip = descrip
        book.pages = pages
        book.rating = rating
        books.append(book)

    cursor.close()
    cnx.close()
    return books


# update method that updates entry based on form submitted
def update(values: tuple):
    """

    :param values: values for entry
    :type values: tuple
    """
    cnx = get_cnx()
    cursor = cnx.cursor()

    update = ("UPDATE rittenhouse.books "
              "SET "
              "title = %s, "
              "author = %s, "
              "descrip = %s, "
              "pages = %s, "
              "rating = %s "
              "WHERE idBooks = %s")

    cursor.execute(update, values)
    cnx.commit()
    cnx.close()
    cursor.close()


# delete method that deletes entry based on id submitted
def delete(id: int):
    """

    :param id: id of book to be deleted.
    :type id:
    """
    cnx = get_cnx()
    cursor = cnx.cursor()

    delete = ("DELETE FROM rittenhouse.books "
              "WHERE idBooks = %s") % id
    cursor.execute(delete)

    cnx.commit()
    cnx.close()
    cursor.close()


# function returns connector to MySQL db
def get_cnx():
    """

    :return: mysql connector
    :rtype:
    """
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
