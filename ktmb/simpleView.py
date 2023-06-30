import sqlite3
from sqlite3 import Error
        
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

m = []

conn = create_connection("./db_folder/ktmb.db")
with conn:
    cur = conn.cursor()
    cur.execute("SELECT queryTime, trainDate, depTime, arrTime, price, seats FROM kl_bm WHERE trainDate = '13/07/2023';")

    rows = cur.fetchall()

    for row in rows:
        t = list(row)
        t[1] = f"{t[1]} || {t[2]}-{t[3]}"
        t.pop(2); t.pop(2)
        m.append(t)
    
    
seen = []    
for i in m: #max control
    if i[1] in seen:
        break
    seen.append(i[1])
    print(i[1])
    #traverse list (actual)
    for j in m:
        if j[1] == i[1]:
            print(f"        {j[0].split(' ')[0]}  {j[-1]}")
    print("\n\n")
    
#if at any point seats hit less than 100 i need to be notified