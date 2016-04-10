#-*- coding: utf-8 -*-

import urllib2
import sys
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool

class ShinhanCardCrawler:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    cur = c1.conn.cursor()

    def premium(self):
        #프리미엄(VIP)
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/premium/vip/vip.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()

        #프리미엄(platinum)
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/premium/platinum/platinum_list.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()

    #신용카드
    def credit(self):
        #고객혜택별 - 선택형
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/oneself/life.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()


        #고객혜택별 - 성/연령
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/life/life.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()




        #고객혜택별 - 금융/시너지
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/wealth/wealth.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 주유/자동차
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/oil/oil.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 항공/여행
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/go/go.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 생활/쇼핑
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/buy/buy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 문화/레져
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/enjoy/enjoy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 공익/기부
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/impartial/impartial.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 범용
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/benefit/large/large.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #기업제휴 - 금융/시너지
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/business/wealth/wealth.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #기업제휴 - 항공/여행
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/business/go/go.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #기업제휴 - 생활/쇼핑
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/business/buy/buy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #기업제휴 - 문화/레져
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/business/enjoy/enjoy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #기업제휴 - 주유/자동차
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/business/oilcar/oilcar.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #공공 - 정부보조금카드
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/public/gov/gov.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #공공 - 공공기관복지카드
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/public/public/public.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #공공 - 지역특화카드
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/public/local/local.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #공공 - 공공멤버쉽카드
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/public/member/member.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #신한BC
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/major/bc/shinhanbc.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



    #체크카드
    def check(self):
        #고객혜택별 - 선택형
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/select/select.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 성/연령
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/life/life.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 금융/시너지
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/wealth/wealth.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 생활/쇼핑
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/buy/buy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 문화/레져
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/enjoy/enjoy.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 공익/기부
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/impartial/impartial.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 범용
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/large/large.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



        #고객혜택별 - 추천
        html = urllib2.urlopen('https://www.shinhancard.com/conts/person/card_info/rookie/benefit/propose/propose.jsp')
        soup = BeautifulSoup(html, "html5lib")

        itemList = soup.find_all("div",attrs={"class":"cardList"})

        for item in itemList:
            image = "https://www.shinhancard.com" + item.find_all("img")[0]['src']
            title = item.find_all("strong")[0].text.strip()
            summary_list = item.find_all("ul")[0].find_all("li")
            annual_fee = item.find_all("ul")[0].find_all("li")[-1].text.strip()
            brand = ""
            summary = ""
            detail = ""

            for i in range(0,(len(summary_list)-1)):
                summary += summary_list[i].text.replace("\""," ").strip() + "\n"

            html = urllib2.urlopen("https://www.shinhancard.com" + item.find_all("a")[0]['href'])
            soup = BeautifulSoup(html, "html5lib")

            brandList = soup.find_all("ul",attrs={"class":"cardInfoDetail"})[0].find_all("span")
            divClassNameList = []
            divClassName = []

            for item2 in brandList:
                brand += item2.text + " "
            brand.strip()

            for item2 in soup.find_all("div"):
                divClassNameList.append(item2.get("class"))

            for item2 in divClassNameList:
                if type(item2)==list and item2[0]=='cardLook':
                    temp = ""
                    for item3 in item2:
                        temp += item3 + " "
                    divClassName.append(temp[0:-1])

            for item2 in divClassName:
                benefit = soup.find_all("div",attrs={"class":item2})[0]
                if bool(benefit.a):
                    benefit.a.decompose()
                    detail += benefit.text.strip() + "\n"
                else:
                    detail += benefit.text.strip() + "\n"

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"면제\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\"", " ") + "\", " + str(result) + ")")
                self.c1.conn.commit()

                
