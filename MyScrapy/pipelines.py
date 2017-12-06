# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from MyScrapy.items import ImageaItem
import sqlite3
import os
import MyScrapy.settings as Settings

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

#//ImagesPipeline 自动下载
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if type(item) == ImageaItem and item['img_url'] is not None:
            yield Request(item['img_url'])
        else:
            yield None

    def item_completed(self, results, item, info):
        for ok, x in results:
            if ok and os.path.exists(Settings.IMAGES_STORE + x['path']):
                os.rename(Settings.IMAGES_STORE + x['path'], unicode(Settings.IMAGES_STORE + x['path'].replace('full/', '图片/')))
        return item
