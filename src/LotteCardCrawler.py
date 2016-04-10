#-*- coding: utf-8 -*-
import urllib
import urllib2
import simplejson as json
from bs4 import BeautifulSoup
from ConnectionPool import ConnectionPool
import sys
import _mysql

class LotteCardCrawler:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    c1 = ConnectionPool()
    c1.setDBEncoding()

    def CreditCard(self):

        #기본 페이지 JSP띄우는 부분
        url = 'http://www.lottecard.co.kr/app/IHCDAAA_P110.do'
        values = {
            'cate1':'',
            'cate2':'',
            'cate1_nm':'',
            'cate2_nm':'전체',
            'page_no':1,
            'isImgList':'Y',
            'cond':1,
            'card_path':'/UploadFiles/ecenterPath/cdInfo/',
            'crd_ofr_fc':'01',
            'pers_url':'www.lottecard.co.kr',
            'vt_cd_knd_c':'',
            'isDet':'N',
            'search_option':1,
            'all_search':'',
            'ex_search':'',
            'ex_srch_cd_nm':'',
            'ex_cond':'',
            'ex_crd_ofr_fc':'',
            'ex_isImgList':'',
            'ex_search_option':'',
            'cardName':'',
            'cardCd':'',
            'search_option_flag_value':1,
            'srch_cd_nm':''
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()

        data = json.loads(result, strict=False)
        total_page = data['Param']['totCnt'] / data['Param']['credit'] + 1
        data = data['Content']
        content = ''.join(data)

        soup = BeautifulSoup(content, "html5lib")


        #for page in range(1,total_page+1):   여기는 페이징 처리하는 for문

        url = 'http://www.lottecard.co.kr/app/IHCDAAA_P110.do'
        values = {
            'cate1':'',
            'cate2':'',
            'cate1_nm':'',
            'cate2_nm':'전체',
            'page_no':1,
            'isImgList':'Y',
            'cond':1,
            'card_path':'/UploadFiles/ecenterPath/cdInfo/',
            'crd_ofr_fc':'01',
            'pers_url':'www.lottecard.co.kr',
            'vt_cd_knd_c':'',
            'isDet':'N',
            'search_option':1,
            'all_search':'',
            'ex_search':'',
            'ex_srch_cd_nm':'',
            'ex_cond':'',
            'ex_crd_ofr_fc':'',
            'ex_isImgList':'',
            'ex_search_option':'',
            'cardName':'',
            'cardCd':'',
            'search_option_flag_value':1,
            'srch_cd_nm':''
        }
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()

        itemList = soup.findAll("ul",attrs={"class":"clfix"})[0].findAll("li",recursive=False)

        #한 페이지 내에서 카드 긁어오는 부분
        for item in itemList:
            title = item.findAll('strong',attrs={'class':'cardname'})[0].text.strip()
            image = "http://www.lottecard.co.kr"+item.findAll("span",attrs={"class":"thumb"})[0].findAll("img")[0]['src']
            summary = item.findAll("div",attrs={"class":"cardlist_more"})[0].findAll("dd")[0].text.strip()
            annual_fee = item.findAll("div",attrs={"class":"cardlist_more"})[0].findAll("dd")[-1].text.encode('euc-kr')



            self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 2)")

        """
            #상세페이지 들어가는 부분
            url = 'http://www.lottecard.co.kr/app/IHCDAAA_V200.do'
            values = {
                'cate1':'',
                'cate2':'',
                'cate1_nm':'',
                'cate2_nm':'전체',
                'page_no':1,
                'isImgList':'Y',
                'cond':1,
                'srch_cd_nm':'',
                'vt_cd_knd_c':'P11015-A11015',
                'isDet':'Y',
                'frv_seq':'',
                'frv_dc':'2',
                'all_search':'',
                'cardName':'올마이쇼핑+카드+(교통),롯데+VEEX+카드,Driving+Pass+카드,롯데포인트+플러스+카드,엠비에이(MBA)+카드,캐시백+플러스+카드(백화점+마트),포인트플러스+GRANDE카드,DC스마트+카드,롯데+Two+in+One+카드,포인트플러스+포텐+카드,VEEX+플래티넘+카드,DC++Supreme+카드',
                'cardCd':'P11015-A11015,P01472-A01472,P01350-A01350,P00276-A00276,P10798-A10798,P10828-A10828,P02483-A02483,P00878-A00878,P03080-A03080,P02632-A02632,P02137-A02137,P01131-A01131',
                'int_booth_mob_app_only_isyn':'Y',
                'int_booth_mob_app_only_ar_phc':''
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = response.read()

            data = json.loads(result, strict=False)
            total_page = data['Param']['totCnt'] / data['Param']['credit'] + 1
            data = data['Content']
            content = ''.join(data)

            soup = BeautifulSoup(content, "html5lib")

            datail = soup.findAll("a",attrs={"class":"first"})[0].findAll("h4")[0].text.encode('euc-kr')




            print title, summary, annual_fee, image, detail
        """




        """
        for page in range(1,total_page+1):
            url = 'http://www.lottecard.co.kr/app/IHCDAAA_V200.do'
            values = {
                'cate1':'',
                'cate2':'',
                'cate1_nm':'',
                'cate2_nm':'전체',
                'page_no':1,
                'isImgList':'Y',
                'cond':1,
                'srch_cd_nm':'',
                'vt_cd_knd_c':'P11015-A11015',
                'isDet':'Y',
                'frv_seq':'',
                'frv_dc':'2',
                'all_search':'',
                'cardName':'올마이쇼핑+카드+(교통),롯데+VEEX+카드,Driving+Pass+카드,롯데포인트+플러스+카드,엠비에이(MBA)+카드,캐시백+플러스+카드(백화점+마트),포인트플러스+GRANDE카드,DC스마트+카드,롯데+Two+in+One+카드,포인트플러스+포텐+카드,VEEX+플래티넘+카드,DC++Supreme+카드',
                'cardCd':'P11015-A11015,P01472-A01472,P01350-A01350,P00276-A00276,P10798-A10798,P10828-A10828,P02483-A02483,P00878-A00878,P03080-A03080,P02632-A02632,P02137-A02137,P01131-A01131',
                'int_booth_mob_app_only_isyn':'Y',
                'int_booth_mob_app_only_ar_phc':''
            }
        """




















