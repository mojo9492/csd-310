
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create _user and grant them all privileges to the database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'%';

USE whatabook;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR (75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);

USE whatabook;
