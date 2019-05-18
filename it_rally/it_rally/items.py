# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItRallyItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    favicon = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    company_type = scrapy.Field()
