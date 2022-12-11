#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para modificar el RGB de las imágenes
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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(268, 132)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.spinBox_rojo = QtGui.QSpinBox(Form)
        self.spinBox_rojo.setMaximum(255)
        self.spinBox_rojo.setObjectName(_fromUtf8("spinBox_rojo"))
        self.horizontalLayout_4.addWidget(self.spinBox_rojo)
        self.Slider_rojo = QtGui.QSlider(Form)
        self.Slider_rojo.setMaximum(255)
        self.Slider_rojo.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_rojo.setObjectName(_fromUtf8("Slider_rojo"))
        self.horizontalLayout_4.addWidget(self.Slider_rojo)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spinBox_verde = QtGui.QSpinBox(Form)
        self.spinBox_verde.setMaximum(255)
        self.spinBox_verde.setObjectName(_fromUtf8("spinBox_verde"))
        self.horizontalLayout_3.addWidget(self.spinBox_verde)
        self.Slider_verde = QtGui.QSlider(Form)
        self.Slider_verde.setMaximum(255)
        self.Slider_verde.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_verde.setObjectName(_fromUtf8("Slider_verde"))
        self.horizontalLayout_3.addWidget(self.Slider_verde)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spinBox_azul = QtGui.QSpinBox(Form)
        self.spinBox_azul.setMaximum(255)
        self.spinBox_azul.setObjectName(_fromUtf8("spinBox_azul"))
        self.horizontalLayout_2.addWidget(self.spinBox_azul)
        self.Slider_azul = QtGui.QSlider(Form)
        self.Slider_azul.setMaximum(255)
        self.Slider_azul.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_azul.setObjectName(_fromUtf8("Slider_azul"))
        self.horizontalLayout_2.addWidget(self.Slider_azul)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aceptar = QtGui.QPushButton(Form)
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.horizontalLayout.addWidget(self.aceptar)
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.horizontalLayout.addWidget(self.cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Slider_rojo, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_rojo.setValue)
        QtCore.QObject.connect(self.spinBox_rojo, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Slider_rojo.setValue)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QObject.connect(self.spinBox_verde, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Slider_verde.setValue)
        QtCore.QObject.connect(self.Slider_verde, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_verde.setValue)
        QtCore.QObject.connect(self.spinBox_azul, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Slider_azul.setValue)
        QtCore.QObject.connect(self.Slider_azul, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_azul.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Rojo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Verde", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Azul", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))


# clase derivada
class Ventana(QtGui.QDialog, Ui_Form):
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
        

    def __aceptar(self):
        '''
        Ejecutar el procedimiento del plugin
        '''
 
        import PythonMagick
        
        color=PythonMagick.Color("#2525")
        for i in range(len(self.__inicialesIn)):
            im = PythonMagick.Image(self.__inicialesIn[i])
            if im:
				red=self.Slider_rojo.value()
				gren=self.Slider_verde.value()
				blue=self.Slider_azul.value()
				im.colorize(red,gren,blue,color)
				im.write(self.__imagenesOut[i])
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

class Modificar_color(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Modificar colores'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Altera el RGB de las imágenes'


    def autores(self):
        return ['Ing. Yuniel Guzmán Bazán']


    def icon(self):
        return os.path.dirname(__file__) + '/images/modificar_color.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
		
		if len(imagenesIn) != len(imagenesOut):
			notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
			return
		else:
			# visualizar la interfaz de usuario del plugin
			window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
			window.show()
