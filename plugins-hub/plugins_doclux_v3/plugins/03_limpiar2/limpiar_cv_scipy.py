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
        '''
        Limpia las imagenesIn y las guarda en imagenesOut usando OpenCV y SciPy
        '''

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        from scipy import misc, ndimage
        import cv2, Image, ImageChops, ImageEnhance, ImageFilter, ImageOps

        for i in range(len(imagenesIn)):
            im = cv2.imread(imagenesIn[i], 0)
            im = cv2.medianBlur(im, 5)
            im = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            cv2.imwrite(imagenesOut[i], im)
            binary_img = misc.imread(imagenesOut[i])
            open_img = ndimage.binary_opening(binary_img)
            close_img = ndimage.binary_closing(open_img)
            misc.imsave(imagenesOut[i], close_img)
            im = Image.open(imagenesOut[i])
            im1 = ImageChops.invert(im)
            result = ImageChops.subtract(im1, im)
            result = result.convert('L')
            result = ImageChops.invert(result)
            result = ImageEnhance.Brightness(result).enhance(2.0)
            result = ImageOps.colorize(result, (0, 0, 0), (255, 255, 255))
            result.save(imagenesOut[i])

        notificador.correcto.emit(self.nombre())
        return
