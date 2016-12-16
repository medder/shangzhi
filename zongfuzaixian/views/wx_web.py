# -*- coding: utf-8 -*
import hashlib

from flask import Blueprint, request, render_template

mod = Blueprint('wx_web', __name__, url_prefix='/wx_web')


@mod.route('/')
def zong_test():
    args = request.args.to_dict()
    print(args)
    if len(args) == 0:
        # return 'Hello Zongfuzaixian'
        return render_template('base.html')
    else:
        signature = args.get('signature')
        timestamp = args.get('timestamp')
        nonce = args.get('nonce')
        echostr = args.get('echostr')

        token = "shangzhikeji"

        ls = [token, timestamp, nonce]
        ls.sort()

        sha1 = hashlib.sha1()
        list(map(sha1.update, (s.encode() for s in ls)))
        hashcode = sha1.hexdigest()

        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return ""


@mod.route('/sign')
def sign_in():
    args = request.args.to_dict()
    print(args)
    return render_template('base.html')


def test():
    print('aa')


@mod.route('/binding')
def binding():

    print("reqests.headers", request.headers)
    print("request.args", request.args)
    print("request.base_url", request.base_url)
    print("request.query_string", request.query_string)
    print("request.referrer", request.referrer)
    print("request.json", request.json)

    return render_template('binding.html')
