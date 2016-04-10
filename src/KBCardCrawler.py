#-*- coding: utf-8 -*-

import urllib2
import re
import sys
from ConnectionPool import ConnectionPool
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql

class KBCardCrawler:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    def credit(self):
        html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0047.cms')
        soup = BeautifulSoup(html, "html5lib")

        link_list = soup.find_all("ul", attrs={"class":"cardList_tab credit"})[0].find_all("li")

        for item in link_list:
            html = urllib2.urlopen('https://card.kbcard.com'+item.a['href'])
            soup = BeautifulSoup(html, "html5lib")

            item_list = soup.find_all("div", attrs={"class":"infoCard"})

            for item2 in item_list:
                value_list = item2.find_all("a")[0]['onclick']
                value = re.findall('[0-9]+|[A-Z][0-9]+', value_list)

                html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode='+value[0]+'&categoryCode='+value[1]+'&sGroupCode='+value[2])
                soup = BeautifulSoup(html, "html5lib")

                title = soup.find_all("h1", attrs={"class":"tit"})[0].text.strip()
                image = soup.find_all("p", attrs={"class":"img"})[0].find_all("img")[0]['src']
                brand_list = soup.find_all("dl", attrs={"class":"cardBrand"})[0].find_all("img")
                annual_fee = soup.find_all("dl", attrs={"class":"cardFee"})[0].find_all("dd")[0].text.strip()
                brand = []
                benefit_summary = soup.find_all("div", attrs={"class":"wrap"})
                summary = ""
                detail = ""
                div_id_list = []

                for item3 in brand_list:
                    brand.append(item3['alt'])

                for item3 in benefit_summary:
                    summary += item3.text.strip() + "\n"

                for item3 in soup.find_all("div"):
                    if type(item3.get("id"))==unicode and bool(re.findall('tabCon01[0-9]', item3.get("id"))):
                        div_id_list.append(item3.text.strip())

                for item3 in div_id_list:
                    detail += item3 + "\n"

                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 3);")

    def premium(self):
        html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0055.cms')
        soup = BeautifulSoup(html, "html5lib")

        link_list = soup.find_all("ul", attrs={"class":"cardList_tab premium"})[0].find_all("li")

        for item in link_list:
            html = urllib2.urlopen('https://card.kbcard.com'+item.a['href'])
            soup = BeautifulSoup(html, "html5lib")

            item_list = soup.find_all("div", attrs={"class":"infoCard"})

            for item2 in item_list:
                value_list = item2.find_all("a")[0]['onclick']
                value = re.findall('[0-9]+|[A-Z][0-9]+', value_list)

                html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode='+value[0]+'&categoryCode='+value[1]+'&sGroupCode='+value[2])
                soup = BeautifulSoup(html, "html5lib")

                title = soup.find_all("h1", attrs={"class":"tit"})[0].text.strip()
                image = soup.find_all("p", attrs={"class":"img"})[0].find_all("img")[0]['src']
                brand_list = soup.find_all("dl", attrs={"class":"cardBrand"})[0].find_all("img")
                annual_fee = soup.find_all("dl", attrs={"class":"cardFee"})[0].find_all("dd")[0].text.strip()
                brand = []
                benefit_summary = soup.find_all("div", attrs={"class":"wrap"})
                summary = ""
                detail = ""
                div_id_list = []

                for item3 in brand_list:
                    brand.append(item3['alt'])

                for item3 in benefit_summary:
                    summary += item3.text.strip() + "\n"

                for item3 in soup.find_all("div"):
                    if type(item3.get("id"))==unicode and bool(re.findall('tabCon01[0-9]', item3.get("id"))):
                        div_id_list.append(item3.text.strip())

                for item3 in div_id_list:
                    detail += item3 + "\n"

                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 3);")

    def check(self):
        html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0056.cms')
        soup = BeautifulSoup(html, "html5lib")

        link_list = soup.find_all("ul", attrs={"class":"cardList_tab check"})[0].find_all("li")

        for item in link_list:
            html = urllib2.urlopen('https://card.kbcard.com'+item.a['href'])
            soup = BeautifulSoup(html, "html5lib")

            item_list = soup.find_all("div", attrs={"class":"infoCard"})

            for item2 in item_list:
                value_list = item2.find_all("a")[0]['onclick']
                value = re.findall('[0-9]+|[A-Z][0-9]+', value_list)

                html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode='+value[0]+'&categoryCode='+value[1]+'&sGroupCode='+value[2])
                soup = BeautifulSoup(html, "html5lib")

                title = soup.find_all("h1", attrs={"class":"tit"})[0].text.strip()
                image = soup.find_all("p", attrs={"class":"img"})[0].find_all("img")[0]['src']
                brand_list = soup.find_all("dl", attrs={"class":"cardBrand"})[0].find_all("img")
                annual_fee = soup.find_all("dl", attrs={"class":"cardFee"})[0].find_all("dd")[0].text.strip()
                brand = []
                benefit_summary = soup.find_all("div", attrs={"class":"wrap"})
                summary = ""
                detail = ""
                div_id_list = []

                for item3 in brand_list:
                    brand.append(item3['alt'])

                for item3 in benefit_summary:
                    summary += item3.text.strip() + "\n"

                for item3 in soup.find_all("div"):
                    if type(item3.get("id"))==unicode and bool(re.findall('tabCon01[0-9]', item3.get("id"))):
                        div_id_list.append(item3.text.strip())

                for item3 in div_id_list:
                    detail += item3 + "\n"

                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 1, 3);")

    def public(self):
        html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0062.cms')
        soup = BeautifulSoup(html, "html5lib")

        item_list = soup.find_all("div", attrs={"class":"infoCard"})

        for item in item_list:
            value_list = item.find_all("a")[0]['onclick']
            value = re.findall('[0-9]+|[A-Z][0-9]+', value_list)

            html = urllib2.urlopen('https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode='+value[0]+'&categoryCode='+value[1]+'&sGroupCode='+value[2])
            soup = BeautifulSoup(html, "html5lib")

            title = soup.find_all("h1", attrs={"class":"tit"})[0].text.strip()
            image = soup.find_all("p", attrs={"class":"img"})[0].find_all("img")[0]['src']
            brand_list = soup.find_all("dl", attrs={"class":"cardBrand"})[0].find_all("img")
            annual_fee = soup.find_all("dl", attrs={"class":"cardFee"})[0].find_all("dd")[0].text.strip()
            brand = []
            benefit_summary = soup.find_all("div", attrs={"class":"wrap"})
            summary = ""
            detail = ""
            div_id_list = []

            for item3 in brand_list:
                brand.append(item3['alt'])

            for item3 in benefit_summary:
                summary += item3.text.strip() + "\n"

            for item3 in soup.find_all("div"):
                if type(item3.get("id"))==unicode and bool(re.findall('tabCon01[0-9]', item3.get("id"))):
                    div_id_list.append(item3.text.strip())

            for item3 in div_id_list:
                detail += item3 + "\n"

            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", \""+ summary +"\", 0, 3);")
