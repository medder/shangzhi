# -*- coding: utf-8 -*-

from flask import Flask
from flask import Flask, render_template
from flask.helpers import get_debug_flag
from zongfuzaixian.views import wx_web
from flask_bootstrap import Bootstrap
from zongfuzaixian.setting import ProdConfig, DevConfig

from zongfuzaixian.extensions import (
    bcrypt, cache, csrf_protect, db,
    debug_toolbar, login_manager, migrate,
    principals, bootstrap, admin, mail, robot
)

from flask.helpers import get_debug_flag
from flask_login import current_user  # It is strange to using current_user here
from flask_principal import identity_loaded, UserNeed, RoleNeed
from sqlalchemy import event
from werobot.contrib.flask import make_view



def create_app(config_object=ProdConfig, register_blue=True):
    """
    :param config_object: The configuration object to use.
    :param register_blue: for create celery
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(wx_web.mod)


def register_extensions(app):
    """Register Flask extensions."""

    bcrypt.init_app(app)
    cache.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    # celery.init_app(app)
    # mail.init_app(app)
    # csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    principals.init_app(app)
    register_loading(app)
    migrate.init_app(app, db)

    app.add_url_rule(rule='/wx/',          # WeRoBot 挂载地址
                     endpoint='werobot',  # Flask 的 endpoint
                     view_func=make_view(robot),
                     methods=['GET', 'POST'])
    # admin.init_app(app)


def register_loading(app):
    # The app is pass from another
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                # print("****", role)
                identity.provides.add(RoleNeed(role.name))

                # has authored, add the needs to the identity
                # if hasattr(current_user, 'posts'):
                #     for post in current_user.posts:
                #         identity.provides.add(RoleNeed(post.id))


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
        }

    app.shell_context_processor(shell_context)


CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
