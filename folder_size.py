'''
@File      :      folder_size.py
@Date      :      2019/12/17 
@Author      :    Wenping WANG
'''
"""
文件说明：统计当前文件夹的大小
"""
import os
import sys

try:
    directory = sys.argv[1]  #文件夹路径
except IndexError:
    sys.exit('必须提供参数')

dir_size = 0 #设置大小为0
fsizedir = {'Byte' : 1,  #比特 1
            'Kilobytes' : float(1) / 1024, #k
            'Megabytes' : float(1) / (1024 * 1024), #M
            'Gigabytes' : float(1) / (1024 * 1024 * 1024) #G
            }
for(path, dirs, files) in os.walk(directory):#os.walk()主要用来遍历目录中各个子目录和文件，里面是一个三元组
    for file in files: #目录里面的文件
        filename = os.path.join(path, file)#得到绝对路径
        dir_size += os.path.getsize(filename)#不断加size


fsizeList = [str(round(fsizedir[key] * dir_size, 2)) + ' ' + key for key in fsizedir]#round(x,n)round函数四舍五入到n位小数，得出一个list，for循环这个list

print(fsizeList)

if dir_size ==0:
    print("空文件夹")
else:
    for units in sorted(fsizeList)[::-1]:#倒序,::是全部包含，-1是倒序
        print("文件夹大小为:" + units)
