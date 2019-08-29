#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","Ruby_123","TESTDB")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS DEPARTMENT")

sql = """CREATE TABLE DEPARTMENT(
DEPTNO INT PRIMARY KEY, DEPTNAME CHAR(20), LOCATION CHAR(20))"""
cursor.execute(sql)

db.close()

