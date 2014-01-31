# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayuda.ui'
#
# Created: Tue Jan 28 13:52:54 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dlg_acerca_de(object):
    def setupUi(self, dlg_acerca_de):
        dlg_acerca_de.setObjectName(_fromUtf8("dlg_acerca_de"))
        dlg_acerca_de.resize(871, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/imagenes/logo_proyecto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlg_acerca_de.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(dlg_acerca_de)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(dlg_acerca_de)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(dlg_acerca_de)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(23, 141, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(224, 100))
        self.label.setMaximumSize(QtCore.QSize(224, 100))
        self.label.setStyleSheet(_fromUtf8("image: url(:/ayuda/recursos/imagenes/ayuda_rcs/logo_doclux.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/imagenes/logo_proyecto.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(49, 141, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(17, 64, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(18, 64, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setEnabled(True)
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_3)
        self.textEdit_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_4.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_4)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 831, 448))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.textEdit_4 = QtGui.QTextEdit(self.tab_5)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 831, 448))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.textEdit_5 = QtGui.QTextEdit(self.tab_6)
        self.textEdit_5.setGeometry(QtCore.QRect(0, 0, 831, 448))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.textEdit_7 = QtGui.QTextEdit(self.tab_8)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 841, 391))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.textEdit_6 = QtGui.QTextEdit(self.tab_7)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 0, 831, 381))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(dlg_acerca_de)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), dlg_acerca_de.close)
        QtCore.QMetaObject.connectSlotsByName(dlg_acerca_de)

    def retranslateUi(self, dlg_acerca_de):
        dlg_acerca_de.setWindowTitle(QtGui.QApplication.translate("dlg_acerca_de", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("dlg_acerca_de", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlg_acerca_de", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlg_acerca_de", "Versión:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlg_acerca_de", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlg_acerca_de", "Tratamiento de imágenes de archivos por lotes.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlg_acerca_de", "3.0 \"Lista-Simple\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dlg_acerca_de", "Enero, 2014", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("dlg_acerca_de", "Versión", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:16pt; font-weight:600; font-style:italic;\">DocLux. Sistema para el tratamiento de imágenes de archivos por lotes.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">A continuación se describen las generalidades del ambiente del sistema DocLux:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:200; font-style:italic; color:#000000;\">     </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/01_visor_inicio.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; color:#000000;\">La aplicación para tratar lotes de imágenes de archivos históricos esta dividida en 7 áreas fundamentales. Cada una de las áreas se muestran a continuación.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Barra de menú</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:200; font-style:italic; color:#000000;\">  </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/02_barra_de_menu.png\" /><span style=\" font-family:\'Sans\'; font-size:10pt;\"><br /></span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Barra de herramientas:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/03_bh_plugins.png\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Área de trabajo:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/04_visor_area_de_trabajo.png\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Imágenes </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">cargadas:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/05_visor_imagenes_cargadas.png\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Lista de comandos:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/06_visor_lista_de_comandos.png\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt; font-weight:200; font-style:italic; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Barra de herramientas inferior:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/07_bh_inferior.png\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt; color:#000000;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("dlg_acerca_de", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_2.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">  </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">BARRA DE MENÚ</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/02_barra_de_menu.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">La Barra de menú contiene cada una de las opciones que posibilita el sistema DocLux.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">. Archivo.</span><span style=\" font-family:\'Sans\'; font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Este menú permite cargar </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Nuevas</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> imágenes al sistema, así como </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Adicionar</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> otras imágenes a la lista existente. Además, permite </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Guardar</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> y </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Exportar</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> la/s imágenes y posibilita </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Minimizar</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> y </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Salir</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> de la aplicación.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/08_menu_archivo.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.1. Nuevas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_nuevas_imgs.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta opción permite cargas nuevas imágenes al sistema para ser procesadas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.2. Adicionar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_adicionar_imgs.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite </span><span style=\" font-family:\'Sans\'; font-size:10pt;\">adicionar otras imágenes a la lista existente, para ser procesadas.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.3. Abrir proyecto. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_open_project_dlx.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite </span><span style=\" font-family:\'Sans\'; font-size:10pt;\">abrir un proyectode DocLux con formato .dlx guardado en un directorio.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.4. Guardar actual. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite guardar la imagen actual en cualquiera de los formatos jpg, jpeg, png, tiff</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.5. Guardar todas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_all_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite guardar todas las imágenes cargadas al sistema en cualquiera de los formatos jpg, jpeg, png, tiff</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.6. Exportar actual. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_one_pdf.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite exporta la imagen actual en formato pdf</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.7. Exportar todas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_all_pdf.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite exportar todas las imágenes formato pdf</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.8. Guardar proyecto. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_project.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite </span><span style=\" font-family:\'Sans\'; font-size:10pt;\">guardar un proyecto de DocLux con formato .dlx guardado en un directorio.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.9. Minimizar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_minimizar.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite minimizar la aplicación.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.10. Salir.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_exit.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta opción permite cerrar/salir la aplicación.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">2</span><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">. Editar.</span><span style=\" font-family:\'Sans\'; font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Este menú permite </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Deshacer</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> y </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Rehacer</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> la/s acciones realizadas a la imagen actual que se muestra en el área de trabajo. Además, permite </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Eliminar</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"> la imagen actual seleccionada en el área de trabajo.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/09_menu_editar.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">2.1. Deshacer. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_deshacer.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite volver al estado anterior en que se encontraba la imagen antes de aplicarle un determinado filtro.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">2.2. Rehacer. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rehacer.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite devolver al estado que había adquirido la imagen anteriormente.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">2.3. Eliminar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_delete_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite eliminar la imagen actual.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">3</span><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">. Herramientas.</span><span style=\" font-family:\'Sans\'; font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Este menú permite </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Limpiar </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">área de intercambio</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">que permite gestionar el directorio donde se desea guardar el archivo raíz del DocLux.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">3.1. Limpiar </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">área de intercambio</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/010_menu_herramientas.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción muestra una lista con cada una de las modificaciones que ha sufrido la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">. Plugins.</span><span style=\" font-family:\'Sans\'; font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Este menú contiene cada uno de los plugins/filtros que brinda el sistema para aplicarle a la/s imágenes que se carguen para ser procesadas. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/011_menu_plugins.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.1. Balancear colores. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_balancear_color.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede balancear los colores de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.2. Brillo.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_brillo.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar el brillo de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.3. Contraste.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_contraste.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar el contraste de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.4. Escala de grises.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_grises.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción convierte a escala de grises (blanco y negro) la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4.5. Invertir imagen.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_rotate_hrzt_vert.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta herramienta puede invertir la imagen actual de derecha a izquierda o de arriba a abajo.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4.6. Limpiar imagen OpenCV.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_01.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4.7. Limpiar imagen PIL.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_02.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4.8. Limpiar imagen SciPy.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_03.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.9. Modificar colores.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_modificar_color.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar los colores, dígase rojo, verde y azul de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.10. OCR Tesseract.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_ocr_tesseract.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Realiza la transcripción del texto de la imagen actual.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.11. Rotar a la derecha.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rotate-right.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta permite rotar la imagen 90</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; vertical-align:super;\">0 </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">a la derecha, es decir, en el sentido de las manecillas del reloj.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.12. Rotar a la izquierda.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rotate-left.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta permite rotar la imagen 90</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; vertical-align:super;\">0 </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">a la izquierda, es decir, en el sentido contrario de las manecillas del reloj.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.13. Zoom In. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_zoom-in.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta herramienta permite aumentar el tamaño de la imagen actual que se muestra en el área de Imagen Procesada. Permite acercar la imagen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4.14. Zoom Out.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_zoom-out.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta herramienta permite disminuir el tamaño de la imagen actual que se muestra en el área de Imagen Procesada. Permite alejar la imagen.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">5</span><span style=\" font-family:\'Sans\'; font-size:12pt; font-weight:600;\">. Ayuda.</span><span style=\" font-family:\'Sans\'; font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Este menú contiene la opción </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Acerca de</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> que brinda información relevante acerca del sistema DocLux; así como la opción </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">Ayuda DocLux</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> que permite acceder a la ayuda del sistema, donde se explica como trabajar con el mismo.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/012_menu_ayuda.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">5</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.1. Acerca de.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_acerca_de.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción muestra datos importante acerca del sistema DocLux, del equipo de desarrollo y la licencia bajo la cual se comercializa dicho sistema.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">5.2. Ayuda DocLux.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_help.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción muestra la ayuda del sistema, es decir, explica el ambiente gráfico de la aplicación, así como cada una de las partes del sistema y cómo trabajar con ellas.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("dlg_acerca_de", "Menú", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_3.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">   </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">BARRA DE HERRAMIENTAS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/03_bh_plugins.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">La Barra de herramientas contiene cada uno de los filtros y herramientas que se le pueden aplicar a las imagenes.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.1. Nuevas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_nuevas_imgs.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta opción permite cargas nuevas imágenes al sistema para ser procesadas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1.2. Adicionar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_adicionar_imgs.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite </span><span style=\" font-family:\'Sans\'; font-size:10pt;\">adicionar otras imágenes a la lista existente, para ser procesadas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">3</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. Balancear colores. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_balancear_color.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede balancear los colores de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. Brillo.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_brillo.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar el brillo de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">5</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. Contraste.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_contraste.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar el contraste de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">6</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. Escala de grises.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_grises.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción convierte a escala de grises (blanco y negro) la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">7. Invertir imagen.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_rotate_hrzt_vert.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta herramienta puede invertir la imagen actual de derecha a izquierda o de arriba a abajo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">8. Limpiar imagen OpenCV.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_01.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">9. Limpiar imagen PIL.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_02.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">10. Limpiar imagen SciPy.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_clean_bg_03.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta binariza la imagen actual que se muestra en el área de Imagen Procesada, es decir, limpia la imagen a blanco y negro.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1. Modificar colores.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_modificar_color.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Con esta opción puede modificar los colores, dígase rojo, verde y azul de la imagen actual que se muestra en el área de Imagen Procesada.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">2. OCR Tesseract.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/plg_ocr_tesseract.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Realiza la transcripción de la imagen actual.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">3. Rotar a la derecha.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rotate-right.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta permite rotar la imagen 90</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; vertical-align:super;\">0 </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">a la derecha, es decir, en el sentido de las manecillas del reloj.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">4. Rotar a la izquierda.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rotate-left.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta herramienta permite rotar la imagen 90</span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; vertical-align:super;\">0 </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">a la izquierda, es decir, en el sentido contrario de las manecillas del reloj.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">5. Zoom In. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_zoom-in.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta herramienta permite aumentar el tamaño de la imagen actual que se muestra en el área de Imagen Procesada. Permite acercar la imagen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">6. Zoom Out.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_zoom-out.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta herramienta permite disminuir el tamaño de la imagen actual que se muestra en el área de Imagen Procesada. Permite alejar la imagen.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">7. Minimizar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_minimizar.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite minimizar la aplicación.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">8. Salir.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_exit.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Esta opción permite cerrar/salir la aplicación.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("dlg_acerca_de", "Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_4.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">ÁREA DE TRABAJO</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/04_visor_area_de_trabajo.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">La Barra de herramientas contiene cada una de las opciones que posibilita el sistema DocLux.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Área de trabajo:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">En esta área se muestra la imagen actual de las imágenes cargadas al sistema.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">2</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; color:#000000;\">Aplicar a todas: </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/chekbox_aplicar_todas.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Opción situada en la parte derecha inferior del área de trabajo, permite si está marcada que las transformaciones que sufra la imagen actual se le aplican a todas las cargadas al sistema, por el contrario de no estar marcada, los cambios sólo se aplican a la imagen actual.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("dlg_acerca_de", "Trabajo", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_5.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">IMÁGENES CARGADAS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/05_visor_imagenes_cargadas.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explica la opción.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Imágenes cargadas</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta área muestra en miniaturas cada una de las imágenes cargadas en el sistema, permitiendo seleccionar cuál de ellas se desea procesar y ser mostrada en el área de trabajo.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("dlg_acerca_de", "Imágenes cargadas", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_7.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">LISTA DE COMANDOS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/06_visor_lista_de_comandos.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">1</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Lista de comandos</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta área muestra imágenes en miniaturas de cada una de las transformaciones que sufre la imagen actual que se muestra en el área de trabajo.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">2. Botón Aplicar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_aplicar_(lista_comando).png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Este botón permite una vez seleccionada la imagen en miniatura deseada permite actualizar la imagen que se muestra en el área de trabajo con la transformación seleccionada y elemina las restantes transformaciones en la lista de comandos.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("dlg_acerca_de", "Lista de comandos", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_6.setHtml(QtGui.QApplication.translate("dlg_acerca_de", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">BARRA DE HERRAMIENTAS INFERIOR</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/07_bh_inferior.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">A continuación se explican cada una de las opciones.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">1. Eliminar. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_delete_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite eliminar la imagen actual.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">2</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. Eliminar todas.</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_delete_all_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite eliminar todas las imagenes cargadas al sistema.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">2</span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600;\">. </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Deshacer. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_deshacer.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite volver al estado anterior en que se encontraba la imagen antes de aplicarle un determinado filtro.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">3. Rehacer. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_rehacer.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite devolver estado que había adquirido la imagen anteriormente.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">4. Guardar actual. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite guardar la imagen actual en cualquiera de los formatos jpg, jpeg, png, tiff</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">5. Guardar todas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_all_img.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite guardar todas las imágenes cargadas al sistema en cualquiera de los formatos jpg, jpeg, png, tiff</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">6. Exportar actual. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_one_pdf.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite exporta la imagen actual en formato pdf</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">7. Exportar todas. </span><img src=\":/ayuda/recursos/imagenes/ayuda_rcs/btn_save_all_pdf.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Esta opción permite exportar todas las imágenes formato pdf</span><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("dlg_acerca_de", "Herramientas inferior", None, QtGui.QApplication.UnicodeUTF8))

import recursos_rc
