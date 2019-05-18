# -*- coding: utf-8 -*-
import re
import json
import extruct
import scrapy
from it_rally.items import ItRallyItem


class InstagramSpider(scrapy.Spider):
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = [
        'https://www.instagram.com/spacex/',
        'https://www.instagram.com/twitter/',
        'https://www.instagram.com/virgingalactic/',
        'https://www.instagram.com/arianespace/',
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'ROBOTSTXT_OBEY': False,
        # 'JOBDIR': f'jobs/{name}',
    }

    def parse(self, response):
        json_ld = extruct.extract(response.body.decode(), base_url=response.url)['json-ld'][0]
        item = ItRallyItem(company_type='')
        item['name'] = json_ld['name']
        item['description'] = json_ld['description']
        item['url'] = json_ld['url']
        item['favicon'] = json_ld['image']
        info = self._find_json(response)['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']

        image_urls = [
            i['node']['display_url']
            for i in info['edges']
        ]
        item['image_urls'] = image_urls
        yield item

    def _find_json(self, response):
        script = response.xpath('.//script[contains(text(), "window._sharedData =")]/text()').extract_first()
        raw_data = re.search(r'window\._sharedData = (\{.*\})', script).group(1)
        return json.loads(raw_data)


