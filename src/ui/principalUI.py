#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os
import pickle

from ui.principal import Ui_MainWindow
from acercaUI import AcercaDe
from swapUI import Swap
from ayudaUI import Ayuda
from cargandoUI import Cargando

from pluginAction import MyQAction
from principalHelper import *

from src.control.docluxControl import DocLux_Control
from miniatura import Miniatura
from plugin_notificador import Notificador

import plugins.plugin_loader as plugin_loader

# declaraciones GLOBALES
# notificador
notificador = Notificador()
# helpers para la clase principal
helper_nuevas_imagenes = NuevasImagenes()
helper_adicionar_imagenes = AdicionarImagenes()
helper_eliminar_imagenes = EliminarImagenes()
helper_guardar_exportar_imagenes = GuardarExportarImagenes()

# ventana principal de la aplicacion
class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, swap, parent = None):
        # inicializar el padre
        super(VentanaPrincipal, self).__init__(parent)
        # configurar la interfaz
        self.setupUi(self)
        # toolbars
        escritorio = QDesktopWidget()
        ancho = escritorio.availableGeometry().width();
        self.toolBarPrincipal.setMinimumWidth(ancho - 100)
        self.toolBarPrincipal.setMaximumWidth(ancho - 100)
        del(escritorio)
        del(ancho)

        # miembros de la clase
        # controlador principal
        self.__controladora = DocLux_Control(swap)

        # lista de plugins activos en la aplicacion
        self.__pluginsActions = []

        # preparando las cosas necesarias
        self.showFullScreen()
        #~ self.areaProcesada.setFixedWidth(self.width() - self.width() / 5)

        # configurar signals/slots
        # nuevas imagenes
        self.actionNuevas.triggered.connect(self.nuevas_imagenes)
        # adicionar imagenes
        self.actionAdicionar.triggered.connect(self.adicionar_imagenes)
        # salir
        self.actionSalir.triggered.connect(self.close)
        # minimizar
        self.actionMinimizar.triggered.connect(self.showMinimized)
        # acerca de
        self.actionAcerca.triggered.connect(self.acerca_de)
        # ayuda de DocLux
        self.actionAyuda.triggered.connect(self.ayuda)
        # deshacer/rehacer
        self.actionDeshacer.triggered.connect(self.deshacer)
        self.actionRehacer.triggered.connect(self.rehacer)
        # guardar/guardar todas
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardarTodas.triggered.connect(self.guardar_todas)
        # exportar/exportar todas
        self.actionExportar.triggered.connect(self.exportar)
        self.actionExportarTodas.triggered.connect(self.exportar_todas)
        # eliminar imagen
        self.actionEliminar.triggered.connect(self.eliminar)
        # actualizar al comando
        self.aplicarCmd.clicked.connect(self.__actualizar_al_comando)
        # conectar el cargador
        notificador.inicio_operacion.connect(self.__mostrar_cargando)
        notificador.fin_operacion.connect(self.__ocultar_cargando)
        # abrir un proyecto docLux
        self.actionAbrirProyecto.triggered.connect(self.__abrir_proyecto)
        # guarar un proyecto creado en docLux
        self.actionGuardarProyecto.triggered.connect(self.__guardar_proyecto)
        #gestionar swap
        self.actionGestionar_rea_de_intercambio.triggered.connect(self.gestionar_swap)
        #limpiar area intercambio
        self.actionLimpiarAreaDeIntercambio.triggered.connect(self.__limpiar)
        self.actionEliminarTodas.triggered.connect(self.__eliminar_todas)

        # cargador
        self.__cargando = None

        # cargar los plugins
        self.__cargar_plugins()

        # inicializar todo el resto de la app
        self.__inicializar()
        # mostrar cantidad de imágenes cargadas(margen derecho)
        self.label_2.setText(u"Imágenes Cargadas:"+str(self.__controladora.get_cant_imagenes_cargadas()))


    def __cargar_plugins(self):
        '''
        Carga los plugins y los activa en la IU
        '''

        plugins = plugin_loader.cargar_plugins('plugins')
        for p in plugins:
            if hasattr(p, 'nombre') and hasattr(p, 'icon') and hasattr(p, 'run'):
                # crear el plugin
                obj = p()
                # crear el action correspondiente adicionandole el plugin
                self.action = MyQAction(obj, self)
                # enlazar el action con la funcion que ejecuta al plugin
                self.action.triggered.connect(self.__emitir)
                # adicionar el plugin a la lista
                self.__pluginsActions.append(self.action)

        # enlazar el notificador
        notificador.correcto.connect(self.__plugin_ejecutado)
        notificador.error.connect(self.__plugin_error)

        # adicionar cada plugin al menu y la barra de herramientas
        for i in self.__pluginsActions:
            self.menuPlugins.addAction(i)
            self.toolBarPrincipal.addAction(i)


    def __emitir(self):
        '''
        Funcion auxiliar que sirve para poder llamar al plugin
        correspondiente dependiendo del QAction que se active
        con los parametros correctos
        '''

        # termina con el retorno de cada plugin (ejecutado o error)

        imgsIn = []
        imgsOut = []

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_cargadas()):
                imgsIn.append(self.__controladora.get_imagen_nro(i)[0])
                imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(i))
        else:
            imgsIn.append(self.__controladora.get_imagen_nro(self.__actualNro)[0])
            imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(self.__actualNro))

        self.sender().execFunc(imgsIn, imgsOut, notificador)


    def __plugin_ejecutado(self, plugin_name):
        '''
        Actualiza la lista de comandos con el resultado de la transformacion
        '''

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_cargadas()):
                self.__controladora.nuevo_comando(plugin_name, i)
        else:
            self.__controladora.nuevo_comando(plugin_name, self.__actualNro)

        # actualizar las miniaturas
        self.__actualizar_miniaturas()
        # actualizar el visor
        self.__mostrar_imagen(self.__actualNro)

        # actualizar las imagenes que debe usar el plugin
        imgsIn = []
        imgsOut = []

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_cargadas()):
                imgsIn.append(self.__controladora.get_imagen_nro(i)[0])
                imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(i))
        else:
            imgsIn.append(self.__controladora.get_imagen_nro(self.__actualNro)[0])
            imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(self.__actualNro))

        if self.sender().parent != None:
            self.sender().parent.update_images(imgsIn, imgsOut)


    def __plugin_error(self, msg):
        print 'Error en plugin, mensaje: ' + msg


    def closeEvent(self, event):
        '''
        Evento que se ejecuta al solicitar que se Cierre la aplicacion, pidiendo
        confirmacion antes de ejecutar la accion
        '''

        resp = QMessageBox.question(self, u'Pregunta', u'¿Realmente desea <b>salir</b>?', QMessageBox.Yes | QMessageBox.No)
        # si respuesta positiva
        if resp == QMessageBox.Yes:
            self.__controladora.limpiar_swap()
            event.accept()
        # salir del metodo sin hacer nada
        else:
            event.ignore()


    def nuevas_imagenes(self):
        '''
        Carga nuevas imagenes en el proyecto

        Realiza las acciones:
        - limpia los visores
        - carga nuevas imagenes
        - muestra la 1ra de ellas
        '''

        # si hay imagenes cargadas preguntamos antes de eliminarlas
        if self.__controladora.get_cant_imagenes_cargadas() > 0:
            resp = QMessageBox.question(self, u'Pregunta', u'¿Desea <b>eliminar</b> las imágenes actuales y cargar otras?',
                                         QMessageBox.Yes | QMessageBox.No)

            if resp == QMessageBox.Yes:
                # si respuesta positiva
                # resetear todo al estado inicial
                self.__inicializar()
            else:
                # salir del metodo sin hacer nada
                return

        # seleccionar las imagenes
        imagenes = QFileDialog.getOpenFileNames(self, u"Cargar Imágenes", QDir.homePath(), u"Imágenes (*.png *.jpg *.gif)")

        if len(imagenes) == 0:
            self.__controladora.eliminar_imagenes()
            return

        # convertir de QStringList a python list sin repetidos
        lista = []
        for i in imagenes:
            if not str(i.toAscii()) in lista:
                lista.append(str(i.toAscii()))

        # ejecutar el HILO paralelo
        helper_nuevas_imagenes.setData(lista, self.__controladora)
        helper_nuevas_imagenes.terminado.connect(self.__slot_nuevas_imagenes)
        helper_nuevas_imagenes.start()

        # cargador
        notificador.inicio_operacion.emit()


    def __slot_nuevas_imagenes(self, msg):
        '''
        Slot auxiliar para conocer cuando se termino el hilo que carga
        nuevas imagenes
        '''

        # cargador
        notificador.fin_operacion.emit()

        if len(msg) == 0:
            # teminado sin errores
            self.__actualNro = 0
            self.mostrar_imagen(self.__controladora.get_imagen_nro(self.__actualNro))
            self.__habilitar_controles_visor()
            self.__actualizar_miniaturas()
            # actualizar cantidad de imágenes(margen derecho)
            self.label_2.setText(u"Imágenes Cargadas:"+str(self.__controladora.get_cant_imagenes_cargadas()))
        else:
            # mostrar cartel con error
            pass


    def adicionar_imagenes(self):
        '''
        Adiciona nuevas imagenes a las actuales del proyecto

        Realiza las acciones:
        - adiciona nuevas imagenes a la lista de imagenes cargadas
        '''

        # seleccionar las imagenes
        imagenes = QFileDialog.getOpenFileNames(self, u"Adicionar Imágenes", QDir.homePath(), u"Imágenes (*.png *.jpg *.gif)")

        if len(imagenes) == 0:
            return

        # convertir de QStringList a python list sin repetidos
        lista = []
        for i in imagenes:
            if not str(i.toAscii()) in lista:
                lista.append(str(i.toAscii()))

        # ejecutar el HILO paralelo
        helper_adicionar_imagenes.setData(lista, self.__controladora)
        helper_adicionar_imagenes.terminado.connect(self.__slot_adicionar_imagenes)
        helper_adicionar_imagenes.start()

        # cargador
        notificador.inicio_operacion.emit()


    def __slot_adicionar_imagenes(self, msg):
        '''
        Slot auxiliar para conocer cuando se termino el hilo que adiciona imagenes
        '''

        # cargador
        notificador.fin_operacion.emit()

        if len(msg) == 0:
            # teminado sin errores
            self.__actualizar_miniaturas()
            self.__habilitar_controles_visor()
            self.__actualizar_info_swap_status_bar()
            # actualizar cantidad de imágenes(margen derecho)
            self.label_2.setText(u"Imágenes Cargadas:"+str(self.__controladora.get_cant_imagenes_cargadas()))
        else:
            # mostrar cartel con error
            pass


    def mostrar_imagen(self, info):
        '''
        Muestra una imagen en el visor

        Parametros:
        - [tuple] info: (urlmagen, nombre)
        '''

        self.img_Original.setPixmap(QPixmap(info[0]))
        self.nombreOriginal.setText(info[1])

        lab = QString('<b>%1</b> de <b>%2</b>').arg(self.__actualNro + 1).arg(self.__controladora.get_cant_imagenes_cargadas())
        self.indicadorOriginal.setText(lab)

        # actualizar la barra de estado
        self.__actualizar_info_swap_status_bar()


    def __actualizar_miniaturas(self):
        '''
        Actualiza las miniaturas de las imagenes cargadas
        '''

        # obtener la lista de las miniaturas
        miniaturas = self.__controladora.get_miniaturas()

        # limpiar las miniaturas
        self.__limpiar_miniaturas()

        # mostrar las nuevas miniaturas
        i = 0
        while i < len(miniaturas):
            lab = Miniatura(i, self)
            lab.setMinimumSize(110, 130)
            lab.setMaximumSize(110, 130)
            lab.signals.ver_miniatura.connect(self.__mostrar_imagen)
            lab.setPixmap(QPixmap(miniaturas[i]))
            if i == self.__actualNro:
                lab.setLineWidth(2)
                lab.setFrameStyle(QFrame.Box)
            # adicionar al layout
            self.miniaturas_cargadas.addWidget(lab)

            i = i + 1

        lab = QString('<b>%1</b> de <b>%2</b>').arg(self.__actualNro + 1).arg(self.__controladora.get_cant_imagenes_cargadas())
        self.indicadorOriginal.setText(lab)


    def __limpiar_miniaturas(self):
        '''
        Limpia las miniaturas
        '''

        # eliminar las miniaturas actuales del layout
        while self.miniaturas_cargadas.count() > 0:
            item = self.miniaturas_cargadas.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


    def __mostrar_imagen(self, indice):
        '''
        Identifica que imagen se debe mostrar en dependencia de la miniatura
        '''

        self.__actualNro = indice
        self.mostrar_imagen(self.__controladora.get_imagen_nro(indice))

        # limpiar las miniaturas
        self.__limpiar_miniaturas_comandos()

        # mostrar las miniaturas de los comandos
        i = 0
        cmds = self.__controladora.get_comandos_imagen_nro(indice)
        while i < len(cmds):
            # mostrar el thumbnail
            lab = Miniatura(i, self)
            lab.setMinimumSize(110, 130)
            lab.setMaximumSize(110, 130)
            lab.setPixmap(QPixmap(cmds[i][2]))
            # mostrar en nombre del comando
            text = QLabel(cmds[i][0], self)
            text.setWordWrap(True)
            # preparar el layout
            layout = QVBoxLayout(self)
            layout.addWidget(lab)
            layout.addWidget(text)
            # adicionar el layout al widget y mostrarlo
            tmp = QWidget(self)
            tmp.setLayout(layout)
            self.miniaturas_comandos.addWidget(tmp)
            # enlazar la signal
            lab.signals.ver_miniatura.connect(self.__ver_imagen_comando_nro)

            i = i + 1

        # resaltar el ultimo comando
        if self.miniaturas_comandos.count() > 0:
            # resaltar el comando actual (ultimo)
            item = self.miniaturas_comandos.itemAt(self.miniaturas_comandos.count() - 1)
            widget = item.widget()
            widget.children()[1].setLineWidth(2)
            widget.children()[1].setFrameStyle(QFrame.Box)

            self.thumbComandos.verticalScrollBar().setMaximum(self.thumbComandos.verticalScrollBar().maximum() + 1000000)
            self.thumbComandos.verticalScrollBar().setValue(self.thumbComandos.verticalScrollBar().maximum())

        self.__actualizar_miniaturas()
        self.__habilitar_controles_visor()
        # actualizar la barra de estado
        self.__actualizar_info_swap_status_bar()


    def __ver_imagen_comando_nro(self, indice):
        '''
        Muestra la imagen actual en el estado del comando i
        '''

        # actualizar el indice del comando actual
        self.__cmd_actual = indice

        # obtener la imagen correspondiente al comando i
        img = self.__controladora.get_imagen_comando_nro(self.__actualNro, self.__cmd_actual)
        self.img_Original.setPixmap(QPixmap(img))

        # resaltar la miniatura del comando actual
        for i in range(self.miniaturas_comandos.count()):
            item = self.miniaturas_comandos.itemAt(i)
            widget = item.widget()
            widget.children()[1].setFrameStyle(QFrame.NoFrame)

            if i == indice:
                widget.children()[1].setLineWidth(2)
                widget.children()[1].setFrameStyle(QFrame.Box)


    def __inicializar(self):
        '''
        Resetea toda la aplicacion con el estado inicial
        '''

        lab = QString('<b>%1</b> de <b>%2</b>').arg('0').arg('0')
        self.indicadorOriginal.setText(lab)
        self.nombreOriginal.setText('')
        self.img_Original.clear()
        self.__limpiar_miniaturas()
        self.__controladora.eliminar_imagenes()
        self.__actualNro = -1
        self.__cmd_actual = -1

        # deshabilitar todos los controles que no se necesitan
        self.actionAdicionar.setEnabled(False)
        self.actionEliminar.setEnabled(False)
        self.actionDeshacer.setEnabled(False)
        self.actionRehacer.setEnabled(False)
        self.actionGuardar.setEnabled(False)
        self.actionGuardarTodas.setEnabled(False)
        self.actionExportar.setEnabled(False)
        self.actionExportarTodas.setEnabled(False)
        self.aplicar_todas.setEnabled(False)
        self.actionGuardarProyecto.setEnabled(False)
        self.actionEliminarTodas.setEnabled(False)
        
        # deshabilitar todos los plugins
        for action in self.menuPlugins.actions():
            action.setEnabled(False)

        # actualizar la barra de estado
        self.__actualizar_info_swap_status_bar()

    def __habilitar_controles_visor(self):
        '''
        Habilita los controles necesarios para que funcione el visor
        de imagenes originales
        '''

        self.actionAdicionar.setEnabled(True)
        self.actionEliminar.setEnabled(True)
        self.actionDeshacer.setEnabled(False)
        self.actionRehacer.setEnabled(False)
        self.actionGuardar.setEnabled(True)
        self.actionExportar.setEnabled(True)
        self.actionGuardarProyecto.setEnabled(True)
        if self.__controladora.get_cant_imagenes_cargadas() > 1:
            self.aplicar_todas.setEnabled(True)
            self.actionGuardarTodas.setEnabled(True)
            self.actionExportarTodas.setEnabled(True)
            self.actionEliminarTodas.setEnabled(True)
        else:
            self.aplicar_todas.setEnabled(False)
            self.aplicar_todas.setChecked(False)
            self.actionGuardarTodas.setEnabled(False)
            self.actionExportarTodas.setEnabled(False)
            self.actionEliminarTodas.setEnabled(False)

        # habilitar todos los plugins
        for action in self.menuPlugins.actions():
            action.setEnabled(True)

        if self.__controladora.puede_deshacer(self.__actualNro):
            self.actionDeshacer.setEnabled(True)
        if self.__controladora.puede_rehacer(self.__actualNro):
            self.actionRehacer.setEnabled(True)



    def acerca_de(self):
        '''
        Muestra la informacion de Acerca de
        '''

        acerca = AcercaDe(self)
        acerca.show()

    def ayuda(self):
        '''
        Muestra la informacion de Ayuda de
        '''

        ayuda = Ayuda(self)
        ayuda.show()


    def __actualizar_al_comando(self):
        '''
        Retorna la imagen actual al comando seleccionado ignorando los
        sucesores de cmd_actual
        '''

        self.__controladora.eliminar_comandos_despues_de( self.__actualNro, self.__cmd_actual + 1)
        # mostrar la imagen
        self.__mostrar_imagen(self.__actualNro)


    def deshacer(self):
        '''
        Deshacer un comando
        '''

        if self.__controladora.deshacer_comando(self.__actualNro):
            self.__mostrar_imagen(self.__actualNro)


    def rehacer(self):
        '''
        Rehacer un comando
        '''

        if self.__controladora.rehacer_comando(self.__actualNro):
            self.__mostrar_imagen(self.__actualNro)


    def guardar(self):
        '''
        Guardar una imagen
        '''

        img = [self.__controladora.get_imagen_nro(self.__actualNro)]
        self.__guardar_exportar(img)


    def guardar_todas(self):
        '''
        Guardar todas las imagenes
        '''

        imgs = []
        for i in range(self.__controladora.get_cant_imagenes_cargadas()):
            imgs.append(self.__controladora.get_imagen_nro(i))
        self.__guardar_exportar(imgs)


    def exportar(self):
        '''
        Exportar una imagen en formato PDF
        '''

        img = [self.__controladora.get_imagen_nro(self.__actualNro)]
        self.__guardar_exportar(img, True)


    def exportar_todas(self):
        '''
        Exportar todas las imagenes en formato PDF
        '''

        imgs = []
        for i in range(self.__controladora.get_cant_imagenes_cargadas()):
            imgs.append(self.__controladora.get_imagen_nro(i))
        imgs= self.__controladora.ordenar_imgs(imgs)
        self.__guardar_exportar(imgs, True)


    def __guardar_exportar(self, imgs, exportar=False):
        '''
        Utilidad que permite seleccionar el directorio para guardar las
        imagenes o para exportar en un fichero PDF

        Parametros:
        - [list] imgs:     lista de urls de las imagenes
        - [bool] exportar: define si se guardan o exportan las imagenes
        '''

        if len(imgs) == 0:
            return

        dirName = QFileDialog.getExistingDirectory(self, u"Seleccionar ubicación", QDir.homePath(), QFileDialog.ShowDirsOnly)

        # si se selecciono CANCELAR
        if dirName.isEmpty():
            QMessageBox.information(self, u"Información", u"Operación cancelada")
            return

        # si se quiere GUARDAR
        if not exportar:
            # ejecutar el HILO paralelo
            helper_guardar_exportar_imagenes.setData(imgs, dirName)
            helper_guardar_exportar_imagenes.terminado.connect(self.__slot_guardar_exportar_imagenes)
            helper_guardar_exportar_imagenes.start()
        else:
            # exportar
            # preguntar por el nombre del PDF
            nombre = QInputDialog.getText(self, u"Nombre del fichero", u"Nombre del fichero", text = "doclux")
            # si no se pudo ejecutar, se cancelo o no se escribio nada entonces salir
            if nombre[0].trimmed().isEmpty() == True:
                QMessageBox.critical(self, u"Error", u"Nombre incorrecto, por favor, seleccione otro nombre")
                return

            if not nombre[1]:
                QMessageBox.information(self, u"Información", u"Operación cancelada")
                return

            nombre = dirName + '/' + nombre[0].append( ".pdf" )
            if QFile.exists(nombre):
                msg = u"En ese directorio <b>ya existe</b> un fichero llamado <b>"+ os.path.basename(str(nombre)) +"</b>, por favor, seleccione otro nombre"
                QMessageBox.critical(self, u"Error", msg)
                return

            # ejecutar el HILO paralelo
            helper_guardar_exportar_imagenes.setData(imgs, exportar = True, pdf = nombre)
            helper_guardar_exportar_imagenes.terminado.connect(self.__slot_guardar_exportar_imagenes)
            helper_guardar_exportar_imagenes.start()

        # cargador
        notificador.inicio_operacion.emit()


    def __slot_guardar_exportar_imagenes(self, msg):
        '''
        Slot auxiliar para conocer cuando se termino el hilo que guarda
        y exporta las imagenes
        '''

        # cargador
        notificador.fin_operacion.emit()

        if len(msg) == 0:
            # teminado sin errores
            QMessageBox.information(self, u"Información", u"Operación realizada con éxito")
        else:
            # mostrar cartel con error
            QMessageBox.critical(self, u"Error", msg)


    def eliminar(self):
        resp = QMessageBox.question(self, u'Pregunta', u'¿Desea <b>eliminar</b> la imagen actual?',
                                           QMessageBox.Yes | QMessageBox.No)

        if resp == QMessageBox.Yes:
            # ejecutar el HILO paralelo
            helper_eliminar_imagenes.setData(self.__actualNro, self.__controladora)
            helper_eliminar_imagenes.terminado.connect(self.__slot_eliminar_imagenes)
            helper_eliminar_imagenes.start()
        else:
            return


    def __slot_eliminar_imagenes(self, msg):
        '''
        Slot auxiliar para conocer cuando se termino el hilo que adiciona imagenes
        '''

        # cargador
        notificador.fin_operacion.emit()

        if len(msg) == 0:
            # teminado sin errores
            self.__limpiar_miniaturas_comandos()

            if self.__controladora.get_cant_imagenes_cargadas() > 0:
                # actualizar el indice
                if self.__actualNro > 0:
                    self.__actualNro = self.__actualNro - 1

                # mostrar la imagen actual
                self.__actualizar_miniaturas()
                self.__mostrar_imagen(self.__actualNro)
                # actualizar la barra de estado
                self.__actualizar_info_swap_status_bar()

            else:
                # inicializar todo
                self.__inicializar()
        else:
            # mostrar cartel con error
            pass
        # mostrar cantidad de imágenes cargadas(margen derecho)
        self.label_2.setText(u"Imágenes Cargadas:"+str(self.__controladora.get_cant_imagenes_cargadas()))


    def __limpiar_miniaturas_comandos(self):
        '''
        Limpia las miniaturas de los comandos
        '''

        while self.miniaturas_comandos.count() > 0:
            item = self.miniaturas_comandos.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


    def __actualizar_info_swap_status_bar(self):
        '''
        Actualiza la informacion de la swap y la muestra en la Barra de Estado
        '''

        # calcular la nueva info
        info = self.__controladora.informacion_swap()
        
        lb = QLabel(self)
        texto = u'Área de intercambio: <b>' + info[1][0] + '</b> ' + info[1][1] + ' (<b>'
        texto += info[0] + '</b> elementos), ' + u'disponibles <b>' + info[2] + '</b> Gb.'
        lb.setText(texto)
        

        # eliminar toda la info actual (eliminar el actual statusBar)
        self.setStatusBar(None)
        # crear el nuevo statusBar
        status = QStatusBar(self)
        status.addWidget(lb)
        self.setStatusBar(status)

    
    def __abrir_proyecto(self):
        '''
        Abre un proyecto previamente guardado
        '''
        bandera = False
        # si ya se esta trabajando en un proyecto
        if self.__controladora.get_cant_imagenes_cargadas()>0:
            pregunta = QMessageBox.question(self, u'Pregunta', u' Ya está trabajando sobre un proyecto ¿Desea <b>eliminarlo</b> para cargar uno nuevo?',
                                           QMessageBox.Yes | QMessageBox.No)
                                           
            if pregunta == QMessageBox.No:
                    return
            else:
                self.__limpiar_miniaturas()
                self.__limpiar_miniaturas_comandos()
                self.__inicializar()
                bandera = True 
            
        if self.__controladora.get_cant_imagenes_cargadas()==0 or bandera:
            # seleccionar un proyecto doclux
            direccion = QFileDialog.getOpenFileNames(self, u"Cargar proyecto", QDir.homePath(), u"Proyecto DocLux (*.dlx)")
            
            for i in direccion:
                direccion = str(i)
            proyecto = direccion
            # se copia el proyecto cargado para la swap
            os.system(str("cp " + proyecto + " " + self.__controladora.get_swap_dir()))
            # descomprimiendo el proyecto
            os.system("cd " + self.__controladora.get_swap_dir() + "; unzip -q " + proyecto)
            # eliminando proyecto comprimido
            #os.remove(self.__controladora.get_swap_dir()+"/"+proyecto[1])
            # reemplazando las direcciones anteriores de la swap en el process.code
            tmp_code = open(self.__controladora.get_swap_dir() + '/procesos.code','rb').read()
            indice_inicial_dir_swap = 0
            indice_doclux_swap = tmp_code.index('/.DocLux/swap')
            for i in xrange(indice_doclux_swap - 1, 0, -1):
                if tmp_code[i] == '/' and tmp_code[i-1] == "'":
                    indice_inicial_dir_swap = i-1
            direccion_swap = tmp_code[indice_inicial_dir_swap + 1 : indice_doclux_swap + 13]
            tmp_code = tmp_code.replace(direccion_swap, str(self.__controladora.get_swap_dir()))
            tmp_code_usuario = open(self.__controladora.get_swap_dir() + '/procesos.code','w')
            tmp_code_usuario.write(tmp_code)
            tmp_code_usuario.close()
            #se carga en la controladora lo que tiene el proyecto que se desea abrir
            self.__controladora = pickle.load(open(self.__controladora.get_swap_dir() + '/procesos.code','rb'))
            #al cargarlo la controladora elimina lo de la swap, por eso se le vuelve a poner en la swap el proyecto descomprimido 
            os.system("cd " + self.__controladora.get_swap_dir() + "; unzip -q " + proyecto)
            #se actualizan las imagenes de ese proyecto cargado en el visor
            self.__actualizar_miniaturas()
            self.__mostrar_imagen(self.__actualNro)
    
    
    def __guardar_proyecto(self):
        '''
        Guarda todo el trabajo realizado
        '''
        #nombre del proyecto a guardar
        nombre_proyecto = str(QInputDialog.getText(self, u"Nombre del proyecto", u"Nombre del proyecto", text = "proyecto_doclux")[0])
        
        # si se selecciono CANCELAR
        if nombre_proyecto=="":
            return
            
        #seleccionar el directorio para salvar el proyecto
        destino = str(QFileDialog.getExistingDirectory(self, u"Seleccione ubicación", QDir.homePath(), QFileDialog.ShowDirsOnly ))
        
        # si se selecciono CANCELAR
        if destino=="":
            QMessageBox.information(self, u"Información", u"Operación cancelada")
            return
            
        # comprobando si ya existe un proyecto en ese directorio con el mismo nombre    
        if os.path.exists(destino+"/"+nombre_proyecto+".dlx"):
            pregunta = QMessageBox.question(self, u'Pregunta', u' Ya existe un proyecto con ese nombre ¿Desea <b>reemplazarlo</b>?',
                                           QMessageBox.Yes | QMessageBox.No)
            # si desea reemplazar el proyecto existente
            if pregunta == QMessageBox.No:
                return
        
        # guardando el dump del proyecto en la propia swap
        pickle.dump(self.__controladora, open(self.__controladora.get_swap_dir() + '/procesos.code','wb'))
           
        #comprimiendo swap en un fichero .zip (juntamente al dump de los procesos de imágenes)
        os.system("cd " + self.__controladora.get_swap_dir()+"; zip -q " + nombre_proyecto + ".dlx *")

        #se mueve la salva del proyecto completa para el destino que el usuario eligio
        os.system("mv " + self.__controladora.get_swap_dir() + "/" + nombre_proyecto + ".dlx " + destino)
       
        # fin de operaciones
        QMessageBox.information(self, u"Información", u"Operación realizada con éxito")

    def __limpiar(self):
        '''
        limpia la swap sin necesidad de cerrar la aplicación
        '''
        
        if self.__controladora.get_cant_imagenes_cargadas()==0:
            QMessageBox.information(self, u"Información", u"No es necesario resetear el proyecto actual")            
        else:
            resp = QMessageBox.question(self, u'Pregunta', u'<b>Esta acción eliminará todos los comandos aplicados a las imágenes</b> y reiniciará el proyecto actual. ¿Esta seguro que es eso lo que desea hacer?',
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            #repuesta positiva
            if resp == QMessageBox.Yes:
				self.__controladora.resetear_proyecto()
				self.__limpiar_miniaturas_comandos()
				self.__limpiar_miniaturas()
				self.__actualizar_miniaturas()
				self.__mostrar_imagen(self.__actualNro)
            else:
                #repuesta negativa
                return
    
    def __eliminar_todas(self):
		
        '''
        limpia la swap sin necesidad de cerrar la aplicación
        '''
        if self.__controladora.get_cant_imagenes_cargadas()==0:
            QMessageBox.information(self, u"Información", u"No es necesario resetear el proyecto actual")            
        else:
		resp = QMessageBox.question(self, u'Pregunta', u'<b>Esta acción eliminará todos los comandos aplicados a las imágenes</b> y reiniciará el proyecto actual. ¿Esta seguro que es eso lo que desea hacer?',
										   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
		#repuesta positiva
		if resp == QMessageBox.Yes:
			self.__inicializar()
			self.__limpiar_miniaturas_comandos()
			self.__limpiar_miniaturas()
			self.__controladora.limpiar_swap()
			# mostrar cantidad de imágenes cargadas(margen derecho)
			self.label_2.setText(u"Imágenes Cargadas:"+str(self.__controladora.get_cant_imagenes_cargadas()))

		else:
			#repuesta negativa
			return
    
                
    
    def __mostrar_cargando(self):
        '''
        Muestra la ventana de Cargando para indicar que HAY una operacion en curso
        '''

        self.setCursor(QCursor(Qt.BusyCursor))

        self.__cargando = Cargando(self)
        self.__cargando.show()
    
    
    
    
    def gestionar_swap(self):
        '''
        Muestra el cuadro de diálogo para que la swap sea gestionada
        '''

        gestionar = Swap(self.__controladora.get_swap_dir(), self)
        # se captura la señal sobre la nueva swap y el nuevo directorio
		# se le envía esa información al metodo __gestionar_swap
        gestionar.terminado.connect(self.__gestionar_swap)
        gestionar.show()
    
    
    def __gestionar_swap(self, nueva_swap, nuevo_dir_swap):
        '''
        Informa a la controladora que el usuario seleccionó un nuevo directorio para la swap
        '''
        # comprobar si el directorio nuevo tiene capacidad 
        swapp = self.__controladora.informacion_swap()
        total_swap=swapp[1][0]        
        nuevo = self.__controladora.informacion_directorios(nuevo_dir_swap)
        total_new_dir=nuevo[1][0]
      
        
        print total_new_dir, "nuevo"
        print total_swap, "total_swap"
        if total_swap > total_new_dir:
			QMessageBox.information(self, u"Información", u" No es posible mover la swap porque el directorio seleccionado no tiene la capacidad suficiente")
			return
			
			
			
			
			
        else:
			# comprobar si el nuevo directorio es válido
			if os.path.isdir(nuevo_dir_swap):
				if self.__controladora.get_swap_dir()== nueva_swap:
					QMessageBox.information(self, u"Información", u" Ha seleccionado el directorio actual, seleccione un nuevo directorio")
					return
				# si ya existe una swap en ese directorio
				elif os.path.exists(nueva_swap):
					QMessageBox.information(self, u"Información", u" Ya existe una swap en ese directorio, debe seleccionar otro directorio o borrar la swap existente en el mismo.")
					return
				else:
					self.__controladora.actualizar_swap(str(nueva_swap))
					QMessageBox.information(self, u"Información", u"OK, la nueva swap es: " + nueva_swap)
					self.__actualizar_info_swap_status_bar()
			else:
				QMessageBox.information(self, u"Información", u" Debe seleccionar un directorio válido para realizar esta acción.")
				return

    def __ocultar_cargando(self, returnCode = -1):
        '''
        Oculta la ventana de Cargando cuando NO HAY operaciones en curso
        '''

        self.__cargando.reject()
        del(self.__cargando)

        self.setCursor(QCursor(Qt.ArrowCursor))
