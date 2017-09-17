#!/usr/bin/python3
# coding: utf-8

from api.ecs_api import EcsApi
from mysql.mysql_operate import MysqlOperate
from log.log import logging
from utils.get_mysql import GetMysql

class DealEcs(object):

    def __init__(self):
        self.opmysql = MysqlOperate()
        self.ecs_mysql = GetMysql()
        self.region_list = ["cn-north-1","cn-east-2","cn-south-1"]

    def shutoff_ecs(self,account_name,region,ecs_id):
        self.account_name = account_name
        self.region = region
        self.ecs_id = ecs_id

        try:
            for i in self.region_list:
                if self.region == i:
                    __pid_str = "pid" + self.region.replace("-","_")
                    __itoken= self.ecs_mysql.get_data("host_token","token",account_name=self.account_name,region=self.region)
                    __ipid = self.ecs_mysql.get_data("hwaccount_account",__pid_str,account_name=self.account_name)
                    __opecs_api = EcsApi(__itoken[0][0],self.region,__ipid[0][0])
                    return __opecs_api.shutoff_ecs(self.ecs_id)
        except Exception as e:
            logging.error(e)

    def delete_ecs(self,account_name,region,ecs_id):
        self.account_name = account_name
        self.region = region
        self.ecs_id = ecs_id

        try:
            ilist = []
            for i in self.region_list:
                if self.region == i:
                    __pid_str = "pid" + self.region.replace("-","_")
                    __itoken= self.ecs_mysql.get_data("host_token","token",account_name=self.account_name,region=self.region)
                    __ipid = self.ecs_mysql.get_data("hwaccount_account",__pid_str,account_name=self.account_name)
                    __opecs_api = EcsApi(__itoken[0][0],self.region,__ipid[0][0])
                    for i in self.ecs_id:
                        n = __opecs_api.delete_ecs(i)
                        ilist.append(n)
                    return ilist
        except Exception as e:
            logging.error(e)
