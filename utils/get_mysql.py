#_!/usr/bin/python3
# coding: utf-8

from mysql.mysql_operate import MysqlOperate
from log.log import logging


class GetMysql(object):

    def __init__(self):
        self.opmysql = MysqlOperate()

    def get_data(self,mysql_tb,*args,**kwargs):
        self.mysql_tb = mysql_tb
        try:
            if not (args or kwargs):
                return self.opmysql.sql("select * from " + self.mysql_tb)

            if args or kwargs:
                args_str = ",".join(args)
                kwargs_list = []
                for k,v in kwargs.items():
                    kwargs_list.append(k + "=" + "'" + v + "'")
                kwargs_str =  " and ".join(kwargs_list)
                if not args_str:
                    return self.opmysql.sql("select * from " + self.mysql_tb + " where " + kwargs_str)
                if not kwargs_str:
                    return self.opmysql.sql("select " + args_str + " from " + self.mysql_tb)

                return self.opmysql.sql("select " + args_str + " from " + self.mysql_tb + " where " + kwargs_str)
        except Exception as e:
            logging.error(e)
