""" moore 20FEB2022 m9.2
this file will execute a join table query on player and team """
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def printJoinTableData(data):
    for row in data:
        print(f"Player ID: {row[0]}\n" +
              f"First Name: {row[1]}\n" +
              f"Last Name: {row[2]}\n" +
              f"Team Name: {row[5]}\n")


try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    new_player = {
        "first_name": "Durin's Bane",
        "last_name": "of the Mines of Moria",
        "team_id": 1

    }

    # JOIN the player and team tables, save the query to use later
    joinTableQuery = 'SELECT * FROM player A INNER JOIN team B ON A.team_id = B.team_id'
    cursor.execute(joinTableQuery)
    data = cursor.fetchall()

    # use printJoinTableData(data) to print the data
    print('\n\n- - DISPLAYING PLAYERS RECORDS - -')
    printJoinTableData(data)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
        print(err)
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    db.close()
    exit()
