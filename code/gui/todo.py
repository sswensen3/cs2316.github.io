#!/usr/bin/env python3

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Todo List")

        self.list_view = QtGui.QListView()
        self.list_model = QtGui.QStandardItemModel(self.list_view)
        self.list_view.setModel(self.list_model)
        self.line_edit = QtGui.QLineEdit()
        self.add_button = QtGui.QPushButton("Add")
        self.add_button.setEnabled(False)

        self.add_button.clicked.connect(self.add_todo_item)
        self.line_edit.textChanged.connect(self.enable_add_button)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.list_view)
        self.vbox.addWidget(self.line_edit)
        self.vbox.addWidget(self.add_button)
        self.setLayout(self.vbox)

    def add_todo_item(self):
        list_item = QtGui.QStandardItem(self.line_edit.text())
        self.list_model.appendRow(list_item)
        self.line_edit.setText('')

    def enable_add_button(self):
        if len(self.line_edit.text()) == 0:
            self.add_button.setEnabled(False)
        else:
            self.add_button.setEnabled(True)

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
