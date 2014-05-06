# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swapUI.ui'
#
# Created: Wed Mar 12 15:48:46 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(486, 184)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.dir_swap = QtGui.QPushButton(Form)
        self.dir_swap.setObjectName(_fromUtf8("dir_swap"))
        self.gridLayout.addWidget(self.dir_swap, 2, 4, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.aceptar = QtGui.QPushButton(Form)
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.horizontalLayout.addWidget(self.aceptar)
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.horizontalLayout.addWidget(self.cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 5)
        self.swap_actual = QtGui.QLabel(Form)
        self.swap_actual.setText(_fromUtf8(""))
        self.swap_actual.setObjectName(_fromUtf8("swap_actual"))
        self.gridLayout.addWidget(self.swap_actual, 1, 1, 1, 1)
        self.swap_actual_2 = QtGui.QLabel(Form)
        self.swap_actual_2.setText(_fromUtf8(""))
        self.swap_actual_2.setObjectName(_fromUtf8("swap_actual_2"))
        self.gridLayout.addWidget(self.swap_actual_2, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.nueva_swap = QtGui.QLineEdit(Form)
        self.nueva_swap.setObjectName(_fromUtf8("nueva_swap"))
        self.gridLayout.addWidget(self.nueva_swap, 2, 1, 1, 3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Directorio de la Swap DocLux", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Swap actual:", None, QtGui.QApplication.UnicodeUTF8))
        self.dir_swap.setToolTip(QtGui.QApplication.translate("Form", "Swap DocLux", None, QtGui.QApplication.UnicodeUTF8))
        self.dir_swap.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Seleccione el directorio en el cual se guardarán los archivos temporales.", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Form", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nueva swap:", None, QtGui.QApplication.UnicodeUTF8))

