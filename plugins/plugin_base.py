#!/usr/bin/python
# -*- coding: utf-8 -*-

plugins_list = []

class PluginType(type):
    def __init__(cls, name, bases, attrs):
        super(PluginType, cls).__init__(name, bases, attrs)

        # registrar el plugin en la lista
        if not cls in plugins_list:
            plugins_list.append(cls)


class PluginBase(object):
    '''
    Clase base para todos los plugins
    '''

    __metaclass__ = PluginType

    pass
