from sqlalchemy import or_

from zongfuzaixian.extensions import db
from zongfuzaixian.models.models import OpenidBinding


def bind_telephone(wx_openid, telephone):
    ret, msg = True, "ok"
    if db.session.query(OpenidBinding).filter(
        or_(OpenidBinding.wx_openid == wx_openid, OpenidBinding.telephone == telephone)
    ).all():
        return False, "账号已经绑定"
    openid_binding = OpenidBinding(wx_openid=wx_openid, telephone=telephone)
    openid_binding.save()
    return ret, msg


def check_binding(wx_openid):
    ret, msg = True, "ok"
    if db.session.query(OpenidBinding).filter(
        or_(OpenidBinding.wx_openid == wx_openid)
    ).all():
        return True, "账号已经绑定"
    else:
        return False, "账号没有绑定，请先绑定账号"