#-*- coding: utf-8 -*-

import urllib2
import _mysql
from ConnectionPool import ConnectionPool
from bs4 import BeautifulSoup
import sys
import re

class CardGorillaCrawler:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    def lotteCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=1&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 2);")

            except IndexError:
                break

            i += 16

    def samsungCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=3&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 5);")

            except IndexError:
                break

            i += 16

    def shinhanCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=4&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 9);")

            except IndexError:
                break

            i += 16

    def hyundaiCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=6&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 8);")

            except IndexError:
                break

            i += 16

    def kbCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=7&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 3);")

            except IndexError:
                break

            i += 16

    def nhCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=9&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 7);")

            except IndexError:
                break

            i += 16

    def citiCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=10&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 10);")

            except IndexError:
                break

            i += 16

    def hanaCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=11&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 1);")

            except IndexError:
                break

            i += 16

    def wooriCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=12&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 6);")

            except IndexError:
                break

            i += 16

    def hyundaiDepartmentCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=13&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 8);")

            except IndexError:
                break

            i += 16

    def ibkCredit(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=14&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 0, 4);")

            except IndexError:
                break

            i += 16

    def lotteCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=3&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 2);")

            except IndexError:
                break

            i += 16

    def citiCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=4&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 10);")

            except IndexError:
                break

            i += 16

    def wooriCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=5&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 6);")

            except IndexError:
                break

            i += 16

    def kbCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=6&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 3);")

            except IndexError:
                break

            i += 16

    def hyundaiCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=7&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 8);")

            except IndexError:
                break

            i += 16

    def ibkCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=8&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 4);")

            except IndexError:
                break

            i += 16

    def hanaCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=9&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 1);")

            except IndexError:
                break

            i += 16

    def shinhanCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=10&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 9);")

            except IndexError:
                break

            i += 16

    def nhCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=11&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 7);")

            except IndexError:
                break

            i += 16

    def samsungCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=17&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 5);")

            except IndexError:
                break

            i += 16

    def hyundaistockCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=18&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 8);")

            except IndexError:
                break

            i += 16

    def standardcharteredCheck(self):
        i = 0
        while True:
            html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu07&load=menu07_01_list&card_list=19&cvalue=&sort=1&mode=image&range='+str(i))
            soup = BeautifulSoup(html, "lxml")

            try:
                item_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")

                for k in range(2,18):
                    link = item_list[k].a['href']
                    html = urllib2.urlopen('http://www.card-gorilla.com'+link)
                    soup = BeautifulSoup(html, "lxml")

                    title = soup.find_all("span", attrs={"class":"p13 b gray01 ls-1"})[0].text.strip()
                    image = "http://www.card-gorilla.com"+soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[1].img['src']
                    annual_fee = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[3].text.strip()
                    brand_list = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")
                    brand = ""
                    benefit = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[5].text.strip()

                    for item in brand_list:
                        brand += item['title'] + " "
                    brand.strip()
                    

                    self.c1.conn.query("INSERT INTO card_prods(name, image, type, card_cooperations_id) VALUES(\"" +title+ "\",\""+ image + "\", 1, 11);")

            except IndexError:
                break

            i += 16
