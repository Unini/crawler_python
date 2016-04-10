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


if __name__ == "__main__":


    #현대카드
    hyundai = HyundaiCardCrawler()

    #hyundai.Black()
    #hyundai.Purple()
    #hyundai.RedEdition2()
    #hyundai.T3Edition2()
    #hyundai.M3Edition2()
    #hyundai.M2Edition2()
    #hyundai.MEdition2()
    hyundai.X2()
    hyundai.X()
    hyundai.Zero()
    #hyundai.MyBusinessCard()
    #hyundai.EmartECard()
    #hyundai.ConnectionCard()
    #hyundai.CheckCard()
    #hyundai.AlphabetCard()
    #hyundai.SpecialCard()


    #네이버카드
    naver = NaverCrawler()

    #naver.CitiCreditCard()
    naver.HyundaiCreditCard()
    #naver.HanaCreditCard()
    #naver.KBCreditCard()
    #naver.ShinhanCreditCard()
    #naver.SamsungCreditCard()
    #naver.LotteCreditCard()
    #naver.WooriCreditCard()
    #naver.NHCreditCard()
    #naver.HDepartCreditCard()
    #naver.IBKCreditCard()

    """
    #하나카드
    hana = HanaCardCrawler()

    hana.CreditCard()
    hana.CheckCard()


    #고릴라카드
    gorilla = CardGorillaCrawler()

    gorilla.lotteCredit()
    gorilla.samsungCredit()
    gorilla.shinhanCredit()
    gorilla.hyundaiCredit()
    gorilla.kbCredit()
    gorilla.nhCredit()
    gorilla.citiCredit()
    gorilla.hanaCredit()
    gorilla.wooriCredit()
    gorilla.hyundaiDepartmentCredit()
    gorilla.ibkCredit()
    gorilla.lotteCheck()
    gorilla.citiCheck()
    gorilla.wooriCheck()
    gorilla.kbCheck()
    gorilla.hyundaiCheck()
    gorilla.ibkCheck()
    gorilla.hanaCheck()
    gorilla.shinhanCheck()
    gorilla.nhCheck()
    gorilla.samsungCheck()
    gorilla.hyundaistockCheck()
    gorilla.standardcharteredCheck()


    #국민카드
    kb = KBCardCrawler()

    kb.credit()
    kb.premium()
    kb.check()
    kb.public()


    #롯데카드
    lotte = LotteCardCrawler()

    lotte.CreditCard()
    #추후에 체크카드 추가하고 마저 완성하기



    #신한카드
    shinhan = ShinhanCardCrawler()

    shinhan.premium()
    shinhan.credit()
    shinhan.check()
    """
