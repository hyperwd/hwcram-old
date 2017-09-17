#!/usr/bin/python3
# coding: utf-8
from api.token_api import TokenApi
from mysql.mysql_operate import MysqlOperate
from log.log import logging
from utils.get_mysql import GetMysql
import datetime

class TokenMysql(object):

    def __init__(self):
        self.opmysql = MysqlOperate()
        self.opaccount = GetMysql()
        self.region_list = ["cn-north-1","cn-east-2","cn-south-1"]

    def get_mysql_token(self,mysql_tb,*args,**kwargs):
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

    def add_mysql_token(self,account_name):
        self.account_name = account_name
        self.__account = self.opaccount.get_data("hwaccount_account","user_name","password",account_name=self.account_name)
        self.user_name = self.__account[0][0]
        self.__password = self.__account[0][1]
        self.utc_time_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        try:
            for i in self.region_list:
                token = TokenApi(self.account_name,self.user_name,self.__password,i).get_token()
                self.opmysql.sql_parm("insert into host_token (token,region,up_time,account_name) values (%s,%s,%s,%s)",(token,i,self.utc_time_now,self.account_name))
        except Exception as e:
            logging.error(e)

    def update_mysql_token(self,account_name):
        self.account_name = account_name
        self.__account = self.opaccount.get_data("hwaccount_account","user_name","password",account_name=self.account_name)
        self.user_name = self.__account[0][0]
        self.__password = self.__account[0][1]
        self.utc_time_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        try:
            for i in self.region_list:
                token = TokenApi(self.account_name,self.user_name,self.__password,i).get_token()
                self.opmysql.sql_parm("update host_token set token=%s,up_time=%s where account_name=%s and region=%s",(token,self.utc_time_now,self.account_name,i))
        except Exception as e:
            logging.error(e)

    def delete_mysql_token(self,account_name):
        self.account_name = account_name
        try:
            self.opmysql.sql("delete from host_token where account_name=" + self.account_name)
        except Exception as e:
            logging.error(e)
