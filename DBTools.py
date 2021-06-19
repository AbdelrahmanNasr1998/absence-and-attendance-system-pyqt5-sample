import mysql.connector

all_err = ""
# - Database Connect
try:
    conn = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        passwd   = "",
        database = "Project"
    )
    print(conn)

except mysql.connector.Error as err:
    all_err += str(err) + " , "

def dbrun(sql):
    all_err = ""
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            return True
        else:
            return False
    except mysql.connector.Error as err:
        all_err += str(err) + " , "
        return False

def dbget(sql):
    all_err = ""
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute(sql)
            all_rows = cur.fetchall()
            return all_rows
        else:
            return []
    except mysql.connector.Error as err:
        all_err += str(err) + " , "
        return []

def dbautonum(table,column):
    all_err = ""
    try:
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute("SELECT MAX(%s)+1 FROM %s" % (column,table))
            row = cur.fetchone()
            if row[0]==None:
                return "1"
            else:
                return row[0]
        else:
            return ""
    except mysql.connector.Error as err:
        all_err += str(err) + " , "
        return ""