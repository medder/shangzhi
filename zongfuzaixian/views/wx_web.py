# -*- coding: utf-8 -*
import hashlib

from flask import Blueprint, request, render_template
from zongfuzaixian.wx_common.wx_api import get_wx_openid
from zongfuzaixian.operations.op_binding import bind_telephone
from zongfuzaixian.forms.form import BindingForm
#  This is we can using web and robot in same url_prefix
wx_web_blue = Blueprint('wx_web', __name__, url_prefix='/wx')


@wx_web_blue.route('/')
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


@wx_web_blue.route('/sign')
def sign_in():
    args = request.args.to_dict()
    print(args)
    return render_template('base.html')


def test():
    print('aa')


@wx_web_blue.route('/binding', methods=['GET', 'POST'])
def binding():

    print("request.headers", request.headers)
    print("request.args", request.args)
    print("request.base_url", request.base_url)
    print("request.query_string", request.query_string)
    print("request.referrer", request.referrer)
    print("request.json", request.json)
    print("request.form", request.form)

    if request.method == "GET":
        bind_form = BindingForm()
        # come from wx redirect
        code = request.args.get("code")
        wx_openid = get_wx_openid(code)
        print(wx_openid)
        bind_form.wx_openid.data = wx_openid
        return render_template('binding.html', form=bind_form)

    elif request.method == "POST":
        # come from client click
        bind_form = BindingForm(request.form)
        if bind_form.validate():
            wx_openid = bind_form.wx_openid.data
            telephone = bind_form.telephone.data
            token = bind_form.token.data
            print("wx_openid:{}, telephone:{}, token:{}".format(
                wx_openid, telephone, token))
            ret, msg = bind_telephone(wx_openid, telephone)
            # TODO return what after success
            return render_template('base.html', ret=ret, msg=msg)
        else:
            return render_template('base.html')

