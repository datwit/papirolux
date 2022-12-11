#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugins.plugin_base import PluginBase
import os

class ZoomIn(PluginBase):
    '''
    Funciones basicas del plugin
    '''

    def nombre(self):
        return 'Zoom In'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Aumenta el tamaño de las imágenes'


    def autores(self):
        return ['Ing. Yuniel Guzmán Bazán']


    def icon(self):
        return os.path.dirname(__file__) + '/images/zoom-in.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
		
		import Image
		scaleFactor = 1.25
		
		if len(imagenesIn)!= len(imagenesOut):
			notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
			return
		for i in range(len(imagenesIn)):
			im = Image.open(imagenesIn[i])
			w= int(im.size[0]* scaleFactor)
			h= int(im.size[1]* scaleFactor)
			
			im= im.resize((w,h), Image.ANTIALIAS)
			if im:
				im.save(imagenesOut[i])
			else:
				notificador.error.emit('Error al procesar la imagen'+ imagenesIn[i])
		notificador.correcto.emit(self.nombre())
				
        # visualizar la interfaz de usuario del plugin
        #window = Ventana(self, imagenesIn, imagenesOut, notificador)
        #window.show()
