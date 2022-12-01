#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog
try:
    from PIL import Image
except ImportError:
    import Image

from ui.comandos import Ui_Comandos
from .miniatura import Miniatura

# clase para las signals
class ComandosSignals( QObject ):
    '''
    Clase para definir las signals que puede emitir la clase Miniatura
    '''

    ver_imagen_comando = pyqtSignal(int)
    retornar_comando = pyqtSignal(int)
    cancelar = pyqtSignal()


class ListaComandos(QDialog, Ui_Comandos):
    def __init__(self, comandos, swap, parent = None):
        super(ListaComandos, self).__init__(parent)
        self.setupUi(self)

        # configuraciones
        self.setWindowModality(Qt.ApplicationModal)
        self.move(0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.comandos_content.setContentsMargins(0, 0, 0, 0)

        # lista de comandos
        self.__comandos = comandos

        # swap
        self.__swap_dir = swap

        # configurar signals/slots
        self.signals = ComandosSignals()

        # hacer el cambio permanente
        self.aplicar.clicked.connect(self.__retornar_al_comando)

        # cancelar el cambio
        self.ignorar.clicked.connect(self.close)

        # nro del comando seleccionado
        self.__nro_comando = -1

        # actualizar la lista de widgets con los comandos actuales
        i = 0
        while i < len(self.__comandos):
            # construir el thumbnail correspondiente
            im = Image.open(self.__comandos[i][1])
            im.thumbnail((90, 114))
            salida = self.__swap_dir + '/' + 'comando_' + str(i + 1) + '.jpg'
            im.save(salida)
            # mostrar el thumbnail
            lab = Miniatura(i, self)
            lab.setMinimumSize(90, 114)
            lab.setMaximumSize(90, 114)
            lab.setPixmap(QPixmap(salida))
            # mostrar en nombre del comando
            text = QLabel(self.__comandos[i][0], self)
            text.setWordWrap(True)
            # preparar el layout
            layout = QHBoxLayout(self)
            layout.addWidget(lab)
            layout.addWidget(text)
            # adicionar el layout al widget y mostrarlo
            cmd = QWidget(self)
            cmd.setLayout(layout)
            self.comandos_content.addWidget(cmd)
            # enlazar la signal
            lab.signals.ver_miniatura.connect(self.__ver_imagen_comando)

            i = i + 1

        # actualizar el nro del comando
        self.__nro_comando = len(self.__comandos)
        # resaltar el comando actual
        item = self.comandos_content.itemAt(self.__nro_comando - 1)
        widget = item.widget()
        widget.children()[1].setLineWidth(2)
        widget.children()[1].setFrameStyle(QFrame.Box)


    def closeEvent(self, event):
        '''
        Salir sin aplicar los cambios
        '''

        self.signals.cancelar.emit()
        event.accept()


    def __ver_imagen_comando(self, i):
        '''
        Emite la signal correspondiente para que se actualice el visor
        con el comando adecuado
        '''

        # actualizar el nro comando
        self.__nro_comando = i
        self.signals.ver_imagen_comando.emit(self.__nro_comando)

        for i in range(self.comandos_content.count()):
            item = self.comandos_content.itemAt(i)
            widget = item.widget()
            widget.children()[1].setFrameStyle(QFrame.NoFrame)

            if i == self.__nro_comando:
                widget.children()[1].setLineWidth(2)
                widget.children()[1].setFrameStyle(QFrame.Box)


    def __retornar_al_comando(self):
        '''
        Emite la signal correspondiente para que se lleve la imagen actual
        al comando que selecciono el usuario y se ignoren los anteriores
        '''

        self.signals.retornar_comando.emit(self.__nro_comando)
        self.close()
