""" moore 21FEB2022 m10.3
Insert new records to fill each table 

1 store

9 books

3 users

1 wishlist item for each user (total of 3 wishlist records)

Take a screenshot of the insert statements """
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def addUsers(db, userList):
    print('\n Inserting users...')
    # add users
    cursor = db.cursor()
    for user in userList:
        query = f'INSERT INTO user(first_name, last_name) VALUES ("{user["first_name"]}", "{user["last_name"]}")'
        cursor.execute(query)
    db.commit()


def addBooks(db, bookList):
    print('\n Inserting books...')
    # add books
    cursor = db.cursor()
    for book in bookList:
        query = f'INSERT INTO book (book_name, author, details) VALUES ("{book["book_name"]}", "{book["author"]}", "{book["details"]}")'
        cursor.execute(query)
    db.commit()


def addStore(db, storeList):
    print('\n Inserting store...')
    # add store
    cursor = db.cursor()
    for store in storeList:
        query = f'INSERT INTO store (locale) VALUES ("{store["locale"]}")'
        cursor.execute(query)
    db.commit()


def addWishlist(db, wishlist):
    print('\n Inserting wishlist...')
    # add wishlist
    cursor = db.cursor()

    for item in wishlist:
        query = f'INSERT INTO wishlist (user_id, book_id) VALUES ("{item["user_id"]}", "{item["book_id"]}")'
        cursor.execute(query)
    db.commit()


users = [
    {"first_name": "Jobidiah", "last_name": "Bober"},
    {"first_name": "Xena", "last_name": "Beans"},
    {"first_name": "Geeter", "last_name": "Oglethorpe"}
]

books = [
    {"book_name": "1984", "author": "George Orwell",
        "details": "A book about a dystopian future."},
    {"book_name": "Moby Dick", "author": "Herman Melville",
        "details": "A book a sailor hunting whale."},
    {"book_name": "The Great Gatsby", "author": "F. Scott Fitzgerald",
        "details": "A book a writer writes to himself."},
    {"book_name": "The Hobbit", "author": "J. R. R. Tolkien",
        "details": "A book about an adventure concerning halflings."},
    {"book_name": "The Count of Monte Cristo", "author": "Alexandre Dumas",
        "details": "A book about a man who seeks revenge."},
    {"book_name": "The Three Musketeers", "author": "Alexandre Dumas",
        "details": "A book about a three musketeers."},
    {"book_name": "Cien Años de Soledad", "author": "Gabriel García Márquez",
        "details": "A book about a secluded village."},
    {"book_name": "The Lord of the Rings", "author": "J. R. R. Tolkien",
        "details": "A book about a friends."},
    {"book_name": "The Divine Comedy", "author": "Dante Alighieri",
        "details": "A book about a man cast to hell."},
    {"book_name": "A Tale of Two Cities", "author": "Charles Dickens",
        "details": "A tale set in London before the French Revolution"}
]

storeList = [{"locale": "123 N Harrison St, Olympia, WA 98504"}]

try:
    db = mysql.connector.connect(**config)
    print(f'\n database user {config["user"]} connected to mysql on host {config["host"]} with database {config["database"]}')

    input("\nInserting data into the database... \nPress any key to continue...")

    addUsers(db, users)
    addBooks(db, books)
    addStore(db, storeList)

    # need to grab the user_id before you can add a wishlist
    wishList = []
    cursor = db.cursor()

    cursor.execute("SELECT user_id FROM user")
    user_ids = cursor.fetchall()

    cursor.execute("SELECT book_id FROM book")
    book_ids = cursor.fetchall()

    # create a wishlist for each user
    wishList.append({"user_id": user_ids[0][0], "book_id": book_ids[0][0]})
    wishList.append({"user_id": user_ids[0][0], "book_id": book_ids[1][0]})
    wishList.append({"user_id": user_ids[0][0], "book_id": book_ids[2][0]})
    wishList.append({"user_id": user_ids[1][0], "book_id": book_ids[3][0]})
    wishList.append({"user_id": user_ids[1][0], "book_id": book_ids[4][0]})
    wishList.append({"user_id": user_ids[1][0], "book_id": book_ids[5][0]})
    wishList.append({"user_id": user_ids[2][0], "book_id": book_ids[6][0]})
    wishList.append({"user_id": user_ids[2][0], "book_id": book_ids[7][0]})
    wishList.append({"user_id": user_ids[2][0], "book_id": book_ids[8][0]})

    addWishlist(db, wishList)

    input("\n Seeding Complete, \nPress any key to continue...")

    # retrieve data
    # users
    print("\n Retrieving data from the database...")
    print("\n Retrieving users...")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()

    for user in data:
        print(user)

    # books
    print("\n Retrieving books...")
    cursor.execute("SELECT * FROM book")
    data = cursor.fetchall()

    for book in data:
        print(book)
    print("\n Retrieving store...")

    cursor.execute("SELECT * FROM store")
    data = cursor.fetchall()

    for store in data:
        print(store)
    print("\n Retrieving wishlist...")

    # wishlist as join
    cursor.execute(
        "SELECT book_name, author, details, first_name, last_name FROM wishlist A INNER JOIN book B ON A.book_id = B.book_id INNER JOIN user C ON A.user_id = C.user_id")
    data = cursor.fetchall()

    for wishlist in data:
        print(wishlist)

    input("\nFinished Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
        print(err)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print('other error: ')
        print(err)
finally:
    db.close()
    exit()
