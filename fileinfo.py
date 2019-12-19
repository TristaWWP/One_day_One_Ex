'''
@File      :      fileinfo.py
@Date      :      2019/12/19 
@Author      :    Wenping WANG
'''
"""
文件说明：显示给定文件的文件信息
"""
#coding: utf-8
import os
import stat
import sys
import time
filename = input('输入文件名')
count = 0
t_char = 0
try:
    with open(filename) as f:
        line = f.readline()
        t_char += len(line)
        while line:
            count += 1
            line = f.readline()#计算总行数
            t_char += len(line)#计算总字符
except FileNotFoundError as e:
    print(e)
    sys.exit()

#创建一个字典文件信息
file_stats = os.stat(filename)#stat用于在给定的路径上执行一个系统stat的调用
file_info = {
    'fname': filename,
    'fsize': file_stats[stat.ST_SIZE],
    'f_lm': time.strftime('%d/%m/%Y %I:%M:%S %p',time.localtime(file_stats[stat.ST_MTIME])),#上次修改的时间
    'f_la': time.strftime('%d/%m/%Y %I:%M:%S %p',time.localtime(file_stats[stat.ST_ATIME])),#上次访问时间
    'f_ct': time.strftime('%d/%m/%Y %I:%M:%S %p',time.localtime(file_stats[stat.ST_CTIME])),#创建时间
    'no_of_lines': count,
    't_char': t_char
}

print('\n文件名 = ', file_info['fname'])
print('文件大小 = ', file_info['fsize'], 'bytes')
print('上次修改时间 = ', file_info['f_lm'])
print('上次访问时间 = ', file_info['f_la'])
print('创建时间 = ', file_info['f_ct'])
print('总行数 = ',file_info['no_of_lines'])
print('总字符 = ',file_info['t_char'])

if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print('这是一个目录')
else:
    print('这不是一个目录\n')
    print('A closer look at the os.stat(%s) tuple:' %filename)
    print(file_stats)
    print('\n上面的元组有以下序列：')
    print("""st_mode(protection bits), st_ino(inode number),
    st_dev(device), st_nlink(number of hard links),
    st_uid(User ID of owner), st_gid(group ID of owner),
    st_size(file size, bytes), st_atime(last access time, seconds since epoch),
    st_mtime(last modification time), st_ctime(time of creation, Windows)
    """)#stat的结构
