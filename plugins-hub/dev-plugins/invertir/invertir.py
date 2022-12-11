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


# clase auxiliar para definir el Thread
class ThreadPlugin(QtCore.QThread):
    '''
    Subclase que ejecuta el procedimiento en un hilo independiente
    '''
    def __init__(self, parent = None):
        super(ThreadPlugin, self).__init__(parent)

        self.plugin = None
        self.notificador = None
        self.imagenesIn = []
        self.imagenesOut = []
        self.ventana = None


    def setData(self, pluginObj, notificador, imagesIn, imagesOut, gui):
        self.plugin = pluginObj
        self.notificador = notificador
        self.imagenesIn = imagesIn
        self.imagenesOut = imagesOut
        self.ventana = gui


    def run(self):
        # notificar el inicio de operaciones
        self.notificador.inicio_operacion.emit()

        # procedimiento principal
        import Image

        for i in range(len(self.imagenesIn)):
            im = Image.open(self.imagenesIn[i])
            if im:
                if self.ventana.horizontal.isChecked():
                    im = im.transpose(Image.FLIP_LEFT_RIGHT)
                else:
                    im = im.transpose(Image.FLIP_TOP_BOTTOM)

                im.save(self.imagenesOut[i])
            else:
                # notificar a la aplicacion el resultado de la operacion
                self.notificador.error.emit('Error al abrir el archivo' + i)
                return

        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()


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

        # hilo auxiliar
        self.thread = ThreadPlugin()


    def __aceptar(self):
        '''
        Ejecutar el procedimiento del plugin
        '''

        # actualizar los datos para que el HILO pueda realizar la operacion
        self.thread.setData(self.__plugin, self.__notificador, self.__imagenesIn, self.__imagenesOut, self)
        # ejecutar el HILO PARELELO
        self.thread.start()


    def update_images(self, urlsIn, urlsOut):
        '''
        Actualiza las urls de los ficheros de entrada y de salida para
        la transformacion que realiza este plugin. Esta funcion es llamada
        por la ventana principal cada vez que el notificador emite la
        signal de procedimiento completado con exito
        '''

        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut


# imports necesarios para el funcionamiento del plugin
from plugins.plugin_base import PluginBase
import os

class Invertir(PluginBase):
    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()


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
        # pre-chequeo obligatorio
        if len(imagenesIn) != len(imagenesOut):
            self.notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        # visualizar la interfaz de usuario del plugin
        window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
        window.show()
