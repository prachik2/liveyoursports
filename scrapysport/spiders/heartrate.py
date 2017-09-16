# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapysport.items import ScrapysportItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

class HeartrateSpider(CrawlSpider):
	name='heartrate'
	allowed_domains=['liveyoursport.com']
	start_urls=['https://www.liveyoursport.com/heart-rate-monitors-1',
				'https://www.liveyoursport.com/heart-rate-monitors-1/?search_query=&page=2',
				'https://www.liveyoursport.com/heart-rate-monitors-1/?search_query=&page=3',
				'https://www.liveyoursport.com/heart-rate-monitors-1/?search_query=&page=4']
	rules=[Rule(SgmlLinkExtractor(allow=('(/products/)')), callback="parse_item")]

	def parse_item(self, response):
		
		item = ScrapysportItem()
		hxs = HtmlXPathSelector(response)
		item['product_name'] = hxs.select('//div[@class="ProductMain"]/h1/text()').extract()
		item['product_price'] = hxs.select('//div[@class="Value"]/em/text()').extract()
		item['product_description'] = hxs.select('//span[@class="prod-descr"]/text()').extract()
		item['product_url'] = response.url
	
		return item