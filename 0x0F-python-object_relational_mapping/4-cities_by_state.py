#!/usr/bin/python3
''' Module to print all states '''
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states,cities ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[0] == row[3]:
            print("({}, '{}', '{}')".format(row[2], row[4], row[1]))
    cur.close()
    conn.close()
