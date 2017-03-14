# -*- coding: utf-8 -*-
import scrapy
import json
from crawler.items import ProxyIPItem


class HidesterSpider(scrapy.Spider):
    name = "hidester"
    allowed_domains = ["hidester.com"]
    start_urls = [
        'https://hidester.com/proxydata/php/data.php?mykey=data&offset=0&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2',
        'https://hidester.com/proxydata/php/data.php?mykey=data&offset=1&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2',
        'https://hidester.com/proxydata/php/data.php?mykey=data&offset=1&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2',
        'https://hidester.com/proxydata/php/data.php?mykey=data&offset=2&limit=10&orderBy=latest_check&sortOrder=DESC&country=&port=&type=undefined&anonymity=undefined&ping=undefined&gproxy=2',
]
    headers = {
        'Host': 'hidester.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer': 'https://hidester.com/proxylist/',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    }
    cookies = {
        '_gat': '1',
        ' _icl_current_language': 'en',
        '_ga': 'GA1.2.1804354853.1489153944',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, cookies=self.cookies)

    def parse(self, response):
        try:
            proxies = json.loads(response.text)
            for proxy in proxies:
                item = ProxyIPItem()
                item['ip'] = proxy['IP']
                item['port'] = proxy['PORT']
                item['type'] = 'http'
                yield item
            pass
        except:
            pass
