# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }

    def parse(self, response):
        pass
