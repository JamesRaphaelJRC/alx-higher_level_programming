#!/usr/bin/python3
''' Lists all states from the database 'hbtn_0e_0_usa' whose name matches with
    the 4th argument supplied by the user
'''
import sys
import MySQLdb


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    query = "SELECT * FROM `states` WHERE `name`='{}'".format(sys.argv[4])
    cursor.execute(query)
    allStates = cursor.fetchall()

    for state in allStates:
        print(state)

    cursor.close()
    db.close()
