#-*- coding: utf-8 -*-
import urllib2
import re
import json
import socket
from bs4 import BeautifulSoup
import _mysql
import sys
import time
from ConnectionPool import ConnectionPool
from NaverCrawler import NaverCrawler

s = socket.socket()
port = 3306
s.bind(('127.0.0.1',3306))

s.connect(('127.0.0.1',3306))

while True:
    c.addr = s.accept()
    c.close()


reload(sys)
sys.setdefaultencoding('utf-8')

c1 = ConnectionPool()
c2 = ConnectionPool()
c1.setDBEncoding()
c2.setDBEncoding()

cur = c1.conn.cursor()
cur2 = c2.conn.cursor()


cur. excute("CREATE TABLE benefits_bak SELECT * FROM benefits")
c1.conn.commit()

# delete benefits
cur.execute("DELETE FROM benefits")
c1.conn.commit()

# run crawler (renew benefits table)
## test
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (800, '카드왕 짱', 1000)")
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (801, '유희왕 딱지zk드 킹왕짱', 1001)")
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (802, '피카츄 딱지ss카드 킹왕짱', 1010)")
c1.conn.commit()

# compare the length of both tables' detail
for row in cur:
    after_length = len(row[0])
    cur2.execute("SELECT detail FROM benefits_bak WHERE card_prods_id = " + str(row[1]))
    result = cur2.fetchall()
    prev_length = len(result[0][0])
    c2.conn.commit()

    if after_length != prev_length:
        # make notice
        ## test
        print str(row[1]) + " card is not same"
        ## real
