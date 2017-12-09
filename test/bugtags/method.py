# -*- coding: utf-8 -*-

import db_my
import json
import random
import time
import urllib2
page = 1
def get_Main(browser, id, load_pages = 5, load_all=False, load_user=False, detay_rand = 0.2):
    global page

    while True:
        url = 'https://work.bugtags.com/api/apps/'+str(id)+'/issues/?page=' + str(page)
        print '---url--get_Main', url
        browser.get(url)

        time.sleep(random.random() * detay_rand)
        # time.sleep(20)
        jsonp = json.loads(browser.find_element_by_css_selector('body').text)
        print '---json--->', jsonp
        try:
            jsons = jsonp['data']['list']
            print '---page', page, '----len', len(jsons)
        except:
            print '---page', page, '----失败'
            break
        page += 1
        ids = db_my.sava_db_main(jsons)
        if load_all or load_user:
            for child_id in ids:
                get_tags(browser,pid=id, id=child_id, load_user=load_user)

        # if not jsonp['data']['has_more']:
        #     break
        if len(jsons) < 20 or page > load_pages: #取前5页
            break




page_tags = 1
def get_tags(browser,pid,id,load_user=False, detay_rand = 0.2):
    global page_tags
    index = 1

    while True:
        url = 'https://work.bugtags.com/api/apps/'+str(pid)+'/issues/'+str(id)+'/crashes/?page=' + str(page_tags)
        print '---url--get_tags', url
        browser.get(url)

        time.sleep(random.random() * detay_rand)
        # time.sleep(20)
        jsonp = json.loads(browser.find_element_by_css_selector('body').text)
        print '---json--->', jsonp
        try:
            jsons = jsonp['data']['list']
            print '---page', page-1, '--index', index, '---page_tags', page_tags, '----len', len(jsons), '---id', id
        except:
            print '---page', page-1, '--index', index, '---page_tags', page_tags, '----失败'
            continue
        page_tags += 1

        user_datas =db_my.sava_db_tags(jsons)

        if load_user:
            get_user_datas(browser, user_datas)

        if not jsonp['data']['has_more']:
            page_tags = 1
            index += 1
            break


def get_user_datas(browser, user_datas, detay_rand = 0.2):
    if len(user_datas)==0:
        return
    for tagid, user_url in user_datas:
        print '---url--get_user_data', user_url
        f = urllib2.urlopen(user_url, timeout=30)

        data = f.read()

        time.sleep(random.random() * detay_rand)
        jsonp = json.loads(data)
        if not len(jsonp):
            print '---json--->', '[]'
            continue
        print '---json--->', jsonp
        jsonp['tagid'] = str(tagid)
        db_my.sava_db_user_data(jsonp)
