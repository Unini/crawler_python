#-*- coding: utf-8 -*-
import urllib2
import re
import json
from bs4 import BeautifulSoup
import _mysql
import sys
from ConnectionPool import ConnectionPool


class NaverCrawler:
#4:씨티 5:현대 6:국민 7:하나 8:신한 9:삼성 10:롯데 11:우리 12:농협 13:현대백화점 14:기업

    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()
    cur = c1.conn.cursor()

    def CitiCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=4&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 10);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()




    def HyundaiCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=5&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()




    def KBCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=6&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 3);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()





    def HanaCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=7&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 1);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def ShinhanCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=8&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 9);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def SamsungCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=9&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 5);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail.replace("\""," ") + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def LotteCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=10&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 2);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def WooriCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=11&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.replace("\"","\'").strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 6);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()




    def NHCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=12&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 7);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def HDepartCreditCard(self):

        response = urllib2.urlopen('http://card.search.naver.com/card.naver?&_callback=window.__jindo_callback._cardfinder9195_0&benfIdList=&tagIdList=&isMobileCard=0&mrcIdList=&cardCoIdList=13&brandIdList=&cardType=&annualFeeRangeIdList=&recordCondRangeIdList=&order=pop&oe=json&where=service&anq=0&query=%EC%8B%A0%ED%95%9C%20%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C&ssc=&affiliateBenefitType=&start=1&display=1000')
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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 8);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()



    def IBKCreditCard(self):

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


        for r in result:
            response2 = urllib2.urlopen(r)
            soup = BeautifulSoup(response2,"html5lib")
            image = soup.findAll("div",attrs={"class":"thmb"})[0].findAll("img")[0]['src']
            title = soup.findAll("h3",attrs={"class":"tit_info"})[0].text.strip()
            annual_fee = soup.findAll("div",attrs={"class":"info_a"})[0].findAll("dd",attrs={"class":"fee"})[0].text.strip()
            summary = soup.findAll("dd",attrs={"class":"dsc"})[0].text.strip()
            detail = soup.findAll("div",attrs={"class":"_detail_1 sum_one sum_one_v1 _tab_detail"})[0].findAll("tbody")[0].text.strip()

            self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
            if bool(self.cur.fetchone()):
                pass
            else:
                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\", \""+ summary +"\", 0, 4);")
                self.cur.execute("SELECT id FROM card_prods WHERE name=\'"+ title.encode("utf-8", "ignore")+"\'")
                result = str(self.cur.fetchone()[0])
                self.c1.conn.query("INSERT INTO annual_fees VALUES(" + result + ", \"" + annual_fee + "\")")
                self.c1.conn.query("INSERT INTO benefits(detail, card_prods_id) VALUES(\"" + detail + "\", " + str(result) + ")")
                self.c1.conn.commit()




"""
tempData = ""

data = raw_data[json_start:-4]
data = json.loads(data, strict=False)

for i in range(0, len(data['aData'])):
    tempData += data['aData'][i].encode("euc-kr")

soup = BeautifulSoup(tempData, "html5lib")
itemList = soup.find_all("div", attrs={"class":"thmb"})

for item in itemList:
    source = list()
    source = item.a['href']
    print source
"""
