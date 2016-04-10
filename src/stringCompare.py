#-*- coding: utf-8 -*-
import urllib2
import re
import json
from bs4 import BeautifulSoup
import _mysql
import sys
import time
from ConnectionPool import ConnectionPool
from NaverCrawler import NaverCrawler


reload(sys)
sys.setdefaultencoding('utf-8')

c1 = ConnectionPool()
c2 = ConnectionPool()
c1.setDBEncoding()
c2.setDBEncoding()
cur = c1.conn.cursor()
cur2 = c2.conn.cursor()

# copy benefits table to benefits_bak
cur.execute("CREATE TABLE benefits_bak SELECT * FROM benefits")
c1.conn.commit()

# delete benefits
cur.execute("DELETE FROM benefits")
c1.conn.commit()

# run crawler (renew benefits table)
## test
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (800, '카드왕 짱', 1000)")
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (801, '유희왕 킹왕짱', 1001)")
cur.execute("INSERT INTO benefits(id, detail, card_prods_id) VALUES (802, '피카츄드 킹왕짱', 1010)")
cur.execute("INSERT INTO beneifts(id, detail, card_prods_id) VALUES (804, '치카치카 카드짱', 1011)")
c1.conn.commit()


# select columns(detail, card_prods_id) from benefits
cur.execute("SELECT detail, card_prods_id FROM benefits")
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


# delete benefits_bak
cur.execute("DROP TABLE benefits_bak")
c1.conn.commit()

c1.conn.close()
c2.conn.close()
