import mysql.connector as mysql
from datetime import datetime

mydb = mysql.connect(
  host="192.168.1.75",
  user="kawa",
  password="12345",
  database="test"
)

mycursor = mydb.cursor()

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

sql = "INSERT INTO detection (type, trigTime) VALUES (%s, %s)"
val = (0, timestamp)

try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
except e:
    print('wrong')
    # print(e.message)