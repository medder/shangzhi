# -*- coding: utf-8 -*
import hashlib

from flask import Blueprint, request, render_template

mod = Blueprint('zong_test', __name__, url_prefix='/api/')


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
