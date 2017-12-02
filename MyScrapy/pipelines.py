# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

class MyscrapyPipeline(object):
    def __init__(self):
        self.f = open(os.getcwd() + "/result/"+self.__class__.__name__+".txt","w+")

    def process_item(self, item, spider):

        self.f.write(item["a"]+'\n')
        return item

    def close_spider(self, spider):
        self.f.close()
        print "---------------------------"
        pass