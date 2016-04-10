#-*- coding: utf-8 -*-
import urllib2
import re
import json
import simplejson as json
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql

class HyundaiCardCrawler:

    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()
    cur = c1.conn.cursor()
    
    def Black(self):
        # 현대카드Black Crawler
        Hyundai_Black_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=M&cardWcd=TB')
        soup = BeautifulSoup(Hyundai_Black_Html,"lxml")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()






    def Purple(self):
        # 현대카드Purple Crawler
        Hyundai_Purple_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=M&cardWcd=TP')
        soup = BeautifulSoup(Hyundai_Purple_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()



    def RedEdition2(self):
        # 현대카드 red deition2
        Hyundai_Red_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=M&cardWcd=TRE2')
        soup = BeautifulSoup(Hyundai_Red_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()



    def T3Edition2(self):
        # 현대카드 T3 Edition2
        Hyundai_T3Edition_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=T3PE2')
        soup = BeautifulSoup(Hyundai_T3Edition_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()




    def M3Edition2(self):
        Hyundai_M3Edition_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=M3PE2')
        soup = BeautifulSoup(Hyundai_M3Edition_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()



    def M2Edition2(self):
        Hyundai_M2Edition_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=MPE2')
        soup = BeautifulSoup(Hyundai_M2Edition_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()



    def MEdition2(self):
        Hyundai_MEdition_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=P&cardWcd=ME2')
        soup = BeautifulSoup(Hyundai_MEdition_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()




    def X2(self):
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()



    def X(self):
        Hyundai_X_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=C&cardWcd=XP')
        soup = BeautifulSoup(Hyundai_X_Html,"html5lib")
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

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()




    def Zero(self):
        Hyundai_Zero_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag=C&cardWcd=ZRO')
        soup = BeautifulSoup(Hyundai_Zero_Html,"html5lib")
        image = soup.findAll("span",attrs={"class":"photo"})[0].findAll("img")[0]['src']
        title = soup.findAll("p",attrs={"class":"info1"})[0].findAll("strong")[0].text.strip()
        summary=""
        annual_fee=""
        itemList = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].findAll("li")
        for item in itemList:
            summary += item.text.strip()

        annual_fee_List = soup.findAll("ul",attrs={"class":'info2 txt-type6 info-detail'})[0].findAll("li")
        for fees in annual_fee_List:
            annual_fee += fees.text.strip()

        self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
        if bool(self.cur.fetchone()):
            pass
        else:
            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            result = str(self.cur.fetchone()[0])
            self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
            #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
            self.c1.conn.commit()












    def MyBusinessCard(self):

        #Premium Card
        Hyundai_MyBusinessCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
        soup = BeautifulSoup(Hyundai_MyBusinessCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard201"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:
            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"

            Hyundai_MyBusinessCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_MyBusinessCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #PointCard
        Hyundai_MyBusinessCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
        soup = BeautifulSoup(Hyundai_MyBusinessCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard202"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_MyBusinessCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_MyBusinessCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #CashbackCard
        Hyundai_MyBusinessCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
        soup = BeautifulSoup(Hyundai_MyBusinessCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard203"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_MyBusinessCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_MyBusinessCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1




    def EmartECard(self):

        #Emart신용 Platinum My Business Card
        Hyundai_EmartECard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=E#popDetailCard')
        soup = BeautifulSoup(Hyundai_EmartECard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard301"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_EmartECard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_EmartECard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Emart CheckCard
        Hyundai_EmartECard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=E#popDetailCard')
        soup = BeautifulSoup(Hyundai_EmartECard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard302"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_EmartECard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_EmartECard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


    def ConnectionCard(self):

        #CommuniacationCard
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard501"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Car Card
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard502"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Oil Card
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard503"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Life Card
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard504"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Shopping Card
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard505"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Finance Card
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard506"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #EtcCard
        Hyundai_ConnectionCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=J#popDetailCard')
        soup = BeautifulSoup(Hyundai_ConnectionCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard507"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_ConnectionCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_ConnectionCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1





    def CheckCard(self):

        #Hybrid Card
        Hyundai_CheckCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=C#popDetailCard')
        soup = BeautifulSoup(Hyundai_CheckCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard601"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_CheckCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_CheckCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Check Card
        Hyundai_CheckCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=C#popDetailCard')
        soup = BeautifulSoup(Hyundai_CheckCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard602"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_CheckCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_CheckCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #Check Card(connection)
        Hyundai_CheckCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=C#popDetailCard')
        soup = BeautifulSoup(Hyundai_CheckCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard603"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_CheckCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_CheckCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


        #HyundaiC Card
        Hyundai_CheckCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=C#popDetailCard')
        soup = BeautifulSoup(Hyundai_CheckCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard604"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_CheckCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_CheckCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


    def AlphabetCard(self):
        Hyundai_AlphabetCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=A#popDetailCard')
        soup = BeautifulSoup(Hyundai_AlphabetCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard701"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_AlphabetCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_AlphabetCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1




        Hyundai_AlphabetCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=A#popDetailCard')
        soup = BeautifulSoup(Hyundai_AlphabetCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard702"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_AlphabetCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_AlphabetCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1




        Hyundai_AlphabetCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=A#popDetailCard')
        soup = BeautifulSoup(Hyundai_AlphabetCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard703"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_AlphabetCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_AlphabetCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1




        Hyundai_AlphabetCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=A#popDetailCard')
        soup = BeautifulSoup(Hyundai_AlphabetCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard704"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_AlphabetCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_AlphabetCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1






    def SpecialCard(self):
        Hyundai_SpecialCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0631_10.hc')
        soup = BeautifulSoup(Hyundai_SpecialCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard0307"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_SpecialCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_SpecialCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1



        Hyundai_SpecialCard_Html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0631_10.hc')
        soup = BeautifulSoup(Hyundai_SpecialCard_Html,"html5lib")

        itemList = soup.findAll("div",attrs={"id":"tabCard0302"})[0].findAll("ul",attrs={"class":"card-info2 card-info2-2"})[0].findAll("li")


        num = 0
        for item in itemList:


            image = item.findAll("img")[0]['src']
            title = item.findAll("strong")[0].text.strip()


            html = urllib2.urlopen('https://www.hyundaicard.com/cpc/cr/CPCCR0621_11.hc?cardflag=M#popDetailCard')
            htmlsource = html.read()
            p = re.compile("javascript:detailCard[(\']+([\w]+)[\', ]+([\w]+)[\');]+")

            cardflag = p.findall(htmlsource)[num][0]
            cardWcd = p.findall(htmlsource)[num][1]
            newurl = "https://www.hyundaicard.com/cpc/cr/CPCCR0201_01.hc?cardflag="+cardflag+"&cardWcd="+cardWcd + "&eventCode=00000"


            Hyundai_SpecialCard_Detail_Html = urllib2.urlopen(newurl)
            soup = BeautifulSoup(Hyundai_SpecialCard_Detail_Html,"html5lib")

            annual_fee = soup.findAll("ul",attrs={"class":"info2 txt-type5 info-detail"})[0].text.strip()
            #summary = soup.findAll("ul",attrs={"class":"info2 txt-type2"})[0].text.encode('euc-kr')
            #summary = soup.findAll("p",attrs={"class":"info2"})[0].text.encode('euc-kr')
            summary = soup.findAll("ul",attrs={"class":"info2"})[0].text.strip()
            detail = soup.findAll()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                #c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()

            num = num+1


# 마지막으로 앱카드는 넣지 않았음!
