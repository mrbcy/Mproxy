#-*- coding: utf-8 -*-
import traceback

from xicidaili.dbpool.poolutil import PoolUtil
from xicidaili.domain.recorditem import RecordItem


class RecordDao:

    def find_record_by_addr(self, proxy_addr):
        ":param proxy_addr format like ip:port"
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "select * from proxy_record where proxy_addr=%s"
            count = cur.execute(sql,(proxy_addr) )
            record_item = None
            if count != 0:
                data = cur.fetchone()
                record_item = RecordItem()
                record_item.proxy_addr = data[0]
                record_item.create_time = data[1]

            cur.close()
            conn.close()
            return record_item
        except Exception as e:
            return None

    def insert_record(self, record_item):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "insert into proxy_record(proxy_addr,create_time) " \
                  "values(%s,%s)"
            cur.execute(sql,(record_item.proxy_addr,record_item.create_time))
            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()