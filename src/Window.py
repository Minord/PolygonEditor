import sys
from PyQt5 import QtWidgets

var = 'Hola'
nombre = 'PolygonEditor'

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.show()
    sys.exit(app.exec_())

window()
