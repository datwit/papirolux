#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# clase para las signals
class MiniaturaSignals( QObject ):
    '''
    Clase para definir las signals que puede emitir la clase Miniatura
    '''

    ver_miniatura = pyqtSignal(int)


class Miniatura(QLabel):
    def __init__(self, indice, parent = None):
        # inicializar el padre
        super(Miniatura, self).__init__(parent)

        #self.setFrameStyle(QFrame.Box)

        # configurar signals/slots
        self.signals = MiniaturaSignals()

        # indice de la miniatura en la lista
        self.__indice = indice


    def mousePressEvent(self, event):
        '''
        Evento que se ejecuta al hacer click sobre la miniatura
        '''

        self.signals.ver_miniatura.emit(self.__indice)
