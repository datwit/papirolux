#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para convertir la imagen a escala de grises
'''

from plugins.plugin_base import PluginBase
import os

class EscalaGrises(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Escala de grises'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Convierte una imagen a Escala de grises'


    def autores(self):
        return ['Ing. Leonel Salazar Videaux']


    def icon(self):
        return os.path.dirname(__file__) + '/images/gray_scale.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
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
