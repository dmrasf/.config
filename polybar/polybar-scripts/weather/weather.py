#!/usr/bin/env python

import wx_sdk
import json
import os
import time
import datetime

path = '/home/dmr/.cache/weather.json'


def isExit():
    if not os.path.exists(path):
        return True
    filetime = time.strftime(
        '%Y-%m-%d-%H', time.localtime(os.stat(path).st_mtime))
    today = datetime.datetime.now().strftime('%Y-%m-%d-%H')
    if today.__eq__(filetime):
        return False
    return True


def getWeather():
    if isExit():
        url = 'https://way.jd.com/jisuapi/weather'
        params = {
            'city': '杭州',
            'cityid': '',
            'citycode': '',
            'appkey': '7ec3e4137c89df841fc4d5cf996b03c8'
        }
        r = wx_sdk.wx_post_req(url, params)
        try:
            f = open(path, 'w')
            f.write(r.text)
        except:
            print('oops !!!')
    try:
        fp = open(path, 'r')
        text = fp.read()
        fp.close()
        all = json.loads(text)
        caseFormat(all)
    except IOError:
        print()


def caseFormat(all):
    days = all['result']['result']['daily']
    night = days[0]['night']
    day = days[0]['day']

    templow = night['templow']
    temphigh = day['temphigh']
    dayWeather = day['weather']
    # nightWeather = night['weather']
    # WindPower = day['windpower']
    # w = {'晴': '', '多云': '', '阴': '', '阵雨': '', '雷阵雨': '',
    # '雷阵雨伴有冰雹': '', '雨夹雪': '', '小雨': '', '中雨': '',
    # '大雨': '', '暴雨': '', '大暴雨': '', '特大暴雨': '',
    # '阵雪': '', '小雪': '', '中雪': '', '大雪': '',
    # '暴雪': '', '雾': '', '冻雨': '', '沙尘暴': '',
    # '小雨-中雨': '', '中雨-大雨': '', '大雨-暴雨': '',
    # '暴雨-大暴雨': '', '大暴雨-特大暴雨': '', '小雪-中雪': '',
    # '中雪-大雪': '<++>', '大雪-暴雪': '<++>', '浮尘': '<++>',
    # '扬沙': '<++>', '强沙尘暴': '<++>', '浓雾': '<++>', '强浓雾': '<++>',
    # '霾': '<++>', '中毒霾': '<++>', '重度霾': '<++>', '严重霾': '<++>',
    # '大雾': '<++>', '特强浓雾': '<++>', '无': '', '雨': '', '雪': '<++>'}

    Temp = str(templow) + '~' + str(temphigh) + '糖 ' + dayWeather
    print(Temp)


getWeather()
