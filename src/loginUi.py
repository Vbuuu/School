# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(370, 560)
        Login.setMinimumSize(QtCore.QSize(370, 560))
        Login.setMaximumSize(QtCore.QSize(370, 560))
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 371, 561))
        self.widget.setStyleSheet("background-color: #22272e;\n"
"border-radius: 16px;")
        self.widget.setObjectName("widget")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(40, 140, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setAcceptDrops(False)
        self.username.setStyleSheet("background-color: #2e313a;\n"
"border-radius: 16px;\n"
"padding-left: 12px;\n"
"padding-right: 12px;")
        self.username.setText("")
        self.username.setDragEnabled(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(40, 210, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password.setFont(font)
        self.password.setAcceptDrops(False)
        self.password.setStyleSheet("background-color: #2e313a;\n"
"border-radius: 16px;\n"
"padding-left: 12px;\n"
"padding-right: 12px;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setGeometry(QtCore.QRect(40, 280, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet("background-color: #ffbf21;\n"
"border-radius: 16px;")
        self.loginBtn.setText("Login")
        self.loginBtn.setObjectName("loginBtn")
        self.exitBtn = QtWidgets.QPushButton(self.widget)
        self.exitBtn.setGeometry(QtCore.QRect(340, 10, 21, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setStyleSheet("background-color: transparent;")
        self.exitBtn.setObjectName("exitBtn")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.username.setPlaceholderText(_translate("Login", "Name"))
        self.password.setPlaceholderText(_translate("Login", "Passwort"))
        self.exitBtn.setText(_translate("Login", "X"))
