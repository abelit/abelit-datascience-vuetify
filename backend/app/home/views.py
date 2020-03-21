# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/03/21 08:32:03
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


from flask import render_template, Blueprint, request, jsonify

home = Blueprint("home", __name__)


# 入口文件，通过入口文件跳转到vue前端
@home.route('/')
def index():
    # flash('You were successfully logged in')
    return render_template('index.html')
