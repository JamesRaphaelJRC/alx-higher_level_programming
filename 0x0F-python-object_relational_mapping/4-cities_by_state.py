#!/usr/bin/python3
''' Lists all cities from the database 'hbtn_0e_04usa' 
    This database contains a states(id, name) and cities(id, state_id, name)
    table

    format (city_id, city_name, state_name)
'''
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
        [print(city) for city in cursor.fetchall()]
    except MySQLdb.Error as e:
        print("Error: ", e)
    finally:
        if db:
            db.close()
