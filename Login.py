# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

# import Logo_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(646, 476)
        Dialog.setModal(True)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 646, 476))
        self.stackedWidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        self.LogIn = QWidget()
        self.LogIn.setObjectName(u"LogIn")
        self.SignInLabel = QLabel(self.LogIn)
        self.SignInLabel.setObjectName(u"SignInLabel")
        self.SignInLabel.setGeometry(QRect(220, 120, 181, 31))
        self.SignInLabel.setStyleSheet(u"background-color: rgba(0,0,0,0%);\n"
"color: white;")
        self.UsernameTextbox = QLineEdit(self.LogIn)
        self.UsernameTextbox.setObjectName(u"UsernameTextbox")
        self.UsernameTextbox.setGeometry(QRect(80, 180, 461, 41))
        self.UsernameTextbox.setMouseTracking(True)
        self.UsernameTextbox.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.UsernameTextbox.setCursorPosition(0)
        self.UsernameTextbox.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.PasswordTextbox = QLineEdit(self.LogIn)
        self.PasswordTextbox.setObjectName(u"PasswordTextbox")
        self.PasswordTextbox.setGeometry(QRect(80, 250, 461, 41))
        self.PasswordTextbox.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.PasswordTextbox.setCursorPosition(0)
        self.SignInBtn = QPushButton(self.LogIn)
        self.SignInBtn.setObjectName(u"SignInBtn")
        self.SignInBtn.setGeometry(QRect(80, 310, 461, 31))
        self.SignInBtn.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(106,255,121);")
        self.NewUserLabel = QLabel(self.LogIn)
        self.NewUserLabel.setObjectName(u"NewUserLabel")
        self.NewUserLabel.setGeometry(QRect(90, 360, 71, 16))
        self.NewUserLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white\n"
"\n"
"")
        self.SignUpBtn = QPushButton(self.LogIn)
        self.SignUpBtn.setObjectName(u"SignUpBtn")
        self.SignUpBtn.setGeometry(QRect(156, 358, 61, 21))
        self.SignUpBtn.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(106,255,121);")
        self.Logo = QLabel(self.LogIn)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(110, -30, 381, 211))
        self.Logo.setStyleSheet(u"background-color: transparent;")
        self.Logo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.Logo.setScaledContents(True)
        self.stackedWidget.addWidget(self.LogIn)
        self.SignUp = QWidget()
        self.SignUp.setObjectName(u"SignUp")
        self.CreateAccountLabel = QLabel(self.SignUp)
        self.CreateAccountLabel.setObjectName(u"CreateAccountLabel")
        self.CreateAccountLabel.setGeometry(QRect(210, 20, 241, 31))
        self.CreateAccountLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")
        self.FirstNameTextbox = QLineEdit(self.SignUp)
        self.FirstNameTextbox.setObjectName(u"FirstNameTextbox")
        self.FirstNameTextbox.setGeometry(QRect(70, 80, 231, 41))
        self.FirstNameTextbox.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.LastNameTextbox = QLineEdit(self.SignUp)
        self.LastNameTextbox.setObjectName(u"LastNameTextbox")
        self.LastNameTextbox.setGeometry(QRect(330, 80, 231, 41))
        self.LastNameTextbox.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"")
        self.EmailAddrTextbox = QLineEdit(self.SignUp)
        self.EmailAddrTextbox.setObjectName(u"EmailAddrTextbox")
        self.EmailAddrTextbox.setGeometry(QRect(70, 140, 491, 41))
        self.EmailAddrTextbox.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"")
        self.PasswordTextbox_2 = QLineEdit(self.SignUp)
        self.PasswordTextbox_2.setObjectName(u"PasswordTextbox_2")
        self.PasswordTextbox_2.setGeometry(QRect(70, 320, 491, 41))
        self.PasswordTextbox_2.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 10px;\n"
"")
        self.PasswordTextbox_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.CreateAcctTextbox = QPushButton(self.SignUp)
        self.CreateAcctTextbox.setObjectName(u"CreateAcctTextbox")
        self.CreateAcctTextbox.setGeometry(QRect(70, 380, 491, 32))
        self.CreateAcctTextbox.setStyleSheet(u"background-color: rgb(106,255,121);\n"
"border-radius: 10px;")
        self.QuestionLabel = QLabel(self.SignUp)
        self.QuestionLabel.setObjectName(u"QuestionLabel")
        self.QuestionLabel.setGeometry(QRect(190, 420, 161, 16))
        self.QuestionLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.SignInBtn_2 = QPushButton(self.SignUp)
        self.SignInBtn_2.setObjectName(u"SignInBtn_2")
        self.SignInBtn_2.setGeometry(QRect(350, 418, 51, 20))
        self.SignInBtn_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(106,255,121);\n"
"")
        self.PhoneNumberTextbox = QLineEdit(self.SignUp)
        self.PhoneNumberTextbox.setObjectName(u"PhoneNumberTextbox")
        self.PhoneNumberTextbox.setGeometry(QRect(70, 200, 491, 41))
        self.PhoneNumberTextbox.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"")
        self.MajorBox = QComboBox(self.SignUp)
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.addItem("")
        self.MajorBox.setObjectName(u"MajorBox")
        self.MajorBox.setGeometry(QRect(70, 260, 491, 41))
        self.MajorBox.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"")
        self.stackedWidget.addWidget(self.SignUp)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.SignInLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt;\">Sign in to Stinder</span></p></body></html>", None))
        self.UsernameTextbox.setText("")
        self.UsernameTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.PasswordTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.SignInBtn.setText(QCoreApplication.translate("Dialog", u"Sign In", None))
        self.NewUserLabel.setText(QCoreApplication.translate("Dialog", u"New User?", None))
        self.SignUpBtn.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.Logo.setText("")
        self.CreateAccountLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Create Your Account</span></p></body></html>", None))
        self.FirstNameTextbox.setText("")
        self.FirstNameTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.LastNameTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.EmailAddrTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email Address", None))
        self.PasswordTextbox_2.setText("")
        self.PasswordTextbox_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.CreateAcctTextbox.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
        self.QuestionLabel.setText(QCoreApplication.translate("Dialog", u"Already have an account?", None))
        self.SignInBtn_2.setText(QCoreApplication.translate("Dialog", u"Sign In", None))
        self.PhoneNumberTextbox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.MajorBox.setItemText(0, QCoreApplication.translate("Dialog", u"Accounting", None))
        self.MajorBox.setItemText(1, QCoreApplication.translate("Dialog", u"Advertising", None))
        self.MajorBox.setItemText(2, QCoreApplication.translate("Dialog", u"Aerospace Engineering", None))
        self.MajorBox.setItemText(3, QCoreApplication.translate("Dialog", u"Biology", None))
        self.MajorBox.setItemText(4, QCoreApplication.translate("Dialog", u"Computer Science", None))
        self.MajorBox.setItemText(5, QCoreApplication.translate("Dialog", u"Civil Engineering", None))
        self.MajorBox.setItemText(6, QCoreApplication.translate("Dialog", u"Mechanical Engineering", None))
        self.MajorBox.setItemText(7, QCoreApplication.translate("Dialog", u"Nursing", None))
        self.MajorBox.setItemText(8, QCoreApplication.translate("Dialog", u"Philosophy", None))

        self.MajorBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Major", None))
    # retranslateUi

