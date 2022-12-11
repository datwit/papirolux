#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para limpiar la imagen
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
        Limpia las imagenesIn y las guarda en imagenesOut usando OpenCV y SciPy
        '''

        if len(self.imagenesIn) != len(self.imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        from scipy import misc, ndimage
        import cv2, Image, ImageChops, ImageEnhance, ImageFilter, ImageOps

        for i in range(len(self.imagenesIn)):
            im = cv2.imread(self.imagenesIn[i], 0)
            im = cv2.medianBlur(im, 5)
            im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(self.imagenesOut[i], im)
            binary_img = misc.imread(self.imagenesOut[i])
            open_img = ndimage.binary_opening(binary_img)
            close_img = ndimage.binary_closing(open_img)
            misc.imsave(self.imagenesOut[i], close_img)
            im = Image.open(self.imagenesOut[i])
            im1 = ImageChops.invert(im)
            result = ImageChops.subtract(im1, im)
            result = result.convert('L')
            result = ImageChops.invert(result)
            result = ImageEnhance.Brightness(result).enhance(2.0)
            result = ImageOps.colorize(result, (0, 0, 0), (255, 255, 255))
            result.save(self.imagenesOut[i])
            
            
        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()

        return    

class LimpiarImagen(PluginBase):
    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()


    def nombre(self):
        return 'Limpiar imagen SciPy'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Limpia la imagen'


    def autores(self):
        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        return os.path.dirname(__file__) + '/images/clean_bg_03.png'


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
        

        
