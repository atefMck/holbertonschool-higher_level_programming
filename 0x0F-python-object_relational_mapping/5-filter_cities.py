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
    i = 0
    for row in query_rows:
        if row[0] == row[3]:
            if sys.argv[4] == row[1]:
                print("{}".format(row[4]), end="")
                i = i + 1
                if i != len(row) + 1:
                    print(", ", end="")
                else:
                    print()
    cur.close()
    conn.close()
