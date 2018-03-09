# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieSpiderItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    cover = scrapy.Field()
    rate = scrapy.Field()
    star = scrapy.Field()
    casts = scrapy.Field()
    directors = scrapy.Field()
