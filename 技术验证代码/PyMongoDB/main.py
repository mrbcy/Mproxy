#-*- coding: utf-8 -*-
import datetime
from pymongo import MongoClient


def insert_user_login_record():
    client = MongoClient('amaster', 27017)
    db = client.test_database
    collection = db.user_login_collection

    record = {'user_name': '张三',
            'last_login_time':datetime.datetime(2017,02,28)}

    collection.insert_one(record)


def find_user_3days_login_record():
    client = MongoClient('amaster', 27017)
    db = client.test_database
    collection = db.user_login_collection

    d = datetime.datetime.now()
    d = d - datetime.timedelta(days=5)
    record = collection.find_one({'user_name': '张三','last_login_time':{"$gt": d}})

    print record
    return record


def update_user_login_time():
    client = MongoClient('amaster', 27017)
    db = client.test_database
    collection = db.user_login_collection

    record = find_user_3days_login_record()

    record['last_login_time'] = datetime.datetime.now()

    collection.save(record)


if __name__ == '__main__':
    update_user_login_time()