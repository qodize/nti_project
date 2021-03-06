# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/SignInWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInWindow(object):
    def setupUi(self, SignInWindow):
        SignInWindow.setObjectName("SignInWindow")
        SignInWindow.resize(570, 255)
        self.password_line = QtWidgets.QLineEdit(SignInWindow)
        self.password_line.setGeometry(QtCore.QRect(170, 100, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_line.sizePolicy().hasHeightForWidth())
        self.password_line.setSizePolicy(sizePolicy)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.sign_in_btn = QtWidgets.QPushButton(SignInWindow)
        self.sign_in_btn.setGeometry(QtCore.QRect(160, 190, 241, 44))
        self.sign_in_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.label_3 = QtWidgets.QLabel(SignInWindow)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.label_3.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SignInWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 141, 25))
        self.label_4.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_4.setObjectName("label_4")
        self.error_label = QtWidgets.QLabel(SignInWindow)
        self.error_label.setGeometry(QtCore.QRect(160, 153, 241, 20))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(SignInWindow)
        QtCore.QMetaObject.connectSlotsByName(SignInWindow)

    def retranslateUi(self, SignInWindow):
        _translate = QtCore.QCoreApplication.translate
        SignInWindow.setWindowTitle(_translate("SignInWindow", "????????"))
        self.sign_in_btn.setText(_translate("SignInWindow", "??????????"))
        self.label_3.setText(_translate("SignInWindow", "????????"))
        self.label_4.setText(_translate("SignInWindow", "?????????????? ????????????"))
