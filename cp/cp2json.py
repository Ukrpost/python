# -*- coding: utf-8 -*-

# coding: utf8

# Устанавливаем стандартную внешнюю кодировку = utf8
import sys
import datetime
# import argparse

reload(sys)
sys.setdefaultencoding('utf8')


def now():
    """ Возвращает текущую дату и время"""
    in_moment = str(datetime.datetime.now())
    in_moment = in_moment.replace(':', '-')
    in_moment = in_moment.replace(' ', 'T')
    in_moment = in_moment.replace(':', '-')
    return in_moment


def if_exist():
    """Проверка на существование файла и его доступности"""
    pass


def bkup(fin):
    """Архивация и создание бекапа исходного файла"""
    pass


def csv_json(fin):
    import json
    import csv

    csvfile = open(fin, 'r')
    jsonfile = open(fin[:-3] + 'json', 'wb')

    # fieldnames = ("Bar_Code", "Price_1", "Price", "Qty")

    reader = csv.reader(csvfile)
    i = 0
    b = []
    for row in reader:
        if i == 0:
            pass
        else:
            # print str(row[0]).split(';')
            a = str(row[0])
            a = a.replace(';', ',')
            b.append(a)
            print a
            # json.dump(row, jsonfile)
            jsonfile.write(b)
        i = i + 1


def to_json(fin):
    """Приведение исходного файла в json"""
    # import xmltodict
    # import json

    # with open(fin) as fin:
        # for root, dirs, files in os.walk('python/Lib/email'):
    # json.dumps(xmltodict.parse(
    # with open(fin)
    pass

print now()

csv_json(sys.argv[1])
