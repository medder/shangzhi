# -*- coding: utf-8 -*

APPID = 'wx780f7e63515af534'
APPSECRET = '0fc9aeabb80b86de32c65868fd9bf27a'


def get_access_token():
    import urllib.request
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}".format(APPID, APPSECRET)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print (response.read().decode('utf-8'))


if __name__ == '__main__':
    get_access_token()

