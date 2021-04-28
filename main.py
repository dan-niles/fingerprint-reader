from zk import ZK
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

from datetime import datetime
from dialog import Ui_Dialog

import mysql.connector
app = QtWidgets.QApplication(sys.argv)

# Connect to db
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pyzk",
    )
    mycursor = db.cursor()
except:
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle('Error')
    msg.setText('Cannot connect to db')
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setStandardButtons(QtWidgets.QMessageBox.Cancel |
                           QtWidgets.QMessageBox.Ok)
    msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
    msg.exec_()
    exit()


# Selecting data from table in db and returning list
def main_select(sql):
    mycursor.execute(sql)
    list = []
    for x in mycursor:
        list.append(x)
    return list


# Adding/Updating/Deleting data to table in db
def main_query(sql, val):
    mycursor.execute(sql, val)
    db.commit()


class Worker(QtCore.QThread):
    sinout = QtCore.pyqtSignal(str)

    def __init__(self, conn, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0
        self.conn = conn

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        try:
            for attendance in self.conn.live_capture():
                if attendance is None:
                    pass
                else:
                    user_data = str(attendance).split()
                    # Transmitting signal
                    self.sinout.emit(user_data[1])
                    # Thread hibernates for 2 seconds
                    self.sleep(2)

        except Exception as e:
            print("Process terminate : {}".format(e))
        finally:
            if self.conn:
                self.conn.disconnect()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow.showFullScreen()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EmployeeData = QtWidgets.QGroupBox(self.centralwidget)
        self.EmployeeData.setGeometry(QtCore.QRect(10, 10, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EmployeeData.setFont(font)
        self.EmployeeData.setObjectName("EmployeeData")
        self.emp_name_label = QtWidgets.QLabel(self.EmployeeData)
        self.emp_name_label.setGeometry(QtCore.QRect(10, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_name_label.setFont(font)
        self.emp_name_label.setObjectName("emp_name_label")
        self.emp_no_label = QtWidgets.QLabel(self.EmployeeData)
        self.emp_no_label.setGeometry(QtCore.QRect(10, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_no_label.setFont(font)
        self.emp_no_label.setObjectName("emp_no_label")
        self.date_label = QtWidgets.QLabel(self.EmployeeData)
        self.date_label.setGeometry(QtCore.QRect(10, 91, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.emp_name = QtWidgets.QLabel(self.EmployeeData)
        self.emp_name.setGeometry(QtCore.QRect(90, 30, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_name.setFont(font)
        self.emp_name.setText("")
        self.emp_name.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_name.setObjectName("emp_name")
        self.emp_no = QtWidgets.QLabel(self.EmployeeData)
        self.emp_no.setGeometry(QtCore.QRect(90, 60, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_no.setFont(font)
        self.emp_no.setText("")
        self.emp_no.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_no.setObjectName("emp_no")
        self.date = QtWidgets.QLabel(self.EmployeeData)
        self.date.setGeometry(QtCore.QRect(90, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setText("")
        self.date.setAlignment(QtCore.Qt.AlignRight |
                               QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.date.setObjectName("date")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 140, 481, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 477, 217))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.data_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.data_table.setGeometry(QtCore.QRect(0, 0, 481, 221))
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(4)
        self.data_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.EmployeeData2 = QtWidgets.QGroupBox(self.centralwidget)
        self.EmployeeData2.setGeometry(QtCore.QRect(500, 20, 331, 411))
        self.EmployeeData2.setTitle("")
        self.EmployeeData2.setObjectName("EmployeeData2")
        self.emp_calling_name_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_calling_name_label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_calling_name_label.setFont(font)
        self.emp_calling_name_label.setObjectName("emp_calling_name_label")
        self.emp_surname_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_surname_label.setGeometry(QtCore.QRect(10, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_surname_label.setFont(font)
        self.emp_surname_label.setObjectName("emp_surname_label")
        self.emp_nic_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_nic_label.setGeometry(QtCore.QRect(10, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_nic_label.setFont(font)
        self.emp_nic_label.setObjectName("emp_nic_label")
        self.emp_gender_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_gender_label.setGeometry(QtCore.QRect(10, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_gender_label.setFont(font)
        self.emp_gender_label.setObjectName("emp_gender_label")
        self.emp_type_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_type_label.setGeometry(QtCore.QRect(10, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_type_label.setFont(font)
        self.emp_type_label.setObjectName("emp_type_label")
        self.emp_designation_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_designation_label.setGeometry(QtCore.QRect(10, 220, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_designation_label.setFont(font)
        self.emp_designation_label.setObjectName("emp_designation_label")
        self.emp_department_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_department_label.setGeometry(QtCore.QRect(10, 260, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_department_label.setFont(font)
        self.emp_department_label.setObjectName("emp_department_label")
        self.emp_section_label = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_section_label.setGeometry(QtCore.QRect(10, 300, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emp_section_label.setFont(font)
        self.emp_section_label.setObjectName("emp_section_label")
        self.emp_calling_name = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_calling_name.setGeometry(QtCore.QRect(110, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_calling_name.setFont(font)
        self.emp_calling_name.setStyleSheet("text-align: right")
        self.emp_calling_name.setText("")
        self.emp_calling_name.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_calling_name.setObjectName("emp_calling_name")
        self.emp_surname = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_surname.setGeometry(QtCore.QRect(110, 60, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_surname.setFont(font)
        self.emp_surname.setText("")
        self.emp_surname.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_surname.setObjectName("emp_surname")
        self.emp_nic = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_nic.setGeometry(QtCore.QRect(110, 100, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_nic.setFont(font)
        self.emp_nic.setText("")
        self.emp_nic.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_nic.setObjectName("emp_nic")
        self.emp_gender = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_gender.setGeometry(QtCore.QRect(110, 140, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_gender.setFont(font)
        self.emp_gender.setText("")
        self.emp_gender.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_gender.setObjectName("emp_gender")
        self.emp_type = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_type.setGeometry(QtCore.QRect(110, 180, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_type.setFont(font)
        self.emp_type.setText("")
        self.emp_type.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_type.setObjectName("emp_type")
        self.emp_designation = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_designation.setGeometry(QtCore.QRect(110, 220, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_designation.setFont(font)
        self.emp_designation.setText("")
        self.emp_designation.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_designation.setObjectName("emp_designation")
        self.emp_department = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_department.setGeometry(QtCore.QRect(110, 260, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_department.setFont(font)
        self.emp_department.setText("")
        self.emp_department.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_department.setObjectName("emp_department")
        self.emp_section = QtWidgets.QLabel(self.EmployeeData2)
        self.emp_section.setGeometry(QtCore.QRect(110, 300, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.emp_section.setFont(font)
        self.emp_section.setText("")
        self.emp_section.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.emp_section.setObjectName("emp_section")
        self.emp_pic_frame = QtWidgets.QFrame(self.centralwidget)
        self.emp_pic_frame.setGeometry(QtCore.QRect(350, 20, 141, 111))
        self.emp_pic_frame.setAutoFillBackground(False)
        self.emp_pic_frame.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.emp_pic_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_pic_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_pic_frame.setObjectName("emp_pic_frame")
        self.emp_pic = QtWidgets.QLabel(self.emp_pic_frame)
        self.emp_pic.setGeometry(QtCore.QRect(40, 10, 61, 81))
        self.emp_pic.setMaximumSize(QtCore.QSize(16777181, 16777215))
        self.emp_pic.setText("")
        self.emp_pic.setPixmap(QtGui.QPixmap("user.png"))
        self.emp_pic.setScaledContents(True)
        self.emp_pic.setObjectName("emp_pic")
        self.PaymentData = QtWidgets.QFrame(self.centralwidget)
        self.PaymentData.setGeometry(QtCore.QRect(10, 370, 481, 201))
        self.PaymentData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PaymentData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PaymentData.setObjectName("PaymentData")
        self.submitBtn = QtWidgets.QPushButton(self.PaymentData)
        self.submitBtn.setGeometry(QtCore.QRect(340, 160, 131, 31))
        self.submitBtn.setObjectName("submitBtn")
        self.total_value_label = QtWidgets.QLabel(self.PaymentData)
        self.total_value_label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_value_label.setFont(font)
        self.total_value_label.setObjectName("total_value_label")
        self.ot_payment = QtWidgets.QPlainTextEdit(self.PaymentData)
        self.ot_payment.setGeometry(QtCore.QRect(340, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ot_payment.setFont(font)
        self.ot_payment.setPlainText("")
        self.ot_payment.setObjectName("ot_payment")
        self.day_payment = QtWidgets.QPlainTextEdit(self.PaymentData)
        self.day_payment.setGeometry(QtCore.QRect(340, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.day_payment.setFont(font)
        self.day_payment.setPlainText("")
        self.day_payment.setObjectName("day_payment")
        self.day_payment_label = QtWidgets.QLabel(self.PaymentData)
        self.day_payment_label.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.day_payment_label.setFont(font)
        self.day_payment_label.setObjectName("day_payment_label")
        self.ot_payment_label = QtWidgets.QLabel(self.PaymentData)
        self.ot_payment_label.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ot_payment_label.setFont(font)
        self.ot_payment_label.setObjectName("ot_payment_label")
        self.total_value = QtWidgets.QLabel(self.PaymentData)
        self.total_value.setGeometry(QtCore.QRect(340, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.total_value.setFont(font)
        self.total_value.setText("")
        self.total_value.setObjectName("total_value")
        self.comments_label = QtWidgets.QLabel(self.PaymentData)
        self.comments_label.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comments_label.setFont(font)
        self.comments_label.setObjectName("comments_label")
        self.comments = QtWidgets.QPlainTextEdit(self.PaymentData)
        self.comments.setGeometry(QtCore.QRect(110, 120, 361, 31))
        self.comments.setObjectName("comments")
        self.ExtraButtons = QtWidgets.QFrame(self.centralwidget)
        self.ExtraButtons.setGeometry(QtCore.QRect(500, 440, 331, 51))
        self.ExtraButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ExtraButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ExtraButtons.setObjectName("ExtraButtons")
        self.exitBtn = QtWidgets.QPushButton(self.ExtraButtons)
        self.exitBtn.setGeometry(QtCore.QRect(230, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet("background-color : rgb(255, 0, 0);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "")
        self.exitBtn.setObjectName("exitBtn")
        self.resetBtn = QtWidgets.QPushButton(self.ExtraButtons)
        self.resetBtn.setGeometry(QtCore.QRect(130, 10, 91, 31))
        self.resetBtn.setObjectName("resetBtn")
        self.shortcut_box = QtWidgets.QGroupBox(self.centralwidget)
        self.shortcut_box.setGeometry(QtCore.QRect(110, 580, 611, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.shortcut_box.setFont(font)
        self.shortcut_box.setObjectName("shortcut_box")
        self.shortcut_1 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_1.setGeometry(QtCore.QRect(10, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_1.setFont(font)
        self.shortcut_1.setObjectName("shortcut_1")
        self.shortcut_2 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_2.setGeometry(QtCore.QRect(140, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_2.setFont(font)
        self.shortcut_2.setObjectName("shortcut_2")
        self.shortcut_3 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_3.setGeometry(QtCore.QRect(260, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_3.setFont(font)
        self.shortcut_3.setObjectName("shortcut_3")
        self.shortcut_4 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_4.setGeometry(QtCore.QRect(360, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_4.setFont(font)
        self.shortcut_4.setObjectName("shortcut_4")
        self.shortcut_5 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_5.setGeometry(QtCore.QRect(440, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_5.setFont(font)
        self.shortcut_5.setObjectName("shortcut_5")
        self.shortcut_6 = QtWidgets.QLabel(self.shortcut_box)
        self.shortcut_6.setGeometry(QtCore.QRect(530, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.shortcut_6.setFont(font)
        self.shortcut_6.setObjectName("shortcut_6")
        self.printBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printBtn.setGeometry(QtCore.QRect(500, 500, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.printBtn.setFont(font)
        self.printBtn.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                    "color: rgb(255, 255, 255);")
        self.printBtn.setObjectName("printBtn")
        self.ExtraButtons.raise_()
        self.PaymentData.raise_()
        self.EmployeeData.raise_()
        self.scrollArea.raise_()
        self.EmployeeData2.raise_()
        self.emp_pic_frame.raise_()
        self.shortcut_box.raise_()
        self.printBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.users = self.config_settings()

        self.resetBtn.clicked.connect(self.reset_system)
        self.exitBtn.clicked.connect(self.close_system)
        self.submitBtn.clicked.connect(self.savePaymentData)
        self.printBtn.clicked.connect(self.handlePreview)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EmployeeData.setTitle(_translate(
            "MainWindow", "Employee Details"))
        self.emp_name_label.setText(_translate("MainWindow", "Name"))
        self.emp_no_label.setText(_translate("MainWindow", "Emp. No"))
        self.date_label.setText(_translate("MainWindow", "Date"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reason"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Credit"))
        item = self.data_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Debit"))
        self.emp_calling_name_label.setText(
            _translate("MainWindow", "First Name"))
        self.emp_surname_label.setText(_translate("MainWindow", "Surname"))
        self.emp_nic_label.setText(_translate("MainWindow", "NIC No"))
        self.emp_gender_label.setText(_translate("MainWindow", "Gender"))
        self.emp_type_label.setText(_translate("MainWindow", "Emp. Type"))
        self.emp_designation_label.setText(
            _translate("MainWindow", "Designation"))
        self.emp_department_label.setText(
            _translate("MainWindow", "Department"))
        self.emp_section_label.setText(_translate("MainWindow", "Section"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))
        self.total_value_label.setText(_translate("MainWindow", "Total"))
        self.day_payment_label.setText(_translate("MainWindow", "Day Payment"))
        self.ot_payment_label.setText(_translate("MainWindow", "OT Payment"))
        self.comments_label.setText(_translate("MainWindow", "Comments"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.shortcut_box.setTitle(_translate("MainWindow", "Shortcuts"))
        self.shortcut_1.setText(_translate("MainWindow", "F1 : Day Payment"))
        self.shortcut_2.setText(_translate("MainWindow", "F2 : OT Payment"))
        self.shortcut_3.setText(_translate("MainWindow", "F3 : Submit"))
        self.shortcut_4.setText(_translate("MainWindow", "F4 : Print"))
        self.shortcut_5.setText(_translate("MainWindow", "F5 : Reset"))
        self.shortcut_6.setText(_translate("MainWindow", "Esc : Exit"))
        self.printBtn.setText(_translate("MainWindow", "Print"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    def close_system(self):
        sys.exit()

    def connect_device(self, ip_address, port):
        port = int(port)
        zk = ZK(ip_address, port=port)
        conn = zk.connect()
        return conn

    def reset_system(self):
        self.emp_name.setText('')
        self.emp_no.setText('')
        self.date.setText('')
        self.emp_calling_name.setText('')
        self.emp_surname.setText('')
        self.emp_nic.setText('')
        self.emp_gender.setText('')
        self.emp_type.setText('')
        self.emp_designation.setText('')
        self.emp_department.setText('')
        self.emp_section.setText('')
        self.total_value.setText('')
        self.day_payment.setPlainText('')
        self.ot_payment.setPlainText('')
        self.comments.setPlainText('')
        self.emp_pic.setPixmap(QtGui.QPixmap("img/default.png"))
        self.data_table.setRowCount(0)

    def readFinger(self, user_id):
        today = datetime.today()
        try:
            for user in self.users:
                if user.user_id == user_id:
                    print(user)
                    self.emp_name.setText(user.name)
                    self.emp_no.setText(user.user_id)
                    time = today.strftime("%d/%m/%Y %H:%M:%S")
                    self.date.setText(time)
                    self.fetchUserData(user_id)
                    self.fetchTransactionData(user_id)
        except:
            print('error')

    def fetchUserData(self, user_id):
        sql = f"SELECT CallingName,Surname,NIC_No,Gender,EmpTypeDescription,DSG_Name,Department,Section,ImageURL FROM all_employee WHERE DisplayNo='{str(user_id).zfill(5)}'"
        user_data = main_select(sql)
        if user_data:
            self.emp_calling_name.setText(user_data[0][0])
            self.emp_surname.setText(user_data[0][1])
            self.emp_nic.setText(user_data[0][2])
            if user_data[0][3] == '1':
                gender = 'Male'
            else:
                gender = 'Female'
            self.emp_gender.setText(gender)
            self.emp_type.setText(user_data[0][4])
            self.emp_designation.setText(user_data[0][5])
            self.emp_department.setText(user_data[0][6])
            self.emp_section.setText(user_data[0][7])
            if(user_data[0][8] != ''):
                self.emp_pic.setPixmap(QtGui.QPixmap(user_data[0][8]))
            else:
                self.emp_pic.setPixmap(QtGui.QPixmap("img/default.png"))

    def fetchTransactionData(self, user_id):
        sql = f"SELECT id,Reason,Type,Value FROM transactions WHERE DisplayNo='{str(user_id).zfill(5)}'"
        transaction_data = main_select(sql)
        self.data_table.setRowCount(0)
        total = 0
        if transaction_data:
            for row in transaction_data:
                rowPosition = self.data_table.rowCount()
                self.data_table.insertRow(rowPosition)
                self.data_table.setItem(
                    rowPosition, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.data_table.setItem(
                    rowPosition, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                if row[2] == 'Debit':
                    debit = row[3]
                    credit = ''
                    total += debit
                else:
                    credit = row[3]
                    debit = ''
                    total -= credit
                self.data_table.setItem(
                    rowPosition, 2, QtWidgets.QTableWidgetItem(str(credit)))
                self.data_table.setItem(
                    rowPosition, 3, QtWidgets.QTableWidgetItem(str(debit)))
                self.total_value.setText(str(total))

    def savePaymentData(self):
        emp_no = self.emp_no.text()
        total_value = self.total_value.text()
        day_payment = self.day_payment.toPlainText()
        ot_payment = self.ot_payment.toPlainText()
        comments = self.comments.toPlainText()
        if emp_no != '' and total_value != '' and day_payment != '' and ot_payment != '' and day_payment.isnumeric() == True and ot_payment.isnumeric() == True:
            sql = "INSERT INTO payments (DisplayNo, day_payment, ot_payment, total, comments) VALUES (%s, %s, %s, %s, %s)"
            val = (f'{str(emp_no).zfill(5)}', f"{day_payment}",
                   f"{ot_payment}", f"{total_value}", f"{comments}")
            main_query(sql, val)
            self.reset_system()
            self.show_popup("Success!", "Success!",
                            QtWidgets.QMessageBox.Information)
        elif (emp_no == ''):
            self.show_popup("Error!", "Please capture a fingerprint to continue",
                            QtWidgets.QMessageBox.Critical)
        elif (day_payment.isnumeric() == False):
            self.show_popup("Error!", "Please enter a valid value for day payment",
                            QtWidgets.QMessageBox.Critical)
        elif (ot_payment.isnumeric() == False):
            self.show_popup("Error!", "Please enter a valid value for day payment",
                            QtWidgets.QMessageBox.Critical)
        elif day_payment == '':
            self.show_popup(
                "Error!", "Please enter a value for day payment", QtWidgets.QMessageBox.Critical)
        elif ot_payment == '':
            self.show_popup(
                "Error!", "Please enter a value for OT payment", QtWidgets.QMessageBox.Critical)
        else:
            self.show_popup(
                "Error!", "Please capture a fingerprint to continue", QtWidgets.QMessageBox.Critical)

    def show_popup(self, title, text, icon):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel |
                               QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def handlePrint(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = self.makeTableDocument()
        document.print_(printer)

    def makeTableDocument(self):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        rows = self.data_table.rowCount()
        columns = self.data_table.columnCount()
        table = cursor.insertTable(rows + 1, columns)
        format = table.format()
        format.setHeaderRowCount(1)
        table.setFormat(format)
        format = cursor.blockCharFormat()
        format.setFontWeight(QtGui.QFont.Bold)
        for column in range(columns):
            cursor.setCharFormat(format)
            cursor.insertText(
                self.data_table.horizontalHeaderItem(column).text())
            cursor.movePosition(QtGui.QTextCursor.NextCell)
        for row in range(rows):
            for column in range(columns):
                cursor.insertText(
                    self.data_table.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        return document

    def config_settings(self):
        dlg = dialog()
        dlg.show()
        ret = dlg.exec_()
        if ret == QtWidgets.QDialog.Accepted:
            ip_address = dlg.ui.ip_address.text()
            port = dlg.ui.port.text()
            try:
                conn = None
                port = int(port)
                zk = ZK(ip_address, port=port)
                conn = zk.connect()
                if(conn != None):
                    users = conn.get_users()
                    self.thread = Worker(conn)
                    self.thread.start()
                    self.thread.sinout.connect(self.readFinger)
                    return users
                else:
                    self.show_popup("Error!", "Device not found!",
                                    QtWidgets.QMessageBox.Critical)
                    self.close_system()
            except Exception as e:
                print(e)
                self.show_popup("Error!", "Device not found!",
                                QtWidgets.QMessageBox.Critical)
                self.close_system()
        else:
            self.close_system()


class dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
