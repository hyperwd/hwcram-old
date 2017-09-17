#!/usr/bin/python3
# coding: utf-8
'''
# =============================================================================
#      FileName: conf.py
#          Desc: 提供get_conf方法,读取配置文件
#        Author: Dong Wei Chao, dwx411174
#         Email: dongweichao@huawei.com
#      HomePage: 
#       Version: 0.0.1
#    LastChange: 2017-07-26 11:50:17
#       History:
# =============================================================================
'''

import configparser
import os

#获取conf配置文件
def get_conf(sec,confFile="/opt/hwcram/conf/cram.conf"):
    strpath = os.path.abspath(confFile)
    if not os.path.exists(strpath):
        raise Exception('%s is not exist'%(strpath))

    cf = configparser.ConfigParser()
    cf.read(confFile)
    secs = cf.sections()
    if sec not in secs:
        raise Exception('%s is not in secs:%s'%(sec,str(secs)))

    items = cf.items(sec)
    idict = {}
    for e in items:
        idict[e[0]]=e[1]
    return idict
