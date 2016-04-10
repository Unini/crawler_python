#-*- coding: utf-8 -*-

import MySQLdb
import _mysql
import pymysql
import sys

conn = _mysql.connect(host='192.168.102.12', user='broccoli', passwd='broccoli', db='broccoli')
conn.query("insert into card_cooperations values(2, \"bbb\")")
conn.query("select * from card_cooperations")

conn.store_result()

print "sssss"
