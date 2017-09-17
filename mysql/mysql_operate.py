#!/usr/bin/python3
# coding: utf-8

import conf.conf as conf
import log.log as log
import pymysql

hw_conf = conf.get_conf("database")

class MysqlOperate(object):

    def __init__(self,host=hw_conf["dbhost"],user=hw_conf["dbuser"],password=hw_conf["dbpassword"],port=int(hw_conf["dbport"]),dbname=hw_conf["dbname"],charset=hw_conf["dbcharset"]):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__dbname = dbname
        self.__charset = charset

    def __conn_mysql(self):
        try:
            self.__co = pymysql.connect(host=self.__host,user=self.__user,passwd=self.__password,port=self.__port,db=self.__dbname,charset=self.__charset)
            return self.__co
        except Exception as e:
            log.logging.error(e)

    def sql_parm(self,sql_str,data_tuple):
        self.sql_str = sql_str
        self.data_tuple = data_tuple
        self.__conn = self.__conn_mysql()
        self.__curs = self.__conn.cursor()

        try:
            res = self.__curs.execute(self.sql_str,self.data_tuple)
            self.__conn.commit()
            return res
        except Exception as e:
            log.logging.error(e)
        finally:
            self.__curs.close()
            self.__conn.close()

    def sql_many_parm(self,sql_str,data_tuple_list):
        self.sql_str = sql_str
        self.data_tuple_list = data_tuple_list
        self.__conn = self.__conn_mysql()
        self.__curs = self.__conn.cursor()

        try:
            res = self.__curs.executemany(self.sql_str,self.data_tuple_list)
            self.__conn.commit()
            return res
        except Exception as e:
            log.logging.error(e)
        finally:
            self.__curs.close()
            self.__conn.close()

    def sql(self,sql_str):
        self.sql_str = sql_str
        self.__conn = self.__conn_mysql()
        self.__curs = self.__conn.cursor()

        try:
            res = self.__curs.execute(self.sql_str)
            fc = self.__curs.fetchall()
            self.__conn.commit()
            if "select" in self.sql_str:
                return fc
            else:
                return res
        except Exception as e:
            log.logging.error(e)
        finally:
            self.__curs.close()
            self.__conn.close()
