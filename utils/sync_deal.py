#!/usr/bin/python3
# coding: utf-8

from utils.token_mysql import TokenMysql
from mysql.mysql_operate import MysqlOperate
from utils.get_mysql import GetMysql
from utils.get_ecs import GetEcs
from utils.deal_ecs import DealEcs
from log.log import logging
import datetime

class SyncAll(object):

    def __init__(self):
        self.optoken = TokenMysql()
        self.opmysql = MysqlOperate()
        self.opaccount = GetMysql()
        self.opget_ecs = GetEcs()
        self.opdeal_ecs = DealEcs()
        self.utc_time_now = datetime.datetime.strptime(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
        self.utc_time_shut = self.utc_time_now + datetime.timedelta(hours=8)
        self.utc_time_delete = self.utc_time_shut + datetime.timedelta(days=7)
        self.region_list = ["cn-north-1","cn-east-2","cn-south-1"]

    def fill_token(self):
        try:
            n = self.opmysql.sql("select * from host_token")
            account_tuple = self.opaccount.get_data("hwaccount_account","account_name")

            if not n:
                for i in account_tuple:
                    self.optoken.add_mysql_token(i[0])
        except Exception as e:
            logging.error(e)

    def update_token(self):
        try:
            n = self.opmysql.sql("select * from host_token")
            account_tuple = self.opaccount.get_data("hwaccount_account","account_name")

            if n:
                mysql_account = self.opmysql.sql("select account_name from host_token where region='cn-north-1'")
                mysql_account_name = set(list(map(lambda x: x[0],mysql_account)))
                account_name = set(list(map(lambda x: x[0],account_tuple)))
                add_token_account = list(account_name - mysql_account_name)
                update_token_account = list(account_name & mysql_account_name)
                delete_token_account = list(mysql_account_name - account_name)

                for i in delete_token_account:
                    self.opmysql.sql("delete from host_token where account_name=" + "'" + i + "'")
                for i in add_token_account:
                    self.optoken.add_mysql_token(i)
                for i in update_token_account:
                    token_time = self.opmysql.sql("select up_time from host_token where account_name=" + "'" + i + "'" + " and region='cn-north-1'")
                    token_time = token_time[0][0] + datetime.timedelta(hours=23)
                    if self.utc_time_now > token_time:
                        self.optoken.update_mysql_token(i)
        except Exception as e:
            logging.error(e)

    def fill_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            account_tuple =self.opaccount.get_data("hwaccount_account","account_name")

            if not n:
                for region in self.region_list:
                    for account in account_tuple:
                        #return self.utc_time_delete
                        ecs_dict = self.opget_ecs.get_ecs(account[0],region)
                        ecs_list = []
                        for key,value in ecs_dict.items():
                            locals()['ituple%s' %value] = (key,value,region,0,0,0,self.utc_time_shut,self.utc_time_delete,account[0])
                            ecs_list.append(locals()['ituple%s' %value])
                        self.opmysql.sql_many_parm("insert into host_ecs (ecs_name,ecs_id,region,shut_ecs_tag,delete_ecs_tag,ecs_status_tag,ecs_shut_time,ecs_delete_time,account_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",ecs_list)
        except Exception as e:
            logging.error(e)

    def add_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            account_tuple =self.opaccount.get_data("hwaccount_account","account_name")
            if n:
                for region in self.region_list:
                    for account in account_tuple:
                        ecs_dict = self.opget_ecs.get_ecs(account[0],region)
                        ecs_dict_reverse = dict(map(lambda x:(x[1],x[0]),ecs_dict.items()))
                        ecs_id_list = self.opget_ecs.get_ecs_id(account[0],region)
                        ecs_id_mysql_list = self.opget_ecs.get_ecs_id_mysql(account[0],region)

                        add_ecs_list = list(set(ecs_id_list) - set(ecs_id_mysql_list))
                        add_ecs = []

                        for i in add_ecs_list:
                            locals()['ituple%s' %i] = (ecs_dict_reverse[i],i,region,0,0,0,self.utc_time_shut,self.utc_time_delete,account[0])
                            add_ecs.append(locals()['ituple%s' %i])

                        self.opmysql.sql_many_parm("insert into host_ecs (ecs_name,ecs_id,region,shut_ecs_tag,delete_ecs_tag,ecs_status_tag,ecs_shut_time,ecs_delete_time,account_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",add_ecs)
        except Exception as e:
            logging.error(e)

    def update_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            account_tuple =self.opaccount.get_data("hwaccount_account","account_name")
            if n:
                for region in self.region_list:
                    for account in account_tuple:
                        ecs_dict = self.opget_ecs.get_ecs(account[0],region)
                        ecs_dict_reverse = dict(map(lambda x:(x[1],x[0]),ecs_dict.items()))
                        ecs_id_list = self.opget_ecs.get_ecs_id(account[0],region)
                        ecs_id_mysql_list = self.opget_ecs.get_ecs_id_mysql(account[0],region)

                        update_ecs_list = list(set(ecs_id_list) & set(ecs_id_mysql_list))
                        update_ecs = []

                        for i in update_ecs_list:
                            locals()['ituple%s' %i] = (ecs_dict_reverse[i],i)
                            update_ecs.append(locals()['ituple%s' %i])

                        self.opmysql.sql_many_parm("update host_ecs set ecs_name=%s where ecs_id=%s",update_ecs)
        except Exception as e:
            logging.error(e)

    def delete_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            account_tuple =self.opaccount.get_data("hwaccount_account","account_name")
            if n:
                delete_ecs_list = []
                for region in self.region_list:
                    for account in account_tuple:
                        ecs_id_list = self.opget_ecs.get_ecs_id(account[0],region)
                        delete_ecs_list.extend(ecs_id_list)
                ecs_id_mysql_all_list = []
                ecs_id_mysql_all =self.opaccount.get_data("host_ecs","ecs_id")
                for i in ecs_id_mysql_all:
                    ecs_id_mysql_all_list.append(i[0])

                delete_ecs = list(set(ecs_id_mysql_all_list) - set(delete_ecs_list))
                self.opmysql.sql_many_parm("delete from host_ecs where ecs_id=%s",delete_ecs)
        except Exception as e:
            logging.error(e)

    def status_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            account_tuple =self.opaccount.get_data("hwaccount_account","account_name")
            if n:
                delete_ecs_list = []
                for region in self.region_list:
                    for account in account_tuple:
                        active_ecs_id_list = self.opget_ecs.get_active_ecs_id(account[0],region)
                        active_ecs_id_list = self.opget_ecs.get_active_ecs_id(account[0],region)
                        ecs_id_mysql_list = self.opget_ecs.get_ecs_id_mysql(account[0],region)
                        active_ecs = list(set(ecs_id_mysql_list) & set(active_ecs_id_list))
                        shutoff_ecs = list(set(ecs_id_mysql_list) ^ set(active_ecs_id_list))
                        self.opmysql.sql_many_parm("update host_ecs set ecs_status_tag=1 where ecs_id=%s",active_ecs)
                        self.opmysql.sql_many_parm("update host_ecs set ecs_status_tag=0 where ecs_id=%s",shutoff_ecs)
        except Exception as e:
            logging.error(e)

    def delete_time_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            if n:
                mysql_shut_time = dict(map(lambda x: x,self.opmysql.sql("select ecs_id,ecs_shut_time from host_ecs where ecs_shut_time>=ecs_delete_time")))
                mysql_delete_time_list = []

                for k,v in mysql_shut_time.items():
                    v = v + datetime.timedelta(days=7)
                    locals()['ituple%s' %k] = (v,k)
                    mysql_delete_time_list.append(locals()['ituple%s' %k])

                self.opmysql.sql_many_parm("update host_ecs set ecs_delete_time=%s where ecs_id=%s",mysql_delete_time_list)
        except Exception as e:
            logging.error(e)

    def delete_tag_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            if n:
                mysql_delete_time_t = dict(map(lambda x: x,self.opmysql.sql("select ecs_id,ecs_delete_time from host_ecs")))
                mysql_delete_tagon_list = []
                mysql_delete_tagoff_list = []

                for k,v in mysql_delete_time_t.items():
                    if self.utc_time_now > v:
                        locals()['ituple%s' %k] = (1,k)
                        mysql_delete_tagon_list.append(locals()['ituple%s' %k])
                    else:
                        locals()['dwxuple%s' %k] = (0,k)
                        mysql_delete_tagoff_list.append(locals()['dwxuple%s' %k])

                self.opmysql.sql_many_parm("update host_ecs set delete_ecs_tag=%s where ecs_id=%s",mysql_delete_tagon_list)
                self.opmysql.sql_many_parm("update host_ecs set delete_ecs_tag=%s where ecs_id=%s",mysql_delete_tagoff_list)
        except Exception as e:
            logging.error(e)

    def shutoff_tag_ecs(self):
        try:
            n =self.opmysql.sql("select * from host_ecs")
            if n:
                mysql_shut_time_t = dict(map(lambda x: x,self.opmysql.sql("select ecs_id,ecs_shut_time from host_ecs")))
                mysql_shut_tagon_list = []
                mysql_shut_tagoff_list = []

                for k,v in mysql_shut_time_t.items():
                    if self.utc_time_now > v:
                        locals()['ituple%s' %k] = (1,k)
                        mysql_shut_tagon_list.append(locals()['ituple%s' %k])
                    else:
                        locals()['dwxuple%s' %k] = (0,k)
                        mysql_shut_tagoff_list.append(locals()['dwxuple%s' %k])

                self.opmysql.sql_many_parm("update host_ecs set shut_ecs_tag=%s where ecs_id=%s",mysql_shut_tagon_list)
                self.opmysql.sql_many_parm("update host_ecs set shut_ecs_tag=%s where ecs_id=%s",mysql_shut_tagoff_list)
        except Exception as e:
            logging.error(e)

    def deal_ecs(self):
        try:
            n = self.opmysql.sql("select * from host_ecs")
            account_tuple = self.opaccount.get_data("hwaccount_account","account_name")

            if n:
                for region in self.region_list:
                    for account in account_tuple:
                        shut_ecs_id_list = []
                        delete_ecs_id_list = []
                        shut_ecs_id = self.opaccount.get_data("host_ecs","ecs_id",account_name=account[0],region=region,shut_ecs_tag="1")
                        delete_ecs_id = self.opaccount.get_data("host_ecs","ecs_id",account_name=account[0],region=region,delete_ecs_tag="1")
                        for i in shut_ecs_id:
                            shut_ecs_id_list.append(i[0])
                        self.opdeal_ecs.shutoff_ecs(account[0],region,shut_ecs_id_list)

                        for j in delete_ecs_id:
                            delete_ecs_id_list.append(j[0])
                        self.opdeal_ecs.delete_ecs(account[0],region,delete_ecs_id_list)
        except Exception as e:
            logging.error(e)
