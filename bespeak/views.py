# coding=utf-8
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bespeak.tools import getResult, meal_permission_required


@login_required
@meal_permission_required("manager")
def saveUserInfo(request):
    username = request.REQUEST.get("username","")
    if not username:
        return getResult(False,u'请提供用户名',None,404)

    last_name = request.REQUEST.get("truename","")#真实姓名
    is_active = request.REQUEST.get("is_active","")#是否在用
    tel = request.REQUEST.get("tel","")#手机号

    if 0 == User.objects.filter(username=username).count():
        user = User()
        user.set_password('111111')
        user.username = username
    else:
        user = User.objects.get(username=username)

    user.last_name = last_name
    if is_active and is_active=='1':
        user.is_active=True
    elif is_active and is_active=='0':
        user.is_active=False
    if tel:
        user.first_name = tel

    user.save()

    return getResult(True,u'创建用户成功',user.username)

@login_required
@meal_permission_required("manager")
def getAllUser(request):
    l=[]
    for user in User.objects.all():
        l.append({'username':user.username,'truename':user.last_name,'is_active':user.is_active,'tel':user.first_name})
    return getResult(True,None,l)

@login_required
@meal_permission_required("manager")
def clearUserPassword(request):
    username = request.REQUEST.get("username","")
    if not username:
        return getResult(False,u'请提供用户名')
    elif 0 == User.objects.filter(username=username).count():
        return getResult(False,u'用户不存在',None,404)
    else:
        user = User.objects.get(username=username)
        user.set_password('111111')
    return getResult(True,u'用户密码恢复为初始密码：111111',user.username)


@login_required
def changeUserPassword(request):
    password = request.REQUEST.get("password","")
    newpassword = request.REQUEST.get("newpassword","")
    if not password and not newpassword:
        return getResult(False,u'请提供旧密码 和 新密码',None,404)
    elif not request.user.check_password(password):
        return getResult(False,u'旧密码错误',None,404)
    else:
        request.user.set_password(password)
        request.user.save()
    return getResult(True,u'用户密码修改成功。',request.user.username)

@login_required
def changeUserInfo(request):
    truename = request.REQUEST.get("truename","")
    tel = request.REQUEST.get("tel","")
    if truename:
        request.user.last_name=truename
    if tel:
        request.user.first_name = tel
    request.user.save()
    return getResult(True,u'修改用户信息成功。',request.user.username)






