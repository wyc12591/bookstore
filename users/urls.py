# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 8:38 上午
# @Author  : Shark
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.register, name='register'),  # 用户注册
    path('register_handle/', views.register_handle, name='register_handle'),  # 用户注册处理
]
