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
        return 'Limpiar imagen PIL'


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
        Limpia las imagenesIn y las guarda en imagenesOut usando PIL
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        import Image, ImageChops, ImageOps, ImageEnhance

        for i in range(len(imagenesIn)):
            im = Image.open(imagenesIn[i])
            if im:
                im1 = ImageChops.invert(im)
                im = ImageChops.subtract( im1, im )
                im = im.convert('L')
                im = ImageChops.invert(im)
                im = ImageEnhance.Brightness(im).enhance(2.0)
                im = ImageOps.colorize(im, (0, 0, 0), (255, 255, 255))
                im.save(imagenesOut[i])
            else:
                notificador.error.emit('Error al procesar la imagen: ' + imagenesIn[i])
                return

        notificador.correcto.emit(self.nombre())
        return
