import sys
from PyQt5 import QtWidgets, QtGui

import Test

from PyQt5.QtWidgets import QWidget, QMainWindow, QAction

name = 'PolygonEditor'

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle(name)
        self.setGeometry(100,100,750,450)

        self.createActions()
        self.createMenus()

    def createActions(self):

        self.openAct = QAction('Open',self)
        self.saveAct = QAction('Save',self)
        self.saveAsAct = QAction('Save As',self)
        self.quitAct = QAction('Quit',self)

        self.RedoAct = QAction('Redo',self)
        self.UndoAct = QAction('Redo',self)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addAction(self.quitAct)

        self.editMenu = self.menuBar().addMenu('Edit')
        self.editMenu.addAction(self.RedoAct)
        self.editMenu.addAction(self.UndoAct)
        pass


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
