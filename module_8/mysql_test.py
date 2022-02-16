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
    print("\n database user {} connected to mysql on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    input("\n Press Enter to continue...")
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
