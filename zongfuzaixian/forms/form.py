from flask_wtf import Form
from wtforms import SubmitField, SelectField
from wtforms import (
    widgets,
    StringField,
    TextAreaField,
    BooleanField,
    HiddenField
)
from wtforms.validators import DataRequired


class BindingForm(Form):

    wx_openid = HiddenField("wx_openid", validators=[DataRequired()])  # This should carry from python and refill into form
    telephone = StringField("telephone", validators=[DataRequired()])
    token = StringField("token", validators=[DataRequired()])
    # draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")