# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categorymanager.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CategoryManager(object):
    def setupUi(self, CategoryManager):
        CategoryManager.setObjectName("CategoryManager")
        CategoryManager.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(CategoryManager)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.categoryView = QtWidgets.QListView(self.centralwidget)
        self.categoryView.setObjectName("categoryView")
        self.verticalLayout.addWidget(self.categoryView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addCatBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addCatBtn.setObjectName("addCatBtn")
        self.horizontalLayout.addWidget(self.addCatBtn)
        self.editCatBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editCatBtn.setObjectName("editCatBtn")
        self.horizontalLayout.addWidget(self.editCatBtn)
        self.removeCatBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeCatBtn.setObjectName("removeCatBtn")
        self.horizontalLayout.addWidget(self.removeCatBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        CategoryManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(CategoryManager)
        QtCore.QMetaObject.connectSlotsByName(CategoryManager)

    def retranslateUi(self, CategoryManager):
        _translate = QtCore.QCoreApplication.translate
        CategoryManager.setWindowTitle(_translate("CategoryManager", "MainWindow"))
        self.addCatBtn.setText(_translate("CategoryManager", "Add"))
        self.editCatBtn.setText(_translate("CategoryManager", "Edit"))
        self.removeCatBtn.setText(_translate("CategoryManager", "Remove"))

