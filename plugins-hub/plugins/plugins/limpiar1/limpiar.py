#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para limpiar la imagen
'''

from plugins.plugin_base import PluginBase
import os

class LimpiarImagen(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Limpiar imagen OpenCV'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Limpia la imagen'


    def autores(self):
        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        return os.path.dirname(__file__) + '/images/clean_bg.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Limpia las imagenesIn y las guarda en imagenesOut usando OpenCV
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        import cv2

        for i in range(len(imagenesIn)):
            im = cv2.imread(imagenesIn[i], 0)
            im = cv2.medianBlur(im, 5)
            im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(imagenesOut[i], im)

        notificador.correcto.emit(self.nombre())
        return
