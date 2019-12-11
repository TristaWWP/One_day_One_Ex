'''
@File      :      youtube_downloader_fast.py
@Date      :      2019/12/10 
@Author      :    Wenping WANG
'''
"""
文件说明：使用aria2c迅速与并行线程下载油管视频，需要翻墙，不能翻墙就尴尬了
"""
import subprocess
import sys

"""
youtube-dl，是一个命令行程序，用于从油管上下载视频，需要安装这个
"""
video_link, threads = sys.argv[1], sys.argv[2]
subprocess.call([
    'youtube-dl',
    video_link,
    '--external-downloader',
    'aria2c',
    '--external-downloader-agrs',
    '-x' + threads
]

)
"""
call里面的内容相当于在shell中直接运行命令：youtube-dl video_link --external-downloader aria2c --external-downloader-agrs -x+threads
"""