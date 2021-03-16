# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'регистрация2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 368)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 20, 191, 31))
        self.label.setStyleSheet("font-family: Yu Gothic UI Semibold;\n"
"font-size: 26px;")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 80, 471, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 9, 0, 0)
        self.formLayout.setVerticalSpacing(13)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("QLabel {font-family: Yu Gothic UI Semibold;\n"
"font-size: 19px;}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.surname_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surname_line.sizePolicy().hasHeightForWidth())
        self.surname_line.setSizePolicy(sizePolicy)
        self.surname_line.setObjectName("surname_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.surname_line)
        self.name_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_line.sizePolicy().hasHeightForWidth())
        self.name_line.setSizePolicy(sizePolicy)
        self.name_line.setObjectName("name_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_line)
        self.father_name_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.father_name_line.sizePolicy().hasHeightForWidth())
        self.father_name_line.setSizePolicy(sizePolicy)
        self.father_name_line.setObjectName("father_name_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.father_name_line)
        self.email_line = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy)
        self.email_line.setObjectName("email_line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email_line)
        self.gender_combobox = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gender_combobox.sizePolicy().hasHeightForWidth())
        self.gender_combobox.setSizePolicy(sizePolicy)
        self.gender_combobox.setStyleSheet("background-color: white;\n"
"border: 1px solid gray;")
        self.gender_combobox.setObjectName("gender_combobox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.gender_combobox)
        self.sign_up_btn = QtWidgets.QPushButton(Form)
        self.sign_up_btn.setGeometry(QtCore.QRect(150, 300, 241, 44))
        self.sign_up_btn.setStyleSheet("QPushButton {font-family:Yu Gothic UI ;\n"
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
        self.sign_up_btn.setObjectName("sign_up_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_2.setText(_translate("Form", "Фамилия"))
        self.label_3.setText(_translate("Form", "Имя"))
        self.label_4.setText(_translate("Form", "Отчество"))
        self.label_5.setText(_translate("Form", "Пол"))
        self.label_6.setText(_translate("Form", "E-mail"))
        self.sign_up_btn.setText(_translate("Form", "Зарегистрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
