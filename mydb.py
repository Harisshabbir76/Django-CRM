import mysql.connector

dataBase = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Harisshabbir76',
    port='3306',
    auth_plugin='mysql_native_password'
)


cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM")

print("ALL DONE!")