import pymysql


conn = None
cur = None
try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test')
    cur = conn.cursor()
    cur.execute("SELECT user_id, user_name FROM cap_user")
    row_count = cur.rowcount
    # row_number = cur.rownumber
    for r in cur.fetchall():
        print("userId is %s, userName is %s" % r)
except Exception as e:
    print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
