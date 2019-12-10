'''
@File      :      create_dir_if_not.py
@Time      :      2019/12/8 5:01 下午
@Author      :    Wenping WANG
'''
"""
文件说明：判断用户主中是否存在目录，不存在就创建
"""

import os

MESSAGE = '目录已经存在'
TESTDIR = 'testdir'   #测试目录
try:
    home = os.path.expanduser('~') #path.expanduser(path)把path中包含的～和～user转换成用户目录，即主目录
    print(home)

    if not os.path.exists(os.path.join(home, TESTDIR)): #exists判断文件或文件夹是否存在都可以
        os.makedirs(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)