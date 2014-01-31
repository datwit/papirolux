#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para <descripcion del plugin>
'''

###################################
#   Definicion del Thread         #
#   ESTA SECCION OBLIGATORIA      #
###################################

# Seccion que define la clase ThreadPlugin, esta se encarga de ejecutar
# el procedimiento del plugin en un hilo independiente evitando que se
# bloquee la IU mientras se ejecutan las operaciones, tambien se encarga
# de notificar a la IU los resultados para que se continue el funcionamiento
# de la aplicacion segun la respuesta

# OBSERVE se debe actualizar esta clase con los elementos que se necesiten
# segun el caso, pero siempre es OBLIGATORIO al menos mantener el metodo
# run() con el codigo principal, tambien los atributos plugin, notificador
# imagenesIn e imagenesOut que sirven de ayudantes a la clase ThreadPlugin

# EJEMPLO (Limpiar Imagen usando PIL)

# imports necesarios para el QThread
from PyQt4 import QtCore

# clase Thread
class ThreadPlugin(QtCore.QThread):
    '''
    Subclase que ejecuta el procedimiento en un hilo independiente
    '''
    def __init__(self, parent = None):
        super(ThreadPlugin, self).__init__(parent)

        # atributos OBLIGATORIOS
        self.plugin = None
        self.notificador = None
        self.imagenesIn = []
        self.imagenesOut = []


    # metodo OBLIGATORIO para actualizar los atributos del Hilo
    # antes de iniciar el funcionamiento
    def setData(self, pluginObj, notificador, imagesIn, imagesOut):
        self.plugin = pluginObj
        self.notificador = notificador
        self.imagenesIn = imagesIn
        self.imagenesOut = imagesOut


    # procedimiento PRINCIPAL, aqui va el codigo del plugin
    def run(self):
        '''
        Limpia las imagenes empleando PIL
        '''
        # notificar el inicio de operaciones
        self.notificador.inicio_operacion.emit()

        import Image, ImageChops, ImageOps, ImageEnhance

        for i in range(len(self.imagenesIn)):
            im = Image.open(self.imagenesIn[i])
            if im:
                im1 = ImageChops.invert(im)
                im = ImageChops.subtract( im1, im )
                im = im.convert('L')
                im = ImageChops.invert(im)
                im = ImageEnhance.Brightness(im).enhance(2.0)
                im = ImageOps.colorize(im, (0, 0, 0), (255, 255, 255))
                im.save(self.imagenesOut[i])
            else:
                self.notificador.error.emit('Error al procesar la imagen: ' + self.imagenesIn[i])
                return

        # notificar a la aplicacion el resultado de la operacion
        self.notificador.correcto.emit(self.plugin.nombre())
        # notificar el fin de operaciones
        self.notificador.fin_operacion.emit()

        return

###################################
#   Definicion del Plugin         #
#   ESTA SECCION OBLIGATORIA      #
###################################

# imports necesarios para el plugin
# importar el plugin base (exactamente asi), la arquitectura conoce
# la direccion real del modulo aunque no esta dentro del plugin
from plugins.plugin_base import PluginBase
# import general (se usa para retornar correctamente el icono)
import os

# Clase plugin
# Puede tener cualquier nombre, preferiblemente uno que se ajuste
# a la tarea que realiza el plugin, es imprescindible implementar
# las funciones basicas que se describen en la plantilla

class Plugin(PluginBase):
    # funciones basicas
    def nombre(self):
        '''
        Retorna el nombre del plugin
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return 'Plugin de ejemplo'
        '''

        return ''


    def version(self):
        '''
        Retorna la version del plugin
        (se usa para informacion general)

        Ej: return '1.0'
        '''

        return ''


    def descripcion(self):
        '''
        Retorna una descripcion acerca de que hace el plugin
        (se usa para informacion general)

        Ej: return 'Plugin de ejemplo'
        '''

        return ''


    def autores(self):
        '''
        Retorna una lista con los nombres de los autores del plugin
        (se usa para informacion general)

        Ej: return ['Autor 1', 'Autor 2']
        '''

        return []


    def icon(self):
        '''
        Retorna la URL absoluta del icono del plugin (emplea el modulo os)
        (se usa para colocarlo en el menu y en la barra de herramientas)

        Ej: return os.path.dirname(__file__) + '/images/flip.png'
        '''

        return os.path.dirname(__file__) + '/images/docluxlogo.jpg'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):
        '''
        Procemimiento principal que ejecuta la aplicacion como punto de entrada
        al plugin

        Parametros:
        [list]        imagenesIn : urls de las imagenes de entrada al plugin
        [list]        imagenesOut: urls de las imagenes de salida al plugin (modificadas)
        [Notificador] notificador: objeto para notificar el estado de las acciones del plugin
        [QWidget]     gui_parent : widget padre para el plugin si tiene una IU

        Debe emplear las imagenes de entrada, modificarlas segun el procedimiento
        del plugin y guardar el resultado empleando las imagenes de salida, para
        esto puede emplear o no una interfaz grafica.

        ES OBLIGATORIO comprobar que las longitudes de las listas de entrada/salida
        sean IGUALES, para garantizar que por cada fichero de entrada existe uno de
        salida, por ejemplo:

        if len(imagenesIn) != len(imagenesOut):
            notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
            return

        Recuerde notificar a la aplicacion el resultado de las operaciones
        empleando el objeto notificador, por ejemplo:

            notificador.correcto.emit('nombre del plugin')
            notificador.error.emit('mensaje de error')

        Despues de esto solo resta inicializar el HILO y llamar al procedimiento
        Vea el EJEMPLO
        '''

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
