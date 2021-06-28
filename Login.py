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

import stinder_images_rc

class Ui_Stinder_Login(object):
    def setupUi(self, Stinder_Login):
        if not Stinder_Login.objectName():
            Stinder_Login.setObjectName(u"Stinder_Login")
        Stinder_Login.resize(646, 476)
        Stinder_Login.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        self.stackedWidget = QStackedWidget(Stinder_Login)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 651, 473))
        self.stackedWidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.StinderLogo = QLabel(self.page)
        self.StinderLogo.setObjectName(u"StinderLogo")
        self.StinderLogo.setGeometry(QRect(110, -40, 411, 201))
        self.StinderLogo.setStyleSheet(u"background-color: transparent;")
        self.StinderLogo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.StinderLogo.setScaledContents(True)
        self.InstructLabel = QLabel(self.page)
        self.InstructLabel.setObjectName(u"InstructLabel")
        self.InstructLabel.setGeometry(QRect(150, 100, 341, 41))
        self.InstructLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 104pt \"Nexa Bold\";")
        self.FirstNameInput = QLineEdit(self.page)
        self.FirstNameInput.setObjectName(u"FirstNameInput")
        self.FirstNameInput.setGeometry(QRect(50, 160, 231, 41))
        self.FirstNameInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"font: 300 13pt \"Nexa Demo\";")
        self.LastNameTb = QLineEdit(self.page)
        self.LastNameTb.setObjectName(u"LastNameTb")
        self.LastNameTb.setGeometry(QRect(350, 160, 251, 41))
        self.LastNameTb.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"font: 300 13pt \"Nexa Demo\";")
        self.EmailInput = QLineEdit(self.page)
        self.EmailInput.setObjectName(u"EmailInput")
        self.EmailInput.setGeometry(QRect(50, 230, 551, 41))
        self.EmailInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"font: 300 13pt \"Nexa Demo\";")
        self.MajorInput = QComboBox(self.page)
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.addItem("")
        self.MajorInput.setObjectName(u"MajorInput")
        self.MajorInput.setGeometry(QRect(50, 300, 551, 41))
        self.MajorInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"font: 300 13pt \"Nexa Demo\";")
        self.MajorInput.setEditable(False)
        self.ContinueBtn = QPushButton(self.page)
        self.ContinueBtn.setObjectName(u"ContinueBtn")
        self.ContinueBtn.setGeometry(QRect(50, 390, 551, 31))
        self.ContinueBtn.setStyleSheet(u"background-color: rgb(106,255,121);\n"
"border-radius: 10px;\n"
"font: 700 13pt \"Nexa Bold\";\n"
"color: white;")
        self.errorLabel = QLabel(self.page)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(60, 347, 491, 16))
        self.errorLabel.setStyleSheet(u"background-color: transparent;\n"
"color: red;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Stinder_Login)

        QMetaObject.connectSlotsByName(Stinder_Login)
    # setupUi

    def retranslateUi(self, Stinder_Login):
        Stinder_Login.setWindowTitle(QCoreApplication.translate("Stinder_Login", u"Stinder", None))
        self.StinderLogo.setText("")
        self.InstructLabel.setText(QCoreApplication.translate("Stinder_Login", u"<html><head/><body><p><span style=\" font-size:24pt;\">please fill out form to continue</span></p></body></html>", None))
        self.FirstNameInput.setPlaceholderText(QCoreApplication.translate("Stinder_Login", u"  First Name", None))
        self.LastNameTb.setPlaceholderText(QCoreApplication.translate("Stinder_Login", u"  Last Name", None))
        self.EmailInput.setPlaceholderText(QCoreApplication.translate("Stinder_Login", u"  Email Address", None))
        self.MajorInput.setItemText(0, QCoreApplication.translate("Stinder_Login", u"Accounting", None))
        self.MajorInput.setItemText(1, QCoreApplication.translate("Stinder_Login", u"Aerospace Engineering", None))
        self.MajorInput.setItemText(2, QCoreApplication.translate("Stinder_Login", u"Anthropology", None))
        self.MajorInput.setItemText(3, QCoreApplication.translate("Stinder_Login", u"Biology", None))
        self.MajorInput.setItemText(4, QCoreApplication.translate("Stinder_Login", u"Botany", None))
        self.MajorInput.setItemText(5, QCoreApplication.translate("Stinder_Login", u"Chemistry", None))
        self.MajorInput.setItemText(6, QCoreApplication.translate("Stinder_Login", u"Computer Science", None))
        self.MajorInput.setItemText(7, QCoreApplication.translate("Stinder_Login", u"Data Science", None))
        self.MajorInput.setItemText(8, QCoreApplication.translate("Stinder_Login", u"Economics", None))
        self.MajorInput.setItemText(9, QCoreApplication.translate("Stinder_Login", u"Education", None))
        self.MajorInput.setItemText(10, QCoreApplication.translate("Stinder_Login", u"Finance", None))
        self.MajorInput.setItemText(11, QCoreApplication.translate("Stinder_Login", u"Geography", None))
        self.MajorInput.setItemText(12, QCoreApplication.translate("Stinder_Login", u"History", None))
        self.MajorInput.setItemText(13, QCoreApplication.translate("Stinder_Login", u"Information Systems", None))
        self.MajorInput.setItemText(14, QCoreApplication.translate("Stinder_Login", u"Journalism", None))
        self.MajorInput.setItemText(15, QCoreApplication.translate("Stinder_Login", u"Marketing", None))
        self.MajorInput.setItemText(16, QCoreApplication.translate("Stinder_Login", u"Nuclear Engineering", None))
        self.MajorInput.setItemText(17, QCoreApplication.translate("Stinder_Login", u"Physics", None))
        self.MajorInput.setItemText(18, QCoreApplication.translate("Stinder_Login", u"Religion", None))
        self.MajorInput.setItemText(19, QCoreApplication.translate("Stinder_Login", u"Sociology", None))
        self.MajorInput.setItemText(20, QCoreApplication.translate("Stinder_Login", u"Theatre", None))

        self.MajorInput.setPlaceholderText(QCoreApplication.translate("Stinder_Login", u"Major", None))
        self.ContinueBtn.setText(QCoreApplication.translate("Stinder_Login", u"Continue", None))
        self.errorLabel.setText("")
    # retranslateUi

