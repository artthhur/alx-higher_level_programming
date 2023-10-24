#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search.

    Returns:
        None
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
