#!/usr/bin/python3

# import connection module; name it mariadb
import mysql.connector as mariadb

# connect to the database
mariadb_connection = mariadb.connect(
    user='sien',
    password='sesamopenu',
    database='sesamstraat')

# create a cursor object for executing queries
cursor = mariadb_connection.cursor()

# read name
naam = input("Geef een sesamstraatpoppennaam:")

# prepare a select query
stmt = "INSERT INTO pop (Naam) VALUES (%s);"

# execute the query (parameter must be a tuple)
cursor.execute(stmt, [naam])
mariadb_connection.commit()

# prepare a select query
stmt = "SELECT * FROM pop;"

# execute the query (parameter must be a tuple)
cursor.execute(stmt)

# print returned rows
row = cursor.fetchone()
while row is not None:
    print("id: %s, naam: %s" % (row[0], row[1]))
    row = cursor.fetchone()

# close cursor and database
cursor.close()
mariadb_connection.close()

# done
print("Einde script")
