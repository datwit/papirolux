#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Plugin para aplicar OCR usando el API Tesseract (Python)
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

# clase base
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(667, 408)
        self.gridLayout_9 = QtGui.QGridLayout(Form)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.lb_imgOrig = QtGui.QLabel(Form)
        self.lb_imgOrig.setObjectName(_fromUtf8("lb_imgOrig"))
        self.gridLayout_7.addWidget(self.lb_imgOrig, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 651, 98))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_imgOrig = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_imgOrig.setText(_fromUtf8(""))
        self.label_imgOrig.setObjectName(_fromUtf8("label_imgOrig"))
        self.gridLayout_3.addWidget(self.label_imgOrig, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.line_separate_2 = QtGui.QFrame(Form)
        self.line_separate_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_separate_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_separate_2.setObjectName(_fromUtf8("line_separate_2"))
        self.gridLayout_6.addWidget(self.line_separate_2, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit_Ocr = QtGui.QTextEdit(Form)
        self.textEdit_Ocr.setObjectName(_fromUtf8("textEdit_Ocr"))
        self.gridLayout.addWidget(self.textEdit_Ocr, 1, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lb_txtOcr = QtGui.QLabel(Form)
        self.lb_txtOcr.setObjectName(_fromUtf8("lb_txtOcr"))
        self.gridLayout_8.addWidget(self.lb_txtOcr, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.line_separate = QtGui.QFrame(Form)
        self.line_separate.setFrameShape(QtGui.QFrame.HLine)
        self.line_separate.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_separate.setObjectName(_fromUtf8("line_separate"))
        self.gridLayout.addWidget(self.line_separate, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.boton_guardar_ocr = QtGui.QPushButton(Form)
        self.boton_guardar_ocr.setObjectName(_fromUtf8("boton_guardar_ocr"))
        self.gridLayout_2.addWidget(self.boton_guardar_ocr, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.boton_cerrar_ocr = QtGui.QPushButton(Form)
        self.boton_cerrar_ocr.setObjectName(_fromUtf8("boton_cerrar_ocr"))
        self.gridLayout_2.addWidget(self.boton_cerrar_ocr, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.boton_cerrar_ocr, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_imgOrig.setText(QtGui.QApplication.translate("Form", "Imagen original", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_txtOcr.setText(QtGui.QApplication.translate("Form", "Texto transcrito", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_guardar_ocr.setText(QtGui.QApplication.translate("Form", "Guardar texto", None, QtGui.QApplication.UnicodeUTF8))
        self.boton_cerrar_ocr.setText(QtGui.QApplication.translate("Form", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))

# clase derivada
class Ventana(QtGui.QDialog, Ui_Form):
    def __init__(self, plugin, urlsIn, urlsOut, notificador = None, parent = None):
        # inicializar el padre
        super(Ventana, self).__init__(parent)
        # configurar la interfaz
        self.setupUi(self)

        # variables necesarias
        # plugin que necesita esta ventana
        self.__plugin = plugin
        # imagenes que modifica el plugin
        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut
        # objeto notificador
        self.__notificador = notificador
        # actualizar el notificador con un parent (obligatorio si hay IU)
        self.__notificador.parent = self

        # configuraciones adicionales
        # mostrar la ventana como modal sobre TODA LA APLICACION
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # establecer el nombre de la ventana
        self.setWindowTitle(self.__plugin.nombre())

        # signals/slots
        # boton guardar texto
        #~ self.boton_guardar_ocr.clicked.connect(self.__guardar_txt_ocr)


    #~ def __guardar_txt_ocr(self, imagenesIn):
#~ 
        #~ dirName = QFileDialog.getExistingDirectory(self, u"Seleccionar ubicación", QDir.homePath(), QFileDialog.ShowDirsOnly )
        #~ #si se selecciono CANCELAR
        #~ if dirName.isEmpty():
            #~ QMessageBox.information(self, u"Información", u"Operación cancelada")
            #~ return
#~ 
        #~ directorio = QDir(dirName)
#~ 
        #~ for i in imagenesIn:
                #~ result = QFile.copy(i[0], dirName + '/' + i[1] + '.txt')
            #~ if not result:
                #~ msg = u"Algunos ficheros <b>no se guardaron</b> porque ya existían en el directorio seleccionado(<b>" + dirName + "</b>)"
                #~ QMessageBox.warning(self, u"Advertencia", msg)
#~ 
        #~ return


    def update_images(self, urlsIn, urlsOut):
        self.__imagenesIn = urlsIn
        self.__imagenesOut = urlsOut

from plugins.plugin_base import PluginBase
import os

class Plugin(PluginBase):
    # funciones basicas
    def nombre(self):
        return 'Ocr Tesseract'


    def version(self):
        return 'v1.0'


    def descripcion(self):
        return 'Ocr Tesseract utilizando API (Python)'


    def autores(self):
        return ['Ing. Eduardo Salazar Martínez']


    def icon(self):
        return os.path.dirname(__file__) + '/images/ocr.png'


    # funcion principal del plugin
    def run(self, imagenesIn, imagenesOut, notificador, gui_parent):

		if len(imagenesIn) != len(imagenesOut):
			notificador.error.emit('No coinciden la cantidades de imagenes de entrada y de salida')
			return

		import cv2.cv as cv
		import tesseract
		for i in range(len(imagenesIn)):
			im = cv.LoadImage(imagenesIn[i], cv.CV_LOAD_IMAGE_GRAYSCALE)
			api = tesseract.TessBaseAPI()
			api.Init(".","spa",tesseract.OEM_DEFAULT)
			api.SetPageSegMode(tesseract.PSM_AUTO)
			tesseract.SetCvImage(im,api)
			text=api.GetUTF8Text()
			conf=api.MeanTextConf()
			#~ print text
			#~ print text.encode('L1')
			#~ print conf

		# visualizar la interfaz de usuario del plugin
		window = Ventana(self, imagenesIn, imagenesOut, notificador, gui_parent)
		#~ window.textEdit_Ocr.setPlainText(text.encode('utf-8'))
		window.textEdit_Ocr.setPlainText(text)
		window.label_imgOrig.setPixmap(QPixmap(imagenesIn[i]))
		window.show()
		return


