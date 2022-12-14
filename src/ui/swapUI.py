#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ui.swap import Ui_Form

class Swap(QDialog, Ui_Form):
    # signal necesaria
    terminado = pyqtSignal(str,str)
    
    def __init__(self, dir_swap, parent = None):
        super(Swap, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(u'Gestión de la Swap')

        self.setWindowModality(Qt.ApplicationModal)
        
        self.__swap = dir_swap
        self.__nueva_swap = ''
        self.__nuevo_dir_swap = ''
        
        # mostar la dirección actual de la swap
        self.swap_actual.setText(self.__swap)
        
        # boton buscar
        self.dir_swap.clicked.connect(self.gestionar)
        # boton guardar
        self.aceptar.clicked.connect(self.guardar)
        # boton cancelar
        self.cancelar.clicked.connect(self.close)


    def gestionar(self):
        '''
        Permite la selección de un nuevo directorio para la swap
        '''
        dirName = QFileDialog.getExistingDirectory(None, u"Seleccionar ubicación de la swap", QDir.homePath(), QFileDialog.ShowDirsOnly )
        if dirName.isEmpty() and self.nueva_swap.text().length()==0:
            return
        else:
			self.__nuevo_dir_swap = str(dirName)
			self.__nueva_swap = str(self.__nuevo_dir_swap + '/.' + 'DocLux' + '/swap')
			self.nueva_swap.setText(self.__nueva_swap)


    def guardar(self):
		'''
		Emite la señal para informar que se seleccionó una nueva swap
		'''
		self.__nueva_swap = self.nueva_swap.text()
		self.terminado.emit(self.__nueva_swap, self.__nuevo_dir_swap)	
