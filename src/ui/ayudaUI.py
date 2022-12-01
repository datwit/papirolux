#!/usr/bin/python
# -*- coding: utf-8 -*-

# main core file
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from ui.ayuda import Ui_dlg_AyudaDocLux

class Ayuda(QDialog, Ui_dlg_AyudaDocLux):
    def __init__(self, parent = None):
        super(Ayuda, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Ayuda de DocLux')

        self.setWindowModality(Qt.ApplicationModal)
        self.showMaximized()
