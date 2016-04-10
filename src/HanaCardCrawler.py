#-*- coding: utf-8 -*-
import urllib2
import re
import json
import simplejson as json
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql

class HanaCardCrawler:

    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    def CreditCard(self):

        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "포인트"카드 12개 다 긁어옴
        Hana_CreditPoint_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221205210337514&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditPoint_Html,"lxml")

        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")




        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "항공/여행"카드 2개 다 긁어옴
        Hana_CreditTravel_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221205030423472&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditTravel_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")



        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "통신.인터넷"카드 5개 다 긁어옴
        Hana_CreditInternet_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221205210337291&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditInternet_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")



        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "여성,생활"카드 3개 다 긁어옴
        Hana_CreditWoman_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221506250706271&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditWoman_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")



        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "문화,쇼핑"카드 14개 다 긁어옴
        Hana_CreditShop_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221205030423436&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditShop_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")



        #image,title,detail모두 반복문 통해 하나카드신용카드페이지에 있는 "주유,교통"카드 7개 다 긁어옴
        Hana_CreditTraffic_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=&CT_ID=221205030428263&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CreditTraffic_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 1)")






    def CheckCard(self):

        #image,title,detail모두 반복문 통해 하나카드체크카드 페이지에 있는 "캐쉬백"카드 5개 다 긁어옴
        Hana_CheckCash_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=H&CT_ID=221506250706321')
        soup = BeautifulSoup(Hana_CheckCash_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 1)")



        #image,title,detail모두 반복문 통해 하나카드체크카드 페이지에 있는 "멤버십"카드 5개 다 긁어옴
        Hana_CheckMembership_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=H&CT_ID=221506250706379&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CheckMembership_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 1)")



        #image,title,detail모두 반복문 통해 하나카드체크카드 페이지에 있는 "포인트"카드 3개 다 긁어옴
        Hana_CheckPoint_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=H&CT_ID=221506300803317&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CheckPoint_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 1)")



        #image,title,detail모두 반복문 통해 하나카드체크카드 페이지에 있는 "해외"카드 3개 다 긁어옴
        Hana_CheckAbroad_Html = urllib2.urlopen('https://m.hanacard.co.kr/MWMO210000D.web?CD_TP=H&CT_ID=221506250706412&SEARCH_KEY=&pFlag=&incCK=&_frame=')
        soup = BeautifulSoup(Hana_CheckAbroad_Html,"lxml")
        itemList = soup.findAll("ul",attrs={"class":"card_list_area"})[0].findAll("li")

        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("dt")[0].text.strip()
            summary = item.findAll("dd")[0].text.strip()

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 1)")
