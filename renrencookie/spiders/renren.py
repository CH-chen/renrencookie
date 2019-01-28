# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/969574735/profile']
                ##个人的人人网主页，直接请求会不成功，需要登录

    def start_requests(self):
        #获取主页的cookie,转换成字典
        cookies = "anonymid=jrg1i50g-7eexp6; depovince=GW; _r01_=1; JSESSIONID=abcj8H8oNBjFffnOJDtIw; ick_login=28035622-0567-4fce-84e7-d2288596f877; ick=e87f9e28-7f1c-4695-a9d5-fc686c74327c; t=11361863ad1785a9ff8498bf8234feee5; societyguester=11361863ad1785a9ff8498bf8234feee5; id=969574735; xnsid=6c889a8c; XNESSESSIONID=7c09723b7d13; jebecookies=0ddc7c08-3ad5-4317-ac36-836ee3c863d4|||||; ver=7.0; loginfrom=null; jebe_key=bf038be3-3e55-4c02-8325-1e6a7938dc70%7Cbb223f6876cd2eb89db3a027b645f7ee%7C1548662439565%7C1%7C1548662439242; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )


    def parse(self, response):
        print("===========")
        print(re.findall("陈陈",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/969574735/profile?v=info_timeline", #再请求一下个人资料页面
            callback=self.parse_detail

        )
        yield scrapy.Request(
            "http://friend.renren.com/managefriends",  # 再请求一下朋友页面
            callback=self.parse_detail

        )
    def parse_detail(self,response):
        print(re.findall("陈陈", response.body.decode()))
        print("++++++++")
        print(re.findall("公司全称", response.body.decode()))
