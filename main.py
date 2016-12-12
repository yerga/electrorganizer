#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Electrorganizer

Organizer for electronic components written in PyQt5

author: Daniel Martin-Yerga (dyerga (at) gmail.com)
"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow
from ui_adddialog import Ui_addDialog
import connectDB


def initializeModel(model):
    model.setTable('components')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "Category")
    model.setHeaderData(3, Qt.Horizontal, "Description")
    model.setHeaderData(4, Qt.Horizontal, "Amount")
    model.setHeaderData(5, Qt.Horizontal, "Manufacturer")
    model.setHeaderData(6, Qt.Horizontal, "Man. ID")
    model.setHeaderData(7, Qt.Horizontal, "Supplier")
    model.setHeaderData(8, Qt.Horizontal, "Supp. ID")
    model.setHeaderData(9, Qt.Horizontal, "Price")
    model.setHeaderData(10, Qt.Horizontal, "Storage")
    model.setHeaderData(11, Qt.Horizontal, "Link")
    model.setHeaderData(12, Qt.Horizontal, "Datasheet")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, model):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(self.quit)
        self.addBtn.clicked.connect(self.showAddDialog)
        self.tableView.setModel(model)
        self.tableView.clicked.connect(self.findrow)
        self.tableView.hideColumn(0)
        self.tableView.setSortingEnabled(True)

        self.setWindowTitle("Electrorganizer")
        self.setWindowIcon(QIcon("icon.png"))

    def findrow(self, i):
        selectedrow = i.row()
        print ("selected row: ", selectedrow)

    def quit(self):
        app.quit()

    def showAddDialog(self):
        self.addDialog = AddDialog()
        self.addDialog.show()



class AddDialog(QMainWindow, Ui_addDialog):
    def __init__(self):
        super(AddDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Add electronic component")
        self.setWindowIcon(QIcon("icon.png"))
        self.buttonBox.accepted.connect(self.addcomponent)
        self.buttonBox.rejected.connect(self.destroy)

    def addcomponent(self):
        print ("adding component")
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if not connectDB.createDB():
         sys.exit(1)

    #button.clicked.connect(addrow)
    #btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))

    model = QSqlTableModel()
    selectedrow = -1
    initializeModel(model)

    window = MainWindow(model)
    window.show()
    sys.exit(app.exec_())

