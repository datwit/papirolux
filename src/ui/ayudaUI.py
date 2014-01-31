#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.ayuda import Ui_dlg_acerca_de

class Ayuda(QDialog, Ui_dlg_acerca_de):
    def __init__(self, parent = None):
        super(Ayuda, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Ayuda de DocLux')

        self.setWindowModality(Qt.ApplicationModal)
