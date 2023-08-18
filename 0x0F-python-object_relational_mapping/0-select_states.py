#!/usr/bin/python3
import sys
import MySQLdb


''' Lists all states from the database 'hbtn_0e_0_usa' '''
if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    allStates = cursor.fetchall()

    for state in allStates:
        print(state)

    cursor.close()
    db.close()
