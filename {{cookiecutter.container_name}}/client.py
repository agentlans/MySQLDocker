import mysql.connector
from dotenv import dotenv_values

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=dotenv_values(".env")["MYSQL_ROOT_PASSWORD"]
)

print(db)
cur = db.cursor()
cur.execute("SHOW DATABASES")
print("Databases: ")
print([x for x in cur])
db.close()
