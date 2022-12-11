#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugins.plugin_base import PluginBase
import os

class RotarIzq(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Rotar Izquierda'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Rota a la izquierda las imágenes'


    def autores(self):
        return ['Ing. Yuniel Guzmán Bazán']


    def icon(self):
        return os.path.dirname(__file__) + '/images/rotar_izq.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
		
		import Image

		if len(imagenesIn)!= len(imagenesOut):
			notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
			return
		for i in range(len(imagenesIn)):
			im = Image.open(imagenesIn[i])
			if im:
				im=im.rotate(90)
				im.save(imagenesOut[i])
			else:
				notificador.error.emit('Error al procesar la imagen'+ imagenesIn[i])
		notificador.correcto.emit(self.nombre())
