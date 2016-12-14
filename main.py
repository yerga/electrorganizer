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
from PyQt5.QtCore import Qt, QSettings
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
        self.removeBtn.clicked.connect(self.removeRow)
        self.tableView.hideColumn(0)
        self.tableView.setSortingEnabled(True)
        self.setWindowTitle("Electrorganizer")
        self.setWindowIcon(QIcon("icon.png"))

        self.settings = QSettings("yerga", "Electrorganizer")
        self.categories = self.loadSettings()
        print ("categories-load: ", self.categories)
        if not self.categories:
            self.categories = ['All']
        print ("categories-not: ", self.categories)

        self.categoryBox.addItems(self.categories)
        self.categoryBox.currentIndexChanged.connect(self.filterByCat)

    def findrow(self, i):
        selectedrow = i.row()
        print ("selected row: ", selectedrow)

    def quit(self):
        app.quit()

    def showAddDialog(self):
        self.addDialog = AddDialog(self)
        self.addDialog.show()

    def removeRow(self):
        model.removeRow(self.tableView.currentIndex().row())
        print model.submitAll()

    def loadSettings(self):
        cats = self.settings.value("categories", None)
        print cats
        return cats

    def writeSettings(self):
        self.settings.setValue("categories", self.categories)

    def updateCategoryBox(self, category):
        self.categoryBox.addItem(category)

    def filterByCat(self):
        catselected = self.categoryBox.currentText()
        if catselected == "All":
            model.setFilter("")
            model.select()
        else:
            #print ("catsleected: ", catselected)
            model.setFilter("category = '%s'" % catselected)
            model.select()


class AddDialog(QMainWindow, Ui_addDialog):
    def __init__(self, mainwindow):
        super(AddDialog, self).__init__()
        self.mainwindow = mainwindow
        self.setupUi(self)
        self.setWindowTitle("Add electronic component")
        self.setWindowIcon(QIcon("icon.png"))
        self.buttonBox.accepted.connect(self.addcomponent)
        self.buttonBox.rejected.connect(self.destroy)

    def addcomponent(self):
        print ("adding component")

        name = self.nameEdit.text()
        category = self.catEdit.text()
        description = self.descEdit.text()
        amounttext = self.amountEdit.text()
        if amounttext:
            amount = int(amounttext)
        else:
            amount = 0
        manufacturer = self.manEdit.text()
        manid = self.manidEdit.text()
        supplier = self.supEdit.text()
        supid = self.supidEdit.text()
        pricetext = self.priceEdit.text()
        if pricetext:
            price = int(pricetext)
        else:
            price = 0
        storage = self.storageEdit.text()
        link = self.linkEdit.text()
        datasheet = self.dataEdit.text()

        rowcount = model.rowCount()
        print ("rowcount: "+str(rowcount))

        model.insertRows(rowcount, 1)

        ids = []
        for i in range(0, rowcount):
            ids += [int(model.data(model.index(i, 0)))]

        model.setData(model.index(rowcount, 0), max(ids)+1)
        model.setData(model.index(rowcount, 1), name)
        model.setData(model.index(rowcount, 2), category)

        print ("categ: ", self.mainwindow.categories)
        self.mainwindow.categories += [category]
        print ("2categ: ", self.mainwindow.categories)
        model.setData(model.index(rowcount, 3), description)
        model.setData(model.index(rowcount, 4), amount)
        model.setData(model.index(rowcount, 5), manufacturer)
        model.setData(model.index(rowcount, 6), manid)
        model.setData(model.index(rowcount, 7), supplier)
        model.setData(model.index(rowcount, 8), supid)
        model.setData(model.index(rowcount, 9), price)
        model.setData(model.index(rowcount, 10), storage)
        model.setData(model.index(rowcount, 11), link)
        model.setData(model.index(rowcount, 12), datasheet)

        if model.submitAll():
            print "data correctly added to database"
            self.mainwindow.writeSettings()
            self.mainwindow.updateCategoryBox(category)
        else:
            print "error adding data to database"
            print model.lastError().driverText()
            print model.lastError().databaseText()

        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if not connectDB.createDB():
         sys.exit(1)

    model = QSqlTableModel()
    selectedrow = -1
    initializeModel(model)

    window = MainWindow(model)
    window.show()
    sys.exit(app.exec_())
