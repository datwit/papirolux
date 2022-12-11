#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para acercar o alejar las imágenes
'''

# imports necesarios para la interfaz grafica
import sys
from PyQt4 import QtGui,QtCore,QtWebKit

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# clase auxiliar para definir el Thread
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
        self.ventana = None


    def setData(self, pluginObj, notificador, imagesIn, imagesOut, gui):
        self.plugin = pluginObj
        self.notificador = notificador
        self.imagenesIn = imagesIn
        self.imagenesOut = imagesOut
        self.ventana = gui


    def run(self):
        # procedimiento principal
        import Image
        import ImageEnhance 


# clase derivada

class Ventana(QtGui.QMainWindow):
    def __init__(self,url):
		QtGui.QMainWindow.__init__(self)
		

		self.pbar = QtGui.QProgressBar()
		self.pbar.setMaximumWidth(120)
		self.wb=QtWebKit.QWebView(loadProgress = self.pbar.setValue, loadFinished = self.pbar.hide, loadStarted = self.pbar.show, titleChanged = self.setWindowTitle)
		self.setCentralWidget(self.wb)
		
		self.tb=self.addToolBar("Zoom")        
		
		self.quit = QtGui.QShortcut("Ctrl+Q", self, activated = self.close)
		self.zoomIn = QtGui.QShortcut("Ctrl++", self, activated = lambda: self.wb.setZoomFactor(self.wb.zoomFactor()+.2))
		self.zoomOut = QtGui.QShortcut("Ctrl+-", self, activated = lambda: self.wb.setZoomFactor(self.wb.zoomFactor()-.2))
		self.zoomOne = QtGui.QShortcut("Ctrl+=", self, activated = lambda: self.wb.setZoomFactor(1))
		self.wb.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)

		
		self.wb.load(url)

    def __aceptar(self):
        '''
        Ejecutar el procedimiento del plugin
        '''
        # actualizar los datos para que el HILO pueda realizar la operacion
        self.thread.setData(self.__plugin, self.__notificador, self.__imagenesIn, self.__imagenesOut , self)
        # ejecutar el HILO PARELELO
        self.thread.start()


    def update_images(self, urlsIn, urlsOut):
        '''
        Actualiza las urls de los ficheros de entrada y de salida para
        la transformacion que realiza este plugin. Esta funcion es llamada
        por la ventana principal cada vez que el notificador emite la
        signal de procedimiento completado con exito
        '''

        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut


from plugins.plugin_base import PluginBase
import os

class Zoom(PluginBase):
    '''
    Funciones basicas del plugin
    '''
    def __init__(self):
        # hilo
        self.thread = ThreadPlugin()

    def nombre(self):
        return 'Zoom +/-'


    def version(self):
        return '1.0'


    def descripcion(self):
        return 'Acerca o aleja la imagen'


    def autores(self):
        return ['José A Escobar Toranzo']


    def icon(self):
        return os.path.dirname(__file__) + '/images/zoom.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        # self.thread.setData(self, notificador, imagenesIn, imagenesOut)
        # visualizar la interfaz de usuario del plugin
        urls = imagenesIn[0]
        url = QtCore.QUrl(urls)
        window = Ventana(url)
        window.show()
