# -*- coding: utf-8 -*-
import scrapy
import re
from crawler.items import ProxyIPItem


class Proxydb(scrapy.Spider):
    name = "proxydb"
    allowed_domains = ["proxydb.net"]
    start_urls = ['http://proxydb.net/?protocol=http&protocol=https'
        '&anonlvl=2&anonlvl=3&anonlvl=4&country=CN&availability=75'
        '&response_time=10']

    def __generateUrl(self, offset):
        return 'http://proxydb.net/?protocol=http' \
            '&anonlvl=2&anonlvl=3&anonlvl=4&country=CN&' \
            'availability=90&response_time=10&offset={0}'.format(offset)

    def parse(self, response):
        num = response.xpath('//div/form/small/text()').extract()[0]
        searchObj = re.search('(\d+)', num)
        for offset in range(0, int(searchObj.group(1)), 50):
            url = self.__generateUrl(offset)
            yield scrapy.Request(url, callback=self.parseDetail)

    def parseDetail(self, response):
        for tr in response.xpath('//tr'):
            item = ProxyIPItem()
            try:
                server = tr.xpath('td/a/text()')[0].extract()
                strs = server.split(':')
                item['ip'] = strs[0]
                item['port'] = strs[1]
            except Exception as e:
                print(e)
                continue
            item['type'] = 'http'
            yield item

