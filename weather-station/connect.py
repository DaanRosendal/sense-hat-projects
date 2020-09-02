#!/usr/bin/python3

# import connection module; name it mariadb
import mysql.connector as mariadb

# connect to the database
mariadb_connection = mariadb.connect(
    user='aart',
    password='sesamopenu',
    database='sesamstraat')

# create a cursor object for executing queries
cursor = mariadb_connection.cursor()

# prepare a select query
stmt = "SELECT naam FROM pop WHERE id=%s"

# we want this id
id = 2

# execute the query (parameter must be a tuple)
cursor.execute(stmt, [id])

# print returned row (a tuple)
row = cursor.fetchone()
print("id: %s, naam: %s" % (id, row[0]))

# close cursor and database
cursor.close()
mariadb_connection.close()

# done
print("Einde script")
