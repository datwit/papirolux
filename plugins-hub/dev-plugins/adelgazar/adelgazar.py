#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para el adelgazamiento de una imagen
'''

from plugins.plugin_base import PluginBase
import os
from PyQt4 import QtCore

from scipy import weave
import numpy as np
import cv2
import sys
import Image


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

        for i in range(len(self.imagenesIn)):
            im = cv2.imread(self.imagenesIn[i])
            imh = ~im
            cv2.imwrite(self.imagenesOut[i], imh)
            src= cv2.imread(self.imagenesOut[i])
            if src == None:
				sys.exit()
            bw= cv2.cvtColor(src, cv2.cv.CV_BGR2GRAY)    
            _, bw2 = cv2.threshold(bw, 100, 255, cv2.THRESH_BINARY)
            bw2 = thinning(bw2)
            cv2.imwrite(self.imagenesOut[i], bw2)
            bm= cv2.imread(self.imagenesOut[i])
            inv= ~bm
            cv2.imwrite(self.imagenesOut[i], inv)
            cv2.imwrite(self.imagenesOut[i], inv)
            
            
            
        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()

        return        
            

def thinning(src):
    dst = src.copy() / 255
    prev = np.zeros(src.shape[:2], np.uint8)
    diff = None

    while True:
        dst = _thinningIteration(dst, 0)
        dst = _thinningIteration(dst, 1)
        diff = np.absolute(dst - prev)
        prev = dst.copy()
        if np.sum(diff) == 0:
            break

    return dst * 255

def _thinningIteration(im, iter):
    I, M = im, np.zeros(im.shape, np.uint8)
    expr = """
    for (int i = 1; i < NI[0]-1; i++) {
        for (int j = 1; j < NI[1]-1; j++) {
            int p2 = I2(i-1, j);
            int p3 = I2(i-1, j+1);
            int p4 = I2(i, j+1);
            int p5 = I2(i+1, j+1);
            int p6 = I2(i+1, j);
            int p7 = I2(i+1, j-1);
            int p8 = I2(i, j-1);
            int p9 = I2(i-1, j-1);

            int A  = (p2 == 0 && p3 == 1) + (p3 == 0 && p4 == 1) +
                     (p4 == 0 && p5 == 1) + (p5 == 0 && p6 == 1) +
                     (p6 == 0 && p7 == 1) + (p7 == 0 && p8 == 1) +
                     (p8 == 0 && p9 == 1) + (p9 == 0 && p2 == 1);
            int B  = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9;
            int m1 = iter == 0 ? (p2 * p4 * p6) : (p2 * p4 * p8);
            int m2 = iter == 0 ? (p4 * p6 * p8) : (p2 * p6 * p8);

            if (A == 1 && B >= 2 && B <= 6 && m1 == 0 && m2 == 0) {
                M2(i,j) = 1;
            }
        }
    } 
    """
    weave.inline(expr, ["I", "iter", "M"])
    return (I & ~M)

class Esqueletizar(PluginBase):
    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()

    def nombre(self):
        return 'Adelgazar'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Adelgaza el trazo del texto contenido en las imágenes'


    def autores(self):
        return ['Ibraham Rojas Salina']


    def icon(self):
        return os.path.dirname(__file__) + '/images/adelgazar.png'


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
        
