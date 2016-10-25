# -*- coding: utf-8 -*-

from flask import Flask

from zongfuzaixian.views import zong_test

app = Flask(__name__)

app.register_blueprint(zong_test.mod)
