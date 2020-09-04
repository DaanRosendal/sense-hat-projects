#!/usr/bin/python3

#
# NAME
#	measure.py - script to store sense hat measurements in SQL database
#
# SYNOPSIS
#	measure.py [-v] [-t interval]
#		-v: verbose
#		-t interval: sample every interval seconds
#
# DESCRIPTION
#	measures temperature data from the raspbery pi sense hat and
#	store data in a local SQL database
#

# import some modules
import sys
import getopt
import sense_hat
import time
import mysql.connector as mariadb
from mysql.connector import errorcode

# sensor name
sensor_name = 'Temperatuur'

# database connection configuration
dbconfig = {
    'user': 'sensem',
    'password': 'h@',
    'host': 'localhost',
    'database': 'weerstation',
    'raise_on_warnings': True,
}

# parse arguments
verbose = True
interval = 10  # second

try:
    opts, args = getopt.getopt(sys.argv[1:], "vt:")
except getopt.GetoptError as err:
    print(str(err))
    print('measure.py -q -t <interval>')
    print('-q: be quiet')
    print('-t <interval>: measure each <interval> seconds (default: 10s)')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-q':
        verbose = False
    elif opt == '-t':
        interval = int(arg)

# instantiate a sense-hat object
sh = sense_hat.SenseHat()

# infinite loop
try:
    while True:
        # instantiate a database connection
        try:
            mariadb_connection = mariadb.connect(**dbconfig)
            if verbose:
                print("Database connected")

        except mariadb.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("Error: {}".format(err))
            sys.exit(2)

        # create the database cursor for executing SQL queries
        cursor = mariadb_connection.cursor(buffered=True)

        # turn on autocommit
        #cursor.autocommit = True

        # get the sensor_id for temperature sensor
        try:
            cursor.execute("SELECT id FROM sensor WHERE naam=%s", [sensor_name])
        except mariadb.Error as err:
            print("Error: {}".format(err))
            sys.exit(2)

        sensor_id = cursor.fetchone()
        if sensor_id is None:
            print("Error: no sensor found with naam = %s" % sensor_name)
            sys.exit(2)

        if verbose:
            print("Reading data from sensor %s with id %s" % (sensor_name, sensor_id[0]))

        # measure temperature
        temp = round(sh.get_temperature(), 1)
	temp = temp - 12

        # verbose
        if verbose:
            print("Temperature: %s C" % temp)

        # store measurement in database
        try:
            cursor.execute('INSERT INTO meting (waarde, sensor_id) VALUES (%s, %s);', (temp, sensor_id[0]))
        except mariadb.Error as err:
            print("Error: {}".format(err))

        else:
            # commit measurements
            mariadb_connection.commit()

            if verbose:
                print("Temperature committed")

            # close db connection
            cursor.close()
            mariadb_connection.close()
            time.sleep(interval)

except KeyboardInterrupt:
    pass

# done
