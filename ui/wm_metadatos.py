# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wm_metadatos.ui'
#
# Created: Thu May 15 10:55:38 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(462, 473)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ayuda/recursos/imagenes/ayuda_rcs/icon_doclux.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.btn_Guardar = QtGui.QPushButton(Dialog)
        self.btn_Guardar.setGeometry(QtCore.QRect(190, 430, 96, 24))
        self.btn_Guardar.setObjectName(_fromUtf8("btn_Guardar"))
        self.InfoMetaDatos = QtGui.QLabel(Dialog)
        self.InfoMetaDatos.setGeometry(QtCore.QRect(70, 0, 341, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoMetaDatos.sizePolicy().hasHeightForWidth())
        self.InfoMetaDatos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InfoMetaDatos.setFont(font)
        self.InfoMetaDatos.setObjectName(_fromUtf8("InfoMetaDatos"))
        self.label_CodigoAH = QtGui.QLabel(Dialog)
        self.label_CodigoAH.setGeometry(QtCore.QRect(20, 40, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_CodigoAH.setFont(font)
        self.label_CodigoAH.setObjectName(_fromUtf8("label_CodigoAH"))
        self.label_NombreAH = QtGui.QLabel(Dialog)
        self.label_NombreAH.setGeometry(QtCore.QRect(20, 80, 190, 20))
        self.label_NombreAH.setObjectName(_fromUtf8("label_NombreAH"))
        self.label_SiglasAH = QtGui.QLabel(Dialog)
        self.label_SiglasAH.setGeometry(QtCore.QRect(20, 120, 180, 20))
        self.label_SiglasAH.setObjectName(_fromUtf8("label_SiglasAH"))
        self.lineEdit_CodigoAH = QtGui.QLineEdit(Dialog)
        self.lineEdit_CodigoAH.setGeometry(QtCore.QRect(210, 40, 240, 24))
        self.lineEdit_CodigoAH.setObjectName(_fromUtf8("lineEdit_CodigoAH"))
        self.label_PasswordMaster = QtGui.QLabel(Dialog)
        self.label_PasswordMaster.setGeometry(QtCore.QRect(20, 160, 130, 20))
        self.label_PasswordMaster.setObjectName(_fromUtf8("label_PasswordMaster"))
        self.lineEdit_NombreAH = QtGui.QLineEdit(Dialog)
        self.lineEdit_NombreAH.setGeometry(QtCore.QRect(210, 80, 240, 24))
        self.lineEdit_NombreAH.setObjectName(_fromUtf8("lineEdit_NombreAH"))
        self.lineEdit_Siglas_AH = QtGui.QLineEdit(Dialog)
        self.lineEdit_Siglas_AH.setGeometry(QtCore.QRect(210, 120, 240, 24))
        self.lineEdit_Siglas_AH.setObjectName(_fromUtf8("lineEdit_Siglas_AH"))
        self.lineEdit_PasswdMaster = QtGui.QLineEdit(Dialog)
        self.lineEdit_PasswdMaster.setGeometry(QtCore.QRect(210, 160, 240, 24))
        self.lineEdit_PasswdMaster.setInputMethodHints(QtCore.Qt.ImhExclusiveInputMask)
        self.lineEdit_PasswdMaster.setObjectName(_fromUtf8("lineEdit_PasswdMaster"))
        self.btn_QR = QtGui.QPushButton(Dialog)
        self.btn_QR.setGeometry(QtCore.QRect(45, 430, 131, 24))
        self.btn_QR.setObjectName(_fromUtf8("btn_QR"))
        self.btn_Cerrar = QtGui.QPushButton(Dialog)
        self.btn_Cerrar.setGeometry(QtCore.QRect(300, 430, 96, 24))
        self.btn_Cerrar.setObjectName(_fromUtf8("btn_Cerrar"))
        self.label_CodigoQR = QtGui.QLabel(Dialog)
        self.label_CodigoQR.setGeometry(QtCore.QRect(160, 230, 160, 160))
        self.label_CodigoQR.setFrameShape(QtGui.QFrame.Box)
        self.label_CodigoQR.setLineWidth(1)
        self.label_CodigoQR.setMidLineWidth(0)
        self.label_CodigoQR.setText(_fromUtf8(""))
        self.label_CodigoQR.setObjectName(_fromUtf8("label_CodigoQR"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 210, 70, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_1 = QtGui.QFrame(Dialog)
        self.line_1.setGeometry(QtCore.QRect(20, 190, 431, 20))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 400, 431, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Guardar.setText(QtGui.QApplication.translate("Dialog", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoMetaDatos.setText(QtGui.QApplication.translate("Dialog", "Metadatos para Marca de Agua (DocLux 3)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_CodigoAH.setText(QtGui.QApplication.translate("Dialog", "Código del Archivo Histórico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_NombreAH.setText(QtGui.QApplication.translate("Dialog", "Nombre del Archivo Histórico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SiglasAH.setText(QtGui.QApplication.translate("Dialog", "Siglas del Archivo Histórico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_PasswordMaster.setText(QtGui.QApplication.translate("Dialog", "Contraseña Master:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_QR.setText(QtGui.QApplication.translate("Dialog", "Generar Código QR", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Cerrar.setText(QtGui.QApplication.translate("Dialog", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Código QR", None, QtGui.QApplication.UnicodeUTF8))

import recursos_rc
