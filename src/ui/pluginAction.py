#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
#~ from PyQt4.QtCore import *
from PyQt5.QtGui import *

# auxiliar para las actions de los Plugins
class MyQAction(QAction):
    '''
    Clase para poder asociar el QAction con la funcion
    correspondiente en cada plugin
    '''

    def __init__(self, pluginObj, parent = None):
        # inicializar el padre
        super(MyQAction, self).__init__(parent)

        # funcion asociada a cada plugin
        self.__plugin = pluginObj

        # configurar el action
        self.setText(self.__plugin.nombre())
        self.setIcon(QIcon(self.__plugin.icon()))


    def execFunc(self, urlsIn, urlsOut, notificador):
        '''
        Ejecutar la funcion con los parametros adecuados
        '''

        self.__plugin.run(urlsIn, urlsOut, notificador, self.parent())
