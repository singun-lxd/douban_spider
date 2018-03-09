# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


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
        因为返回的是json格式的数据，所以这里直接通过json.loads获取结果
        :param response:
        :return:
        '''
        # result = json.loads(response.text)
