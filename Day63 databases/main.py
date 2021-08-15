import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
cursor.execute(
    "INSERT INTO books VALUES(2, 'I steve, SJ in his own words', 'George.Beahm', '7.3')")
db.commit()
cursor.execute(
    "INSERT INTO books VALUES(3, 'The short history of nearly everything ', 'Bill. Bryson', '9.5')")
db.commit()
