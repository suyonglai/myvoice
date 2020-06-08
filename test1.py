# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy import Request
from anjuke.items import AnjukeItem
import re
import lxml
import time
urls=[]
for i in range(1, 80):
    urllist = 'https://www.fuxianhu.com/forum-62-' + str(i) + '.html'
    url_respons = requests.get(urllist).content.decode()

    url_20 =re.findall('<a href="thread(.*?).html" onclick"',url_respons)
    for url_one in url_20:
        urls.append('https://www.fuxianhu.com/thread' +url_one + '.html')
    with open('urls.csv', 'w') as f:
            f.writelines(urls)
            f.close()
            #yield scrapy.Request(url)'''