#ConnectionCard 부분 json 부분에서 에러납니다 line211에서



"""

        def ConnectionCard(self):

        #기본 페이지 JSP띄우는 부분
            url = 'http://www.lottecard.co.kr/app/IHCDAAA_V102.do'
            values = {
                'cate1':'',
                'cate2':'',
                'cate1_nm':'',
                'cate2_nm':'전체',
                'page_no':1,
                'isImgList':'Y',
                'cond':1,
                'card_path':'/UploadFiles/ecenterPath/cdInfo/',
                'crd_ofr_fc':'01',
                'pers_url':'www.lottecard.co.kr',
                'vt_cd_knd_c':'',
                'isDet':'N',
                'search_option':1,
                'all_search':'',
                'ex_search':'',
                'ex_srch_cd_nm':'',
                'ex_cond':'',
                'ex_crd_ofr_fc':'',
                'ex_isImgList':'',
                'ex_search_option':'',
                'cardName':'',
                'cardCd':'',
                'search_option_flag_value':1,
                'srch_cd_nm':''
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = response.read()

            data = json.loads(result, strict=False)
            total_page = data['Param']['totCnt'] / data['Param']['credit'] + 1
            data = data['Content']
            content = ''.join(data)

            soup = BeautifulSoup(content, "html5lib")


            #for page in range(1,total_page+1):   여기는 페이징 처리하는 for문

            url = 'http://www.lottecard.co.kr/app/IHCDAAA_V102.do'
            values = {
                'cate1':'',
                'cate2':'',
                'cate1_nm':'',
                'cate2_nm':'전체',
                'page_no':1,
                'isImgList':'Y',
                'cond':1,
                'card_path':'/UploadFiles/ecenterPath/cdInfo/',
                'crd_ofr_fc':'01',
                'pers_url':'www.lottecard.co.kr',
                'vt_cd_knd_c':'',
                'isDet':'N',
                'search_option':1,
                'all_search':'',
                'ex_search':'',
                'ex_srch_cd_nm':'',
                'ex_cond':'',
                'ex_crd_ofr_fc':'',
                'ex_isImgList':'',
                'ex_search_option':'',
                'cardName':'',
                'cardCd':'',
                'search_option_flag_value':1,
                'srch_cd_nm':''
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = response.read()

            itemList = soup.findAll("ul",attrs={"class":"clfix"})[0].findAll("li",recursive=False)

            #한 페이지 내에서 카드 긁어오는 부분
            for item in itemList:
                title = item.findAll('strong',attrs={'class':'cardname'})[0].text.strip()
                image = "http://www.lottecard.co.kr"+item.findAll("span",attrs={"class":"thumb"})[0].findAll("img")[0]['src']
                summary = item.findAll("div",attrs={"class":"cardlist_more"})[0].findAll("dd")[0].text.strip()
                annual_fee = item.findAll("div",attrs={"class":"cardlist_more"})[0].findAll("dd")[-1].text.encode('euc-kr')



                self.c1.conn.query("INSERT INTO card_prods(name, image, summary, type, card_cooperations_id) VALUES(\"" + title + "\",\""+ image + "\",\"" + summary + "\",0, 8)")





"""
