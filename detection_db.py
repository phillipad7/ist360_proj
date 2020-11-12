import mysql.connector as mysql
from datetime import datetime
'''
MySQL DB: test
Table: detection(rid, type, trigTime)
rid: auto inc
type: 0:human 1:cat 2:err
trigTime: current time
'''

db = mysql.connect(
    host="192.168.1.75",
    user="kawa",
    password="12345",
    database="test"
)

cur = db.cursor()


def insert(type):
    query = "INSERT INTO detection (type, trigTime) VALUES (%s, %s)"
    val = (0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        cur.execute(query, val)
        db.commit()
        print(cur.rowcount, "record inserted\n")
    except:
        print('ERR: cannot insert')


def fetch():
    td = datetime.now()
    ytd = td.replace(day=td.day-1) 

    result = []

    try:
        cur.execute("SELECT * FROM detection where trigTime>%s and trigTime<%s", (ytd, td))
        # result is list of tuple
        result = cur.fetchall()
        
    except:
        print('ERR: cannot retrieve')
    finally:
        return result

if __name__=='__main__':
    print('\n*********************start*************\n')
    a = fetch()
    print(a)

