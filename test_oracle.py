import cx_Oracle


conn = None
cur = None

host = "127.0.0.1"
port = 1521
dbname = "orclgbk"
username = "JDCSJSB"
userpwd = "jdcsjsb"
try:
    dsn = cx_Oracle.makedsn(host, port, dbname)
    conn = cx_Oracle.connect(username, userpwd, dsn)
    cur = conn.cursor()
    cur.execute("SELECT * FROM A1_DW")
    row_count = cur.rowcount
    # row_number = cur.rownumber
    for r in cur.fetchall():
        # print("userId is %s, userName is %s" % r)
        print(r)
except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
