
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create _user and grant them all privileges to the database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';
-- GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'172.23.0.1';
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
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
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

-- insert some users
INSERT INTO user (first_name, last_name) VALUES 
    ('Jobi', 'Bober'),
    ('Geeter', 'Oglethorpe');

-- insert some books
INSERT INTO book (book_name, author, details) VALUES
    ('1984', 'George Orwell', 'A book about a dystopian future.'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'A book about a guy who lives in the suburbs.'),
    ('The Hobbit', 'J. R. R. Tolkien', 'A book about a hobbit who goes on an adventure.'),    
    ('Moby Dick', 'Herman Melville', 'A book a sailor hunting whale.'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'A book a writer writes to himself.'),
    ('The Count of Monte Cristo', 'Alexandre Dumas', 'A book about a man who seeks revenge.'),
    ('The Three Musketeers', 'Alexandre Dumas', 'A book about three musketeers.'),
    ('Cien Años de Soledad', 'Gabriel García Márquez', 'A book about a secluded village.'),
    ('The Lord of the Rings', 'J. R. R. Tolkien', 'A book about friends.'),
    ('The Divine Comedy', 'Dante Alighieri', 'A book about a man cast to hell.'),
    ('A Tale of Two Cities', 'Charles Dickens', 'A tale set in London before the French Revolution'),
    ('Klara and the Sun', 'Kazuo Ishiguro', 'A robot girl with artificial intelligence is designed as a playmate for children'),
    ('Punch Me Up to the Gods', 'Brian Broome', 'A story about a man growing up in America'),
    ('Stories from Suffragette City', 'M. J. Rose, Fiona Davis', 'A collection of short stories that all take place on a single day: October 23, 1915.'),
    ('Cloud Cuckoo Land', 'Anthony Doerr', 'A triumph of imagination and compassion, a novel about children on the cusp of adulthood in a broken world, who find resilience, hope, and story.'),
    ('Bewilderment', 'Richard Powers', 'The astrobiologist Theo Byrne searches for life throughout the cosmos while single-handedly raising his unusual nine-year-old, Robin, following the death of his wife'),
    ('Lightning Strike', 'William Kent Kreuger', 'A book about fathers and sons, long-simmering conflicts in a small Minnesota town, and the events that echo through youth and shape our lives forever.'),
    ('Three Girls from Bronzeville', 'Dawn Turner', 'A memoir about three Black girls from the storied Bronzeville section of Chicago that offers a penetrating exploration of race, opportunity, friendship, sisterhood, and the powerful forces at work that allow some to flourish…and others to falter.');


DELIMITER //
CREATE PROCEDURE grab_book_id(IN book_name VARCHAR(200), OUT book_id INT)
BEGIN
    SELECT book_id FROM book WHERE book_name = book_name;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE grab_user_id(IN user_name VARCHAR(75), OUT user_id INT)
BEGIN
    SELECT user_id FROM user WHERE last_name REGEXP user_name;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE show_wishlist(IN user_id INT)
BEGIN
    SELECT book_name, author, details
    FROM book, wishlist
    WHERE book.book_id = wishlist.book_id
    AND wishlist.user_id = user_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE show_not_in_wishlist(IN user_id INT)
BEGIN
    SELECT book_name, author, details
    FROM book
    WHERE book.book_id NOT IN (
        SELECT book_id
        FROM wishlist
        WHERE user_id = user_id
    );
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_to_wishlist(IN user_id INT, IN book_id INT)
BEGIN
    INSERT INTO wishlist(user_id, book_id)
    VALUES(user_id, book_id);
END //
DELIMITER;

USE whatabook;
