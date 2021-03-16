import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QDate

from MainWindowUi import Ui_MainWindow
from forms.Ui_FirstWindow import Ui_FirstWindow
from forms.Ui_RegistrationWindow import Ui_RegistrationWindow
from forms.Ui_SignInEmailWindow import Ui_SignInEmailWindow
from forms.Ui_SetPasswordWindow import Ui_SetPasswordWindow
from forms.Ui_SignInWindow import Ui_SignInWindow
from forms.Ui_MainWindow import Ui_MainWindow

import psycopg2
import psycopg2.extras


con = psycopg2.connect(
    dbname="dardtccrbfmi7r",
    user="wxemjkjzpfmeoy",
    password="b150f60a68f89703625837e3ae8cf116e93e5cae92806339f926421d022079ba",
    host="ec2-54-228-174-49.eu-west-1.compute.amazonaws.com"
)


class FirstWindow(QWidget, Ui_FirstWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registration_btn.clicked.connect(self.registration)
        self.log_in_btn.clicked.connect(self.sign_in)


    def registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def sign_in(self):
        self.sign_in_email_window = SignInEmailWindow(self)
        self.sign_in_email_window.show()


class RegistrationWindow(QWidget, Ui_RegistrationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_up_btn.clicked.connect(self.sign_up)

    def sign_up(self):
        cur = con.cursor()
        email = self.email_line.text()
        cur.execute(f"""SELECT id from main.enrollees
        WHERE email LIKE '{email}'""")
        if cur.fetchall():
            self.error_label.setText("Пользователь с такой почтой уже существует")
        elif not all(
                [
                    bool(self.name_line.text()),
                    bool(self.surname_line.text()),
                    bool(self.father_name_line.text()),
                ]
        ):
            self.error_label.setText("Все поля должны быть заполнены")
        elif '@' not in email or '.' not in email.split('@')[1]:
            self.error_label.setText("Email должен быть введен корректно")
        else:
            cur.execute(f"""
            INSERT INTO main.enrollees
            (second_name, first_name, father_name, sex, email)
            VALUES ('{self.surname_line.text()}',
            '{self.name_line.text()}',
            '{self.father_name_line.text()}',
            '{self.gender_combobox.currentText()}',
            '{self.email_line.text()}')""")
            con.commit()
            cur.execute(f"""SELECT id FROM main.enrollees
            WHERE email LIKE '{self.email_line.text()}'""")
            student_id = cur.fetchone()[0]
            cur.execute(f"""
            INSERT INTO main.application_forms
            (student_id)
            VALUES ({student_id})""")
            con.commit()
            cur.execute(f"""
            INSERT INTO main.passports
            (student_id)
            VALUES ({student_id})""")
            con.commit()
            cur.close()
            self.close()


class SignInEmailWindow(QWidget, Ui_SignInEmailWindow):
    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.continue_clicked)

    def continue_clicked(self):
        cur = con.cursor()
        email = self.email_line.text()

        if '@' not in email or '.' not in email.split('@')[1]:
            self.error_label.setText("Email должен быть введен корректно")
        else:
            cur.execute(f"""SELECT id, password_setted FROM main.enrollees
                        WHERE email like '{email}'""")
            items = cur.fetchone()
            if not items:
                self.error_label.setText("Пользователя с таким Email не существует")
            else:
                print(items)
                if not items[1]:  # if not password_setted
                    self.set_password(items[0])
                else:
                    self.sign_in(items[0])

    def set_password(self, enrollee_id):
        self.set_password_window = SetPasswordWindow(self, enrollee_id)
        self.set_password_window.show()

    def sign_in(self, enrollee_id):
        self.sign_in_window = SignInWindow(self, enrollee_id)
        self.sign_in_window.show()

    def close_with_parent(self):
        self.parent_widget.close()
        self.close()


class SetPasswordWindow(QWidget, Ui_SetPasswordWindow):
    def __init__(self, parent_widget, enrollee_id):
        super().__init__()
        self.setupUi(self)
        self.parent_widget = parent_widget
        self.enrollee_id = enrollee_id
        self.set_password_btn.clicked.connect(self.continue_clicked)

    def continue_clicked(self):
        password = self.create_password_line.text()
        repeat_password = self.repeat_password_line.text()
        if not password:
            self.error_label.setText("Пароль не может быть пустым")
        elif password != repeat_password:
            self.error_label.setText("Пароли не совпадают")
        else:
            cur = con.cursor()
            cur.execute(f"""UPDATE main.enrollees
            SET password='{password}',
                password_setted=true
            WHERE id={self.enrollee_id}""")
            con.commit()
            cur.close()
            self.parent_widget.sign_in(self.enrollee_id)
            self.close()


class SignInWindow(QWidget, Ui_SignInWindow):
    def __init__(self, parent_widget, enrollee_id):
        super().__init__()
        self.setupUi(self)
        self.parent_widget = parent_widget
        self.enrollee_id = enrollee_id
        self.sign_in_btn.clicked.connect(self.sign_in)

    def sign_in(self):
        password = self.password_line.text()
        cur = con.cursor()
        cur.execute(f"""SELECT password FROM main.enrollees
        WHERE id={self.enrollee_id}""")
        real_password = cur.fetchone()[0]
        if password != real_password:
            self.error_label.setText('Неверный пароль')
        else:
            main_window.init(self.enrollee_id)
            main_window.show()
            self.parent_widget.close_with_parent()
            self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.enrollee_id = 0

    def init(self, enrollee_id):
        self.enrollee_id = enrollee_id
        self.fill_personal_data()
        self.fill_passport_data()

    def fill_personal_data(self):
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(f"""SELECT * FROM main.enrollees
        WHERE id={self.enrollee_id}""")
        items = cur.fetchone()
        self.surname_line.setText(items['second_name'])
        self.first_name_line.setText(items['first_name'])
        self.father_name_line.setText(items['father_name'])
        self.gender_cmb.setCurrentText(items['sex'])
        self.email_line.setText(items['email'])
        self.birth_date.setDate(QDate(*map(int, str(items['birth_date']).split('-'))))
        self.phone_line.setText(items['phone_number'])
        self.birthplace_line.setText(items['birth_city'])
        self.dormitory_cmb.setCurrentText(items['dorm_needed'])
        cur.close()
    
    def fill_passport_data(self):
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(f"""SELECT * FROM main.passports
        WHERE student_id={self.enrollee_id}""")
        items = cur.fetchone()
        self.passport_series_line.setText(items['serial_n'])
        self.pasport_number_line.setText(items['number'])
        self.who_gave_line.setText(items['given_by'])
        self.subdivision_code_line.setText(items['code'])
        self.given_date.setDate(QDate(*map(int, str(items['given_date']).split('-'))))
        self.index_line.setText(items['mail_index'])
        self.city_line.setText(items['city'])
        self.street_line.setText(items['street'])
        self.house_line.setText(items['house'])
        self.flat_line.setText(items['apartments'])
        cur.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    start_window = FirstWindow()
    start_window.show()
    sys.exit(app.exec())
