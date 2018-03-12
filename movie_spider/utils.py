# -*- coding: utf-8 -*-


def object2dict(item):
    dict((key, value) for key, value in item.items()
         if not key.startswith('__'))

