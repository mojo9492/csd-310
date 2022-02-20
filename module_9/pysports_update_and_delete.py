""" moore 20FEB2022 m9.3
this file will insert a new player, then update the player, then delete the player """
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
    # INSERT the coolest demonic monster ever into the player table
    query = f'INSERT INTO player (first_name, last_name, team_id) VALUES ("{new_player["first_name"]}", "{new_player["last_name"]}", {new_player["team_id"]})'
    cursor.execute(query)

    # JOIN the player and team tables, save the query to use later
    joinTableQuery = 'SELECT * FROM player A INNER JOIN team B ON A.team_id = B.team_id'
    cursor.execute(joinTableQuery)
    data = cursor.fetchall()

    # use printJoinTableData(data) to print the data
    print('\n\n- - DISPLAYING PLAYERS AFTER INSERT - -')
    printJoinTableData(data)

    # UPDATE the player TEAM to the team sauron because balrogs are evil
    query = f'UPDATE player SET team_id = 2 WHERE first_name = "Durin\'s Bane"'
    cursor.execute(query)

    # JOIN the tables again
    cursor.execute(joinTableQuery)
    data = cursor.fetchall()

    # use printJoinTableData(data) to print the data
    print('\n\n- - DISPLAYING PLAYERS AFTER UPDATE - -')
    printJoinTableData(data)

    # DELETE the player
    query = f'DELETE FROM player WHERE first_name = "Durin\'s Bane"'
    cursor.execute(query)

    # JOIN the tables again
    cursor.execute(joinTableQuery)
    data = cursor.fetchall()
    print('\n\n- - DISPLAYING PLAYERS AFTER DELETE - -')
    printJoinTableData(data)
    input("\n\nPress any key to continue...")
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
