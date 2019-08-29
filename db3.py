#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","Ruby_123","TESTDB")
cursor = db.cursor()

sql="""INSERT INTO DEPARTMENT(DEPTNO, DEPTNAME, LOCATION) values (100,'Production','Mumbai')"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


db.close()

