#-*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql

class CitiCardCrawler:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    #신용카드
    def credit(self):
        #혜택 - 프리미엄카드

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL503000_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")



        #혜택 - 백화점/쇼핑

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL151000_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #혜택 - 항공마일리지

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL203500_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")

        #혜택 - 포인트/리워드

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL301000_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #혜택 - 할인/캐시백

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL401000_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #혜택 - 전액결제/기타

        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL502000_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 10)")


    #체크카드
    def check(self):
        #화면 상단의 추천카드
        html = urllib2.urlopen('http://www.citicard.co.kr/jsp/crd/apl/apl10/apl1010/APL452500_p1.jsp')
        soup = BeautifulSoup(html, "lxml")

        itemList = soup.find_all("div",attrs={"class":"intro"})[0]

        image = itemList.find_all("img")[0]['src']
        title = itemList.find_all("strong")[0].text.strip()#.encode("euc-kr")
        summaryList = itemList.find_all("li")
        summary = ""

        for summaryContent in summaryList:
            summary += summaryContent.text.strip() + "\n"

        self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 10)")


        #화면 main의 카드 리스트
        itemList = soup.find_all("div",attrs={"class":"sumWrap"})
        summaryList = itemList[0].find_all("li")

        for item in itemList:
            image = item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary = ""
            for summaryContent in summaryList:
                summary += summaryContent.text.strip() + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",1, 10)")
