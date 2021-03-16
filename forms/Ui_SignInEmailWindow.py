# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/SignInEmailWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInEmailWindow(object):
    def setupUi(self, SignInEmailWindow):
        SignInEmailWindow.setObjectName("SignInEmailWindow")
        SignInEmailWindow.resize(570, 252)
        self.label = QtWidgets.QLabel(SignInEmailWindow)
        self.label.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.label.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label.setObjectName("label")
        self.continue_btn = QtWidgets.QPushButton(SignInEmailWindow)
        self.continue_btn.setGeometry(QtCore.QRect(160, 180, 241, 44))
        self.continue_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
"                    font-size: 20px;\n"
"                    background-color: #FFF44F;\n"
"                    border: 1px solid #911E42;\n"
"                    border-radius: 5px;\n"
"                    color: #911E42;\n"
"                    position: relative;\n"
"                    box-sizing: border-box;\n"
"                    transition: all 700ms ease;}\n"
"\n"
"QPushButton:hover {\n"
"    background: #911E42;\n"
"    color: #FFF44F;\n"
"    box-shadow: inset 0 0 0 3px #b84642;\n"
"}")
        self.continue_btn.setObjectName("continue_btn")
        self.email_line = QtWidgets.QLineEdit(SignInEmailWindow)
        self.email_line.setGeometry(QtCore.QRect(170, 100, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy)
        self.email_line.setObjectName("email_line")
        self.label_2 = QtWidgets.QLabel(SignInEmailWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 141, 25))
        self.label_2.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_2.setObjectName("label_2")
        self.error_label = QtWidgets.QLabel(SignInEmailWindow)
        self.error_label.setGeometry(QtCore.QRect(166, 150, 271, 20))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(SignInEmailWindow)
        QtCore.QMetaObject.connectSlotsByName(SignInEmailWindow)

    def retranslateUi(self, SignInEmailWindow):
        _translate = QtCore.QCoreApplication.translate
        SignInEmailWindow.setWindowTitle(_translate("SignInEmailWindow", "Ввод почты"))
        self.label.setText(_translate("SignInEmailWindow", "Вход"))
        self.continue_btn.setText(_translate("SignInEmailWindow", "Далее"))
        self.label_2.setText(_translate("SignInEmailWindow", "Введите e-mail"))