# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ввод_пароля_дважды.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 300)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 181, 25))
        self.label_4.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 71, 31))
        self.label_3.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label_3.setObjectName("label_3")
        self.create_password_line = QtWidgets.QLineEdit(Form)
        self.create_password_line.setStyleSheet("QLineEdit {font-family: Yu Gothic UI;"
"font-size:14px;"
"padding-left:6px;}")
        self.create_password_line.setGeometry(QtCore.QRect(210, 100, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_password_line.sizePolicy().hasHeightForWidth())
        self.create_password_line.setSizePolicy(sizePolicy)
        self.create_password_line.setObjectName("create_password_line")
        self.log_in_first_time_btn = QtWidgets.QPushButton(Form)
        self.log_in_first_time_btn.setGeometry(QtCore.QRect(180, 220, 241, 44))
        self.log_in_first_time_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.log_in_first_time_btn.setObjectName("log_in_first_time_btn")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 171, 25))
        self.label_5.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_5.setObjectName("label_5")
        self.repeat_password_line = QtWidgets.QLineEdit(Form)
        self.repeat_password_line.setGeometry(QtCore.QRect(210, 150, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeat_password_line.sizePolicy().hasHeightForWidth())
        self.repeat_password_line.setSizePolicy(sizePolicy)
        self.repeat_password_line.setObjectName("repeat_password_line")
        self.repeat_password_line.setStyleSheet("QLineEdit {font-family: Yu Gothic UI;"
"font-size:14px;"
"padding-left:6px;}")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Придумайте пароль"))
        self.label_3.setText(_translate("Form", "Вход"))
        self.log_in_first_time_btn.setText(_translate("Form", "Войти"))
        self.label_5.setText(_translate("Form", "Повторите пароль"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
