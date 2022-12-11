#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para modificar el brillo de las imágenes
'''

##########
#  GUI   #
##########

# imports necesarios para la interfaz grafica
from PyQt4 import QtCore, QtGui

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(264, 144)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.automatico = QtGui.QRadioButton(Dialog)
        self.automatico.setObjectName(_fromUtf8("automatico"))
        self.gridLayout.addWidget(self.automatico, 0, 0, 1, 1)
        self.manual = QtGui.QRadioButton(Dialog)
        self.manual.setObjectName(_fromUtf8("manual"))
        self.gridLayout.addWidget(self.manual, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setMinimum(-100)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.horizontalSlider = QtGui.QSlider(Dialog)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aceptar = QtGui.QPushButton(Dialog)
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.horizontalLayout.addWidget(self.aceptar)
        self.cancelar = QtGui.QPushButton(Dialog)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.horizontalLayout.addWidget(self.cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.manual, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.horizontalSlider.setEnabled)
        QtCore.QObject.connect(self.automatico, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.horizontalSlider.setDisabled)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox.setValue)
        QtCore.QObject.connect(self.automatico, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinBox.setDisabled)
        QtCore.QObject.connect(self.manual, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.automatico.setText(QtGui.QApplication.translate("Dialog", "Automático", None, QtGui.QApplication.UnicodeUTF8))
        self.manual.setText(QtGui.QApplication.translate("Dialog", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Dialog", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))



# clase derivada
class Ventana(QtGui.QDialog, Ui_Dialog):
    def __init__(self, plugin, urlsIn, urlsOut, notificador = None, parent = None):
        # inicializar el padre
        super(Ventana, self).__init__(parent)
        # configurar la interfaz  
        self.setupUi(self)
        # variables necesarias
        # plugin que necesita esta ventana
        self.__plugin = plugin
        # imagenes que modifica el plugin
        self.__imagenesIn = urlsIn        
        self.__imagenesOut = urlsOut
        # copias iniciales
        self.__inicialesIn = urlsIn
        # objeto notificador
        self.__notificador = notificador
        # actualizar el notificador con un parent (obligatorio si hay IU)
        self.__notificador.parent = self

        # configuraciones adicionales
        # mostrar la ventana como modal sobre TODA LA APLICACION
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # establecer el nombre de la ventana
        self.setWindowTitle(self.__plugin.nombre())

        # signals/slots
        # boton aceptar
        self.aceptar.clicked.connect(self.__aceptar)
        
        # boton cancelar
        self.cancelar.clicked.connect(self.close)

        #inicialmente el Slider está desactivado
        self.horizontalSlider.setEnabled(False)
        
        # inicialmente aparece al automático chequeado
        self.automatico.setChecked(True)
        self.spinBox.setEnabled(False)
        #incializando variable para guardar valor del slide...
        self.valor_anterior = 0
        

    def __aceptar(self):
        '''
        Ejecutar el procedimiento del plugin
        '''

        import Image
        
        for i in range(len(self.__inicialesIn)):
            im = Image.open(self.__inicialesIn[i])
 
            if im:
                if self.automatico.isChecked():
                  im= im.point(lambda i: i+25)
                else:
					im= im.point(lambda i: i + self.horizontalSlider.value())
                    
                im.save(self.__imagenesOut[i])  
            else:
                # notificar a la aplicacion el resultado de la operacion
                self.__notificador.error.emit('Error al abrir el archivo' + i)
                return

        # notificar a la aplicacion el resultado de la operacion
        self.__notificador.correcto.emit(self.__plugin.nombre())


    def update_images(self, urlsIn, urlsOut):
        '''
        Actualiza las urls de los ficheros de entrada y de salida para
        la transformacion que realiza este plugin. Esta funcion es llamada
        por la ventana principal cada vez que el notificador emite la
        signal de procedimiento completado con exito
        '''

        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut


##########
#  GUI   #
##########

from plugins.plugin_base import PluginBase
import os

class Brillo(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Brillo'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Aplicar brillo a las imágenes'


    def autores(self):
        return ['Ing. Eddy Figueredo Aguilar']


    def icon(self):
        return os.path.dirname(__file__) + '/images/brillo.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador,padre):
		
		if len(imagenesIn) != len(imagenesOut):
			notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
			return
		else:
			# visualizar la interfaz de usuario del plugin
			window = Ventana(self, imagenesIn, imagenesOut, notificador,padre)
			window.show()
