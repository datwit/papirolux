# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargando.ui'
#
# Created: Thu Jan 30 10:52:51 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Cargando(object):
    def setupUi(self, Cargando):
        Cargando.setObjectName(_fromUtf8("Cargando"))
        Cargando.resize(224, 68)
        self.gridLayout = QtGui.QGridLayout(Cargando)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(Cargando)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lb_busy = QtGui.QLabel(Cargando)
        self.lb_busy.setStyleSheet(_fromUtf8("image: url(:/imgs/recursos/imagenes/cargando.gif);"))
        self.lb_busy.setObjectName(_fromUtf8("lb_busy"))
        self.horizontalLayout.addWidget(self.lb_busy)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Cargando)
        QtCore.QMetaObject.connectSlotsByName(Cargando)

    def retranslateUi(self, Cargando):
        self.label.setText(QtGui.QApplication.translate("Cargando", "Espere por favor...", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_busy.setText(QtGui.QApplication.translate("Cargando", "Aqui va el gif...", None, QtGui.QApplication.UnicodeUTF8))

import recursos_rc
