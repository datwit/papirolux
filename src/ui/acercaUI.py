#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog

from ui.acerca_de import Ui_dlg_acerca_de

class AcercaDe(QDialog, Ui_dlg_acerca_de):
    def __init__(self, parent = None):
        super(AcercaDe, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Acerca de DocLux')

        self.setWindowModality(Qt.ApplicationModal)
