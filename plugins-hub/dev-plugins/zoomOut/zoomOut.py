#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para disminuir el tamaño de las imágenes
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
        Disminuye el tamaño de las imágenes
        '''
        # notificar el inicio de operaciones
        self.notificador.inicio_operacion.emit()
        
        import Image
        scaleFactor = 0.8
        
        for i in range(len(self.imagenesIn)):
            im = Image.open(self.imagenesIn[i])
            w= int(im.size[0]* scaleFactor)
            h= int(im.size[1]* scaleFactor)
            
            im= im.resize((w,h), Image.ANTIALIAS)
            if im:
                im.save(self.imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen'+ self.imagenesIn[i])
        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()
        return
        
        
class ZoomOut(PluginBase):

    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()


    def nombre(self):
        return 'Escalar -'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Disminuye el tamaño de las imágenes'


    def autores(self):
        return ['Ing. Yuniel Guzmán Bazán']


    def icon(self):
        return os.path.dirname(__file__) + '/images/zoom-out.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        # pre-chequeo obligatorio
        if len(imagenesIn) != len(imagenesOut):
            self.notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        # inicializar los atributos necesarios
        # en este caso se ignora el atributo gui_parent
        # es ignorado tambien en setData dentro de ThreadPlugin
        self.thread.setData(self, notificador, imagenesIn, imagenesOut)
        # iniciar el hilo
        self.thread.start()
