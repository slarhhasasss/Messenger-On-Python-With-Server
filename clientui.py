# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textViewCorp = QtWidgets.QLabel(self.centralwidget)
        self.textViewCorp.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.textViewCorp.setObjectName("textViewCorp")
        self.textViewHeader = QtWidgets.QLabel(self.centralwidget)
        self.textViewHeader.setGeometry(QtCore.QRect(300, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textViewHeader.setFont(font)
        self.textViewHeader.setObjectName("textViewHeader")
        self.editTextName = QtWidgets.QLineEdit(self.centralwidget)
        self.editTextName.setGeometry(QtCore.QRect(100, 130, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editTextName.setFont(font)
        self.editTextName.setObjectName("editTextName")
        self.textViewName = QtWidgets.QLabel(self.centralwidget)
        self.textViewName.setGeometry(QtCore.QRect(30, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textViewName.setFont(font)
        self.textViewName.setObjectName("textViewName")
        self.textViewMessages = QtWidgets.QTextBrowser(self.centralwidget)
        self.textViewMessages.setGeometry(QtCore.QRect(30, 170, 711, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textViewMessages.setFont(font)
        self.textViewMessages.setObjectName("textViewMessages")
        self.editTextMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.editTextMessage.setGeometry(QtCore.QRect(30, 540, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editTextMessage.setFont(font)
        self.editTextMessage.setObjectName("editTextMessage")
        self.buttonSend = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSend.setGeometry(QtCore.QRect(640, 540, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buttonSend.setFont(font)
        self.buttonSend.setObjectName("buttonSend")
        self.buttonEntry = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEntry.setGeometry(QtCore.QRect(640, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonEntry.setFont(font)
        self.buttonEntry.setObjectName("buttonEntry")
        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setGeometry(QtCore.QRect(310, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.buttonExit.setFont(font)
        self.buttonExit.setObjectName("buttonExit")
        self.buttonConnect = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConnect.setGeometry(QtCore.QRect(640, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonConnect.setFont(font)
        self.buttonConnect.setObjectName("buttonConnect")
        self.textViewUrl = QtWidgets.QLabel(self.centralwidget)
        self.textViewUrl.setGeometry(QtCore.QRect(30, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textViewUrl.setFont(font)
        self.textViewUrl.setObjectName("textViewUrl")
        self.editTextUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.editTextUrl.setGeometry(QtCore.QRect(100, 81, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editTextUrl.setFont(font)
        self.editTextUrl.setObjectName("editTextUrl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textViewCorp.setText(_translate("MainWindow", "KolesnikobINC"))
        self.textViewHeader.setText(_translate("MainWindow", "Messager!!!!"))
        self.editTextName.setPlaceholderText(_translate("MainWindow", "Введите Имя"))
        self.textViewName.setText(_translate("MainWindow", "Name:"))
        self.editTextMessage.setPlaceholderText(_translate("MainWindow", "Введите Текст..."))
        self.buttonSend.setText(_translate("MainWindow", "Send"))
        self.buttonEntry.setText(_translate("MainWindow", "Войти"))
        self.buttonExit.setText(_translate("MainWindow", "Exit"))
        self.buttonConnect.setText(_translate("MainWindow", "Connect"))
        self.textViewUrl.setText(_translate("MainWindow", "Url:"))
        self.editTextUrl.setPlaceholderText(_translate("MainWindow", "Введите url"))
