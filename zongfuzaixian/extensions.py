# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask.helpers import get_debug_flag
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_principal import Principal, Permission, RoleNeed
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

from zongfuzaixian.setting import DevConfig, ProdConfig
from werobot import WeRoBot

CONFIG = DevConfig if get_debug_flag() else ProdConfig


bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
principals = Principal()
bootstrap = Bootstrap()
admin = Admin()
mail = Mail()

# init in app.py
# worker: celery -A app.extensions.celery worker -l debug
# But has this time, it don't have config

admin_permission = Permission(RoleNeed('admin'))
default_permission = Permission(RoleNeed('default'))

#
# def get_celery():
#     """ It is inited aready"""
#     return celery

robot = WeRoBot(token=CONFIG.WEIXIN_TOKN)
