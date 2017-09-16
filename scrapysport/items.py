# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapysportItem(scrapy.Item):
    # define the fields for your item here like:
   
    
    product_price = scrapy.Field()
    product_name = scrapy.Field()
    product_description = scrapy.Field()
    product_url = scrapy.Field() 
    pass
