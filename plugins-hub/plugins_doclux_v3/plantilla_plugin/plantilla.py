#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para <descripcion del plugin>
'''

###################################
#   Interfaz de Usuario           #
#   ESTA SECCION ES OPCIONAL      #
###################################

# Seccion necesaria solamente cuando el plugin emplea una interfaz de usuario

# OBSERVE que de las formas en que se puede emplear PyQt para crear
# interfaces de usuario se emplea el metodo HERENCIA MULTIPLE
# Usted puede seleccionar cualquiera de los otros, tomando todas
# las medidas necesarias para su correcto funcionamiento

# El contenido de este bloque debe se COPIADO EXACTAMENTE de la salida
# del comando pyuic4 fichero.ui -o fichero.py

# ASEGURESE de que todos los componentes empleados esten precedidos
# de su correspondiente namespace: QtGui o QtCore (y otros si fuera el caso)

# EJEMPLO (ventana sencilla con 2 botones)

# imports necesarios para la interfaz grafica
# importar PyQt4
from PyQt4 import QtCore, QtGui

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(194, 45)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.gridLayout.addWidget(self.cancelar, 0, 0, 1, 1)
        self.aplicar = QtGui.QPushButton(Form)
        self.aplicar.setObjectName(_fromUtf8("aplicar"))
        self.gridLayout.addWidget(self.aplicar, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
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
            im = Image.open(self.__imagenesIn[i]).convert('L')
            if im:
                im.save(self.__imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + self.__imagenesIn[i])
                return

        self.__notificador.correcto.emit(self.__plugin.nombre())
        return


    def update_images(self, urlsIn, urlsOut):
        '''
        Actualiza las urls de los ficheros de entrada y de salida para
        la transformacion que realiza este plugin. Esta funcion es llamada
        por la ventana principal cada vez que el notificador emite la
        signal de procedimiento completado con exito
        '''

        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut


###################################
#   Definicion del Plugin         #
#   ESTA SECCION OBLIGATORIA      #
###################################

# imports necesarios para el plugin
# importar el plugin base (exactamente asi), la arquitectura conoce
# la direccion real del modulo aunque no esta dentro del plugin
from plugins.plugin_base import PluginBase
# import general (se usa para retornar correctamente el icono)
import os

# clase plugin

# Puede tener cualquier nombre, preferiblemente uno que se ajuste
# a la tarea que realiza el plugin, es imprescindible implementar
# las funciones basicas que se describen en la plantilla

class Plugin(PluginBase):
    # funciones basicas
    def nombre(self):
        '''
        Retorna el nombre del plugin
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return 'Plugin de ejemplo'
        '''

        return ''


    def version(self):
        '''
        Retorna la version del plugin
        (se usa para informacion general)

        Ej: return '1.0'
        '''

        return ''


    def descripcion(self):
        '''
        Retorna una descripcion acerca de que hace el plugin
        (se usa para informacion general)

        Ej: return 'Plugin de ejemplo'
        '''

        return ''


    def autores(self):
        '''
        Retorna una lista con los nombres de los autores del plugin
        (se usa para informacion general)

        Ej: return ['Autor 1', 'Autor 2']
        '''

        return []


    def icon(self):
        '''
        Retorna la URL absoluta del icono del plugin (emplea el modulo os)
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return os.path.dirname(__file__) + '/images/flip.png'
        '''

        return os.path.dirname(__file__) + '/images/docluxlogo.jpg'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Procemimiento principal que ejecuta la aplicacion como punto de entrada
        al plugin

        Parametros:
        [list]        imagenesIn : urls de las imagenes de entrada al plugin
        [list]        imagenesOut: urls de las imagenes de salida al plugin (modificadas)
        [Notificador] notificador: objeto para notificar el estado de las acciones del plugin
        [QWidget]     gui_parent : widget padre para el plugin si tiene una IU

        Debe emplear las imagenes de entrada, modificarlas segun el procedimiento
        del plugin y guardar el resultado empleando las imagenes de salida, para
        esto puede emplear o no una interfaz grafica.

        ES OBLIGATORIO comprobar que las longitudes de las listas de entrada/salida
        sean IGUALES, para garantizar que por cada fichero de entrada existe uno de
        salida, por ejemplo:

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        Recuerde notificar a la aplicacion el resultado de las operaciones
        empleando el objeto notificador, por ejemplo:

            notificador.correcto.emit('nombre del plugin')
            notificador.error.emit('mensaje de error')

        Puede emplear cualquiera de las bibliotecas de procesamiento de
        imagenes existentes, solo debe indicar las dependencias del plugin
        en el fichero LEEME adjunto a este fichero
        '''

        # EJEMPLO (Convertir a escala de grises SIN interfaz grafica)
        '''
        Convierte las imagenes imagenesIn en escala de grises y la guarda en
        imagenesOut usando PIL
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        import Image

        for i in range(len(imagenesIn)):
            im = Image.open(imagenesIn[i]).convert('L')
            if im:
                im.save(imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + imagenesIn[i])
                return

        notificador.correcto.emit(self.nombre())
        return


        # EJEMPLO (Convertir a escala de grises CON interfaz grafica)
        '''
        Convierte las imagenes imagenesIn en escala de grises y la guarda en
        imagenesOut usando una interfaz de usuario y PIL
        '''
        # visualizar la interfaz de usuario del plugin
        window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
        window.show()
