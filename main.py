from PyQt4 import QtGui, QtCore, Qt
import sys

def plot():
    print ("Hello you!")

def main():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    button = QtGui.QPushButton("Hello, PyQt!")

    button.connect(button, Qt.SIGNAL("clicked()"), plot)

    window.setCentralWidget(button)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()