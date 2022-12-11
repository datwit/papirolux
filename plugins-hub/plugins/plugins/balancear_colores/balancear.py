#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para balancear los colores de las imágenes
'''

from plugins.plugin_base import PluginBase
import os

class BalancearColores(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Balancear colores'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Nivela los colores de las imágenes'


    def autores(self):
        return ['Ing. Yuniel Guzmán Bazán']


    def icon(self):
        return os.path.dirname(__file__) + '/images/balancear_color.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Ecualiza el color de las imagenes imagenesIn y la guarda en
        imagenesOut usando PIL - ImageOps
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        import Image
        import ImageOps

        for i in range(len(imagenesIn)):
            im = Image.open(imagenesIn[i])
            im=ImageOps.autocontrast(im,cutoff=0.5)
            if im:
                im.save(imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + imagenesIn[i])
                return

        notificador.correcto.emit(self.nombre())
        return
