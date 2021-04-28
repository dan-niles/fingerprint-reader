# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(232, 157)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setGeometry(QtCore.QRect(30, 120, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Settings)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.ip_address = QtWidgets.QLineEdit(self.groupBox)
        self.ip_address.setGeometry(QtCore.QRect(90, 10, 111, 31))
        self.ip_address.setText("172.21.0.8")
        self.ip_address.setObjectName("ip_address")
        self.port = QtWidgets.QLineEdit(self.groupBox)
        self.port.setGeometry(QtCore.QRect(90, 50, 71, 31))
        self.port.setText("4370")
        self.port.setObjectName("port")

        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept)
        self.buttonBox.rejected.connect(Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.label.setText(_translate("Settings", "IP Address"))
        self.label_2.setText(_translate("Settings", "Port"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
