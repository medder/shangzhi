# -*- coding: utf-8 -*-
"""User models."""
import base64
import datetime as dt
import os
from flask_login import UserMixin, AnonymousUserMixin
from zongfuzaixian.database import Column, Model, SurrogatePK, db
from zongfuzaixian.extensions import bcrypt


roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    roles = db.relationship('Role', secondary=roles, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None
        if self.otp_secret is None:
            # generate a random secret
            self.otp_secret = base64.b32encode(os.urandom(10)).decode('utf-8')

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)


    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class OpenidBinding(SurrogatePK, Model):
    id = db.Column(db.Integer(), primary_key=True)
    wx_openid = db.Column(db.String(80), unique=True)
    telephone = db.Column(db.String(15), unique=True)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,**kwargs)


class FixOrder(SurrogatePK, Model):
    id = db.Column(db.Integer(), primary_key=True)
    wx_openid = db.Column(db.String(80))
    fix_type = db.Column(db.String(20))
    service_address = db.Column(db.String(200))
    fix_number = db.Column(db.Integer())
    client_contact = db.Column(db.String(25))
    client_phone = db.Column(db.String(15))
    desc = db.Column(db.String(200))
    price = db.Column(db.Integer())
    status = db.Column(db.Integer())
    # 0 is close # 1 is open to be accept
    # 2 is accept and handing 3 is hander to check 4 checked it finished
    invalid = db.Column(db.Boolean())
    # 0 is not true
    create_time = db.Column(db.DateTime, default=dt.datetime.now)
    update_time = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self,**kwargs)
