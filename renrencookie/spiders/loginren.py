# -*- coding: utf-8 -*-
import scrapy


class LoginrenSpider(scrapy.Spider):
    name = 'loginren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']


    def parse(self, response):
        print(response.request.url)

        yield scrapy.Request(
            url=""
        )
