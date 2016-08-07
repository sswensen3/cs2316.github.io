#!/usr/bin/env python3

import sys
from PyQt4 import QtGui

def up():
    print("up!")

app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
w.setWindowTitle('Hello PyQt!')
btn = QtGui.QPushButton('Push it ...', w)
btn.clicked.connect(lambda: print('real good!'))
btn.clicked.connect(up)
w.show()
sys.exit(app.exec_())
