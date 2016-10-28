# -*- coding: utf-8 -*
import hashlib

from flask import Blueprint,request

mod = Blueprint('zong_test', __name__, url_prefix='/wx/')

@mod.route('/')
def zong_test():
    args = request.args.to_dict()
    print(args)
    if len(args) == 0:
        return 'Hello Zongfuzaixian'
    else:
        signature = args.get('signature')
        timestamp = args.get('timestamp')
        nonce = args.get('nonce')
        echostr = args.get('echostr')

        token = "shagnzhikeji"

        ls = [token, timestamp, nonce]
        ls.sort()

        sha1 = hashlib.sha1()
        map(sha1.update, ls)
        hashcode = sha1.hexdigest()

        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return ""
