# -*- coding: utf-8 -*-
import MySQLdb

from DBUtils.PooledDB import PooledDB
pool = PooledDB(MySQLdb,5,host='localhost',user='root',passwd='sorry',db='jokedb',port=3306,charset="utf8") #5为连接池里的最少连接数

conn = pool.connection()
cur =conn.cursor()
cur.callproc('addJoke',('1000','张三',0,100,100,'测试啊啊啊啊'))

cur.close()
conn.commit()
conn.close()