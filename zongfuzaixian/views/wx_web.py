# -*- coding: utf-8 -*
import hashlib

from flask import Blueprint, request, render_template
from zongfuzaixian.wx_common.wx_api import get_wx_openid
from zongfuzaixian.operations.op_binding import (
    bind_telephone,
    check_binding
)
from zongfuzaixian.forms.form import (
    BindingForm,
    FixOrderFrom
)

from zongfuzaixian.operations.op_fix_order import (
    add_fix_order
)
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
            # token = bind_form.token.data
            print("wx_openid:{}, telephone:{}".format(
                wx_openid, telephone))
            ret, msg = bind_telephone(wx_openid, telephone)
            # TODO return what after success
            return render_template('base.html', ret=ret, msg=msg)
        else:
            return render_template('base.html')


@wx_web_blue.route('/do_fix_order', methods=['GET', 'POST'])
def do_fix_order():

    if request.method == "GET":
        fix_order_form = FixOrderFrom()
        # come from wx redirect
        code = request.args.get("code")
        wx_openid = get_wx_openid(code)
        already_binding, msg = check_binding(wx_openid)
        if not already_binding:
            return render_template("base.html", msg=msg)
        fix_order_form.wx_openid.data = wx_openid
        return render_template('do_fix_order.html', form=fix_order_form)

    elif request.method == "POST":
        # come from client click
        fix_order_form = FixOrderFrom(request.form)
        if fix_order_form.validate():
            wx_openid = fix_order_form.wx_openid.data
            fix_type = fix_order_form.fix_type.data
            service_address = fix_order_form.service_address.data
            fix_number = fix_order_form.fix_number.data
            client_contact = fix_order_form.client_contact.data
            client_phone = fix_order_form.client_phone.data
            desc = fix_order_form.desc.data
            price = fix_order_form.price.data
            # token = bind_form.token.data
            print("wx_openid:{}, fix_type:{}, fix_number:{}, price:{}".format(
                wx_openid, fix_type, fix_number, price))
            ret, msg = add_fix_order(
                wx_openid, fix_type, service_address, fix_number, client_contact,
                client_phone, desc, price
            )
            # TODO return what after success
            return render_template('base.html', ret=ret, msg=msg)
        else:
            return render_template('do_fix_order')

