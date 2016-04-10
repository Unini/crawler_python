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






    #신한카드
    shinhan = ShinhanCardCrawler()

    shinhan.premium()
    shinhan.credit()
    shinhan.check()
