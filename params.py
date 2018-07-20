# -*- coding:utf8 -*-
"""搜狗搜索时需要的param"""
import re
import sys
import time
import random
import requests
sys.setrecursionlimit(10000000)


def get_token_id(uid):
    """
    初始化时喂一个uid，递归生成，
    :param uid:
    :return:
    """
    login_url = "https://www.sogou.com/web?"
    params = {
        "query": 333,
        "_asf": "www.sogou.com",
        "_ast": 1488955851,
        "w": "01019900",
        "p": "40040100",
        "ie": "utf8",
        "from": "index-nologin"
    }
    cookie = "ABTEST=0|1510641197|v1;IPLOC=CN3301;SUID="
    cookie += uid
    cookie += ";PHPSESSID=rfrcqafv5v74hbgpt98ah20vf3;SUIR=1510641197"
    headers = {
        "Cookie": cookie
    }
    try:
        r = requests.head(login_url, headers=headers, params=params).headers
    except Exception, e:
        "token id error with {}".format(e)
        r = ''
    if not r:
        return

    result = re.findall(r'SNUID=[0-9a-zA-Z]+;', r)
    result = result[0] if result else ''
    return result


def get_suv():
    """SUV获取方式"""
    suv = int(time.time()*1000)*1000 + random.randint(1, 1000)
    return suv
