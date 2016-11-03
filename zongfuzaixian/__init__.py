# -*- coding: utf-8 -*-

from flask import Flask

from zongfuzaixian.views import zong_test
from flask_bootstrap import Bootstrap
app = Flask(__name__)

app.register_blueprint(zong_test.mod)

bootstrap = Bootstrap()
bootstrap.init_app(app)

