# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import interprete

def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Lanas')
    win = interprete.Ventana()
    win.show()
    win.raise_()
    sys.exit(app.exec_())
