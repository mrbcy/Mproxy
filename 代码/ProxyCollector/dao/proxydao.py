#-*- coding: utf-8 -*-
import traceback

from dao.proxystatus import ProxyStatus
from dbpool.poolutil import PoolUtil
from domain.proxydaoitem import ProxyDaoItem


class ProxyDao:

    def find_proxy_by_addr(self, proxy_addr):
        ":param proxy_addr format like ip:port"
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "select * from proxy_list where proxy_addr=%s"
            count = cur.execute(sql,(proxy_addr) )
            proxy_dao_item = None
            if count != 0:
                data = cur.fetchone()
                proxy_dao_item = ProxyDaoItem()
                proxy_dao_item.proxy_addr = data[0]
                proxy_dao_item.location = data[1]
                proxy_dao_item.anonymity = data[2]
                proxy_dao_item.type = data[3]
                proxy_dao_item.create_time = data[4]
                proxy_dao_item.last_validate_time = data[5]
                proxy_dao_item.retry_count = data[6]
                proxy_dao_item.last_available_time = data[7]
                proxy_dao_item.status = data[8]

            cur.close()
            conn.close()
            return proxy_dao_item
        except Exception as e:
            return None

    def find_proxy_need_to_recheck(self,timestamp):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "select * from proxy_list where last_validate_time < %s and status != %s limit 500"
            count = cur.execute(sql,(timestamp,ProxyStatus.PERMANENT_UNAVAILABLE) )
            proxy_dao_items = None
            if count != 0:
                proxy_dao_items = []
                result = cur.fetchall()
                for data in result:
                    proxy_dao_item = ProxyDaoItem()
                    proxy_dao_item.proxy_addr = data[0]
                    proxy_dao_item.location = data[1]
                    proxy_dao_item.anonymity = data[2]
                    proxy_dao_item.type = data[3]
                    proxy_dao_item.last_validate_time = data[4]
                    proxy_dao_item.retry_count = data[5]
                    proxy_dao_item.last_available_time = data[6]
                    proxy_dao_item.status = data[7]
                    proxy_dao_items.append(proxy_dao_item)
            cur.close()
            conn.close()
            return proxy_dao_items
        except Exception as e:
            return None

    def insert_proxy(self, dao_item):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "insert into proxy_list(proxy_addr,location,anonymity,type,create_time,last_validate_time,retry_count,last_available_time,status) " \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,(dao_item.proxy_addr,dao_item.location,dao_item.anonymity,dao_item.type,dao_item.create_time,
                             dao_item.last_validate_time,dao_item.retry_count,
                             dao_item.last_available_time,dao_item.status))
            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()
            traceback.print_exc()

    def update_proxy(self, dao_item):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "update proxy_list set location = %s,anonymity = %s,type = %s,create_time = %s,last_validate_time = %s,retry_count = %s,last_available_time = %s,status = %s where proxy_addr=%s"
            cur.execute(sql,(dao_item.location,dao_item.anonymity,dao_item.type,dao_item.create_time,dao_item.last_validate_time,dao_item.retry_count,
                             dao_item.last_available_time,dao_item.status,dao_item.proxy_addr))
            cur.close()
            conn.commit()
            conn.close()
        except Exception as e:
            traceback.print_exc()