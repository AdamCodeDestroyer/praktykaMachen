import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktyki"
)

print("Connected:", connection.is_connected())

cursor = connection.cursor()

cursor.execute("SELECT * FROM articlescrapper")

wyniki = cursor.fetchall()

for wiersz in wyniki:
    print(wiersz)

cursor.close()
connection.close()