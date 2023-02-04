import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from src.backend import LoginManager


class UiLogin(object):
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
        self.loginBtn.setGeometry(QtCore.QRect(40, 280, 131, 41))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet("background-color: #ffbf21;\n"
                                    "border-radius: 16px;")
        self.loginBtn.setText("Login")
        self.loginBtn.setObjectName("loginBtn")
        self.idkBtn = QtWidgets.QPushButton(self.widget)
        self.idkBtn.setGeometry(QtCore.QRect(200, 280, 131, 41))
        self.idkBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.idkBtn.setStyleSheet("background-color: #ffbf21;\n"
                                  "border-radius: 16px;")
        self.idkBtn.setText("Login")
        self.idkBtn.setObjectName("idkBtn")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.username.setPlaceholderText(_translate("Login", "Name"))
        self.password.setPlaceholderText(_translate("Login", "Passwort"))


class MyApp(QtWidgets.QWidget, UiLogin):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        self.loginBtn.clicked.connect(lambda: self.login())

    def login(self):
        LoginManager.login(self.username.text(), self.password.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.exit(app.exec_())
