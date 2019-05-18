# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from scrapy.utils.project import get_project_settings


class ItRallyImageDataToCSVPipeline:

    settings = get_project_settings()
    fieldnames = ['checksum', 'path', 'url']

    def open_spider(self, spider):
        self._file = open(f'{self.settings["RESULT_DIR"]}/image_csv_result/image.csv', 'w')
        self.writer = csv.DictWriter(self._file, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self._file.close()

    def process_item(self, item, spider):
        for i in item['images']:
            self.writer.writerow(i)
        # Item must be returned. Because it's using in following pipelines
        return item


class ItRallyDoNothingPipeline:

    def process_item(self, item, spider):
        return item
