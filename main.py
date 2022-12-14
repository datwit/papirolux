#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# import PyQt4 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
import os

appName = "papirolux"
appVersion = "0.4a"

from src.ui.principalUI import VentanaPrincipal

def quit(self):
    self.commTerminate()
    QApplication.quit()

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName(appName)

    # preparar el area de intercambio (debe ser configurable)
    swap_dir = QDir.toNativeSeparators(os.path.join(QDir.homePath(), appName, 'swap'))
    swap = QDir()
    swap.mkpath(swap_dir)

    # create widget
    w = VentanaPrincipal(str(swap_dir))
    w.setWindowTitle(appName + ' - ' + appVersion)
    w.show()

    # connection
    app.quit()

    # execute application
    sys.exit(app.exec_())
