#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from PIL import Image
except ImportError:
    import Image
import os
#~ from PyQt4.QtCore import *
#~ from PyQt4.QtGui import *

ancho_maximo = 1200
miniatura_size = (32, 40)

class DocLux_Imagen:
    '''
    Define el concepto de Imagen en DocLux.

    Contiene elementos como:
    - url de la imagen original en el disco
    - lista de comandos aplicados a la imagen
    -

    Almacena los ficheros temporales en el directorio swapDir
    '''

    def __init__(self, swapDir, imgURL, seleccionada=False):
        '''
        Constructor de la clase

        Parametros:
        - [string] swapDir:      directorio para guardar los temporales
        - [string] imgURL:       ruta del archivo en el disco
        - [bool]   seleccionada: define si la imagen esta seleccionada o no
        '''
        #variable para controlar si la imagen está seleccionada o no (original o procesada)
        self.__seleccionada = seleccionada


        # donde guardar los temporales (ruta sin el / al final)
        self.__swap = swapDir

        # datos de la imagen original
        # nombre (sin extension)
        self.__nombre = str(os.path.splitext(os.path.basename(imgURL))[0])
        # copiar la imagen al area de intercambio
        salida = self.__swap + '/' + self.__nombre + '.jpg'
        tmp = Image.open(imgURL)
        # ajuste del ancho
        if tmp.size[0] > ancho_maximo:
            tmp = tmp.resize((ancho_maximo, int(ancho_maximo * tmp.size[1] / tmp.size[0])))
        tmp.save(salida)
        self.__ruta = salida

        # actualizar estado
        self.__seleccionada = seleccionada

        if seleccionada == False:
            # construir la miniatura original y guardarla
            self.__miniatura_orig = self.__constriur_miniatura_original()
        else:
            # datos de la imagen procesada
            # lista de comandos (strings)
            self.__comandos = []
            self.__comandos_deshechos = []
            # ruta (swapDir/nombre+#COMANDO+ext)
            self.__procesada_actual = self.__ruta
            # miniatura procesada
            self.__miniatura_proc = self.__constriur_miniatura_procesada()


    def get_original(self):
        '''
        Retorna la ruta de la imagen original
        '''

        return self.__ruta


    def get_nombre(self):
        '''
        Retorna el nombre de la imagen
        '''

        return self.__nombre


    def get_miniatura_original(self):
        '''
        Retorna la miniatura de la imagen original
        '''

        return self.__miniatura_orig


    def get_miniatura_procesada(self):
        '''
        Retorna la miniatura de la imagen procesada
        '''

        return self.__miniatura_proc


    def __constriur_miniatura_original(self):
        '''
        Constriur la miniatura original y guardarla en swapDir

        Ruta:
        - swapDir/miniatura_NOMBRE.jpg
        '''

        salida = self.__swap + '/' + 'miniatura_' + self.__nombre + '.jpg'
        im = Image.open(self.get_original())
        im.thumbnail(miniatura_size)
        im.save(salida)

        return salida


    def __constriur_miniatura_procesada(self):
        '''
        Constriur la miniatura procesada y guardarla en swapDir

        Ruta:
        - swapDir/miniatura_proc_NOMBRE.jpg
        '''

        salida = self.__swap + '/' + 'miniatura_proc_' + self.__nombre + '.jpg'
        im = Image.open(self.get_procesada())
        im.thumbnail(miniatura_size)
        im.save(salida)

        return salida


    def get_procesada(self):
        '''
        Retorna la ruta de la imagen procesada
        '''

        if len(self.__comandos) > 0:
            return self.__swap + '/' + self.__nombre + '_' + str(len(self.__comandos)) + '.jpg'
        else:
            return self.__procesada_actual


    def nuevo_comando(self, comando):
        '''
        Aplica un nuevo comando a la imagen

        Parametros:
        - [string] comando: nombre del comando

        Realiza las operaciones:
        - adiciona el comando a la lista de comandos
        - crea la nueva miniatura de la imagen procesada
        '''

        # guardar el comando
        self.__comandos.append(comando)

        # actualizar la miniatura
        self.__miniatura_proc = self.__constriur_miniatura_procesada()


    def puede_deshacer(self):
        '''
        Retorna si se puede deshacer un comando
        '''

        return len(self.__comandos) > 0


    def puede_rehacer(self):
        '''
        Retorna si se puede rehacer un comando
        '''

        return len(self.__comandos_deshechos) > 0


    def deshacer(self):
        '''
        Deshace un comando

        Retorna True si se pudo deshacer y False en caso contrario

        Realiza las operaciones:
        - mueve el ultimo comando a la lista de comandos_deshechos
        - actualiza la miniatura
        '''

        resultado = True

        if self.puede_deshacer():
            # mover el comando hacia comandos_deshechos
            self.__comandos_deshechos.append(self.__comandos.pop())
            # reconstruir la miniatura
            self.__constriur_miniatura_procesada()
        else:
            resultado = False

        return resultado


    def rehacer(self):
        '''
        Rehace un comando

        Retorna True si se pudo rehacer y False en caso contrario

        Realiza las operaciones:
        - mueve el ultimo comando desecho a la lista de comandos
        - actualiza la miniatura
        '''

        resultado = True

        if self.puede_rehacer():
            # mover el comando hacia comandos
            self.__comandos.append(self.__comandos_deshechos.pop())
            # reconstruir la miniatura
            self.__constriur_miniatura_procesada()
        else:
            resultado = False

        return resultado


    def get_siguiente_transformacion(self):
        '''
        Retorna el nombre de la imagen que representa la siguiente
        transformacion
        '''

        return self.__swap + '/' + self.__nombre + '_' + str(len(self.__comandos) + 1) + '.jpg'


    def get_comandos(self):
        '''
        Retorna los comandos que se han aplicado a la imagen con la ruta
        de las imagenes que se corresponden con cada comando
        '''

        salida = []
        i = 0
        while i < len(self.__comandos):
            salida.append((self.__comandos[i], self.__swap + '/' + self.__nombre + '_' + str(i + 1) + '.jpg'))
            i = i + 1

        return salida


    def get_imagen_comando_nro(self, cmd_nro):
        '''
        Retorna el estado del comando cmd_nro
        '''

        return self.__swap + '/' + self.__nombre + '_' + str(cmd_nro + 1) + '.jpg'


    def eliminar_comandos_despues_de(self, cmd_nro):
        '''
        Elimina los comandos a partir del cmd_nro
        '''

        self.__comandos = self.__comandos[:cmd_nro]
        self.__miniatura_proc = self.__constriur_miniatura_procesada()


    def eliminar_img(self):
        '''
        Elimina las transformaciones que se le han aplicado a una imagen
        '''
        if self.__seleccionada==True:
                salida = self.get_comandos()
                if len(salida) > 0:
                        for i in salida:
                               os.remove(i[1])
                               #os.remove(self.get_miniatura_procesada())
        else:
                os.remove(self.get_original())
                os.remove(self.get_miniatura_original())
