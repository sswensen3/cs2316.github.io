import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
w.setWindowTitle('Hello PyQt!')
lbl = QtGui.QLabel('Hello, label!', w)
w.show()
sys.exit(app.exec_())
