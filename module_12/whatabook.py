""" moore module 12.2 whatabook script
this script will act as the inteface for updating user wishlists
"""
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

    def show_menu(self):
        print('\n📚Whatabook Home📚')
        user_selection = input('\nWhat would you like to do?\n'
                                '1. View book catalog\n'
                                '2. View locations\n'
                                '3. Go to your account\n'
                                'Press Q to Exit\n')
        return user_selection

    def validate_user(self, username):
        print('\nValidating user...')

        cursor = self._db.cursor()
        cursor.callproc('grab_user_id', (username,))
        # todo[6]: ^ won't return anything
        user = cursor.fetchone()
        cursor.close()
        print(f'\nUser: {user}')
        if user:
            self._user_id = user[0]
            return True
        else:
            return False

    def show_account_menu(self, did_login=False):
        if did_login:
            print('\n📚My Whatabook Account📚')
            user_selection = input('\nWhat would you like to do?\n'
                                    '1. View your wishlist\n'
                                    '2. Add to your wishlist\n'
                                    '3. Remove books from your wishlist\n'
                                    '4. Go Home\n'
                                    'Press Q to Exit\n')
            return user_selection
        else:
            user_check_query = input('\nUser not found!\n'
                                    'Please enter your username: \n'
                                    'Press Q to Exit\n').lower()
            if user_check_query.upper() == 'Q':
                print('\n📚Thanks for using Whatabook📚')
                exit()
            validation_result = self.validate_user(user_check_query)
            self.show_account_menu(validation_result)

    def show_catalog(self):
        print("\nRetrieving books...")

        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM book")

        catalog = cursor.fetchall()
        cursor.close()
        
        if catalog:
            for book in catalog:
                print(f'\n{book[1]}' 
                        f'\n\tAuthor: {book[2]}'
                        f'\n\tDetails:\n\t\t{book[3]}')
        else:
            print('\nNo books found...')

    def show_locations(self):
        print("\nRetrieving store locations...")

        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM store")

        stores = cursor.fetchall()
        cursor.close()

        if stores:
            # todo[1]: add formatting
            for store in stores:
                print(store)

    def show_wishlist(self):
        # todo[2]: add functionality
        pass

    def add_to_wishlist(self):
        # todo[3]: add functionality
        pass
    
    def remove_from_wishlist(self):
        # todo[4]: add functionality
        pass

    def show_books_to_add(self):
        # todo[5]: add functionality
        pass

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
                validation_result = self.validate_user(user_check_query)
                self.show_account_menu(validation_result)
            elif selection.upper() == 'Q':
                print('\n📚Thanks for using Whatabook!📚')
            else:
                print('\nInvalid selection. Please try again.')
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
        except Exception as e:
            print('\nSomething went wrong: ')
            print(e)
        finally:
            self._db.close()
            exit()

repo = WhatabookRepository()
repo.main()
