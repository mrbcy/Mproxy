#-*- coding: utf-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB

from conf.configloader import ConfigLoader


class PoolUtil:
    config_loader = ConfigLoader()
    pool = PooledDB(MySQLdb, 5, host=config_loader.get_mysql_host(),
                    user=config_loader.get_mysql_user(), passwd=config_loader.get_mysql_pwd(),
                    db=config_loader.get_mysql_db_name(), port=config_loader.get_mysql_port(), charset="utf8")
