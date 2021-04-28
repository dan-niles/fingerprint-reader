# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
from glob import _ishidden

import mysql
import mysql.connector
from mysql.connector import Error

import serial

from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtWidgets import QComboBox

from functools import partial
from datetime import date
import easygui

from zk import ZK
import os
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("USER LOGIN")
        MainWindow.resize(450, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")
        Form.setStyleSheet("*{\n"
                           " font-family:Verdana, Geneva, sans-serif;\n"
                           "font-size:24px;\n"
                           "}\n"
                           "QFrame{\n"
                           "background:#333;\n"
                           "border-radius:15px;\n"
                           "}\n"
                           "#Form{\n"
                           "background:url(:images/bg5.jfif)\n"
                           "}\n"
                           "QPushButton{\n"
                           "\n"
                           "background:green;\n"
                           "border-radius:60px;\n"
                           "}\n"
                           "QToolButton{\n"
                           "\n"
                           "background:green;\n"
                           "border-radius:60px;\n"
                           "}\n"
                           "\n"
                           "QLabel{\n"
                           "color:white;\n"
                           "}\n"
                           "\n"
                           "QPushButton{\n"
                           "color:white;\n"
                           "border-radius:15px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "color:#333;\n"
                           "border-radius:15px;\n"
                           "background:#49ebff;\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "color:#717072;\n"
                           "border:none;\n"
                           "background:transparent;\n"
                           "border-bottom: 1px solid #717072;\n"
                           "}\n"
                           "\n"
                           "")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 60, 321, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 70, 181, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 301, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.login_system)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 291, 51))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(160, 0, 121, 121))
        self.toolButton.setText("")
        self.toolButton.setIcon(QtGui.QIcon())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName("toolButton")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(60, 390, 321, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 291, 61))
        self.label_2.setObjectName("label_2")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOGIN HERE"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Password"))
        self.label_2.setText(_translate("Form", "Astron Limited"))

        QtCore.QMetaObject.connectSlotsByName(Form)

        MainWindow.setCentralWidget(Form)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connection_data2(self):
        con = mysql.connector.connect(host='localhost', port='3306', database='electronics', user='root',
                                      charset='utf8', password='')
        return con

    def login_system(self):
        password = self.lineEdit.text()
        try:
            connection = self.connection_data2()
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM login where login.Password = '" + password + "'")
            rows = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count > 0:
                self.select_home()
            else:
                print("no data")
                # self.close()
            # print('Total Row(s):', cursor.rowcount)
            # for row in rows:
            #    print(row)

        except Error as e:
            print(e)

        finally:
            cursor.close()
            connection.close()

    def select_home(self):
        MainWindow.setObjectName("Home Window")
        MainWindow.resize(600, 570)
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        Form = QtWidgets.QWidget()
        Form.setObjectName("Form")

        Form.setObjectName("Form")
        Form.resize(600, 520)
        Form.setStyleSheet("*{\n"
                           " font-family:Verdana, Geneva, sans-serif;\n"
                           "font-size:24px;font-weight:bold\n"
                           "}\n"
                           "QFrame{\n"
                           "background:#333;\n"
                           "border-radius:15px;\n"
                           "}\n"
                           "#Form{\n"
                           "background:url(:images/bg5.jfif)\n"
                           "}\n"
                           "QPushButton{\n"
                           "\n"
                           "background:green;\n"
                           "border-radius:60px;\n"
                           "}\n"
                           "QToolButton{\n"
                           "\n"
                           "background:green;\n"
                           "border-radius:60px;\n"
                           "}\n"
                           "\n"
                           "QLabel{\n"
                           "color:white;\n"
                           "}\n"
                           "\n"
                           "QPushButton{\n"
                           "color:white;\n"
                           "border-radius:15px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "color:#333;\n"
                           "border-radius:15px;\n"
                           "background:#49ebff;\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "color:#717072;\n"
                           "border:none;\n"
                           "background:transparent;\n"
                           "border-bottom: 1px solid #717072;\n"
                           "}\n"
                           "\n"
                           "")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 580, 520))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 560, 90))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "\n"
                                      "background:red;\n"
                                      "border-radius:60px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton{\n"
                                      "color:white;\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "color:red;\n"
                                      "border-radius:15px;\n"
                                      "background:#49ebff;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_system)

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "LOGOUT"))
        #self.pushButton_2.setText(_translate("Form", "Paddy Weighing Process"))
        #self.pushButton_3.setText(_translate("Form", "RICE DISPATCH"))
        #self.pushButton_4.setText(_translate("Form", "Warehouse to Production"))
        #self.pushButton_5.setText(_translate("Form", "OTHER ITEM DISPATCH"))
        #self.label.setText(_translate("Form", "R.M.S WEIGHING PROCESS - HOME"))
        QtCore.QMetaObject.connectSlotsByName(Form)

        MainWindow.setCentralWidget(Form)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def back_home(self):
        self.system_home()

    def close_system(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.pushButton.setText(_translate("MainWindow", "ADD NEW"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.login_system()
    MainWindow.show()

    sys.exit(app.exec_())
