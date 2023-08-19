#!/usr/bin/python3
''' Takes in the name of a state as an argument and lists all cities of
    that state from the database 'hbtn_0e_04usa'

    This database contains a states(id, name) and cities(id, state_id, name)
    table
    This script handles SQL injections
'''
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()

        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id"
        query += " = states.id WHERE states.name = %s"
        cursor.execute(query, ('{}'.format(sys.argv[4]), ))
        print(", ".join([city[0] for city in cursor.fetchall()]))
    except MySQLdb.Error as e:
        print("Error: ", e)
    finally:
        if db:
            db.close()
