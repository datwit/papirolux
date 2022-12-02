# Papirolux

Papirolux is a Qt-Application to execute a command or a set of command to an image or a collection of images. The objective is to get doing gray scale, brigh, contrast corrections a new image better to make Human Character Recognition.

Originally was designed to parse old documents from 1800.

## Features



# Acknowledgment

Based on original idea of DocLux created by the Historical Archive of "Manzanillo, Granma", Cuba in 2012.

# Important

Convert .qrc to .py
```bash
pyrcc5 resource.qrc -o resource.py
```

QLayout.setMargin(0) -> QLayout.setContentsMargins(0,0,0,0)
https://doc.qt.io/qt-5/qlayout-obsolete.html

QHBoxLayout, QFrame, QSplitter, QGridLayout, QMessageBox, QInputDialog, QMainWindow, QApplication are now in QtWidgets
```python
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, QHBoxLayout, QSplitter
```

QPrinter is now part of QtPrintSupport
```python
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
```

QString now doesn't exist must be python str
```python
lab = QString('<b>%1</b> de <b>%2</b>').arg('0').arg('0')
```
Se transforma en:
```python
lab = '<b>{0}</b> de <b>{1}</b>'.format('0', '0')
```

For new Signals and Slot look here
https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html

https://wiki.qt.io/Transition_from_Qt_4.x_to_Qt5