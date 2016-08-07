import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.setWindowTitle('Hello PyQt!')
w.show()
return_code = app.exec_()
sys.exit(return_code)
