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

# EJEMPLO (ventana sencilla con 2 botones y otros controles para Invertir Imagen)

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


###################################
#   Definicion del Thread         #
#   ESTA SECCION OBLIGATORIA      #
###################################

# Seccion que define la clase ThreadPlugin, esta se encarga de ejecutar
# el procedimiento del plugin en un hilo independiente evitando que se
# bloquee la IU mientras se ejecutan las operaciones, tambien se encarga
# de notificar a la IU los resultados para que se continue el funcionamiento
# de la aplicacion segun la respuesta

# OBSERVE se debe actualizar esta clase con los elementos que se necesiten
# segun el caso, pero siempre es OBLIGATORIO al menos mantener el metodo
# run() con el codigo principal, tambien los atributos plugin, notificador
# imagenesIn e imagenesOut que sirven de ayudantes a la clase ThreadPlugin

# EJEMPLO (Invertir imagen usando PIL)

# imports necesarios para el QThread, solo si no se importo anteriormente
# from PyQt4 import QtCore

# clase auxiliar para definir el Thread
class ThreadPlugin(QtCore.QThread):
    '''
    Subclase que ejecuta el procedimiento en un hilo independiente
    '''
    def __init__(self, parent = None):
        super(ThreadPlugin, self).__init__(parent)

        # atributos OBLIGATORIOS
        self.plugin = None
        self.notificador = None
        self.imagenesIn = []
        self.imagenesOut = []
        self.ventana = None


    # metodo OBLIGATORIO para actualizar los atributos del Hilo
    # antes de iniciar el funcionamiento
    def setData(self, pluginObj, notificador, imagesIn, imagesOut, gui):
        self.plugin = pluginObj
        self.notificador = notificador
        self.imagenesIn = imagesIn
        self.imagenesOut = imagesOut
        self.ventana = gui


    # procedimiento PRINCIPAL, aqui va el codigo del plugin
    def run(self):
        '''
        Invierte imagenes empleando PIL
        '''
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


###################################
#   Definicion de la Ventana      #
#   ESTA SECCION OBLIGATORIA      #
###################################

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

        # ahora los procedimientos los realiza el HILO AUXILIAR
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

class Invertir(PluginBase):
    # funciones basicas
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()


    def nombre(self):
        '''
        Retorna el nombre del plugin
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return 'Plugin de ejemplo'
        '''

        return 'Invertir imagen'


    def version(self):
        '''
        Retorna la version del plugin
        (se usa para informacion general)

        Ej: return '1.0'
        '''

        return '1.0'


    def descripcion(self):
        '''
        Retorna una descripcion acerca de que hace el plugin
        (se usa para informacion general)

        Ej: return 'Plugin de ejemplo'
        '''

        return 'Invierte una imagen vertical/horizontalmente'


    def autores(self):
        '''
        Retorna una lista con los nombres de los autores del plugin
        (se usa para informacion general)

        Ej: return ['Autor 1', 'Autor 2']
        '''

        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        '''
        Retorna la URL absoluta del icono del plugin (emplea el modulo os)
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return os.path.dirname(__file__) + '/images/flip.png'
        '''

        return os.path.dirname(__file__) + '/images/flip.png'


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

        Despues de esto solo resta inicializar el HILO y llamar al procedimiento
        Vea el EJEMPLO
        '''
        # pre-chequeo obligatorio
        if len(imagenesIn) != len(imagenesOut):
            self.notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        # visualizar la interfaz de usuario del plugin
        window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
        window.show()
