#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","Ruby_123","TESTDB")
cursor = db.cursor()

sql="""UPDATE DEPARTMENT SET LOCATION='BANGALORE' WHERE DEPTNO=100"""

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print("Exception ", e)
    print("Type ", type(e))
    db.rollback()


db.close()

