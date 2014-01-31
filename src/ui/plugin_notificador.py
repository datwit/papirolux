#!/usr/bin/python
# -*- coding: utf-8 -*-

# auxiliares del plugin
from PyQt4 import QtCore

class Notificador(QtCore.QObject):
    '''
    Sirve para notificar a la aplicacion principal el
    estado de una operacion para mostrar los mensajes
    correspondientes
    '''

    # en caso de operacion con exito
    # el parametro es: nombre del plugin
    correcto = QtCore.pyqtSignal(str)
    # en caso de error
    # el parametro es: mensaje de error
    error = QtCore.pyqtSignal(str)
    # se usara en caso de tener interfaz grafica
    parent = None
    # notificar el inicio de una operacion
    # al emitirse esta signal se debera mostrar la
    # ventana cargando
    inicio_operacion = QtCore.pyqtSignal()
    # notificar el fin de una operacion
    # al emitirse esta signal se debera ocultar la
    # ventana cargando
    fin_operacion = QtCore.pyqtSignal()

    pass
