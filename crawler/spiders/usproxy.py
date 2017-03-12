# -*- coding: utf-8 -*-
import scrapy
from crawler.items import ProxyIPItem


class UsproxySpider(scrapy.Spider):
    name = "usproxy"
    allowed_domains = ["https://www.us-proxy.org/"]
    start_urls = ['https://www.us-proxy.org/']

    def parse(self, response):
        for tr in response.xpath('//tr'):
            item = ProxyIPItem()
            try:
                item['ip'] = tr.xpath('td/text()')[0].extract()
                item['port'] = tr.xpath('td/text()')[1].extract()
            except:
                continue
            item['type'] = 'http'
            yield item
