#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

appName = "DocLux"
appVersion = "3.0"

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName(appName)

    # preparar el area de intercambio (debe ser configurable)
    swap_dir = QDir.toNativeSeparators(QDir.homePath() + '/.' + appName + '/swap')
    swap = QDir()
    swap.mkpath(swap_dir)

    # importar la ventana principal, es necesario el import aqui despues de
    # creada la QApplicarion
    from src.ui.principalUI import VentanaPrincipal

    # create widget
    w = VentanaPrincipal(str(swap_dir))
    w.setWindowTitle(appName + ' - ' + appVersion)
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())
