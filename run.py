from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

from main import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F1:
            self.day_payment.setFocus()
        elif event.key() == QtCore.Qt.Key_F2:
            self.ot_payment.setFocus()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_F5:
            self.reset_system()
        elif event.key() == QtCore.Qt.Key_F3:
            self.savePaymentData()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
