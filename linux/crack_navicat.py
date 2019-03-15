#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 每次运行均会重置试用期到14天，要求64位版Navicat
# 插在Navicat启动脚本之前即可
import os
import re

# 试用时间重置的正则
ps = (
        re.compile(r'\[Software\\\\PremiumSoft\\\\Data\\\\\{[^\}]*\}\\\\Info\].*?\n[^\[]*'),
        re.compile(r'\[Software\\\\Classes\\\\CLSID\\\\\{[^\}]*\}\\\\Info\].*?\n[^\[]*')
    )

# user.reg 的路径
regfile = os.path.join(os.environ['HOME'], '.navicat64', 'user.reg')

# 正则替换
with open(regfile, 'r+') as f:
    regstr = f.read()
    for p in ps:
        regstr = p.sub(lambda m: '', regstr)

    f.seek(0, 0)
    f.truncate()
    f.write(regstr)