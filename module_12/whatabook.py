""" moore module 12.2 whatabook script
this script will act as the inteface for updating user wishlists
"""
from time import sleep
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

class WhatabookRepository:
    def __init__(self):
        self._db = mysql.connector.connect(**config)
        self._user_id = None
        print(f'\nuser: {config["user"]}' 
        f'\nconnected @{config["host"]}'
        f'\ndatabase: <{config["database"]}>')
    # return the selected main menu option
    def show_menu(self):
        print('\n📚Whatabook Home📚')
        user_selection = input('\nWhat would you like to do?\n'
                                '1. View book catalog\n'
                                '2. View locations\n'
                                '3. Go to your account\n'
                                'Press Q to Exit\n')
        return user_selection
    # returns true or false if user is authenitcated and sets user_id for future operations
    def validate_user(self, username):
        print('\nValidating user...')

        cursor = self._db.cursor()
        # cursor.callproc('grab_user_id', (username, 0))
        # todo[6]: ^ won't return anything
        query = f'SELECT user_id FROM user WHERE last_name = "{username}"'
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()

        if user:
            self._user_id = user[0]
            return True
        else:
            return False
    # show account menu and invokes account_execute
    def show_account_menu(self, did_login=False):
        if did_login:
            print('\n📚My Whatabook Account📚')
            sleep(.5)
            user_selection = input('\nWhat would you like to do?\n'
                                    '1. View your wishlist\n'
                                    '2. Add books to your wishlist\n'
                                    '3. Remove books from your wishlist\n'
                                    '4. Go Home\n'
                                    'Press Q to Exit\n')
            sleep(.5)
            return self.account_execute(user_selection, did_login)
        else:
            user_check_query = input('\nUser not found!\n'
                                    'Please enter your username: \n'
                                    'Press Q to Exit\n').lower()
            sleep(.5)
            if user_check_query.upper() == 'Q':
                print('\n📚Thanks for using Whatabook📚')            
                sleep(.5)
                exit()
            validation_result = self.validate_user(user_check_query)
            self.show_account_menu(validation_result)
    # execute account menu slection
    def account_execute(self, selection, validation_result):
        if not selection or not validation_result:
            selection = self.show_account_menu()

        if selection == '4' or selection.upper() == 'Q':
            return self.main()
        
        dict = {
            '1': self.show_wishlist,
            '2': self.show_books_to_add,
            '3': self.show_books_to_remove,
        }

        dict[selection]()
        return self.show_account_menu(validation_result)
    # shows all books in db
    def show_catalog(self):
        sleep(.5)
        print("\nRetrieving books...")

        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM book")

        catalog = cursor.fetchall()
        cursor.close()
        
        if catalog:
            self.print_books(catalog)
        else:
            print('\nNo books found...')
    # show all locations
    def show_locations(self):
        sleep(.5)
        print("\nRetrieving store locations...")

        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM store")

        stores = cursor.fetchall()
        cursor.close()

        if stores:
            for store in stores:
                print(f'Location: {store[0]}'
                    f'Address: {store[1]}')
    # shows wishlist using the current validated user_id
    def show_wishlist(self):
        sleep(.5)
        cursor = self._db.cursor()

        query =  f"SELECT book_name, author, details FROM wishlist A INNER JOIN book B ON A.book_id = B.book_id INNER JOIN user C ON A.user_id = {self._user_id} WHERE C.user_id = {self._user_id}"
        cursor.execute(query)
        data = cursor.fetchall()
        if data:
            for wishlist in data:
                print('-' * 50 +
                    f'\nTitle: {wishlist[0]}'
                    f'\Author: {wishlist[1]}'
                    f'\nDetails: {wishlist[2]}'
                    '\n' + '-' * 50)
    # adds to current selected user wishlist
    def add_to_wishlist(self, book_id):
        sleep(.5)
        print(f'\nAdding book to wishlist...')
        cursor = self._db.cursor()
        query = f'INSERT INTO wishlist (book_id, user_id) VALUES ({book_id}, {self._user_id})'
        cursor.execute(query)
        print('\n\ndone✅')
        sleep(.5)
    # removes from current selected user wishlist
    def remove_from_wishlist(self, book_id):
        sleep(.5)
        print(f'\nRemoving book from wishlist...')
        cursor = self._db.cursor()
        query = f'DELETE FROM wishlist WHERE user_id = {self._user_id} AND book_id = {book_id}'
        cursor.execute(query)
        print('\n\ndone✅')
        sleep(.5)
    # shows books that are not in the current user wishlist
    def show_books_to_add(self):
        cursor = self._db.cursor()
        query = f'SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {self._user_id})'
        cursor.execute(query)
        result = cursor.fetchall()
        
        if result:
            self.print_books(result)

        sleep(1)
        book_to_add = input('which book would you like to add? (use book id number)')
        # if book_to_add is a number
        if book_to_add.isdigit():
            self.add_to_wishlist(book_to_add)
        else:
            print('\n\nInvalid input...')
            sleep(1)
            self.show_books_to_add()
    # shows books to remove from current user wishlist
    def show_books_to_remove(self):
        cursor = self._db.cursor()
        query = f'SELECT book_id, book_name, author, details FROM wishlist WHERE user_id = {self._user_id}'
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            self.print_books(result)

        sleep(1)
        book_to_remove = input('which book would you like to remove? (use book id number)')
        # if book_to_remove is a number
        if book_to_remove.isdigit():
            self.remove_from_wishlist(book_to_remove)
        else:
            print('\n\nInvalid input...')
            sleep(1)
            self.show_books_to_remove()
    # print books
    def print_books(self, books):
        for book in books:
            print('-' * 50 +
                f'\nID: {book[0]}'
                f'\nTitle: {book[1]}'
                f'\nAuthor: {book[2]}'
                f'\nDetails: {book[3]}'
                '\n' + '-' * 50 + '\n')
            sleep(.5)
    # runs the program
    def main(self):
        try:
            selection = self.show_menu()
            if selection == '1':
                self.show_catalog()
                self.main()
            elif selection == '2':
                self.show_locations()
                self.main()
            elif selection == '3':
                user_check_query = input('\nPlease enter your username: ').lower()
                validated = self.validate_user(user_check_query)
                self.show_account_menu(validated)
            elif selection.upper() == 'Q':
                print('\n📚Thanks for using Whatabook!📚')
                sleep(.5)
            else:
                print('\nInvalid selection. Please try again.')
                sleep(.5)
                self.main()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('\nSomething is wrong with your user name or password')
                print(err)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('\nDatabase does not exist')
            else:
                print('\nDatabase error: ')
                print(err)
        except KeyboardInterrupt:
            print('\n📚Thanks for using Whatabook📚')
            sleep(.5)
        except Exception as e:
            print('\nSomething went wrong: ')
            print(e)
            sleep(.5)
        finally:
            self._db.close()
            exit()
# instanitate the class
repo = WhatabookRepository()
# run the program
repo.main()
