#!/usr/bin/python

import wx_sdk
import json

url = 'https://way.jd.com/jisuapi/weather'
params = {
        'city' : '杭州',
        'cityid' : '',
        'citycode' : '',
        'appkey' : '7ec3e4137c89df841fc4d5cf996b03c8'
        }

response = wx_sdk.wx_post_req( url, params )

m = json.loads(response.text)
days = m['result']['result']['daily']
night = days[1]['night']
day = days[1]['day']

templow = night['templow']
temphigh = day['temphigh']

dayWeather = day['weather']
nightWeather = night['weather']

WindPower = day['windpower']

print(templow, temphigh)
print(dayWeather, nightWeather)

Temp = str(templow) + '~' + str(temphigh) + ''
print(Temp)

w = {'晴': '', '多云': '', '阴': '', '阵雨': '', '雷阵雨': '',
        '雷阵雨伴有冰雹': '', '雨夹雪': '', '小雨': '', '中雨': '',
        '大雨': '', '暴雨': '', '大暴雨': '', '特大暴雨': '',
        '阵雪': '', '小雪': '', '中雪': '', '大雪': '',
        '暴雪': '', '雾': '', '冻雨': '', '沙尘暴': '',
        '小雨-中雨': '', '中雨-大雨': '', '大雨-暴雨': '',
        '暴雨-大暴雨': '', '大暴雨-特大暴雨': '', '小雪-中雪': '',
        '中雪-大雪': '<++>', '大雪-暴雪': '<++>', '浮尘': '<++>',
        '扬沙': '<++>', '强沙尘暴': '<++>', '浓雾': '<++>', '强浓雾': '<++>',
        '霾': '<++>', '中毒霾': '<++>', '重度霾': '<++>', '严重霾': '<++>',
        '大雾': '<++>', '特强浓雾': '<++>', '无': '', '雨': '', '雪': '<++>'}

print(w['晴'])






