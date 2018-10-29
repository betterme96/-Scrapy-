# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class PheiPipeline(object):
    def process_item(self, item, spider):
        # 自己先把数据库完全建好
        conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="pheibooks", port=3306)
        cur = conn.cursor()
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            author = item["author"][i]
            pbt = item["pbt"][i]
            price = item["price"][i]

            sql = "insert into goods(title,author,pbt,price) values('" + title + "','" + author + "','" + pbt + "','" + price + "')"

            cur.execute(sql)
            conn.commit()

        conn.close()
        return item
