#!/usr/bin/evn python
# -*- coding: utf-8 -*-

'''
Get ip infomation
'''

import socket
import json
import time

def info(data=None):
    info = {
        "name": "ip info",
        "info": "ip info",
        "level": "info",
        "type": "info",
    }
    return info

def prove(data):
    try:
        hostname = socket.gethostbyname(data['target_host'])
    except:
        return data
    info = hostname
    data['flag'] = 1
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % hostname
    while True:
        try:
            res = curl('get', url)
            if res.status_code == 200:
                jsondata = json.loads(res.text)
                if jsondata['code'] == 1:
                    jsondata['data'] = {'region': '', 'city': '', 'isp': ''}
                else:
                    if jsondata['data']['region']:
                        info += " | Region: " + jsondata['data']['region']
                    if jsondata['data']['isp']:
                        info += " | ISP: " + jsondata['data']['isp']
                    if jsondata['data']['city']:
                        info += " | City: " + jsondata['data']['city']
                break
            elif res.status_code == 502:
                time.sleep(0.3)
            else:
                break
        except :
            pass
    data['res'].append({"info": info, "key": 'IP Information'})
    return data

if __name__=='__main__':
    from script import init, curl
    print(prove({'url':'http://www.baidu.com','flag':-1,'data':[],'res':[]}))