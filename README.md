# csd-310
bellevue university course repo

## modules 5-6
- mongodb
---
## modules 8-11
- mysql
- [whatabook ord](./module_10/whatabook_ord.uxf)
![ord](./module_10/whatabook_ord.png)
---
## module 12 whatabook.py
### objectives
- [x] Create a method to for “show_menu()”
- [x] Create a method for “show_books(_cursor)”
- [x] Create a method for “show_locations(_cursor)”
- [x] Create a method for “validate_user()”
- [x] Create a method for “show_account_menu()”
- [x] Create a method for “show_wishlist(_cursor, _user_id)”
- [x] Create a method for “show_books_to_add(_cursor, _user_id)”
- [x] Create a method for “add_book_to_wishlist(_cursor, _user_id, _book_id)”
- [x] Create a method to display the account menu
- [x] Use variables to capture the user entry for user_id
- [x] User variables to capture the user entry for book_id
---

getting started in 1, 2, 3!
please refer to ./init-db.d for init.sql files used to administrate this database
1. run the 002_whatabook_init.sql file in your database
2. run whatabook.py
3. use the menu to navigate through the program 
    - you can head over to a user's wishlist from the main menu by selecting (3) and entering the last name when prompted
      - the username you can enter is 'bober' or 'oglethorpe'
      - you can view, add, and remove books from their wishlist
---

### advanced running procedures
  this project supports docker compose for easy setup
  1. clone the repo
  2. ensure docker is running and in your terminal type 
     - `docker compose -f whatabook_docker.yaml up --build -d`
  3. now you can run whatabook.py to interact with the application as above
---

### troubleshooting
  - is your database on and receiving connections?
  - did your database successfully run the init.sql file?
  - did you enter the correct username? ('bober' or 'oglethorpe')
  - did you have coffee this morning? ☕️
  - did you turn it off and back on again?
  - if none of the above are helpful, please address your concern in the form of a PR
---
