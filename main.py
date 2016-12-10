#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Electrorganizer

Organizer for electronic components written in PyQt5

author: Daniel Martin-Yerga (dyerga (at) gmail.com)
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(self.quit)
        #self.addbtn.clicked.connect(self.addbtn_clicked)

    def quit(self):
        app.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

