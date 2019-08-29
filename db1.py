#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","Ruby_123","TESTDB")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print "Database version : %s " % data

db.close()

