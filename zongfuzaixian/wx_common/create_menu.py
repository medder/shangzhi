# -*- coding: utf-8 -*

import urllib.request
import json
from zongfuzaixian.wx_common.get_access_token import get_access_token


def create_menu():
    access_token = get_access_token()
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}".format(access_token)
    menu_body = '''{
                    "button":[
                    {
                        "name": "众服在线",
                        "sub_button":[
                        {
                            "type": "click",
                            "name": "关于我们",
                            "key": "zf_guanyuwomen"
                        },
                        {
                            "type": "view",
                            "name": "账号绑定",
                            "url": "http://www.zhongfor.com/wx/binding"
                        },
                        {
                            "type": "click",
                            "name": "工程师注册",
                            "key": "zf_gongchengshizhuce"
                        },
                        {
                            "type": "click",
                            "name": "客户注册",
                            "key": "zf_kehuzhuce"
                        }]
                    },
                    {
                        "name": "客户服务",
                        "sub_button":[
                        {
                            "type": "click",
                            "name": "客户中心",
                            "key": "zf_kehuzhongxin"
                        },
                        {
                            "type": "click",
                            "name": "安装调试",
                            "key": "zf_anzhuangtiaoshi"
                        },
                        {
                            "type": "click",
                            "name": "维修维保",
                            "key": "zf_weixiuweibao"
                        },
                        {
                            "type": "click",
                            "name": "咨询服务",
                            "key": "zf_zixunfuwu"
                        }]
                    },
                    {
                        "name": "工程师",
                        "sub_button": [
                        {
                            "type": "click",
                            "name": "工程师中心",
                            "key": "zf_gongchengshizhongxin"
                        },
                        {
                            "type": "click",
                            "name": "订单处理",
                            "key": "zf_dingdanchuli"
                        },
                        {
                            "type": "click",
                            "name": "工程师接单",
                            "key": "zf_gongchengshijiedan"
                        }]
                    }]
                }'''
    body = menu_body.encode('utf-8')

    # view_menu_body = '''{
    #                      "button": [
    #                      {
    #                          "type": "view",
    #                          "name": "view",
    #                          "url": "http://www.zhongfor.com/wx/"
    #                      },
    #                      {
    #                          "type": "click",
    #                          "name": "click",
    #                          "key": "zf_click"
    #                      }]
    # }'''
    # body = view_menu_body.encode('utf-8')
    print("----", body)
    request = urllib.request.Request(url, body)
    response = urllib.request.urlopen(request)
    print('This is only for test')
    data = response.read().decode('utf-8')
    print(data)


if __name__ == "__main__":
    create_menu()
