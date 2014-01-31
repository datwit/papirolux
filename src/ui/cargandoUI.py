#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.cargando import Ui_Cargando

class Cargando(QDialog, Ui_Cargando):
    def __init__(self, parent = None):
        super(Cargando, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('DocLux')
        self.setWindowModality(Qt.ApplicationModal)

        #~ # set the GIF image
        self.__movie = QMovie(":/imgs/recursos/imagenes/cargando.gif")
        self.lb_busy.setMovie(self.__movie)
        self.__movie.start()

        # para evitar la salida con ESCAPE
        self.__escape = False


    def __del__(self):
        self.__movie.stop()
        #~ pass


    def closeEvent(self, event):
        # ignorar siempre la salida, esta ventana debe cerrarla el hilo de procesos
        # cuando termine
        event.ignore()


    def keyPressEvent(self, keyEvent):
        # solo implementado para evitar el cierre por default al
        # presionar ESCAPE u otra TECLA
        pass
