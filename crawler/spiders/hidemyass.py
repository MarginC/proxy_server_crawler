# -*- coding: utf-8 -*-
import scrapy


class HidemySpider(scrapy.Spider):
    name = "hidemy"
    allowed_domains = ["hidemy.name"]
    start_urls = [
        'https://hidemy.name/en/proxy-list/?maxtime=2000&type=hs&anon=234&start=0#list',
        'https://hidemy.name/en/proxy-list/?maxtime=2000&type=hs&anon=234&start=64#list',
        'https://hidemy.name/en/proxy-list/?maxtime=2000&type=hs&anon=234&start=128#list',
        'https://hidemy.name/en/proxy-list/?maxtime=2000&type=hs&anon=234&start=192#list',
    ]

    def parse(self, response):
        ip_list = response.xpath('//table[@class="proxy__t"]/tbody/tr')
        for ip in ip_list:
            item = ProxyIPItem()
            item['ip'] = ip.xpath('td[0]/text()').extract()[0]
            item['port'] = ip.xpath('td[1]/text()').extract()[0]
            item['type'] = 'http'
            yield item
