#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
# import urllib

filename = 'DN.list'


def lookup(domain_name_list_filename):
    domain_name_list_file = open(domain_name_list_filename, 'r')
    for line in domain_name_list_file:
        print(line, end='')
    domain_name_list_file.close()


def lookup_line(domain_name_list_filename, line):
    domain_name_list_file = open(domain_name_list_filename, 'r')
    domain_name_list_file.close


# def replace(domain_name_list_filename, source, replaced):
#     shutil.copy(domain_name_list_filename,
#                 '{}.bak'.format(domain_name_list_filename))
#     domain_name_list_file = open(
#         '{}.bak'.format(domain_name_list_filename), 'r')
#     domain_name_list_file_edited = open(domain_name_list_filename, 'w')
#     for line in domain_name_list_file:
#         if line == '{}\n'.format(source):
#             line = '{}\n'.format(replaced)
#         domain_name_list_file_edited.write(line)
#     domain_name_list_file.close()
#     domain_name_list_file_edited.close()
#     os.remove('{}.bak'.format(domain_name_list_filename))


def edit():
    pass


def add(domain_name_list_filename, domain_name, explain):
    domain_name_list_file = open(domain_name_list_filename, 'a')
    domain_name_list_file.write('{}#{}\n'.format(domain_name, explain))
    domain_name_list_file.close()


def update():
    # domain_name_list_file_url=''

    # if not os.path.exists(domain_name_list_filename):
    #     urllib.request.urlretrieve(domain_name_list_file_url,domain_name_list_filename)

    # domain_name_list_file=open(domain_name_list_filename)
    pass


def find(domain_name_list_filename, string):
    lines = []
    line = 0
    domain_name_list_file = open(domain_name_list_filename, 'r')
    for line in domain_name_list_file:
        if string in line:
            lines.append(line)
        line += 1
    domain_name_list_file.close()
    return (0 if (lines == 0) else lines)


if __name__ == "__main__":
    try:
        temp = input('域名列表文件名（Ctrl + C）以跳过：')
        filename = temp
        del temp
    except:
        print('\n已跳过，文件路径：{}'.format(filename))
    while True:
        mode = input("""\n\n------\n
输入你要进行的操作：
输入'l'用来查看；
输入'e'用来编辑；
输入'a'用来附加；
输入'u'以从网络寻找更新；
输入'^'以退出。
l/e/a/u/^>\
""")
        if mode == 'l':
            lookup(filename)
        if mode == 'e':
            while True:
                temp = input("你想替换那一项？（'^'以退出）")
                if temp == '^':
                    break
                source = temp
                temp = input("你想替成什么？（'^'以不变）")
                if temp == '^':
                    continue
                replaced = temp
                edit(filename, source, replaced)
        if mode == 'a':
            while True:
                temp = input("你想增加什么？（'^'以退出）")
                if temp == '^':
                    break
                domain_name = temp
                temp = input("中文：（'^'以留空）")
                if temp == '^':
                    explain = '<unkonw>'
                explain = temp
                add(filename, domain_name, explain)
        if mode == 'u':
            update()
        if mode == '^':
            exit()
