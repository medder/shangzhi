# -*- coding: utf-8 -*-

from flask import Blueprint

mod = Blueprint('zong_test', __name__, url_prefix='/wx/')

@mod.route('/test/')
def zong_test():
    return 'Hello Zongfuzaixian'
