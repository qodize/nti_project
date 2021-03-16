# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ввод_почты.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 252)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.label.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label.setObjectName("label")
        self.registration_to_password_btn = QtWidgets.QPushButton(Form)
        self.registration_to_password_btn.setGeometry(QtCore.QRect(160, 170, 241, 44))
        self.registration_to_password_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.registration_to_password_btn.setObjectName("registration_to_password_btn")
        self.log_in_email_line = QtWidgets.QLineEdit(Form)
        self.log_in_email_line.setGeometry(QtCore.QRect(170, 100, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_in_email_line.sizePolicy().hasHeightForWidth())
        self.log_in_email_line.setSizePolicy(sizePolicy)
        self.log_in_email_line.setObjectName("log_in_email_line")
        self.log_in_email_line.setStyleSheet("QLineEdit {font-family: Yu Gothic UI;"
"font-size:14px;"
"padding-left:6px;}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 141, 25))
        self.label_2.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вход"))
        self.registration_to_password_btn.setText(_translate("Form", "Далее"))
        self.label_2.setText(_translate("Form", "Введите e-mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
