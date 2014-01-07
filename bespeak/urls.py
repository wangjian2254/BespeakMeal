#coding=utf-8
'''
Created on 2011-3-19

@author: 王健
'''
from django.conf.urls import patterns
from bespeak.views import changeUserInfo, changeUserPassword, clearUserPassword, saveUserInfo, getAllUser


urlpatterns = patterns('^meal/$',
                        (r'^saveUserInfo/$',saveUserInfo),#管理员添加、修改用户
                        (r'^getAllUser/$',getAllUser),#管理员添加、修改用户
                        (r'^clearUserPassword/$',clearUserPassword),#管理员重置用户密码
                        (r'^changeUserPassword/$',changeUserPassword),#用户自己修改密码
                        (r'^changeUserInfo/$',changeUserInfo),#用户自己修改个人信息

                       )