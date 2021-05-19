# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 9:47 下午
# @Author  : Shark
# @Site    : 
# @File    : get_hash.py
# @Software: PyCharm
from hashlib import sha1


def get_hash(str):
    """取一个字符串的hash值"""
    sh = sha1()
    sh.update(str.encode('utf-8'))
    return sh.hexdigest()
