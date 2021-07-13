# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoTest.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from os import linesep
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import sqlite3

from stinder.stinder_images_rc import *

class Ui_Stinder(object):
    counter = 0
    students = 0
    s_length = 0

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
        self.students, self.s_length = self.list()
        self.BrowseButton = QPushButton(self.frame)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setGeometry(QRect(0, 51, 81, 41))
        self.BrowseButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
                                        "font: 500 13pt \"Nexa Bold\";\n"
                                        "")
        self.ProfileButton = QPushButton(self.frame, clicked=lambda: self.likes_counter())
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
                                      "font: 700 13pt \"Nexa Text Demo\";")
        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.BrowseLabel = QLabel(self.BrowsePage)
        self.BrowseLabel.setObjectName(u"BrowseLabel")
        self.BrowseLabel.setGeometry(QRect(130, 30, 300, 300))
        self.BrowseLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                       "font: 700 12pt \"Nexa Text Demo\";")
        self.NextBottun = QPushButton(self.BrowsePage, clicked=lambda: self.next_user(self.students, self.s_length))
        self.NextBottun.setObjectName(u"NextBottun")
        self.NextBottun.setGeometry(QRect(235, 370, 64, 20))
        self.NextBottun.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                      "background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
                                      "font: 9pt \"Nexa Text Demo\";")
        self.PrevButton = QPushButton(self.BrowsePage, clicked=lambda: self.prev_user(self.students, self.s_length))
        self.PrevButton.setObjectName(u"PrevBottun")
        self.PrevButton.setGeometry(QRect(235, 340, 64, 20))
        self.PrevButton.setStyleSheet(u"color:rgb(255, 255, 255);\n"
                                              "background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
                                              "font: 9pt \"Nexa Text Demo\";")
        self.FilterDropdown = QComboBox(self.BrowsePage)
        self.FilterDropdown.addItem("")
        self.FilterDropdown.addItem("")
        self.FilterDropdown.addItem("")
        self.FilterDropdown.addItem("")
        self.FilterDropdown.setObjectName(u"FilterDropdown")
        self.FilterDropdown.setGeometry(QRect(130, 400, 103, 32))
        self.FilterDropdown.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"padding: 5px;")
        self.FilterLine = QLineEdit(self.BrowsePage)
        self.FilterLine.setObjectName(u"FilterLine")
        self.FilterLine.setGeometry(QRect(260, 400, 113, 31))
        self.FilterLine.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"font: 500 13pt \"Nexa Bold\";\n"
"padding: 5px;")
        self.FilterBtn = QPushButton(self.BrowsePage, clicked=lambda: self.handleFilter())
        self.FilterBtn.setObjectName(u"FilterBtn")
        self.FilterBtn.setGeometry(QRect(30, 390, 81, 51))
        self.FilterBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"font: 500 13pt \"Nexa Bold\";\n"
"\n"
"")
        self.stackedWidget.addWidget(self.BrowsePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.label = QLabel(self.ProfilePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 10, 201, 41))
        self.label.setStyleSheet(u"background-color: transparent;\n"
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
        self.line_2.setGeometry(QRect(40, 250, 480, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.ProfilePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 310, 51, 21))
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.line_3 = QFrame(self.ProfilePage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(40, 370, 480, 3))
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
        self.LikesLabel = QLabel(self.ProfilePage)
        self.LikesLabel.setObjectName(u"LikesLabel")
        self.LikesLabel.setGeometry(QRect(40, 420, 251, 21))
        self.LikesLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")
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
        self.BrowseLabel.setText(QCoreApplication.translate("Stinder", self.students[0], None))
        self.NextBottun.setText(QCoreApplication.translate("Stinder", u"Next", None))
        self.PrevButton.setText(QCoreApplication.translate("Stinder", u"Previous", None))
        self.FilterBtn.setText(QCoreApplication.translate("Stinder", u"Filter", None))
        self.FilterDropdown.setItemText(0, QCoreApplication.translate("Stinder", u"Filter By", None))
        self.FilterDropdown.setItemText(1, QCoreApplication.translate("Stinder", u"Major", None))
        self.FilterDropdown.setItemText(2, QCoreApplication.translate("Stinder", u"Year", None))

        self.FilterDropdown.setPlaceholderText(QCoreApplication.translate("Stinder", u"Filter By", None))
        self.FilterLine.setPlaceholderText(QCoreApplication.translate("Stinder", u"Category", None))
        self.label.setText(QCoreApplication.translate("Stinder",
                                                              u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">Profile</span></p></body></html>",
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
        self.LikesLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))

    def next_user(self, users, length):
        counter = self.counter
        counter = counter + 1
        if counter == length:
            counter = counter - 1
        self.counter = counter
        self.BrowseLabel.setText(users[counter])

    def prev_user(self, users, length):
        counter = self.counter
        if counter == 0:
            counter = counter + 1
        counter = counter - 1
        self.counter = counter
        self.BrowseLabel.setText(users[counter])

    def list(self):
        connection = sqlite3.connect("stinder/users.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM contacts")
            users = []
            length = 0
            for row in cursor:
                user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                       row[3] + "\n\nYear: " + row[4]
                users.append(user)
                length = length + 1
            return users, length

    def handleFilter(self):
        cat = self.FilterDropdown.currentText()
        line = self.FilterLine.text()

        if (cat != 'Filter By') & (line != 'Category'):
            filter_conn = sqlite3.connect("stinder/users.db")
            filter_cur = filter_conn.cursor()
            print("Filtered by " + line) 
            filter_cur.execute("SELECT * FROM contacts WHERE " + cat + " == ?", (line,))
            filter_conn.commit()
            fltr_users = []
            fltr_length = 0
            for row in filter_cur:
                fltr_user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                    row[3] + "\n\nYear: " + row[4]
                fltr_users.append(fltr_user)
                fltr_length = fltr_length + 1
                
            if fltr_length == 0:
                # self.errorLabel.setText("No results matching your search.")
                print("No results matching your search.")
                filter_cur.execute("SELECT * FROM contacts")
                filter_conn.commit()
                fltr_users = []
                fltr_length = 0
                for row in filter_cur:
                    fltr_user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                        row[3] + "\n\nYear: " + row[4]
                    fltr_users.append(fltr_user)
                    fltr_length = fltr_length + 1

            filter_conn.close()
            print(fltr_length, "students")
            self.students = fltr_users
            self.s_length = fltr_length
            self.prev_user(self.students, self.s_length)
            self.counter = 0
    
    def likes_counter(self):
        u_email = self.EmailLabel.text()
        
        likes_conn = sqlite3.connect("stinder/users.db")
        likes_cur = likes_conn.cursor()

        likes_cur.execute("SELECT like_fname, like_lname, like_email FROM likes where user_email = ?", (u_email,))
        likes_conn.commit()
        users_liked = []
        like_counter = 0

        for row in likes_cur:
            like = row[0] + "\n\n" + row[1] + "\n\n" + row[2]
            users_liked.append(like)
            like_counter = like_counter + 1

        likes_conn.close()
        result = ""
        if like_counter == 1:
            result = "You have received " + str(like_counter) + " like!"
        else:
            result = "You have received " + str(like_counter) + " likes!"
        self.LikesLabel.setText(result)
