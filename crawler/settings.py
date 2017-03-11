# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware' : 300,
    'crawler.middleware.random_user_agent.RandomUserAgentMiddleware' : 500,
	# 'crawler.middleware.proxy.StaticProxyMiddleware' : 100 ,
}

ITEM_PIPELINES = {
    'crawler.pipelines.ProxyScanPipeline': 500,
    # 'crawler.pipelines.PrintPipeline': 800,
}

LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1
import urllib2
LOCAL_IP = urllib2.urlopen('http://ifconfig.io/ip').read()[:-1]
# PROXY = "http://61.53.143.179:80"

# used by StaticProxyMiddleware, if you want to crawl through a proxy server
PROXY = "http://localhost:8088"

# used by RandomProxyMiddleware, if you want to crawl through proxy servers
PROXY_LIST = [
	"http://120.83.5.164:18000",
	"http://111.161.126.100:80",
	"http://61.53.143.179:80"
]

RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 405, 408]

# valid proxy saved filename
PROXY_LIST_FILE = 'proxy_list'
