# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _fieldnames = ['coname', 'coinfo', 'vocation', 'description']
    courlid = scrapy.Field()
    coname = scrapy.Field()
    coinfo = scrapy.Field()
    vocation = scrapy.Field()
    description = scrapy.Field()
    pass
