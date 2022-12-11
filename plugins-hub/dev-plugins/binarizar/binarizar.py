#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para binarizar imágenes a partir de su valor umbral
'''

from PyQt4 import QtCore, QtGui
from plugins.plugin_base import PluginBase
import os

#Se importa Image de SimpleCV
from SimpleCV import Image

#~ import Image
import mahotas
import scipy

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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


    def setData(self, pluginObj, notificador, imagesIn, imagesOut):
        self.plugin = pluginObj
        self.notificador = notificador
        self.imagenesIn = imagesIn
        self.imagenesOut = imagesOut


    def run(self):
        '''
        Limpia las imagenesIn y las guarda en imagenesOut usando PIL
        '''

        # notificar el inicio de operaciones
        self.notificador.inicio_operacion.emit()
        if len(self.imagenesIn) != len(self.imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        for i in range(len(self.imagenesIn)):

            # cargar la imagen con (scipy & imread)
            im = scipy.misc.pilutil.imread(self.imagenesIn[i])

            # obtener el valor umbral de la imagen a partir del histograma (mediante el metodo otsu)
            value_threshold = mahotas.thresholding.otsu(im)

            # se vuelve a cargar la imagen. en este caso la clase Image 
            # hace referencia a la que se importa desde el SimpleCV
            im = Image(self.imagenesIn[i])

            # aplicar la binarizacion de imagem a partir de su valor umbral
            im = im.binarize(value_threshold)

            if im:
                im.save(self.imagenesOut[i])
            else:
                self.notificador.error.emit('Error al procesar la imagen: ' + self.imagenesIn[i])
                return
        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()

        return
from plugins.plugin_base import PluginBase
import os

class Plugin(PluginBase):
    # funciones basicas
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()
    
    def nombre(self):
        '''
        Retorna el nombre del plugin
        (se usa para colocarlo en el menu y en la barra de herramientas)
        '''

        return 'Binarizar imagen'


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

        return 'Plugins para binarizar imágenes a partir de su valor umbral obtenido por metodo otsu'


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

        return os.path.dirname(__file__) + '/images/binarizar.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        # pre-chequeo obligatorio
        if len(imagenesIn) != len(imagenesOut):
            self.notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        # inicializar los atributos necesarios
        # en este caso se ignora el atributo gui_parent
        # es ignorado tambien en setData dentro de ThreadPlugin
        self.thread.setData(self,notificador,imagenesIn,imagenesOut)
        # iniciar el hilo
        self.thread.start()
