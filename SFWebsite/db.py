#this just needs to be done once to create the db. Can be done using other methods.
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Samabtch$8',
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE StoreFrontDB")
print("Created db")