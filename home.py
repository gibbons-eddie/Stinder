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

from stinder.stinder_images_rc import *

class Ui_Stinder(object):
    counter = 0

    def setupUi(self, Stinder):
        if not Stinder.objectName():
            Stinder.setObjectName(u"Stinder")
        Stinder.resize(646, 476)
        Stinder.setAutoFillBackground(False)
        Stinder.setStyleSheet(
            u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(56, 0, 83, 255), stop:1 rgba(75, 0, 149, 255))")
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
        self.BrowseButton = QPushButton(self.frame)
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
        self.AboutLabel.setGeometry(QRect(10, 10, 600, 600))
        self.AboutLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "font: 700 13pt \"Nexa Text Demo\";")
        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.BrowseLabel = QLabel(self.BrowsePage)
        self.BrowseLabel.setObjectName(u"BrowseLabel")
        self.BrowseLabel.setGeometry(QRect(130, 90, 300, 240))
        self.BrowseLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                       "font: 700 15pt \"Nexa Text Demo\";")
        self.NextBottun = QPushButton(self.BrowsePage, clicked=lambda: self.next_user(lists, length))
        self.NextBottun.setObjectName(u"NextBottun")
        self.NextBottun.setGeometry(QRect(235, 370, 64, 20))
        self.NextBottun.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                      "background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
                                      "font: 9pt \"Nexa Text Demo\";")
        self.PrevButton = QPushButton(self.BrowsePage, clicked=lambda: self.prev_user(lists, length))
        self.PrevButton.setObjectName(u"PrevBottun")
        self.PrevButton.setGeometry(QRect(235, 340, 64, 20))
        self.PrevButton.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                              "background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
                                              "font: 9pt \"Nexa Text Demo\";")
        self.stackedWidget.addWidget(self.BrowsePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.label0 = QLabel(self.ProfilePage)
        self.label0.setObjectName(u"label0")
        self.label0.setGeometry(QRect(180, 10, 201, 41))
        self.label0.setStyleSheet(u"background-color: transparent;\n"
                                 "color: white;")
        self.label_2 = QLabel(self.ProfilePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 51, 21))
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
                                   "color: white;\n"
                                   "")
        self.line = QFrame(self.ProfilePage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 140, 480, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.ProfilePage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 190, 51, 21))
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
                                   "color: white;")
        self.line_2 = QFrame(self.ProfilePage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(40, 250, 450, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.ProfilePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 310, 51, 21))
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
                                   "color: white;")
        self.line_3 = QFrame(self.ProfilePage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(40, 370, 450, 3))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.NameLabel = QLabel(self.ProfilePage)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(40, 120, 451, 21))
        self.NameLabel.setStyleSheet(u"background-color: transparent;\n"
                                     "color: white;\n"
                                     "font-size: 18px;")
        self.EmailLabel = QLabel(self.ProfilePage)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setGeometry(QRect(40, 230, 431, 21))
        self.EmailLabel.setStyleSheet(u"background-color: transparent;\n"
                                      "color: white;\n"
                                      "font-size: 18px;")
        self.MajorLabel = QLabel(self.ProfilePage)
        self.MajorLabel.setObjectName(u"MajorLabel")
        self.MajorLabel.setGeometry(QRect(40, 350, 451, 21))
        self.MajorLabel.setStyleSheet(u"background-color: transparent;\n"
                                      "color: white;\n"
                                      "font-size: 18px;")
        self.stackedWidget.addWidget(self.ProfilePage)
        Stinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stinder)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Stinder)

    # setupUi

    def retranslateUi(self, Stinder):
        userL, i = self.list()
        Stinder.setWindowTitle(QCoreApplication.translate("Stinder", u"Stinder", None))
        self.actionTemp_Button.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_2.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_3.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.AboutButton.setText(QCoreApplication.translate("Stinder", u"About", None))
        self.BrowseButton.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.ProfileButton.setText(QCoreApplication.translate("Stinder", u"Profile", None))
        self.logo.setText("")
        self.AboutLabel.setText(QCoreApplication.translate("Stinder", u"About", None))
        self.BrowseLabel.setText(QCoreApplication.translate("Stinder", userL[0], None))
        self.NextBottun.setText(QCoreApplication.translate("Stinder", u"Next", None))
        self.PrevButton.setText(QCoreApplication.translate("Stinder", u"Previous", None))
        self.label0.setText(QCoreApplication.translate("Stinder",
                                                              u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Your Profile</span></p></body></html>",
                                                              None))
        self.label_2.setText(QCoreApplication.translate("Stinder",
                                                                u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Name</span></p></body></html>",
                                                                None))
        self.label_3.setText(QCoreApplication.translate("Stinder",
                                                                u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Email</span></p></body></html>",
                                                                None))
        self.label_4.setText(QCoreApplication.translate("Stinder",
                                                                u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Major</span></p></body></html>",
                                                                None))
        self.NameLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
        self.EmailLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
        self.MajorLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))

    def next_user(self, users, length):
        counter = self.counter
        counter = counter + 1
        if counter == length:
            counter = counter - 1
        self.counter = counter
        # print(users[counter])
        self.BrowseLabel.setText(users[counter])

    def prev_user(self, users, length):
        counter = self.counter
        if counter == 0:
            counter = counter + 1
        counter = counter - 1
        self.counter = counter
        self.BrowseLabel.setText(users[counter])

    def list(self):
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM contacts")
            users = []
            length = 0
            for row in cursor:
                user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + row[3]
                users.append(user)
                length = length + 1
            return users, length
