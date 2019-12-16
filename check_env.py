'''
@File      :      check_env.py
@Date      :      2019/12/16 
@Author      :    Wenping WANG
'''
"""
文件说明：检查是否已经设置需要的环境变量
"""
import os

conf_dir = os.getenv("XXX")  #获取一个环境变量conf_dir，没有返回none,参数为需要检查的环境变量
print(conf_dir)
conf_file = 'check_env.conf'  #
con_filename = os.path.join(conf_dir, conf_file) #

for check_env in open(conf_filename): #打开配置文件，读取所有设置
    check_env = check_env.strip()    #删除空白符
    print('[{}]'.format(check_env)) # #在方括号中格式化输出
    new_env = os.getenv(check_env) #新的环境变量

    if new_env is None:
        print(check_env, 'is not set')
    else:
        print('Current setting for {}={}\n'.format(check_env, new_env))