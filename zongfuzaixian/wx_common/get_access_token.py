# -*- coding: utf-8 -*

import urllib.request
APPID = 'wx780f7e63515af534'
APPSECRET = '0fc9aeabb80b86de32c65868fd9bf27a'
import json


def get_access_token():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}".format(APPID, APPSECRET)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    data = json.loads(data)
    print(data)
    return data.get('access_token')

