import sys
from PyQt5 import QtWidgets,QtGui

var = 'Esto es una prueba para probrar los labels'
name = 'PolygonEditor'

#Creating Window
def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    w.setWindowTitle(name)
    w.setGeometry(100,100,750,450)

    label1 = QtWidgets.QLabel(w)
    label2 = QtWidgets.QLabel(w)

    label1.setText(var)

    image = QtGui.QPixmap('image.png')
    label2.setPixmap(image)

    label1.move(10,10)
    label2.move(50,70)


    w.show()
    sys.exit(app.exec_())

window()
