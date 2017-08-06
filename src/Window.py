import sys
from PyQt5 import QtWidgets, QtGui

import Test

from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

name = 'PolygonEditor'

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.setWindowTitle(name)
        self.setGeometry(100,100,750,450)

        self.createActions()
        self.createButtons()
        self.createMenus()
        self.createLabels()
        self.createLayouts()


    def createActions(self):

        self.openAct = QAction('Open',self)
        self.saveAct = QAction('Save',self)
        self.saveAsAct = QAction('Save As',self)
        self.quitAct = QAction('Quit',self)

        self.RedoAct = QAction('Redo',self)
        self.UndoAct = QAction('Undo',self)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addAction(self.quitAct)

        self.editMenu = self.menuBar().addMenu('Edit')
        self.editMenu.addAction(self.RedoAct)
        self.editMenu.addAction(self.UndoAct)

    def createLabels(self):
        self.label1 = QLabel()
        self.label1.setText('Hello World')
        self.label1.move(10,10)

    def createButtons(self):
        self.button1 = QPushButton()
        self.button1.setText('Hello its Me')

    def createLayouts(self):
        self.hBox = QHBoxLayout()
        self.hBox.addStretch()
        self.hBox.addWidget(self.label1)
        self.hBox.addStretch()


        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.button1)
        self.vBox.addLayout(self.hBox)

        self.widget.setLayout(self.vBox)



app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
