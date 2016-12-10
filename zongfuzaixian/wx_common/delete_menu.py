# -*- coding: utf-8 -*

import urllib.request
from zongfuzaixian.wx_common.get_access_token import get_access_token

def delete_menu():
    access_token = get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={0}".format(access_token)

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    print(data)


if __name__ == "__main__":
    delete_menu()
