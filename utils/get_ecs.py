#!/usr/bin/python3
# coding: utf-8

from api.ecs_api import EcsApi
from mysql.mysql_operate import MysqlOperate
from log.log import logging
from utils.get_mysql import GetMysql

class GetEcs(object):

    def __init__(self):
        self.opmysql = MysqlOperate()
        self.ecs_mysql = GetMysql()
        self.region_list = ["cn-north-1","cn-east-2","cn-south-1"]

    def get_ecs_id_mysql(self,account_name,region):
        self.account_name = account_name
        self.region = region

        try:
            for i in self.region_list:
                if self.region == i:
                    ecs_list = []
                    ecs = self.ecs_mysql.get_data("host_ecs","ecs_id",region=self.region,account_name=self.account_name)
                    for i in ecs:
                        ecs_list.append(i[0])
                    return ecs_list
        except Exception as e:
            logging.error(e)

    def get_ecs(self,account_name,region):
        self.account_name = account_name
        self.region = region

        try:
            for i in self.region_list:
                if self.region == i:
                    __pid_str = "pid" + self.region.replace("-","_")
                    __itoken= self.ecs_mysql.get_data("host_token","token",account_name=self.account_name,region=self.region)
                    __ipid = self.ecs_mysql.get_data("hwaccount_account",__pid_str,account_name=self.account_name)
                    __opecs_api = EcsApi(__itoken[0][0],self.region,__ipid[0][0])
                    return __opecs_api.get_ecs()
        except Exception as e:
            logging.error(e)

    def get_ecs_id(self,account_name,region):
        self.account_name = account_name
        self.region = region

        try:
            for i in self.region_list:
                if self.region == i:
                    __pid_str = "pid" + self.region.replace("-","_")
                    __itoken= self.ecs_mysql.get_data("host_token","token",account_name=self.account_name,region=self.region)
                    __ipid = self.ecs_mysql.get_data("hwaccount_account",__pid_str,account_name=self.account_name)
                    __opecs_api = EcsApi(__itoken[0][0],self.region,__ipid[0][0])
                    return list(__opecs_api.get_ecs().values())
        except Exception as e:
            logging.error(e)

    def get_active_ecs_id(self,account_name,region):
        self.account_name = account_name
        self.region = region

        try:
            for i in self.region_list:
                if self.region == i:
                    __pid_str = "pid" + self.region.replace("-","_")
                    __itoken= self.ecs_mysql.get_data("host_token","token",account_name=self.account_name,region=self.region)
                    __ipid = self.ecs_mysql.get_data("hwaccount_account",__pid_str,account_name=self.account_name)
                    __opecs_api = EcsApi(__itoken[0][0],self.region,__ipid[0][0])
                    return list(__opecs_api.get_active_ecs().values())
        except Exception as e:
            logging.error(e)
