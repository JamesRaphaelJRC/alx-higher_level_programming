#!/usr/bin/python3
''' Lists all states from the database 'hbtn_0e_0_usa' '''
import sys
import MySQLdb


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    query = "SELECT * FROM `states` WHERE `name` LIKE 'N%' COLLATE utf8mb4_bin"
    cursor.execute(query)
    allStates = cursor.fetchall()

    for state in allStates:
        print(state)

    cursor.close()
    db.close()
