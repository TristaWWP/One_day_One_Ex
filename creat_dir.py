'''
@File      :      creat_dir.py
@Date      :      2019/12/10 
@Author      :    Wenping WANG
'''
"""
文件说明：测试目录是否存在，不存在则创建
"""

import os

def main():
    TargetDir = input('输入要测试的目录')
    print(TargetDir)

    if os.path.exists(TargetDir):
        print('目录存在')
    else:
        print("目录不存在，需创建")
        os.makedirs(TargetDir)

if __name__ == '__main__':
    main()
