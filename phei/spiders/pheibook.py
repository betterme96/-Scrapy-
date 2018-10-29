# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request


from phei.items import PheiItem, UrlItem


class PheiSpider(scrapy.Spider):
    name = 'pheibook'
    allowed_domains = ['phei.com.cn']
    start_urls = ['https://www.phei.com.cn/module/goods/searchkey.jsp?searchKey=python']

    def parse(self, response):
        base_url = 'https://www.phei.com.cn'
        url_items = UrlItem()
        url_items["link"] = response.xpath("//span[@class='book_title']/a/@href").extract()
        count=0
        #print("this is parse")
        for i in range(0, len(url_items["link"])):
            url = base_url + url_items["link"][i]
            #print(url)
            count=count+1
            yield Request(url, callback=self.dataparse)
        print(count)
        for i in range(2, 6):
            url = "https://www.phei.com.cn/module/goods/searchkey.jsp?Page=" + str(i) + "&searchKey=python"
            yield Request(url, callback=self.parse)

    def dataparse(self,response):

        item=PheiItem()

        item["title"] = response.xpath("//div[@class='content_book_info']/h1/text()").extract()
        item["author"] = response.xpath("//div[@class='content_book_info']/p[2]/text()").extract()
        item["price"] = response.xpath("//p[@class='book_price']/span/text()").extract()#已获得
        item["pbt"] = response.xpath("//div[@class='content_book_info']/p[3]//span[1]/text()").extract()

        yield item


