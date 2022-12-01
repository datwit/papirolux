#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QDesktopWidget, QFileDialog, QFrame, QMessageBox, QInputDialog
from PyQt5.QtCore import QDir, QFile
from PyQt5.QtPrintSupport import QPrinter

import os

from ui.principal import Ui_MainWindow
from .acercaUI import AcercaDe
from .comandosUI import ListaComandos

from src.control.docluxControl import DocLux_Control
from .miniatura import Miniatura
from .plugin_notificador import Notificador

import plugins.plugin_loader as plugin_loader

# notificador
notificador = Notificador()

class MyQAction(QAction):
    '''
    Clase para poder asociar el QAction con la funcion
    correspondiente en cada plugin
    '''

    def __init__(self, pluginObj, parent = None):
        # inicializar el padre
        super(MyQAction, self).__init__(parent)

        # funcion asociada a cada plugin
        self.__plugin = pluginObj

        # configurar el action
        self.setText(self.__plugin.nombre())
        self.setIcon(QIcon(self.__plugin.icon()))


    def execFunc(self, urlsIn, urlsOut, notificador):
        '''
        Ejecutar la funcion con los parametros adecuados
        '''

        self.__plugin.run(urlsIn, urlsOut, notificador, self.parent())


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
        # seleccionar actual
        self.actionSeleccionar_actual.triggered.connect(self.seleccionar_actual)
        # seleccionar todas
        self.actionSeleccionar_todas.triggered.connect(self.seleccionar_todas)
        # salir
        self.actionSalir.triggered.connect(self.close)
        # minimizar
        self.actionMinimizar.triggered.connect(self.showMinimized)
        # acerca de
        self.actionAcerca.triggered.connect(self.acerca_de)
        # lista de comandos
        self.actionListaComandos.triggered.connect(self.lista_cmds)
        # deshacer/rehacer
        self.actionDeshacer.triggered.connect(self.deshacer)
        self.actionRehacer.triggered.connect(self.rehacer)
        # guardar/guardar todas
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardarTodas.triggered.connect(self.guardar_todas)
        # exportar/exportar todas
        self.actionExportar.triggered.connect(self.exportar)
        self.actionExportarTodas.triggered.connect(self.exportar_todas)
        #elinimar imagen
        self.actionEliminar.triggered.connect(self.eliminar)



        # cargar los plugins
        self.__cargar_plugins()

        # inicializar todo el resto de la app
        self.__inicializar()


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

        imgsIn = []
        imgsOut = []

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_seleccionadas()):
                imgsIn.append(self.__controladora.get_imagen_procesada_nro(i)[0])
                imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(i))
        else:
            imgsIn.append(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro)[0])
            imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(self.__procesadaNro))

        self.sender().execFunc(imgsIn, imgsOut, notificador)


    def __plugin_ejecutado(self, plugin_name):
        '''
        Actualiza la lista de comandos con el resultado de la transformacion
        '''

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_seleccionadas()):
                self.__controladora.nuevo_comando(plugin_name, i)
        else:
            self.__controladora.nuevo_comando(plugin_name, self.__procesadaNro)

        # actualizar las miniaturas procesadas
        self.__actualizar_miniaturas_procesadas()
        # actualizar el visor procesada
        self.__mostrar_procesada(self.__procesadaNro)

        # actualizar las imagenes que debe usar el plugin
        imgsIn = []
        imgsOut = []

        if self.aplicar_todas.isChecked():
            for i in range(self.__controladora.get_cant_imagenes_seleccionadas()):
                imgsIn.append(self.__controladora.get_imagen_procesada_nro(i)[0])
                imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(i))
        else:
            imgsIn.append(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro)[0])
            imgsOut.append(self.__controladora.get_siguiente_transformacion_imagen_nro(self.__procesadaNro))

        if self.sender().parent != None:
            self.sender().parent.update_images(imgsIn, imgsOut)


    def __plugin_error(self, msg):
        print ('Error en plugin, mensaje: ' + msg)


    def closeEvent(self, event):
        '''
        Evento que se ejecuta al solicitar que se Cierre la aplicacion, pidiendo
        confirmacion antes de ejecutar la accion
        '''

        resp = QMessageBox.question(self, u'Pregunta', u'¿Realmente desea <b>salir</b>?', QMessageBox.Yes | QMessageBox.No)
        # si respuesta positiva
        if resp == QMessageBox.Yes:
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
        imagenes = imagenes[0]

        if len(imagenes) == 0:
            self.__controladora.eliminar_imagenes()
            return

        # convertir de QStringList a python list sin repetidos
        lista = []
        for i in imagenes:
            if not str(i) in lista:
                lista.append(str(i))



        self.__controladora.nuevas_imagenes(lista)
        self.__originalNro = 0
        self.__procesadaNro = -1
        self.mostrar_imagen_original(self.__controladora.get_imagen_original_nro(self.__originalNro))

        # actualizar las miniaturas
        self.__actualizar_miniaturas_originales()

        # habilitar los controles de la IU original
        self.__habilitar_controles_visor_original()


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
            if not str(i) in lista:
                lista.append(str(i))

        # adicionamos las imagenes a las actuales
        self.__controladora.nuevas_imagenes(lista, True)

        # actualizar las miniaturas
        self.__actualizar_miniaturas_originales()

        # habilitar los controles de la IU original
        self.__habilitar_controles_visor_original()


    def mostrar_imagen_original(self, info):
        '''
        Muestra una imagen en el visor original

        Parametros:
        - [tuple] info: (urlmagen, nombre)
        '''

        self.img_Original.setPixmap(QPixmap(info[0]))
        self.nombreOriginal.setText(info[1])

        lab = '<b>{0}</b> de <b>{1}</b>'.format(self.__originalNro + 1, self.__controladora.get_cant_imagenes_cargadas())
        self.indicadorOriginal.setText(lab)
        
        #~ # verificar si la imagen esta seleccionada para actualizar el icono de la accion
        #~ if self.__controladora.verificar_seleccionada(self.__originalNro):
            #~ self.actionSeleccionar_actual.setIcon(QIcon(":/imgs/recursos/imagenes/deseleccionar_actual.png"))
            #~ self.actionSeleccionar_actual.setToolTip("Deseleccionar Actual")
        #~ else:
            #~ self.actionSeleccionar_actual.setIcon(QIcon(":/imgs/recursos/imagenes/seleccionar_actual.png"))
            #~ self.actionSeleccionar_actual.setToolTip("Seleccionar Actual")


    def __actualizar_miniaturas_originales(self):
        '''
        Actualiza las miniaturas de las imagenes originales
        '''

        # obtener la lista de las miniaturas
        miniaturas = self.__controladora.get_miniaturas_originales()

        # limpiar las miniaturas originales
        self.__limpiar_miniaturas_originales()

        # mostrar las nuevas miniaturas
        i = 0
        while i < len(miniaturas):
            lab = Miniatura(i, self)
            lab.setMinimumSize(40, 50)
            lab.setMaximumSize(40, 50)
            lab.signals.ver_miniatura.connect(self.__mostrar_original)
            lab.setPixmap(QPixmap(miniaturas[i]))
            if i == self.__originalNro:
                lab.setLineWidth(2)
                lab.setFrameStyle(QFrame.Box)
            # adicionar al layout
            self.miniaturas_originales.addWidget(lab)

            i = i + 1

        lab = '<b>{0}</b> de <b>{1}</b>'.format(self.__originalNro + 1, self.__controladora.get_cant_imagenes_cargadas())
        self.indicadorOriginal.setText(lab)


    def __mostrar_original(self, indice):
        '''
        Identifica que imagen se debe mostrar en dependencia de la miniatura
        '''

        self.__originalNro = indice
        self.mostrar_imagen_original(self.__controladora.get_imagen_original_nro(indice))

        self.__actualizar_miniaturas_originales()


    def __mostrar_procesada(self, indice):
        '''
        Identifica que imagen se debe mostrar en dependencia de la miniatura
        '''

        self.__procesadaNro = indice
        self.mostrar_imagen_procesada(self.__controladora.get_imagen_procesada_nro(indice))

        self.__actualizar_miniaturas_procesadas()


    def __limpiar_miniaturas_originales(self):
        '''
        Limpia las miniaturas originales
        '''

        # eliminar las miniaturas actuales del layout
        while self.miniaturas_originales.count() > 0:
            item = self.miniaturas_originales.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


    def __limpiar_miniaturas_procesadas(self):
        '''
        Limpia las miniaturas procesadas
        '''

        # eliminar las miniaturas actuales del layout
        while self.miniaturas_procesadas.count() > 0:
            item = self.miniaturas_procesadas.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


    def __inicializar(self):
        '''
        Resetea toda la aplicacion con el estado inicial
        '''

        lab = '<b>{0}</b> de <b>{1}</b>'.format('0', '0')
        self.indicadorOriginal.setText(lab)
        self.nombreOriginal.setText('')
        self.img_Original.clear()
        self.__limpiar_miniaturas_originales()
        self.__originalNro = -1
        self.__procesadaNro = -1
        self.indicadorProcesada.setText(lab)
        self.nombreProcesada.setText('')
        self.img_Procesada.clear()
        self.__limpiar_miniaturas_procesadas()

        # deshabilitar todos los controles que no se necesitan
        self.actionAdicionar.setEnabled(False)
        self.actionSeleccionar_actual.setEnabled(False)
        self.actionSeleccionar_todas.setEnabled(False)
        self.actionEliminar.setEnabled(False)
        self.actionDeshacer.setEnabled(False)
        self.actionRehacer.setEnabled(False)
        self.actionGuardar.setEnabled(False)
        self.actionGuardarTodas.setEnabled(False)
        self.actionExportar.setEnabled(False)
        self.actionExportarTodas.setEnabled(False)
        self.actionListaComandos.setEnabled(False)
        self.aplicar_todas.setEnabled(False)
        # deshabilitar todos los plugins
        for action in self.menuPlugins.actions():
            action.setEnabled(False)


    def seleccionar_actual(self):
        '''
        Realiza las acciones:
        - verifica si esa imagen ya esta seleccionada
            * si ya esta seleccionada, posibilita deseleccionarla
            * si no esta seleccionada adiciona la imagen actual a la lista de procesadas
        '''
        if self.__controladora.verificar_seleccionada(self.__originalNro)==True:
            resp = QMessageBox.question(self, u'Pregunta', u' Esta imagen ya está seleccionada ¿Desea <b>deseleccionarla</b>?', QMessageBox.Yes | QMessageBox.No)
            
            if resp == QMessageBox.Yes:
                self.__controladora.deseleccionar(self.__originalNro)
                self.actualizar_img_seleccionadas()
                
            else:
                return
        else:
            
            if self.__originalNro < 0:
                return
            self.__controladora.seleccionar_imagen_nro(self.__originalNro)
            if self.__controladora.get_cant_imagenes_seleccionadas() == 1:
                self.__procesadaNro = 0
                # mostrar la imagen en el visor
                self.mostrar_imagen_procesada(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro))

            # actualizar las miniaturas
            self.__actualizar_miniaturas_procesadas()

            # habilitar los controles de la IU original
            self.__habilitar_controles_visor_procesada()


    def seleccionar_todas(self):
        '''
        Selecciona todas las imagenes y las adiciona a la lista de imagenes
        procesadas

        Realiza las acciones:
        - adiciona todas las imagenes a la lista de imagenes procesadas
        '''
        
        if self.__controladora.get_cant_imagenes_cargadas()==self.__controladora.get_cant_imagenes_seleccionadas():
            resp = QMessageBox.question(self, u'Pregunta', u' Todas las imágenes ya están seleccionadas ¿Desea <b>deseleccionarlas</b>?', QMessageBox.Yes | QMessageBox.No)
            if resp == QMessageBox.Yes:
               self.__controladora.deseleccionar_todas()
               self.actualizar_img_seleccionadas()
            else:
                return   
                
        else:
            seleccionadas = self.__controladora.get_cant_imagenes_seleccionadas()
            self.__controladora.seleccionar_todas_las_imagenes()

            # si no habia ninguna antes, mostrar la primera
            if seleccionadas == 0:
                self.__procesadaNro = 0
                # mostrar la imagen en el visor
                self.mostrar_imagen_procesada(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro))

            # actualizar las miniaturas
            self.__actualizar_miniaturas_procesadas()

            # habilitar los controles de la IU original
            self.__habilitar_controles_visor_procesada()


    def mostrar_imagen_procesada(self, info):
        '''
        Muestra una imagen en el visor procesadas

        Parametros:
        - [tuple] info: (urlmagen, nombre)
        '''

        self.img_Procesada.setPixmap(QPixmap(info[0]))
        self.nombreProcesada.setText(info[1])

        # actualizar informacion
        lab = QString('<b>%1</b> de <b>%2</b>').arg(self.__procesadaNro + 1).arg(self.__controladora.get_cant_imagenes_seleccionadas())
        self.indicadorProcesada.setText(lab)

        # sincronizar los visores
        self.__sincronizar_visores()

        # habilitar los controles de la IU original
        self.__habilitar_controles_visor_procesada()


    def __actualizar_miniaturas_procesadas(self):
        '''
        Actualiza las miniaturas de las imagenes procesadas
        '''

        # obtener la lista de las miniaturas
        miniaturas = self.__controladora.get_miniaturas_procesadas()

        # limpiar las miniaturas originales
        self.__limpiar_miniaturas_procesadas()

        # mostrar las nuevas miniaturas
        i = 0
        while i < len(miniaturas):
            lab = Miniatura(i, self)
            lab.setMinimumSize(40, 50)
            lab.setMaximumSize(40, 50)
            lab.signals.ver_miniatura.connect(self.__mostrar_procesada)
            lab.setPixmap(QPixmap(miniaturas[i]))
            if i == self.__procesadaNro:
                lab.setLineWidth(2)
                lab.setFrameStyle(QFrame.Box)
            # adicionar al layout
            self.miniaturas_procesadas.addWidget(lab)

            i = i + 1

        lab = QString('<b>%1</b> de <b>%2</b>').arg(self.__procesadaNro + 1).arg(self.__controladora.get_cant_imagenes_seleccionadas())
        self.indicadorProcesada.setText(lab)


    def __sincronizar_visores(self):
        '''
        Sincroniza los visores para que se vea en el original la imagen
        correspondiente a la procesada actual

        Realiza las acciones:
        - busca la imagen procesada en la lista de originales
        - actualiza el visor original
        '''

        nroOriginal = self.__controladora.sincronizar(self.__procesadaNro)
        if nroOriginal == -1:
            return

        self.__mostrar_original(nroOriginal)


    def __habilitar_controles_visor_original(self):
        '''
        Habilita los controles necesarios para que funcione el visor
        de imagenes originales
        '''

        self.actionAdicionar.setEnabled(True)
        self.actionSeleccionar_actual.setEnabled(True)
        if self.__controladora.get_cant_imagenes_cargadas() > 1:
            self.actionSeleccionar_todas.setEnabled(True)
        else:
            self.actionSeleccionar_todas.setEnabled(False)
        self.actionEliminar.setEnabled(True)


    def __habilitar_controles_visor_procesada(self):
        '''
        Habilita los controles necesarios para que funcione el visor
        de imagenes procesadas
        '''

        # debe ser deseleccionar...
        self.actionSeleccionar_actual.setEnabled(True)
        self.actionSeleccionar_todas.setEnabled(True)

        self.actionEliminar.setEnabled(True)
        self.actionDeshacer.setEnabled(False)
        self.actionRehacer.setEnabled(False)
        self.actionGuardar.setEnabled(True)
        self.actionExportar.setEnabled(True)
        if self.__controladora.get_cant_imagenes_seleccionadas() > 1:
            self.aplicar_todas.setEnabled(True)
            self.actionGuardarTodas.setEnabled(True)
            self.actionExportarTodas.setEnabled(True)
        else:
            self.aplicar_todas.setEnabled(False)
            self.actionGuardarTodas.setEnabled(False)
            self.actionExportarTodas.setEnabled(False)

        # habilitar todos los plugins
        for action in self.menuPlugins.actions():
            action.setEnabled(True)

        self.actionListaComandos.setEnabled(False)
        if len(self.__controladora.get_comandos_imagen_nro(self.__procesadaNro)) > 0:
            self.actionListaComandos.setEnabled(True)

        if self.__controladora.puede_deshacer(self.__procesadaNro):
            self.actionDeshacer.setEnabled(True)
        if self.__controladora.puede_rehacer(self.__procesadaNro):
            self.actionRehacer.setEnabled(True)


    def acerca_de(self):
        '''
        Muestra la informacion de Acerca de
        '''

        acerca = AcercaDe(self)
        acerca.show()


    def lista_cmds(self):
        '''
        Muestra la lista de comandos de la imagen procesada actual
        '''

        cmds = ListaComandos(self.__controladora.get_comandos_imagen_nro(self.__procesadaNro),
                self.__controladora.get_swap_dir(), self)
        # conectar las signals
        cmds.signals.ver_imagen_comando.connect(self.__mostrar_comando_nro)
        cmds.signals.cancelar.connect(self.__cancelar_comando)
        cmds.signals.retornar_comando.connect(self.__actualizar_procesada_al_comando)
        cmds.show()


    def __mostrar_comando_nro(self, i):
        '''
        Muestra la imagen actual en el estado del comando i
        '''

        # obtener la imagen correspondiente al comando i
        img = self.__controladora.get_imagen_comando_nro(self.__procesadaNro, i)
        self.img_Procesada.setPixmap(QPixmap(img))


    def __cancelar_comando(self):
        '''
        Actualiza la imagen actual mostrandola en su ultimo estado
        '''

        self.__mostrar_procesada(self.__procesadaNro)


    def __actualizar_procesada_al_comando(self, i):
        '''
        Retorna la imagen actual al comando seleccionado ignorando los
        sucesores del i
        '''

        self.__controladora.eliminar_comandos_despues_de( self.__procesadaNro, i + 1)
        self.__actualizar_miniaturas_procesadas()


    def deshacer(self):
        '''
        Deshacer un comando
        '''

        if self.__controladora.deshacer_comando(self.__procesadaNro):
            self.__mostrar_procesada(self.__procesadaNro)


    def rehacer(self):
        '''
        Rehacer un comando
        '''

        if self.__controladora.rehacer_comando(self.__procesadaNro):
            self.__mostrar_procesada(self.__procesadaNro)


    def guardar(self):
        '''
        Guardar una imagen
        '''

        img = [self.__controladora.get_imagen_procesada_nro(self.__procesadaNro)]
        self.__guardar_exportar(img)


    def guardar_todas(self):
        '''
        Guardar todas las imagenes
        '''

        imgs = []
        for i in range(self.__controladora.get_cant_imagenes_seleccionadas()):
            imgs.append(self.__controladora.get_imagen_procesada_nro(i))
        self.__guardar_exportar(imgs)


    def exportar(self):
        '''
        Exportar una imagen en formato PDF
        '''

        img = [self.__controladora.get_imagen_procesada_nro(self.__procesadaNro)]
        self.__guardar_exportar(img, True)


    def exportar_todas(self):
        '''
        Exportar todas las imagenes en formato PDF
        '''

        imgs = []
        for i in range(self.__controladora.get_cant_imagenes_seleccionadas()):
            imgs.append(self.__controladora.get_imagen_procesada_nro(i))
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

        dirName = QFileDialog.getExistingDirectory(self, u"Seleccionar ubicación", QDir.homePath(), QFileDialog.ShowDirsOnly )

        # si se selecciono CANCELAR
        if dirName.isEmpty():
            QMessageBox.information(self, u"Información", u"Operación cancelada")
            return

        directorio = QDir(dirName)

        # si se quiere GUARDAR
        if not exportar:
            # si se quiere guardar en cualquier directorio
            result = True
            for i in imgs:
                result = QFile.copy(i[0], dirName + '/' + i[1] + '.jpg')
            if not result:
                msg = u"Algunos ficheros <b>no se guardaron</b> porque ya existían en el directorio seleccionado(<b>" + dirName + "</b>)"
                QMessageBox.warning(self, u"Advertencia", msg)

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

            # configurar la impresora
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setPaperSize(QPrinter.Letter)
            printer.setOutputFileName(nombre)
            painter = QPainter(printer)
            rect = painter.viewport()
            for i in range(len(imgs)):
                img = QImage(imgs[i][0])
                size = img.size()
                size.scale(rect.size(), Qt.KeepAspectRatio)
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                painter.setWindow(img.rect())
                painter.drawImage(0, 0, img)
                if i < (len(imgs) - 1):
                   printer.newPage()

            # eliminar la "basura"
            del painter
            del printer
    
    def actualizar_img_seleccionadas(self):
        '''
        método que actualiza el visor y las miniaturas de las 
        imágenes seleccionadas en dependencia de la acción que se 
        realice sobre ellas (deseleccionarlas o eliminarlas) 
            - Desactiva los componentes que no sean necesarios
            - muestra la imágen correspondiente 
        '''
        #verifica el estado de la lista de imágenes seleccionadas (para procesar) después de la eliminación
        if self.__controladora.get_cant_imagenes_seleccionadas()==0:
            self.__procesadaNro = -1
            self.img_Procesada.clear()
            self.nombreProcesada.setText('')
            self.actionDeshacer.setEnabled(False)
            self.actionRehacer.setEnabled(False)
            self.actionGuardar.setEnabled(False)
            self.actionGuardarTodas.setEnabled(False)
            self.actionExportar.setEnabled(False)
            self.actionExportarTodas.setEnabled(False)
            self.actionListaComandos.setEnabled(False)
            self.aplicar_todas.setEnabled(False)
            # deshabilitar todos los plugins
            for action in self.menuPlugins.actions():
                action.setEnabled(False)                        
        else:
            if self.__controladora.get_cant_imagenes_seleccionadas()==1:
                self.__procesadaNro = 0
                self.mostrar_imagen_procesada(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro))
            else:
                if self.__controladora.get_cant_imagenes_seleccionadas()>1:
                    if self.__procesadaNro > 0:
                        self.__procesadaNro = self.__procesadaNro - 1
                    self.mostrar_imagen_procesada(self.__controladora.get_imagen_procesada_nro(self.__procesadaNro))
        self.__actualizar_miniaturas_procesadas()
        
        
    
    def eliminar(self):
        resp = QMessageBox.question(self, u'Pregunta', u'¿Desea <b>eliminar</b> la imagen actual?',
                                           QMessageBox.Yes | QMessageBox.No)
        
        if resp == QMessageBox.Yes:
                self.__controladora.eliminar(self.__originalNro)
                self.actualizar_img_seleccionadas()
                
                #verifica el estado de la lista de imágenes cargadas después de la eliminación
                if self.__controladora.get_cant_imagenes_cargadas()==0:
                        self.__originalNro = -1
                else:
                        if self.__controladora.get_cant_imagenes_cargadas()==1:
                                self.__originalNro = 0
                                self.mostrar_imagen_original(self.__controladora.get_imagen_original_nro(self.__originalNro))
                        else:
                                if self.__controladora.get_cant_imagenes_cargadas()>1:
                                        if self.__originalNro > 0:
                                                self.__originalNro = self.__originalNro - 1
                                        self.mostrar_imagen_original(self.__controladora.get_imagen_original_nro(self.__originalNro))
                self.__actualizar_miniaturas_originales()
                self.__actualizar_miniaturas_procesadas()
                if self.__controladora.get_cant_imagenes_cargadas()==0 and self.__controladora.get_cant_imagenes_seleccionadas()==0:
                    self.__inicializar()
        else:
            return
