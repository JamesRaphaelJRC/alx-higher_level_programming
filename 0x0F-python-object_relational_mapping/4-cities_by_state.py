#!/usr/bin/python3
''' Lists all cities from the database 'hbtn_0e_0_usa' '''
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()

        query = "SELECT cities.id, cities.name, states.name FROM cities"
        query += " JOIN states ON cities.state_id = states.id"
        cursor.execute(query)
        [print(state) for state in cursor.fetchall()]
    except MySQLdb.Error as e:
        print("Error: ", e)
    finally:
        if db:
            db.close()
