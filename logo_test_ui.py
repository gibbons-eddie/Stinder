# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoTest.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import sqlite3


import stinder_images_rc

class Ui_Stinder(object):
    counter = 0
    def setupUi(self, Stinder):
        if not Stinder.objectName():
            Stinder.setObjectName(u"Stinder")
        Stinder.resize(646, 476)
        Stinder.setAutoFillBackground(False)
        Stinder.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
        Stinder.setAnimated(True)
        self.actionTemp_Button = QAction(Stinder)
        self.actionTemp_Button.setObjectName(u"actionTemp_Button")
        self.actionTemp_Button_2 = QAction(Stinder)
        self.actionTemp_Button_2.setObjectName(u"actionTemp_Button_2")
        self.actionTemp_Button_3 = QAction(Stinder)
        self.actionTemp_Button_3.setObjectName(u"actionTemp_Button_3")
        self.centralwidget = QWidget(Stinder)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 81, 481))
        self.frame.setStyleSheet(u"background-color:rgb(33, 33, 34)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.AboutButton = QPushButton(self.frame)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setGeometry(QRect(0, 1, 81, 41))
        self.AboutButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"font: 700 13pt \"Nexa Text Demo\";\n"
"")
        lists, length = self.list()
        self.BrowseButton = QPushButton(self.frame, clicked= lambda: self.next_user(lists, length))
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setGeometry(QRect(0, 51, 81, 41))
        self.BrowseButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"font: 500 13pt \"Nexa Bold\";\n"
"")
        self.ProfileButton = QPushButton(self.frame)
        self.ProfileButton.setObjectName(u"ProfileButton")
        self.ProfileButton.setGeometry(QRect(0, 100, 81, 41))
        self.ProfileButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"font: 700 13pt \"Nexa Bold\";")
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 430, 81, 41))
        self.logo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.logo.setScaledContents(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(80, 0, 561, 471))
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.AboutLabel = QLabel(self.AboutPage)
        self.AboutLabel.setObjectName(u"AboutLabel")
        self.AboutLabel.setGeometry(QRect(180, 190, 161, 101))
        self.AboutLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 13pt \"Nexa Demo\";")
        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.BrowseLabel = QLabel(self.BrowsePage)
        self.BrowseLabel.setObjectName(u"BrowseLabel")
        self.BrowseLabel.setGeometry(QRect(180, 120, 200, 160))
        self.BrowseLabel.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.stackedWidget.addWidget(self.BrowsePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.ProfileLabel = QLabel(self.ProfilePage)
        self.ProfileLabel.setObjectName(u"ProfileLabel")
        self.ProfileLabel.setGeometry(QRect(250, 220, 58, 16))
        self.ProfileLabel.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.stackedWidget.addWidget(self.ProfilePage)
        Stinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stinder)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Stinder)
    # setupUi


    def retranslateUi(self, Stinder):
        Stinder.setWindowTitle(QCoreApplication.translate("Stinder", u"Stinder", None))
        self.actionTemp_Button.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_2.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_3.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.AboutButton.setText(QCoreApplication.translate("Stinder", u"About", None))
        self.BrowseButton.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.ProfileButton.setText(QCoreApplication.translate("Stinder", u"Profile", None))
        self.logo.setText("")
        self.AboutLabel.setText(QCoreApplication.translate("Stinder", u"About", None))
        self.BrowseLabel.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.ProfileLabel.setText(QCoreApplication.translate("Stinder", u"Profile", None))

    def next_user(self, users, length):
        counter = self.counter
        if counter == length:
            counter = counter - 1
        print(users[counter])
        self.BrowseLabel.setText(users[counter])
        self.counter = counter + 1

    def list(self):
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM contacts")
            users = []
            length = 0
            for row in cursor:
                user = "Name: " + row[0] + "\n\nMajor: " + row[1] + "\n\nEmail: " + row[2]
                users.append(user)
                length = length + 1
            return users, length

