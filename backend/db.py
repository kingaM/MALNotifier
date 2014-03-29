# EXAMPLE
#
# from db import DBHelper
# db = DBHelper()
# print db.retrieveData("SELECT * FROM `users`", ())

import MySQLdb as mdb

class DBHelper:

    try:
        con = mdb.connect(host = '127.0.0.1', user = 'root', passwd = 'root', db = 'MALNotifier')
    except Exception, e:
        print e

    def executeQuery(self, query, args=()):
        cursor = DBHelper.con.cursor()
        cursor.execute(query, args)
        id = cursor.lastrowid
        cursor.close()
        DBHelper.con.commit()
        return id

    def retrieveData(self, query, args=()):
        cursor = DBHelper.con.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        cursor.close()
        return rows
