# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from movie_spider import utils


class MovieSpiderPipeline(object):
    def __init__(self, result_path):
        self.file_path = result_path
        self.file = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            result_path=crawler.settings.get('RESULT_PATH'),
        )

    def open_spider(self, spider):
        self.file = open(self.file_path, 'a', encoding="utf-8")

    def close_spider(self, spider):
        if self.file is not None:
            self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False, default=utils.object2dict) + "\n")
        return item
