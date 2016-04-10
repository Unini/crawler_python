#-*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

#card_list 1:롯데 3:삼성 4:신한 6:현대 7:KB 9:NH 10:씨티 11:하나 12:우리 13:현대백화점 14:ibk

i = 0
j = 1
while i != 10000:
    html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=7&cvalue=&sort=1&mode=image&range='+str(i))
    soup = BeautifulSoup(html, "lxml")
    try:
        images = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")[0] #페이지의 첫번째 요소가 있는지
        for k in range(2,18):
            try:
                images = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[k].find_all("img")[0] #페이지의 첫번째 요소가 있는지
                cardName = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[k].find_all("span")[0].text.encode("euc-kr")
            except IndexError: #없을경우 indexError
                break
            print j
            print images['src']
            print cardName
            j+=1
    except IndexError: #없을경우 indexError
        print("finish")
        i=10000
    else: #에러 발생하지 않을시 출력
        i += 16




#html = urllib2.urlopen('http://www.card-gorilla.com/sub.php?contents=submenu03&load=menu03_01_list&card_list=7&cvalue=&sort=1&mode=image&range=80')#+str(i)
#soup = BeautifulSoup(html, "lxml")

#print len(str(soup))
#print type(soup)

#images = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("img")[0]
#cardName = soup.find_all("div",attrs={"id":"contents"})[0].find_all("table")[2].find_all("span")[0].text.encode("euc-kr")

#print images[2].find_all("span")[0].text.encode("euc-kr")
