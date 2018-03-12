# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request

from movie_spider.items import MovieSpiderItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['http://movie.douban.com//']

    movie_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={start_index}'
    start_index = 0

    def start_requests(self):
        '''
        请求电影内容
        :return:
        '''
        yield Request(self.movie_url.format(start_index=self.start_index),callback=self.parse_data)

    def parse_data(self, response):
        '''
        解析json数据
        :param response:
        :return:
        '''
        result = json.loads(response.text)
        item_list = result.get('data')
        if len(item_list) == 0:
            # 空列表代表解析完成
            return
        for item in item_list:
            movie = MovieSpiderItem()
            # 直接赋值对应字段
            for field in movie.fields:
                if field in item.keys():
                    movie[field] = item.get(field)

            yield item

        # self.start_index += 20
        # yield Request(self.movie_url.format(start_index=self.start_index), callback=self.parse_data)
