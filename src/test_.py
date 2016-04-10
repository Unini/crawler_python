#-*- coding: utf-8 -*-
import urllib2
import re
import json
import simplejson as json
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql



reload(sys)
sys.setdefaultencoding('utf-8')

c1 = ConnectionPool()
c1.setDBEncoding()
cur = c1.conn.cursor()



Hyundai_X2_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=C&cardWcd=XP')
soup = BeautifulSoup(Hyundai_X2_Html,"html5lib")
image = soup.findAll("span",attrs={"class":"photo"})[0].findAll("img")[0]['src']
title = soup.findAll("p",attrs={"class":"info1"})[0].findAll("strong")[0].text.strip()
summary=""
annual_fee=""
itemList = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].findAll("li")
for item in itemList:
    summary += item.text.strip()

annual_fee_List = soup.findAll("ul",attrs={"class":'info2 txt-type5 info-detail'})[0].findAll("li")
for fees in annual_fee_List:
    annual_fee += fees.text.strip()

print title, summary, annual_fee
