# -*- coding: utf-8 -*-

# coding: utf8

# Устанавливаем стандартную внешнюю кодировку = utf8
import sys
import datetime
import argparse

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


def to_json(fin):
    """Приведение исходного файла в json"""
    import xmltodict
    import json

    # with open(fin) as fin:
        # for root, dirs, files in os.walk('python/Lib/email'):
    # json.dumps(xmltodict.parse(
    # with open(fin)
    pass

print now()
