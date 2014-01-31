#!/usr/bin/python
# -*- coding: utf-8 -*-

import Image
import os

ancho_maximo = 1200
miniatura_size = (100, 120)

class DocLux_Imagen:
    '''
    Define el concepto de Imagen en DocLux.

    Contiene elementos como:
    - url de la imagen en el disco
    - lista de comandos aplicados a la imagen
    -

    Almacena los ficheros temporales en el directorio swapDir
    '''

    def __init__(self, swapDir, imgURL):
        '''
        Constructor de la clase

        Parametros:
        - [string] swapDir:      directorio para guardar los temporales
        - [string] imgURL:       ruta del archivo en el disco
        '''

        # donde guardar los temporales (ruta sin el / al final)
        self.__swap = swapDir

        # datos de la imagen original
        # nombre (sin extension)
        self.__nombre = str(os.path.splitext(os.path.basename(imgURL))[0])
        # copiar la imagen al area de intercambio
        salida = self.__swap + '/' + self.__nombre + '.jpg'
        tmp = Image.open(imgURL.decode('L1'))
        # ajuste del ancho
        if tmp.size[0] > ancho_maximo:
            tmp = tmp.resize((ancho_maximo, int(ancho_maximo * tmp.size[1] / tmp.size[0])))
        tmp.save(salida.decode('L1'))
        self.__ruta = salida.decode('L1')

        self.__comandos = []
        self.__comandos_deshechos = []

        # construir la miniatura y guardarla
        self.__miniatura = self.__constriur_miniatura()


    def get_original(self):
        '''
        Retorna la ruta de la imagen actual
        '''

        if len(self.__comandos) > 0:
            return self.__swap + '/' + self.__nombre + '_' + str(len(self.__comandos)) + '.jpg'
        else:
            return self.__ruta


    def get_nombre(self):
        '''
        Retorna el nombre de la imagen
        '''

        return self.__nombre


    def get_miniatura(self):
        '''
        Retorna la miniatura de la imagen
        '''

        return self.__miniatura


    def __constriur_miniatura(self):
        '''
        Constriur la miniatura y guardarla en swapDir

        Ruta:
        - swapDir/miniatura_NOMBRE.jpg
        '''

        salida = self.__swap + '/' + 'miniatura_' + self.__nombre + '.jpg'
        im = Image.open(self.get_original())
        im.thumbnail(miniatura_size)
        im.save(salida.decode('L1'))

        return salida.decode('L1')


    def nuevo_comando(self, comando):
        '''
        Aplica un nuevo comando a la imagen

        Parametros:
        - [string] comando: nombre del comando

        Realiza las operaciones:
        - adiciona el comando a la lista de comandos
        - crea la nueva miniatura de la imagen
        '''

        # guardar el comando
        self.__comandos.append(comando)

        # actualizar la miniatura
        self.__miniatura = self.__constriur_miniatura()

        # eliminar la lista de comandos desechos
        self.__comandos_deshechos = []


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
            # actualizar la miniatura
            self.__miniatura = self.__constriur_miniatura()
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
            # actualizar la miniatura
            self.__miniatura = self.__constriur_miniatura()
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
        de las imagenes que se corresponden con cada comando y a cada miniatura
        '''

        salida = []
        i = 0
        while i < len(self.__comandos):
            cmd_url = self.__swap + '/' + self.__nombre + '_' + str(i + 1) + '.jpg'
            im = Image.open(cmd_url)
            im.thumbnail(miniatura_size)
            cmd_miniatura = self.__swap + '/' + self.__nombre + '_miniatura_' + str(i + 1) + '.jpg'
            im.save(cmd_miniatura)
            salida.append((self.__comandos[i], cmd_url, cmd_miniatura))
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
        self.__comandos_deshechos = []
        # actualizar la miniatura
        self.__miniatura = self.__constriur_miniatura()


    def eliminar_img(self):
        '''
        Elimina TODAS la copias de la imagen actual dentro de la swap
        '''

        # elimina todos los comandos y sus miniaturas
        for i in self.get_comandos():
            os.remove(i[1])
            os.remove(i[2])

        # limpiar la lista de comandos
        self.__comandos = []

        # elimina la imagen y su miniatura
        os.remove(self.get_original())
        os.remove(self.get_miniatura())
