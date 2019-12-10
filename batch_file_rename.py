"""
批处理文件后缀名
"""
# -*- coding: UTF-8 -*-

__author__ = 'wwp'

import argparse
import os

"""
argparse是python标准库用来处理命令行参数的库，可以编辑用户友好的命令行接口
"""

def batch_rename(work_dir, old_extensions, new_extensions):
    """
    批量将指定文件夹的后缀名修改为新的后缀名
    :param work_dir: 工作目录
    :param old_extensions: 旧的扩展名
    :param new_extensions: 新的扩展名
    :return:
    """
    #files = os.listdir(work_dir)，该方法是返回path指定的文件见包含的文件和文件夹的名字列表
    for filename in os.listdir(work_dir):
        #得到文件扩展名
        split_file = os.path.splitext(filename) #path.splitext分割路径，返回路径名和文件扩展名的元组
        file_extension = split_file[1]
        #当文件扩展名和给出的旧扩展名相同，就修改扩展名
        if old_extensions == file_extension:
        #返回修改后的带新扩展名的文件名
            newfile = split_file[0] + new_extensions

             #重命名文件或目录，参数用join是因为计算机要识别的完整路径，而不是人为的直接修改名称
            os.rename(
                 os.path.join(work_dir, filename),
                 os.path.join(work_dir, newfile),
            )
            """
            os.path.join连接两个或多个路径名组件
            1 如果各组件名首字母不包括/，则函数会自动加上
            2 如果有一个组件是绝对路径，则在它之前的所有组件都会被舍弃
            3 如果最好一个组件为空，则生成的路径会以/分割符结尾
            """
    print("rename is done")
    #print(os.listdir(work_dir))

def get_parser():
    parser = argparse.ArgumentParser(description='批量修改指定文件夹下的文件后缀') #创建解析器，ArgumentParser对象包含将命令行解析成python数据类型所需的全部信息
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='要修改后缀文件夹路径') #metavar：在使用方法消息中使用参数值示例，type：命令行参数应当被转换成的类型，nargs：命令行参数应当消耗的数目
    parser.add_argument('old_extensions', metavar='OLD_EXTENSIONS', type=str, nargs=1,
                        help='旧后缀')
    parser.add_argument('new_extensions', metavar='NEW_EXTENSIONS', type=str, nargs=1,
                        help='新后缀')
    return parser

def main():
    """
    脚本被触发会调用
    """
    #增加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())#parse_args()方法用来解析参数，vars返回对象的属性和属性值的字典对象
    print(args)

    #使用传递的第一个参数为工作目录变量
    work_dir = args['work_dir'][0]
    #使用传递的第二个参数为工作旧的扩展名
    old_extensions = args['old_extensions'][0]
    #使用python中的切片
    if old_extensions[0] != '.':
        old_extensions = '.' + old_extensions
    # 使用传递的第三个参数为工作新的扩展名
    new_extensions = args['new_extensions'][0]
    if new_extensions[0] != '.':
        new_extensions = '.' + new_extensions

    batch_rename(work_dir, old_extensions, new_extensions)

if __name__ == '__main__':
    main()

