from flask_wtf import Form
from wtforms import SubmitField, SelectField
from wtforms import (
    widgets,
    StringField,
    IntegerField,
    TextAreaField,
    BooleanField,
    HiddenField
)
from wtforms.validators import DataRequired


class BindingForm(Form):

    wx_openid = HiddenField("wx_openid", validators=[DataRequired()])  # This should carry from python and refill into form
    telephone = StringField("telephone", validators=[DataRequired()])
    # token = StringField("token", validators=[DataRequired()])
    # draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")

fix_type_dict = {
    "video_monitor": "视频监控",
    "anti_thief": "防盗报警",
    "computer_network": "计算机网络",
    "wifi_network": "WIFI网络",
    "reinstall": "系统重装",
    "printer": "打印机维修",
}


class FixOrderFrom(Form):

    wx_openid = HiddenField("wx_openid", validators=[DataRequired()])
    fix_type = SelectField("fix_type", choices=[
        ("video_monitor", fix_type_dict["video_monitor"]),
        ("anti_thief", fix_type_dict["anti_thief"], ),
        ("computer_network", fix_type_dict["computer_network"], ),
        ("wifi_network", fix_type_dict["wifi_network"], ),
        ("reinstall", fix_type_dict["reinstall"], ),
        ("printer", fix_type_dict["printer"], ),
    ], default="video_monitor")

    service_address = StringField("telephone", validators=[DataRequired()])
    fix_number = IntegerField("fix_number", validators=[DataRequired()])
    client_contact = StringField("client_contact", validators=[DataRequired()])
    client_phone = StringField("telephone", validators=[DataRequired()])
    desc = StringField("desc")
    price = StringField("price")
    submit = SubmitField("submit")

    def set_data_fields(self, fix_order_obj):
        self.wx_openid.data = fix_order_obj.wx_openid
        self.fix_type.data = fix_order_obj.fix_type
        self.fix_number.data = fix_order_obj.fix_number
        self.service_address.data = fix_order_obj.service_address
        self.client_contact.data = fix_order_obj.client_contact
        self.client_phone.data = fix_order_obj.client_phone
        self.desc.data = fix_order_obj.desc
        self.price.data = fix_order_obj.price

        # add a data for show
        self.id = fix_order_obj.id

