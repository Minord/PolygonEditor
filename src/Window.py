import sys
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QWidget, QMainWindow, QAction

var = 'Esto es una prueba para probrar los labels'
name = 'PolygonEditor'

#Tool Bar class
class MenuBar(QWidget):
    """ MenuBar."""
    def __init__(self):
        super(MenuBar, self).__init__()
        pass



#Creating Window
def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QMainWindow()

    w.setWindowTitle(name)
    w.setGeometry(100,100,750,450)

    label1 = QtWidgets.QLabel(w)
    label2 = QtWidgets.QLabel(w)

    label1.setText(var)

    image = QtGui.QPixmap('image.png')
    label2.setPixmap(image)

    label1.move(10,10)
    label2.move(50,70)

    bar = w.menuBar()
    file = bar.addMenu ('File')

    any_action = QAction('Any', w)
    file.addAction(any_action)

    file.triggered.connect(respond)

    w.show()
    sys.exit(app.exec_())

def respond(q):
    signal = q.text()
    if signal == 'Any':
        print ('Hola')
    pass

window()
