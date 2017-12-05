# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys

from MyScrapy.spiders.haha import HahaSpider
from MyScrapy.spiders import JieKou
import sqlite3
import os
reload(sys)
sys.setdefaultencoding('utf8')

class MyscrapyFilePipeline(object):
    def __init__(self):
        self.f = open(os.getcwd() + "/result/" + self.__class__.__name__ + ".txt", "w+")

    def process_item(self, item, spider):
        if spider.name == 'haha':
            self.f.write(item["a"] + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()



class MyscrapyDBPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite3")

    def process_item(self, item, spider):
        if spider.name == 'haha':
            cursor = self.conn.cursor()
            sqlstr = """insert into biaoqian (name, a) VALUES (?, ?)"""
            # param = (unicode(item['name']), unicode(item['a']))
            param = (item['name'], item['a'])
            cursor.execute(sqlstr, param)
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()
