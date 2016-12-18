from zongfuzaixian.wx_common.get_access_token import APPID, APPSECRET
import requests
import json

WX_OPENID_URL = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={secret}&code={code}&grant_type=authorization_code"


def get_wx_openid(code):
    wx_response = requests.get(
        WX_OPENID_URL.format(appid=APPID, secret=APPSECRET, code=code)
    )
    wx_json = json.loads(wx_response.text)
    print(wx_json)
    if "errcode" in wx_json:
        return "Error"
    return wx_json["openid"]


