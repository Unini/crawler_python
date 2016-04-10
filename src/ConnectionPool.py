#-*- coding: utf-8 -*-

import sys
import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import _mysql

class ConnectionPool:
    def __init__(self):
        self.my_conv = { FIELD_TYPE.LONG: int }
        #self.conn = MySQLdb.connect(conv=self.my_conv, host='192.168.102.12', user='broccoli', passwd='broccoli', db='broccoli_backup')

        ##localDB
        self.conn = MySQLdb.connect(conv=self.my_conv, host='127.0.0.1', user='root', passwd='dbsgl88322!', db='testdb')

    def setDBEncoding(self):
        self.conn.query("set character_set_connection=utf8;")
        self.conn.query("set character_set_server=utf8;")
        self.conn.query("set character_set_client=utf8;")
        self.conn.query("set character_set_results=utf8;")
        self.conn.query("set character_set_database=utf8;")
