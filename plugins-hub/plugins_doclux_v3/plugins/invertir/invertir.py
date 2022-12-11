#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para invertir una imagen horizonta/verticalmente
'''

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
        Form.resize(196, 105)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontal = QtGui.QRadioButton(Form)
        self.horizontal.setChecked(True)
        self.horizontal.setObjectName(_fromUtf8("horizontal"))
        self.verticalLayout.addWidget(self.horizontal)
        self.vertical = QtGui.QRadioButton(Form)
        self.vertical.setObjectName(_fromUtf8("vertical"))
        self.verticalLayout.addWidget(self.vertical)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.horizontalLayout.addWidget(self.cancelar)
        self.aplicar = QtGui.QPushButton(Form)
        self.aplicar.setObjectName(_fromUtf8("aplicar"))
        self.horizontalLayout.addWidget(self.aplicar)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontal.setText(QtGui.QApplication.translate("Form", "Izquierda-Derecha", None, QtGui.QApplication.UnicodeUTF8))
        self.vertical.setText(QtGui.QApplication.translate("Form", "Arriba-Abajo", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.aplicar.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))


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
        # boton aplicar
        self.aplicar.clicked.connect(self.__aceptar)
        # boton cancelar
        self.cancelar.clicked.connect(self.close)


    def __aceptar(self):
        '''
        Ejecutar el procedimiento del plugin
        '''

        import Image

        for i in range(len(self.__imagenesIn)):
            im = Image.open(self.__imagenesIn[i])
            if im:
                if self.horizontal.isChecked():
                    im = im.transpose(Image.FLIP_LEFT_RIGHT)
                else:
                    im = im.transpose(Image.FLIP_TOP_BOTTOM)

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


from plugins.plugin_base import PluginBase
import os

class Invertir(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Invertir imagen'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Invierte una imagen vertical/horizontalmente'


    def autores(self):
        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        return os.path.dirname(__file__) + '/images/rotar_hrzt_vert.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Invierte las imagenes imagenesIn vertical/horizontalmente y las guarda en
        imagenesOut usando PIL
        '''

        # visualizar la interfaz de usuario del plugin
        window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
        window.show()
