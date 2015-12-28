# -*- coding: utf-8 -*-
"""  Из всего дерева текущей папки копирует все найденные
   файлы в новую папку AllInOne.
   если AllInOne уже существует, тогда перезаписывает
   все содержимое"""

import os
import shutil
import sys

reload(sys)
sys.setdefaultencoding('utf8')

src = os.getcwd()
dest = 'AllInOne'
src_files = os.listdir(src)


def in_one(src):
    """  Из всего дерева текущей папки копирует все найденные
       файлы в новую папку AllInOne.
       если AllInOne уже существует, тогда перезаписывает
       все содержимое"""
    if not os.path.exists(dest):
        os.mkdir(dest)
        print "mkdir AllInOne"

    if os.path.exists(dest):
        shutil.rmtree(dest)
        print "rm AllInOne"
        os.mkdir(dest)
        print "mkdir AllInOne"

    for dirname, dirnames, filenames in os.walk(src):
        # print path to all filenames.
        for filename in filenames:
            fin = os.path.join(dirname, filename)
            print fin
            shutil.copy(fin, dest)

in_one(sys.argv[1])

# for dirname, dirnames, filenames in os.walk('.'):
#     # print path to all subdirectories first.
#     # for subdirname in dirnames:
#     #     print(os.path.join(dirname, subdirname))
#     # print path to all filenames.
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
