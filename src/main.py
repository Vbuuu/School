import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from src.backend import LoginManager


class UiLogin(object):
    def __init__(self):
        self.widget = None
        self.username = None
        self.password = None
        self.loginBtn = None
        self.idkBtn = None
        self.exitBtn = None

    def setupUi(self, login):
        login.setObjectName("Login")
        login.resize(370, 560)
        login.setMinimumSize(QtCore.QSize(370, 560))
        login.setMaximumSize(QtCore.QSize(370, 560))
        login.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        login.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        login.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(login)
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

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("Login", "Form"))
        self.username.setPlaceholderText(_translate("Login", "Name"))
        self.password.setPlaceholderText(_translate("Login", "Passwort"))
        self.exitBtn.setText(_translate("Login", "X"))


class MyApp(QtWidgets.QWidget, UiLogin):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        self.loginBtn.clicked.connect(lambda: self.login())
        self.exitBtn.clicked.connect(lambda: sys.exit())

    def login(self):
        LoginManager.login(self.username.text(), self.password.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = MyApp()
    form.show()
    sys.exit(app.exec_())
