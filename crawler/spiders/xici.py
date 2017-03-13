from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from crawler.items import ProxyIPItem

class XiciSpider(Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls_prefix = [
        'http://www.xicidaili.com/nn',
        'http://www.xicidaili.com/nt',
        'http://www.xicidaili.com/wt',
    ]
    start_page = 1
    end_page = 20

    def start_requests(self):
        for prefix in self.start_urls_prefix:
            for page in range(self.start_page, self.end_page + 1):
                url = '{0}/{1}'.format(prefix, page)
                yield Request(url=url, headers={'Referer': prefix})

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]/tr')
        if len(ip_list) > 0:
            ip_list.pop(0)
        for ip in ip_list:
            item = ProxyIPItem()
            item['ip'] = ip.xpath('td[2]/text()').extract()[0]
            item['port'] = ip.xpath('td[3]/text()').extract()[0]
            item['type'] = 'http'
            yield item
