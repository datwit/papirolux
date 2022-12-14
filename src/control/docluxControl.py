#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from src.imagen.docluxImagen import DocLux_Imagen

class DocLux_Control:
    '''
    Define el Controlador de trabajo en DocLux.

    Contiene elementos como:
    - lista de imagenes de doclux
    - gestion del espacio de trabajo
    -

    Apoya a la IU como proveedor de datos
    '''

    def __init__(self, swapDir):
        '''
        Constructor de la clase

        Parametros:
        - [string] swapDir: directorio para guardar los temporales
        '''

        # donde guardar los temporales (ruta sin el / al final)
        self.__swap = swapDir

        # preparar el espacio de trabajo
        self.__limpiar_swap();

        # datos de la lista de imagenes
        # lista de imagenes cargadas
        self.__imgs_cargadas = []
        # lista de imagenes seleccionadas
        self.__imgs_seleccionadas = []
        # indice de la imagen original actual
        self.__original_actual = -1


    def __del__(self):
        '''
        Destructor de la clase
        '''

        self.__limpiar_swap()


    def __limpiar_swap(self):
        '''
        Limpia el contenido del area de intercambio para comenzar
        una nueva sesion de trabajo
        '''

        # eliminar todo el contenido del area de trabajo
        for i in os.listdir(self.__swap):
            os.remove(self.__swap + '/' + i)


    def nuevas_imagenes(self, urlImagenes, adicionar=False):
        '''
        Inicia el espacio de trabajo al cargar nuevas imagenes

        Parametros:
        - [list] urlImagenes: lista de urls de las imagenes
        - [bool] adicionar: define si son nuevas imagenes o si son para adicionar

        Realiza las acciones:
        - elimina todo lo que esta en la swap actual si no son para adicionar
        - limpia la lista de imagenes actuales y seleccionadas si no son para adicionar
        - carga/adiciona las nuevas imagenes
        '''

        # si se trata de Nuevas Imagenes
        if adicionar == False:
            # limpiar la swap actual
            self.__limpiar_swap()

            # limpia las listas actuales
            self.__imgs_cargadas = []
            self.__imgs_seleccionadas = []

            # actualizar el cursor
            self.__original_actual = 0

        for i in urlImagenes:
            # creamos una imagen y la guardamos en la lista de cargadas
            self.adicionar_imagen(i)


    def adicionar_imagen(self, urlImagen, seleccionada=False):
        '''
        Adiciona una nueva imagen a la lista de imagenes cargadas

        Parametros:
        - [string] urlImagen:    url de las imagen
        - [string] urlImagen:    url de las imagen
        - [bool]   seleccionada: define si se adiciona a la lista de procesadas

        Realiza las acciones:
        - crea una nueva imagen
        - adiciona la imagen a la lista
        '''

        if seleccionada == False:
            for i in self.__imgs_cargadas:
                if str(os.path.splitext(os.path.basename(urlImagen))[0]) == i.get_nombre():
                    return

            # si no esta adicionada, crear una nueva imagen y guardarla en la lista
            tmp = DocLux_Imagen(self.__swap, urlImagen)
            self.__imgs_cargadas.append(tmp)
        else:
            tmp = DocLux_Imagen(self.__swap, urlImagen, True)
            self.__imgs_seleccionadas.append(tmp)


    def get_miniaturas_originales(self):
        '''
        Retorna las miniaturas de todas las imagenes
        '''

        salida = []

        for i in self.__imgs_cargadas:
            salida.append(i.get_miniatura_original())

        return salida


    def get_imagen_original_nro(self, i):
        '''
        Retorna la imagen original actual y su nombre

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return (self.__imgs_cargadas[i].get_original(),
                 self.__imgs_cargadas[i].get_nombre())


    def get_cant_imagenes_cargadas(self):
        '''
        Retorna la cantidad de imagenes cargadas
        '''

        return len(self.__imgs_cargadas)


    def get_cant_imagenes_seleccionadas(self):
        '''
        Retorna la cantidad de imagenes seleccionadas
        '''

        return len(self.__imgs_seleccionadas)



    def eliminar_imagenes(self):
        '''
        Elimina todas las imagenes actuales
        '''

        self.__imgs_cargadas = []
        self.__imgs_seleccionadas = []


    def __buscar_imagen_seleccionada(self, imgUrl):
        '''
        Retorna si esta o no la imagen imgUrl dentro de la
        lista de imagenes seleccionadas

        Parametros:
        - [string] imgUrl: ruta de la imagen
        '''

        for i in self.__imgs_seleccionadas:
            if imgUrl == i.get_original():
                return True

        return False


    def seleccionar_imagen_nro(self, i):
        '''
        Selecciona una imagen

        Parametros:
        - [int] i: indice de la imagen que se quiere seleccionar
        '''

        if i < 0 or i >= self.get_cant_imagenes_cargadas():
            return False

        img = self.__imgs_cargadas[i].get_original()
        # si la imagen ya esta seleccionada entonces salir
        if self.__buscar_imagen_seleccionada(img) == True:
            return

        # adicionamos la imagen a la lista de las seleccionadas
        self.adicionar_imagen(img, True)


    def seleccionar_todas_las_imagenes(self):
        '''
        Selecciona todas las imagenes
        '''

        for i in range(self.get_cant_imagenes_cargadas()):
            img = self.__imgs_cargadas[i].get_original()
            # adicionar la imagen si no existe
            if self.__buscar_imagen_seleccionada(img) == False:
                self.adicionar_imagen(img, True)


    def get_imagen_procesada_nro(self, i, sincronizar=False):
        '''
        Retorna la imagen procesada actual y su nombre

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        if not sincronizar:
            return (self.__imgs_seleccionadas[i].get_procesada(),
                    self.__imgs_seleccionadas[i].get_nombre())

        return (self.__imgs_seleccionadas[i].get_original(),
                    self.__imgs_seleccionadas[i].get_nombre())


    def get_miniaturas_procesadas(self):
        '''
        Retorna las miniaturas de todas las imagenes
        '''

        salida = []

        for i in self.__imgs_seleccionadas:
            salida.append(i.get_miniatura_procesada())

        return salida


    def sincronizar(self, nroProcesada):
        '''
        Sincroniza los visores para identificar la imagen
        original correspondiente a la procesada actual
        '''

        urlTmp = self.get_imagen_procesada_nro(nroProcesada, True)[0]

        i = 0
        encontrado = False
        while (not encontrado) and (i < len(self.__imgs_cargadas)):
            if urlTmp == self.__imgs_cargadas[i].get_original():
                encontrado = True
            i = i + 1

        if encontrado == True:
            return i - 1
        else:
            return -1


    def get_siguiente_transformacion_imagen_nro(self, i):
        '''
        Retorna el nombre de la imagen que representa a la siguiente
        transformacion de la imagen con numero i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_seleccionadas[i].get_siguiente_transformacion()


    def nuevo_comando(self, nombre_comando, i):
        '''
        Aplica un nuevo comando a la imagen procesada con numero i
        '''

        self.__imgs_seleccionadas[i].nuevo_comando(nombre_comando)


    def get_comandos_imagen_nro(self, i):
        '''
        Retorna la lista de comandos de la imagen numero i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_seleccionadas[i].get_comandos()


    def get_swap_dir(self):
        '''
        Retorna la direccion del directorio swap
        '''

        return self.__swap


    def get_imagen_comando_nro(self, imagen, cmd_nro):
        '''
        Retorna la el estado de la imagen correspondiente al comando cmd_nro

        Parametros:
        - [int] imagen: indice de la imagen que se quiere consultar
        - [int] cmd_nro: indice del comando de la imagen que se quiere consultar
        '''

        return self.__imgs_seleccionadas[imagen].get_imagen_comando_nro(cmd_nro)


    def deshacer_comando(self, i):
        '''
        Deshace un comando a la imagen i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_seleccionadas[i].deshacer()


    def rehacer_comando(self, i):
        '''
        Rehace un comando a la imagen i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_seleccionadas[i].rehacer()


    def puede_deshacer(self, i):
        '''
        Retorna si se puede deshacer algun comando para la imagen i
        '''

        return self.__imgs_seleccionadas[i].puede_deshacer()


    def puede_rehacer(self, i):
        '''
        Retorna si se puede rehacer algun comando para la imagen i
        '''

        return self.__imgs_seleccionadas[i].puede_rehacer()


    def eliminar_comandos_despues_de(self, i, j):
        '''
        Elimina los comandos de la imagen i a partir del comando j
        '''

        self.__imgs_seleccionadas[i].eliminar_comandos_despues_de(j)


    def eliminar(self, indice_im):
        #verificar si esa imagen está en las procesadas
        img = self.__imgs_cargadas[indice_im].get_original()
        
        lista_img_sel = []
        for i in xrange(len(self.__imgs_seleccionadas)):
            lista_img_sel.append(self.__imgs_seleccionadas[i].get_original())
        
        if img in lista_img_sel:            
            self.__imgs_seleccionadas[lista_img_sel.index(img)].eliminar_img()
            del self.__imgs_seleccionadas[lista_img_sel.index(img)]
                
        #eliminar la imagen de las imágenes cargadas
        self.__imgs_cargadas[indice_im].eliminar_img()
        del self.__imgs_cargadas[indice_im]

    
    def ordenar_imgs(self, lista_img):
        import Queue
        lista_ordenada=[]
        prioridad = Queue.PriorityQueue()
        for i in lista_img:
            try:
                prioridad.put((int(i[1]), i[0]))
            except:
                prioridad.put((i[1], i[0]))
                
        while not prioridad.empty():
            sgt = prioridad.get()
            lista_ordenada.append((sgt[1],str(sgt[0])))
        return lista_ordenada
   
    def verificar_seleccionada(self, indice):
        '''
        Retorna True si la imagen ACTUAL de las cargadas está seleccionada.
        - Se crea este método porque al método self.__buscar_imagen_seleccionada(img)
          se le pasa una imagen y en este caso se quiere comprobar la imagen actual
            
        '''
        img=self.__imgs_cargadas[indice].get_original()
        return self.__buscar_imagen_seleccionada(img)
        
    def deseleccionar(self,indice):
        '''
        Deselecciona una imagen
        Parametros:
        - [int] indice: indice de la imagen que se quiere consultar
        '''
        img=self.__imgs_cargadas[indice].get_original()
        lista_img_sel = []
        for i in xrange(len(self.__imgs_seleccionadas)):
            lista_img_sel.append(self.__imgs_seleccionadas[i].get_original())
        if img in lista_img_sel:
            # elimina la imagen de las seleccionadas con sus transformaciones(si tiene)
            self.__imgs_seleccionadas[lista_img_sel.index(img)].eliminar_img()
            # elimina la imagen de las seleccionadas 
            del self.__imgs_seleccionadas[lista_img_sel.index(img)]
    
    def deseleccionar_todas(self):
        for i in xrange(len(self.__imgs_seleccionadas)):
            self.__imgs_seleccionadas[i].eliminar_img()
        self.__imgs_seleccionadas = []
