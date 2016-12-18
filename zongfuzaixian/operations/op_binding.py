from zongfuzaixian.models.models import OpenidBinding
from zongfuzaixian.extensions import db


def bind_telephone(wx_openid, telephone):
    ret, msg = True, "ok"
    if db.session.query(OpenidBinding).filter(OpenidBinding.wx_openid == wx_openid).all():
        return False, "账号已经绑定"
    openid_binding = OpenidBinding(wx_openid=wx_openid, telephone=telephone)
    openid_binding.save()
    return ret, msg