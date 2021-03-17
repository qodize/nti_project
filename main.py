import sys
import os
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtCore import QDate

from forms.Ui_FirstWindow import Ui_FirstWindow
from forms.Ui_RegistrationWindow import Ui_RegistrationWindow
from forms.Ui_SignInEmailWindow import Ui_SignInEmailWindow
from forms.Ui_SetPasswordWindow import Ui_SetPasswordWindow
from forms.Ui_SignInWindow import Ui_SignInWindow
from MainWindowUi2 import Ui_MainWindow

import psycopg2
import psycopg2.extras
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

con = psycopg2.connect(
    dbname="dardtccrbfmi7r",
    user="wxemjkjzpfmeoy",
    password="b150f60a68f89703625837e3ae8cf116e93e5cae92806339f926421d022079ba",
    host="ec2-54-228-174-49.eu-west-1.compute.amazonaws.com"
)
cur = con.cursor()
cur.execute("set datestyle='ISO, DMY'")
con.commit()

def fill_pdf_pd2(student_id):
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f"""SELECT * FROM main.enrollees
    WHERE id={student_id}""")
    items = cur.fetchone()
    packet = io.BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    can.setFont('Arial', 13)
    can.drawString(90, 650, f"{items['second_name']} {items['first_name']} {items['father_name']}")
    cur.execute(f"""SELECT * from main.passports
    WHERE student_id={student_id}""")
    items = cur.fetchone()
    can.drawString(120, 595, f"{items['serial_n']} {items['number']}")
    can.drawString(73, 544, f"{'.'.join(reversed(str(items['given_date']).split('-')))} {items['given_by']}")
    can.drawString(75, 495, f"{items['city']}, {items['street']}, {items['house']}, {items['apartments']}")
    cur.execute(f"""SELECT * FROM main.application_forms
    WHERE student_id={student_id}""")
    items = cur.fetchone()
    can.drawString(160, 430, f"{items['specialization']}")
    can.drawString(250, 415, f"{items['edu_form']}")
    can.showPage()
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # Read your existing PDF
    existing_pdf = PdfFileReader(open("Заявление о зачислении.pdf", "rb"))
    output = PdfFileWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)

    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # Finally, write "output" to a real file
    outputStream = open("заявление о зачислении студента.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    os.startfile("заявление о зачислении студента.pdf")


def fill_pdf_pd(student_id):
    cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f"""SELECT * FROM main.enrollees
    WHERE id={student_id}""")
    items = cur.fetchone()
    packet = io.BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    can.setFont('Arial', 13)
    can.drawString(75, 743, f"{items['second_name']} {items['first_name']} {items['father_name']}")
    cur.execute(f"""SELECT * from main.passports
    WHERE student_id={student_id}""")
    items = cur.fetchone()
    can.drawString(102, 700, f"{items['serial_n']} {items['number']}")
    # print(items['serial_n'], items['number'])
    # print(items['given_date'].splti('-'), items['given_by'])
    can.drawString(92, 665, f"{'.'.join(list(reversed(str(items['given_date']).split('-'))))} {items['given_by']}")
    can.showPage()
    can.save()
    print('here')
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # Read your existing PDF
    existing_pdf = PdfFileReader(open("СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ.pdf", "rb"))
    output = PdfFileWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)

    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # Finally, write "output" to a real file
    outputStream = open("согласие на обработку ПД.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    os.startfile("согласие на обработку ПД.pdf")


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
        self.save_changes_btn1.clicked.connect(self.save_changes1)
        self.save_changes_btn2.clicked.connect(self.save_changes2)
        self.photo_of_person_btn.clicked.connect(self.open_photo)
        self.photo_of_passport_btn.clicked.connect(self.open_passport_pdf)
        self.certificate_photo_btn.clicked.connect(self.open_edu_doc_photo)
        self.photo_of_document_ia_btn.clicked.connect(self.open_ind_awards_photo)

        reg = QRegExp("[0-9]{4}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.passport_series_line.setValidator(pValidator)

        # номер и индекс
        reg3 = QRegExp("[0-9]{6}")
        pValidator3 = QRegExpValidator(self)
        pValidator3.setRegExp(reg3)
        self.pasport_number_line.setValidator(pValidator3)
        self.index_line.setValidator(pValidator3)

        # код подразделения
        reg4 = QRegExp("^\\d{3}\\-\\d{3}$")
        pValidator4 = QRegExpValidator(self)
        pValidator4.setRegExp(reg4)
        self.subdivision_code_line.setValidator(pValidator4)
        self.generate_consent_btn.clicked.connect(self.generate_consent)
        self.upload_consent_btn.clicked.connect(self.upload_consent)
        self.generate_consent_btn_2.clicked.connect(self.generate_consent2)
        self.upload_consent_btn_2.clicked.connect(self.upload_consent2)

    def generate_consent2(self):
        fill_pdf_pd2(self.enrollee_id)

    def upload_consent2(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать pdf-файл',
                                            '', "(*.pdf)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""
                UPDATE main.application_forms
                SET consent_doc=%s,
                consent_doc_name=%s
                """, (file.read(), fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1]))
                con.commit()
            self.message_label_2.setText("Заявление загружено")

    def init(self, enrollee_id):
        self.enrollee_id = enrollee_id
        self.fill_personal_data()
        self.fill_passport_data()
        self.fill_application_data()

    def generate_consent(self):
        fill_pdf_pd(self.enrollee_id)

    def upload_consent(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать pdf-файл',
                                            '', "(*.pdf)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""
                UPDATE main.enrollees
                SET consent_doc=%s,
                consent_doc_name=%s
                """, (file.read(), fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1]))
                con.commit()
            self.message_label_1.setText("Согласие загружено")

    def open_ind_awards_photo(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать pdf-файл',
                                            '', "(*.pdf)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""UPDATE main.application_forms
                SET ind_awards_photo_name=%s,
                ind_awards_photo=%s
                WHERE student_id={self.enrollee_id}""",
                            (fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1],
                             file.read()))
            con.commit()
            self.photo_of_document_ia_btn.setText(f'{fname.split("/")[-1]} (Загрузить заново?)')

    def open_edu_doc_photo(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать pdf-файл',
                                            '', "(*.pdf)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""UPDATE main.application_forms
                SET edu_doc_photo_name=%s,
                edu_doc_photo=%s
                WHERE student_id={self.enrollee_id}""",
                            (fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1],
                             file.read()))
            con.commit()
            self.certificate_photo_btn.setText(f'{fname.split("/")[-1]} (Загрузить заново?)')

    def open_passport_pdf(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать pdf-файл',
                                            '', "(*.pdf)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""UPDATE main.passports
                SET photo_name=%s,
                photo=%s
                WHERE student_id={self.enrollee_id}""",
                            (fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1],
                             file.read()))
            con.commit()
            self.photo_of_passport_btn.setText(f'{fname.split("/")[-1]} (Загрузить заново?)')

    def open_photo(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать фото',
                                            '', "(*.jpg, *.jpeg, *.png)")[0]
        if fname:
            cur = con.cursor()
            with open(fname, 'rb') as file:
                cur.execute(f"""UPDATE main.enrollees
                SET photo=%s,
                photo_name=%s
                WHERE id={self.enrollee_id}""", (file.read(),
                                                 fname.split('.')[0].split('/')[-1] + '.' + fname.split('.')[-1]))
                con.commit()
                self.photo_of_person_btn.setText(f'{fname.split("/")[-1]} (Загрузить заново?)')

    def save_changes1(self):
        cur = con.cursor()
        cur.execute(f"""
        UPDATE main.enrollees
        SET second_name='{self.surname_line.text()}',
        first_name='{self.first_name_line.text()}',
        father_name='{self.father_name_line.text()}',
        sex='{self.gender_cmb.currentText()}',
        email='{self.email_line.text()}',
        birth_date='{self.birth_date.text()}',
        phone_number='{self.phone_line.text()}',
        birth_city='{self.birthplace_line.text()}',
        dorm_needed='{self.dormitory_cmb.currentText()}'
        WHERE id={self.enrollee_id}""")
        con.commit()
        cur.execute(f"""UPDATE main.passports
        SET serial_n='{self.passport_series_line.text()}',
        number='{self.pasport_number_line.text()}',
        given_by='{self.who_gave_line.text()}',
        code='{self.subdivision_code_line.text()}',
        given_date='{self.given_date.text()}',
        mail_index='{self.index_line.text()}',
        city='{self.city_line.text()}',
        street='{self.street_line.text()}',
        house='{self.house_line.text()}',
        apartments='{self.flat_line.text()}'
        WHERE student_id={self.enrollee_id}""")

        con.commit()
        cur.close()
        self.message_label_1.setText('Данные сохранены')

    def save_changes2(self):
        cur = con.cursor()
        cur.execute(f"""UPDATE main.application_forms
        SET edu_doc_number='{self.certificate_number_line.text()}',
        edu_form='{self.form_of_education_cmb.currentText()}',
        exam1={self.form_math_res.text()},
        exam2={self.form_russian_res.text()},
        exam3={self.form_prof_res.text()},
        ind_awards='{self.ind_awards_cmb.currentText()}',
        is_original='{self.orig_or_copy_combobox.currentText()}'
        WHERE student_id={self.enrollee_id}""")
        con.commit()
        self.message_label_2.setText('Данные сохранены')

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
        if items['photo_name']:
            self.photo_of_person_btn.setText(f'{items["photo_name"]} (Загрузить заново?)')
        else:
            self.photo_of_person_btn.setText('Выбрать фото (.jpeg, .png)')
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
        if items['photo_name']:
            self.photo_of_passport_btn.setText(f'{items["photo_name"]} (Загрузить заново?)')
        else:
            self.photo_of_passport_btn.setText(f'Выберите pdf-файл')
        cur.close()

    def fill_application_data(self):
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(f"""SELECT * FROM main.application_forms
        WHERE student_id={self.enrollee_id}""")
        items = cur.fetchone()
        self.certificate_number_line.setText(items['edu_doc_number'])
        self.form_of_education_cmb.setCurrentText(items['edu_form'])
        self.field_of_study_cmb.setCurrentText(items['specialization'])
        self.ind_awards_cmb.setCurrentText(items['ind_awards'])
        self.orig_or_copy_combobox.setCurrentText(items['is_original'])
        self.form_russian_res.setText(str(items['exam1']))
        self.form_math_res.setText(str(items['exam2']))
        self.form_prof_res.setText(str(items['exam3']))
        if items['edu_doc_photo_name']:
            self.certificate_photo_btn.setText(f'{items["edu_doc_photo_name"]} (Загрузить заново?)')
        if items['ind_awards_photo_name']:
            self.photo_of_document_ia_btn.setText(f'{items["ind_awards_photo_name"]} (Загрузить заново?)')

        cur.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    start_window = FirstWindow()
    start_window.show()
    sys.exit(app.exec())
