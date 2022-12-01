#!/usr/bin/python
# -*- coding: utf-8 -*-

# auxiliares del plugin
from PyQt5 import QtCore
from PyQt5 import QtGui

class Notificador(QtCore.QObject):
    '''
    Sirve para notificar a la aplicacion principal que ya termino
    una operacion y asi poder actualizar la ventana
    '''

    # en caso de operacion con exito
    # el parametro es: nombre del plugin
    correcto = QtCore.pyqtSignal(str)
    # en caso de error
    # el parametro es: mensaje de error
    error = QtCore.pyqtSignal(str)
    # se usara en caso de tener interfaz grafica
    parent = None

    pass


# notificador = Notificador()
# emitir una notificacion con la siguiente linea cada vez que se
# realice una modificacion correcta, especificando los parametros
#
# notificador.correcto.emit(nombre())
#
# o esta linea en caso de errores
#
# notificador.error.emit('mensaje de error')
