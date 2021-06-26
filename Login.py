# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_updated.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

# import logo_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(646, 476)
        Dialog.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 646, 476))
        self.stackedWidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.StinderLogo = QLabel(self.page)
        self.StinderLogo.setObjectName(u"StinderLogo")
        self.StinderLogo.setGeometry(QRect(110, -40, 371, 201))
        self.StinderLogo.setStyleSheet(u"background-color: transparent;")
        self.StinderLogo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.StinderLogo.setScaledContents(True)
        self.InstructLabel = QLabel(self.page)
        self.InstructLabel.setObjectName(u"InstructLabel")
        self.InstructLabel.setGeometry(QRect(150, 100, 311, 41))
        self.InstructLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.FirstNameInput = QLineEdit(self.page)
        self.FirstNameInput.setObjectName(u"FirstNameInput")
        self.FirstNameInput.setGeometry(QRect(50, 160, 231, 41))
        self.FirstNameInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.LastNameTb = QLineEdit(self.page)
        self.LastNameTb.setObjectName(u"LastNameTb")
        self.LastNameTb.setGeometry(QRect(310, 160, 251, 41))
        self.LastNameTb.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.EmailInput = QLineEdit(self.page)
        self.EmailInput.setObjectName(u"EmailInput")
        self.EmailInput.setGeometry(QRect(50, 230, 511, 41))
        self.EmailInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
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
        self.MajorInput.setGeometry(QRect(50, 300, 511, 41))
        self.MajorInput.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.ContinueBtn = QPushButton(self.page)
        self.ContinueBtn.setObjectName(u"ContinueBtn")
        self.ContinueBtn.setGeometry(QRect(50, 370, 511, 31))
        self.ContinueBtn.setStyleSheet(u"background-color: rgb(106,255,121);\n"
"border-radius: 10px;")
        self.errorLabel = QLabel(self.page)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(60, 347, 491, 16))
        self.errorLabel.setStyleSheet(u"background-color: transparent;\n"
"color: red;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.StinderLogo.setText("")
        self.InstructLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt;\">Please fill out form to continue</span></p></body></html>", None))
        self.FirstNameInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.LastNameTb.setPlaceholderText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.EmailInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email Address", None))
        self.MajorInput.setItemText(0, QCoreApplication.translate("Dialog", u"Accounting", None))
        self.MajorInput.setItemText(1, QCoreApplication.translate("Dialog", u"Aerospace Engineering", None))
        self.MajorInput.setItemText(2, QCoreApplication.translate("Dialog", u"Anthropology", None))
        self.MajorInput.setItemText(3, QCoreApplication.translate("Dialog", u"Biology", None))
        self.MajorInput.setItemText(4, QCoreApplication.translate("Dialog", u"Botany", None))
        self.MajorInput.setItemText(5, QCoreApplication.translate("Dialog", u"Chemistry", None))
        self.MajorInput.setItemText(6, QCoreApplication.translate("Dialog", u"Computer Science", None))
        self.MajorInput.setItemText(7, QCoreApplication.translate("Dialog", u"Data Science", None))
        self.MajorInput.setItemText(8, QCoreApplication.translate("Dialog", u"Economics", None))
        self.MajorInput.setItemText(9, QCoreApplication.translate("Dialog", u"Education", None))
        self.MajorInput.setItemText(10, QCoreApplication.translate("Dialog", u"Finance", None))
        self.MajorInput.setItemText(11, QCoreApplication.translate("Dialog", u"Geography", None))
        self.MajorInput.setItemText(12, QCoreApplication.translate("Dialog", u"History", None))
        self.MajorInput.setItemText(13, QCoreApplication.translate("Dialog", u"Information Systems", None))
        self.MajorInput.setItemText(14, QCoreApplication.translate("Dialog", u"Journalism", None))
        self.MajorInput.setItemText(15, QCoreApplication.translate("Dialog", u"Marketing", None))
        self.MajorInput.setItemText(16, QCoreApplication.translate("Dialog", u"Nuclear Engineering", None))
        self.MajorInput.setItemText(17, QCoreApplication.translate("Dialog", u"Physics", None))
        self.MajorInput.setItemText(18, QCoreApplication.translate("Dialog", u"Religion", None))
        self.MajorInput.setItemText(19, QCoreApplication.translate("Dialog", u"Sociology", None))
        self.MajorInput.setItemText(20, QCoreApplication.translate("Dialog", u"Theatre", None))

        self.MajorInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Major", None))
        self.ContinueBtn.setText(QCoreApplication.translate("Dialog", u"Continue", None))
        self.errorLabel.setText("")
    # retranslateUi

