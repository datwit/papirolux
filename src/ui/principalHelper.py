#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4 import QtCore, QtGui

# cada clase define un HILO para realizar un procedimiento determinado
# y una SIGNAL para indicar que termino el proceso, a esta SIGNAL se
# conecta la IU principal para conocer cuando se concluyo el proceso y
# continue con la rutina correspondiente, la signal contiene un parametro
# para indicar el TEXTO aclaratorio si ocurriera un error, si NO HAY ERROR
# este parametro debe ser una cadena VACIA

# cargar nuevas imagenes
class NuevasImagenes(QtCore.QThread):
    # signal necesaria
    terminado = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(NuevasImagenes, self).__init__(parent)

        # variables necesarias para que funcione el hilo
        self.__listaImgs = []
        self.__controladora = None


    def setData(self, imagenesIn, control):
        self.__listaImgs = imagenesIn
        self.__controladora = control


    def run(self):
        # procedimiento
        self.__controladora.nuevas_imagenes(self.__listaImgs)

        # notificar el fin de operaciones
        self.terminado.emit('')

        return


# adicionar nuevas imagenes
class AdicionarImagenes(QtCore.QThread):
    # signal necesaria
    terminado = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(AdicionarImagenes, self).__init__(parent)

        # variables necesarias para que funcione el hilo
        self.__listaImgs = []
        self.__controladora = None


    def setData(self, imagenesIn, control):
        self.__listaImgs = imagenesIn
        self.__controladora = control


    def run(self):
        # procedimiento
        self.__controladora.nuevas_imagenes(self.__listaImgs, True)

        # notificar el fin de operaciones
        self.terminado.emit('')

        return


# eliminar imagenes
class EliminarImagenes(QtCore.QThread):
    # signal necesaria
    terminado = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(EliminarImagenes, self).__init__(parent)

        # variables necesarias para que funcione el hilo
        self.__nro = -1
        self.__controladora = None


    def setData(self, nro, control):
        self.__nro = nro
        self.__controladora = control


    def run(self):
        # procedimiento
        self.__controladora.eliminar(self.__nro)

        # notificar el fin de operaciones
        self.terminado.emit('')

        return


# guardar y exportar
class GuardarExportarImagenes(QtCore.QThread):
    # signal necesaria
    terminado = QtCore.pyqtSignal(str)

    def __init__(self, parent = None):
        super(GuardarExportarImagenes, self).__init__(parent)

        # variables necesarias para que funcione el hilo
        self.__listaImgs = []
        self.__dir = ''
        self.__exportar = False
        self.__pdf = ''


    def setData(self, imagenesIn, dirSalida = '', exportar = False, pdf = 'doclux.pdf'):
        self.__listaImgs = imagenesIn
        self.__dir = dirSalida
        self.__exportar = exportar
        self.__pdf = pdf


    def run(self):
        # procedimiento
        result = True
        # si se quiere guardar en cualquier directorio
        if not self.__exportar:
            for i in self.__listaImgs:
                # intentar copiar los archivos al directorio de salida
                if not QtCore.QFile.copy(i[0], self.__dir + '/' + i[1] + '.png'):
                    # marcador de errores
                    result = False
        else:
            # si se quiere exportar
            # configurar la impresora
            printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            printer.setPaperSize(QtGui.QPrinter.Letter)
            printer.setOutputFileName(self.__pdf)
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            for i in range(len(self.__listaImgs)):
                img = QtGui.QImage(self.__listaImgs[i][0])
                size = img.size()
                size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                painter.setWindow(img.rect())
                painter.drawImage(0, 0, img)
                if i < (len(self.__listaImgs) - 1):
                   printer.newPage()

            # eliminar la "basura"
            del painter
            del printer

        # reportar los errores
        if not result:
            msg = u"Algunos ficheros <b>ya existían</b> en el directorio \"" + self.__dir + "\" y <b>no se guardaron.</b>"
            self.terminado.emit(msg)
        else:
            # notificar el fin de operaciones
            self.terminado.emit('')

        return
