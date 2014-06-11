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
        self.limpiar_swap();

        # datos de la lista de imagenes
        # lista de imagenes cargadas
        self.__imgs_cargadas = []
        # indice de la imagen original actual
        self.__original_actual = -1


    def __del__(self):
        '''
        Destructor de la clase
        '''

        self.limpiar_swap()


    def limpiar_swap(self):
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
            self.limpiar_swap()

            # limpia las listas actuales
            self.__imgs_cargadas = []

            # actualizar el cursor
            self.__original_actual = 0

        for i in urlImagenes:
            # creamos una imagen y la guardamos en la lista de cargadas
            self.adicionar_imagen(i)


    def adicionar_imagen(self, urlImagen):
        '''
        Adiciona una nueva imagen a la lista de imagenes cargadas

        Parametros:
        - [string] urlImagen: url de la imagen

        Realiza las acciones:
        - crea una nueva imagen
        - adiciona la imagen a la lista
        '''

        for i in self.__imgs_cargadas:
            if str(os.path.splitext(os.path.basename(urlImagen))[0]) == i.get_nombre():
                return

        # crear una nueva imagen y guardarla en la lista
        tmp = DocLux_Imagen(self.__swap, urlImagen)
        self.__imgs_cargadas.append(tmp)


    def get_miniaturas(self):
        '''
        Retorna las miniaturas de todas las imagenes
        '''

        salida = []

        for i in self.__imgs_cargadas:
            salida.append(i.get_miniatura())

        return salida


    def get_imagen_nro(self, i):
        '''
        Retorna la imagen nro i y su nombre

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


    def eliminar_imagenes(self):
        '''
        Elimina todas las imagenes
        '''

        # limpiar la swap
        self.limpiar_swap()
        # inicializar la lista de imagenes
        self.__imgs_cargadas = []


    def get_siguiente_transformacion_imagen_nro(self, i):
        '''
        Retorna el nombre de la imagen que representa a la siguiente
        transformacion de la imagen con numero i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_cargadas[i].get_siguiente_transformacion()


    def nuevo_comando(self, nombre_comando, i):
        '''
        Aplica un nuevo comando a la imagen procesada con numero i
        '''

        self.__imgs_cargadas[i].nuevo_comando(nombre_comando)


    def get_comandos_imagen_nro(self, i):
        '''
        Retorna la lista de comandos de la imagen numero i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_cargadas[i].get_comandos()


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

        return self.__imgs_cargadas[imagen].get_imagen_comando_nro(cmd_nro)


    def deshacer_comando(self, i):
        '''
        Deshace un comando a la imagen i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_cargadas[i].deshacer()


    def rehacer_comando(self, i):
        '''
        Rehace un comando a la imagen i

        Parametros:
        - [int] i: indice de la imagen que se quiere consultar
        '''

        return self.__imgs_cargadas[i].rehacer()


    def puede_deshacer(self, i):
        '''
        Retorna si se puede deshacer algun comando para la imagen i
        '''

        return self.__imgs_cargadas[i].puede_deshacer()


    def resetear_proyecto(self):
        '''
        Retorna si se puede rehacer algun comando para la imagen i
        '''

        for i in self.__imgs_cargadas:
			i.eliminar_img(True)
    
    
    def puede_rehacer(self, i):
        '''
        Retorna si se puede rehacer algun comando para la imagen i
        '''

        return self.__imgs_cargadas[i].puede_rehacer()
    
    
    
    
    def actualizar_swap(self, nueva_swap):
        '''
        Mueve la swap actual para un nuevo directorio 
        '''
        import shutil
        import os.path
		#copia el directorio actual para el nuevo directorio
        swap_actual = self.get_swap_dir()
        shutil.copytree(str(swap_actual),str(nueva_swap))
        self.limpiar_swap()
        #actualizar la swap
        self.__swap= nueva_swap
        # se le cambia la dirección de cada imagen
        for i in self.__imgs_cargadas:
			i.actualizar_swap_img(str(nueva_swap))


    def eliminar_comandos_despues_de(self, i, j):
        '''
        Elimina los comandos de la imagen i a partir del comando j
        '''

        self.__imgs_cargadas[i].eliminar_comandos_despues_de(j)


    def eliminar(self, indice_im):
        '''
        Elimina una imagen de la lista de imagenes cargadas

        Parametros:
        - [int] indice_im: indice de la imagen que se quiere eliminar
        '''

        self.__imgs_cargadas[indice_im].eliminar_img()
        del self.__imgs_cargadas[indice_im]


    def ordenar_imgs(self, lista_img):
        '''
        Ordena las imágenes de manera ascendente por el criterio "nombre"
        '''
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



    def informacion_swap(self):
        '''
        Calcula la informacion relacionada con la swap
        '''

        # obtener la informacion
        st = os.statvfs(self.__swap)

        # espacio libre en Gb (dividir 3 veces x 1000)
        free = st.f_bavail * st.f_frsize
        free_ok = round(float(free / 1000) / 1000 / 1000, 1)

        for root, dirs, files in os.walk(self.__swap):
            cant = len(files)
            usado = sum(os.path.getsize(os.path.join(root, name)) for name in files)

        # UM del contenido de la swap (Kb o Mb)
        um = 'Kb'
        # en Kb (dividir 2 veces x 1000)
        total_swap = round(float(usado / 1000), 1)

        # llevar a Mb si es necesario
        if total_swap > 1023:
            um = 'Mb'
            total_swap = round(float(total_swap / 1000), 1)

        return (str(cant), (str(total_swap), um), str(free_ok))
    
    
    def informacion_directorios(self, directorio):
        '''
        Calcula la informacion relacionada con la swap
        '''

        # obtener la informacion
        st = os.statvfs(str(directorio))

        # espacio libre en Gb (dividir 3 veces x 1000)
        free = st.f_bavail * st.f_frsize
        free_ok = round(float(free / 1000) / 1000 / 1000, 1)

        for root, dirs, files in os.walk(str(directorio)):
            cant = len(files)
            usado = sum(os.path.getsize(os.path.join(root, name)) for name in files)

        # UM del contenido de la swap (Kb o Mb)
        um = 'Kb'
        # en Kb (dividir 2 veces x 1000)
        total_swap = round(float(usado / 1000), 1)

        # llevar a Mb si es necesario
        if total_swap > 1023:
            um = 'Mb'
            total_swap = round(float(total_swap / 1000), 1)

        return (str(cant), (str(total_swap), um), str(free_ok))
   
   
    


        
    
    
    
