import re

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from users.models import Passport


def register(request):
    """显示用户注册页面"""
    return render(request, 'users/register.html')


def register_handle(request):
    """进行用户注册处理"""
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    # 进行数据校验
    if not all([username, password, email]):
        # 有数据为空
        return render(request, 'users/register.html', {'errmsg': '参数不能为空！'})
    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        # 邮箱不合法
        return render(request, 'users/register.html', {'errmsg': '邮箱不合法！'})
    # 进行业务处理：注册，向账户系统中添加账户
    try:
        Passport.objects.create(username=username, password=password, email=email)
    except Exception as e:
        print("e: ", e)  # 把异常打印出来
        return render(request, 'users/register.html', {'errmsg': '用户名已存在'})
    # 注册完，还是返回注册页
    return redirect(reverse('user:register'))
