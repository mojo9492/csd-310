import mysql.connector
from mysql.connector import errorcode

config = {
    'user': "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    query = 'SELECT team_id, team_name, mascot FROM team'
    cursor.execute(query)

    data = cursor.fetchall()

    print('\n- - DISPLAYING TEAM RECORDS - -')
    for row in data:
        print(f"Team ID: {row[0]}\n" +
        f"Team Name: {row[1]}\n" +
        f"Team Mascot: {row[2]}\n")

    query = 'SELECT player_id, first_name, last_name, team_id FROM player'
    cursor.execute(query)

    data = cursor.fetchall()
    print('\n\n- - DISPLAYING PLAYER RECORDS - -')
    for row in data:
        print(f"Player ID: {row[0]}\n" +
        f"First Name: {row[1]}\n" +
        f"Last Name: {row[2]}\n" +
        f"Team ID: {row[3]}\n")
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
