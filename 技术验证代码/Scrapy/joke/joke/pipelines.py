# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from DBUtils.PooledDB import PooledDB


class JokePipeline(object):
    def process_item(self, item, spider):
        return item


class JokeFilePipeLine(object):
    def __init__(self):
        self.file = open('d:/jokes', 'wb')

    def process_item(self, item, spider):
        line = "%s\t%s\t%s\t%s\t%s\t%s\n" % (item['joke_id'],
                                             item['user_name'],
                                             item['up_vote_num'],
                                             item['down_vote_num'],
                                             item['comment_num'],
                                             item['joke_text'])
        self.file.write(line.encode("utf-8"))
        return item

class JokeMySqlPipeLine(object):
    def __init__(self):
        self.pool = PooledDB(MySQLdb,5,host='localhost',user='root',passwd='sorry',db='jokedb',port=3306,charset="utf8")

    def process_item(self, item, spider):
        conn = self.pool.connection()
        cur = conn.cursor()
        cur.callproc('addJoke', (item['joke_id'], item['user_name'], int(item['up_vote_num']),
                                 int(item['down_vote_num']), int(item['comment_num']), item['joke_text']))

        cur.close()
        conn.commit()
        conn.close()

