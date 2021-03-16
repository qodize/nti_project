# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ввод_пароля.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 255)
        self.log_in_password_line = QtWidgets.QLineEdit(Form)
        self.log_in_password_line.setGeometry(QtCore.QRect(170, 100, 381, 31))
        self.log_in_password_line.setStyleSheet("QLineEdit {font-family: Yu Gothic UI;"
"font-size:14px;"
"padding-left:6px;}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_in_password_line.sizePolicy().hasHeightForWidth())
        self.log_in_password_line.setSizePolicy(sizePolicy)
        self.log_in_password_line.setObjectName("log_in_password_line")
        self.log_in_btn = QtWidgets.QPushButton(Form)
        self.log_in_btn.setGeometry(QtCore.QRect(160, 170, 241, 44))
        self.log_in_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.log_in_btn.setObjectName("log_in_btn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 71, 31))
        self.label_3.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 141, 25))
        self.label_4.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.log_in_btn.setText(_translate("Form", "Войти"))
        self.label_3.setText(_translate("Form", "Вход"))
        self.label_4.setText(_translate("Form", "Введите пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
