# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/SetPasswordWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetPasswordWindow(object):
    def setupUi(self, SetPasswordWindow):
        SetPasswordWindow.setObjectName("SetPasswordWindow")
        SetPasswordWindow.resize(612, 309)
        self.label_4 = QtWidgets.QLabel(SetPasswordWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 181, 25))
        self.label_4.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(SetPasswordWindow)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 261, 31))
        self.label_3.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label_3.setObjectName("label_3")
        self.create_password_line = QtWidgets.QLineEdit(SetPasswordWindow)
        self.create_password_line.setGeometry(QtCore.QRect(210, 100, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_password_line.sizePolicy().hasHeightForWidth())
        self.create_password_line.setSizePolicy(sizePolicy)
        self.create_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_password_line.setObjectName("create_password_line")
        self.set_password_btn = QtWidgets.QPushButton(SetPasswordWindow)
        self.set_password_btn.setGeometry(QtCore.QRect(180, 240, 241, 44))
        self.set_password_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.set_password_btn.setObjectName("set_password_btn")
        self.label_5 = QtWidgets.QLabel(SetPasswordWindow)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 171, 25))
        self.label_5.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_5.setObjectName("label_5")
        self.repeat_password_line = QtWidgets.QLineEdit(SetPasswordWindow)
        self.repeat_password_line.setGeometry(QtCore.QRect(210, 150, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeat_password_line.sizePolicy().hasHeightForWidth())
        self.repeat_password_line.setSizePolicy(sizePolicy)
        self.repeat_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeat_password_line.setObjectName("repeat_password_line")
        self.error_label = QtWidgets.QLabel(SetPasswordWindow)
        self.error_label.setGeometry(QtCore.QRect(190, 203, 251, 20))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(SetPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(SetPasswordWindow)

    def retranslateUi(self, SetPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        SetPasswordWindow.setWindowTitle(_translate("SetPasswordWindow", "???????????????????? ????????????"))
        self.label_4.setText(_translate("SetPasswordWindow", "???????????????????? ????????????"))
        self.label_3.setText(_translate("SetPasswordWindow", "???????????????????? ????????????"))
        self.set_password_btn.setText(_translate("SetPasswordWindow", "??????????????????"))
        self.label_5.setText(_translate("SetPasswordWindow", "?????????????????? ????????????"))
