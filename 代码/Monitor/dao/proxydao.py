#-*- coding: utf-8 -*-
import traceback

from dao.proxystatus import ProxyStatus
from dbpool.poolutil import PoolUtil
from domain.proxydaoitem import ProxyDaoItem


class ProxyDao:

    def find_proxy_last_validate_time(self):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "select * from proxy_list order by last_validate_time desc limit 1"
            count = cur.execute(sql)
            last_validate_time = None
            if count != 0:
                data = cur.fetchone()
                last_validate_time = data[5]

            cur.close()
            conn.close()
            return last_validate_time
        except Exception as e:
            return None

    def get_avaliable_proxy_count(self):
        try:
            conn = PoolUtil.pool.connection()
            cur = conn.cursor()
            sql = "select count(*) from proxy_list where status = %s"
            count = cur.execute(sql,ProxyStatus.AVAILABLE)
            result = None
            if count != 0:
                data = cur.fetchone()
                result = int(data[0])

            cur.close()
            conn.close()
            return result
        except Exception as e:
            return 0

