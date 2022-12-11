#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para convertir la imagen a escala de grises
'''

from plugins.plugin_base import PluginBase
import os
from PyQt4 import QtCore

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
        import Image

        for i in range(len(self.imagenesIn)):
            im = Image.open(self.imagenesIn[i]).convert('L')
            if im:
                im.save(self.imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + self.imagenesIn[i])
                return
        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()

        return        
            

class EscalaGrises(PluginBase):
    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()

    def nombre(self):
        return 'Escala de grises'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Convierte una imagen a Escala de grises'


    def autores(self):
        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        return os.path.dirname(__file__) + '/images/escala_de_grises.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Convierte las imagenes imagenesIn en escala de grises y la guarda en
        imagenesOut usando PIL
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return
        # inicializar los atributos necesarios
        # en este caso se ignora el atributo gui_parent
        # es ignorado tambien en setData dentro de ThreadPlugin
        self.thread.setData(self, notificador, imagenesIn, imagenesOut)
        # iniciar el hilo
        self.thread.start()  
        
