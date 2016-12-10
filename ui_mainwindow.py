# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 320, 801, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.categoryBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.categoryBox.setMinimumSize(QtCore.QSize(250, 40))
        self.categoryBox.setObjectName("categoryBox")
        self.horizontalLayout.addWidget(self.categoryBox)
        self.filterEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.filterEdit.setMinimumSize(QtCore.QSize(250, 40))
        self.filterEdit.setObjectName("filterEdit")
        self.horizontalLayout.addWidget(self.filterEdit)
        self.addBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.editBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout.addWidget(self.editBtn)
        self.removeBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeBtn.setMinimumSize(QtCore.QSize(0, 40))
        self.removeBtn.setObjectName("removeBtn")
        self.horizontalLayout.addWidget(self.removeBtn)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuExit.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuExit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.editBtn.setText(_translate("MainWindow", "Edit"))
        self.removeBtn.setText(_translate("MainWindow", "Remove"))
        self.menuExit.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About Electrorganizer"))

