#!/usr/bin/env python

import requests
import json
import time
import datetime
import os

path = '/home/dmr/.cache/corona.json'


def isExit():
    """
    function: 判断缓存是否存在且及时
    returns: bool
    """
    if not os.path.exists(path):
        return True
    filetime = time.strftime(
        '%Y-%m-%d-%H', time.localtime(os.stat(path).st_mtime))
    today = datetime.datetime.now().strftime('%Y-%m-%d-%H')
    if today.__eq__(filetime):
        return False
    return True


def getCase():
    """
    function: 获取肺炎
    returns: 现存确诊，现存疑似，新增确诊，新增死亡
    """
    if isExit():
        url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            f = open(path, 'w')
            f.write(r.text)
        except:
            print('oops !!!')

    try:
        fp = open(path, 'r')
        text = fp.read()
        fp.close()
        all = json.loads(json.loads(text)['data'])
        caseFormat(all)
    except IOError:
        print()


def caseFormat(all):
    # updateTime = all['lastUpdateTime']
    chinaTotal = all['chinaTotal']
    chinaAdd = all['chinaAdd']
    nowConfirm = chinaTotal['nowConfirm']
    nowDead = chinaTotal['dead']
    # suspect = chinaTotal['suspect']
    confirm = chinaAdd['confirm']
    dead = chinaAdd['dead']
    s = '😷 ' + str(nowConfirm) + '(' + '' + str(confirm) + ') '\
        + '💀 ' + str(nowDead) + '(' + '' + str(dead) + ')'
    print(s)


getCase()
