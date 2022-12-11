#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para aplicar negitvo a las imagenes (invertir las imagenes binarias)
'''

from PyQt4 import QtCore, QtGui

#Se importa Image de SimpleCV
from SimpleCV import Image

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# clase derivada
class Ventana(QtGui.QDialog):
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

        #~ self.__notificador.correcto.emit(self.__plugin.nombre())
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


from plugins.plugin_base import PluginBase
import os

class Plugin(PluginBase):
    # funciones basicas
    def nombre(self):
        '''
        Retorna el nombre del plugin
        (se usa para colocarlo en el menu y en la barra de herramientas)
        '''

        return 'Negativo de imagen'


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

        return 'Plugin para aplicar negitvo a las imagenes'


    def autores(self):
        '''
        Retorna una lista con los nombres de los autores del plugin
        (se usa para informacion general)

        Ej: return ['Autor 1', 'Autor 2']
        '''

        return ['Ing. Eduardo Salazar Martínez']


    def icon(self):
        '''
        Retorna la URL absoluta del icono del plugin (emplea el modulo os)
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return os.path.dirname(__file__) + '/images/flip.png'
        '''

        return os.path.dirname(__file__) + '/images/negativo.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        for i in range(len(imagenesIn)):

            # cargar la imagen imagenesIn[i] y aplicar funcion "invert"
            im = Image(imagenesIn[i]).invert()

            if im:
                im.save(imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + imagenesIn[i])
                return

        notificador.correcto.emit(self.nombre())
        return


        # EJEMPLO (Aplicar negativo a imagenes CON uso de una interfaz grafica)
        '''
        Convierte las imagenes imagenesIn en imagenes negativas y la 
        guarda en imagenesOut usando una interfaz de usuario y PIL
        '''
        # visualizar la interfaz de usuario del plugin
        window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
        window.show()
