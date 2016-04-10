#-*- coding: utf-8 -*-
from HyundaiCardCrawler import HyundaiCardCrawler
from NaverCrawler import NaverCrawler
from HanaCardCrawler import HanaCardCrawler
from CardGorillaCrawler import CardGorillaCrawler
from KBCardCrawler import KBCardCrawler
from LotteCardCrawler import LotteCardCrawler
from ShinhanCardCrawler import ShinhanCardCrawler
import json
import pymysql
import sys
import urllib
import urllib2
import re
import simplejson as json
from bs4 import BeautifulSoup
from django.utils import encoding
import _mysql

reload(sys)
sys.setdefaultencoding('utf-8')

conn = _mysql.connect('192.168.102.12', 'broccoli', 'broccoli', 'broccoli')

response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=14&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
#data = json.load(response)
raw_data = response.read()
p = re.compile('window.__jindo_callback._cardfinder[0-9]*_[0-9]*[(]')
json_start = p.match(raw_data).end()




#data = "[" + raw_data[json_start:-4] + "]"
data = raw_data[json_start:-4]
#data = json.dumps(data)
data = json.loads(data, strict=False)
data = data['aData']
aData_source = ''.join(data)

pattern = re.compile('<div class="thmb">[\t]+<a href="(http://card.search.naver.com/card.naver[?]where=service&query=[^\"]*)"')
result = pattern.findall(aData_source)

result = [s.encode('ascii') for s in result]


conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")

for r in result:
    response2 = urllib2.urlopen(r)
    soup = BeautifulSoup(response2,"html5lib")
    image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
    title= soup.findAll("h3",attrs={"class":"tit_info"})[0].text
    annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text
    summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.encode('euc-kr')
    detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text


    conn.query("INSERT INTO card_prods(name, image, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", 2)")
