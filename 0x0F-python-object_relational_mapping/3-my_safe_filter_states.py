#!/usr/bin/python3
''' Takes an argumet and displays all values in the states table of a database
    where 'name' matches the argument. This script is safe from MySQL
    injections.

    arguments:
    arg[1]: mysql username
    arg[2]: mysql password
    arg[3]: database name
    arg[4]: state name to search (safe from MySQL injection)
'''
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name=%s COLLATE utf8mb4_bin"

        cursor.execute(query, ('{}'.format(sys.argv[4]),))
        [print(state) for state in cursor.fetchall()]
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if db:
            db.close()
