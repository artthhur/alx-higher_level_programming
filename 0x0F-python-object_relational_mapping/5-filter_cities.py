#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state.

    Returns:
        None
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    crsr = db.cursor()
    crsr.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in crsr.fetchall() if ct[4] == sys.argv[4]]))
