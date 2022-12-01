# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comandos.ui'
#
# Created: Wed Oct  9 14:08:03 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Comandos(object):
    def setupUi(self, Comandos):
        Comandos.setObjectName(_fromUtf8("Comandos"))
        Comandos.resize(278, 455)
        Comandos.setMinimumSize(QtCore.QSize(278, 455))
        Comandos.setMaximumSize(QtCore.QSize(278, 455))
        self.gridLayout_2 = QtGui.QGridLayout(Comandos)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.vista_comandos = QtGui.QScrollArea(Comandos)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vista_comandos.sizePolicy().hasHeightForWidth())
        self.vista_comandos.setSizePolicy(sizePolicy)
        self.vista_comandos.setMinimumSize(QtCore.QSize(260, 400))
        self.vista_comandos.setMaximumSize(QtCore.QSize(260, 400))
        self.vista_comandos.setLineWidth(0)
        self.vista_comandos.setWidgetResizable(True)
        self.vista_comandos.setObjectName(_fromUtf8("vista_comandos"))
        self.main_layout = QtGui.QWidget()
        self.main_layout.setGeometry(QtCore.QRect(0, 0, 258, 398))
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.gridLayout = QtGui.QGridLayout(self.main_layout)
        self.gridLayout.setMargin(5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comandos_content = QtGui.QVBoxLayout()
        self.comandos_content.setSpacing(1)
        self.comandos_content.setMargin(1)
        self.comandos_content.setObjectName(_fromUtf8("comandos_content"))
        self.gridLayout.addLayout(self.comandos_content, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.vista_comandos.setWidget(self.main_layout)
        self.gridLayout_2.addWidget(self.vista_comandos, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.aplicar = QtGui.QPushButton(Comandos)
        self.aplicar.setObjectName(_fromUtf8("aplicar"))
        self.horizontalLayout.addWidget(self.aplicar)
        self.ignorar = QtGui.QPushButton(Comandos)
        self.ignorar.setObjectName(_fromUtf8("ignorar"))
        self.horizontalLayout.addWidget(self.ignorar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Comandos)
        QtCore.QObject.connect(self.ignorar, QtCore.SIGNAL(_fromUtf8("clicked()")), Comandos.close)
        QtCore.QMetaObject.connectSlotsByName(Comandos)

    def retranslateUi(self, Comandos):
        Comandos.setWindowTitle(QtGui.QApplication.translate("Comandos", "Comandos", None, QtGui.QApplication.UnicodeUTF8))
        self.aplicar.setText(QtGui.QApplication.translate("Comandos", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))
        self.ignorar.setText(QtGui.QApplication.translate("Comandos", "Ignorar", None, QtGui.QApplication.UnicodeUTF8))

