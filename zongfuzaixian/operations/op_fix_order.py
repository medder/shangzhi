from zongfuzaixian.models.models import FixOrder
from zongfuzaixian.extensions import db
from sqlalchemy import or_, and_


def add_fix_order(
    wx_openid, fix_type, service_address, fix_number, client_contact,
    client_phone, desc, price
):
    ret, msg = True, "success"
    fix_order = FixOrder(
        wx_openid=wx_openid,
        fix_type=fix_type,
        service_address=service_address,
        fix_number=fix_number,
        client_contact=client_contact,
        client_phone=client_phone,
        desc=desc,
        price=price,
    )
    fix_order.save()
    return ret, msg


def get_fix_orders(wx_openid=None):
    if not wx_openid:
        return None

    fix_orders = FixOrder.query.filter(FixOrder.wx_openid == wx_openid).all()
    return fix_orders



def get_fix_order(wx_openid=None, fix_order_id=None):
    if not wx_openid:
        return None

    fix_orders = FixOrder.query.filter(
        and_(FixOrder.wx_openid == wx_openid, FixOrder.id == fix_order_id )).one()
    return fix_orders
