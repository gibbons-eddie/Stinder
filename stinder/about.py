# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import stinder_images_rc

class Ui_Stinder(object):
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
        self.stackedWidget.setGeometry(QRect(80, 0, 571, 481))
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.scrollArea = QScrollArea(self.AboutPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 561, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 542, 1006))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutlogo = QLabel(self.scrollAreaWidgetContents_3)
        self.aboutlogo.setObjectName(u"aboutlogo")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.aboutlogo.sizePolicy().hasHeightForWidth())
        self.aboutlogo.setSizePolicy(sizePolicy)
        self.aboutlogo.setMinimumSize(QSize(541, 200))
        self.aboutlogo.setTextFormat(Qt.AutoText)
        self.aboutlogo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.aboutlogo.setScaledContents(True)
        self.aboutlogo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.aboutlogo)

        self.abouttext1 = QLabel(self.scrollAreaWidgetContents_3)
        self.abouttext1.setObjectName(u"abouttext1")
        self.abouttext1.setMinimumSize(QSize(15, 0))
        font = QFont()
        font.setFamilies([u"Nexa Bold"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.abouttext1.setFont(font)
        self.abouttext1.setAutoFillBackground(False)
        self.abouttext1.setStyleSheet(u"font: 500 15pt \"Nexa Bold\"")
        self.abouttext1.setScaledContents(False)
        self.abouttext1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.abouttext1)

        self.abouttext2 = QLabel(self.scrollAreaWidgetContents_3)
        self.abouttext2.setObjectName(u"abouttext2")
        self.abouttext2.setStyleSheet(u"font: 500 8pt \"Nexa Demo\"")
        self.abouttext2.setScaledContents(False)
        self.abouttext2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.abouttext2.setWordWrap(False)

        self.verticalLayout.addWidget(self.abouttext2)

        self.abouttext3 = QLabel(self.scrollAreaWidgetContents_3)
        self.abouttext3.setObjectName(u"abouttext3")
        self.abouttext3.setStyleSheet(u"font: 500 8pt \"Nexa Bold\"")

        self.verticalLayout.addWidget(self.abouttext3)

        self.aboutteamtext = QLabel(self.scrollAreaWidgetContents_3)
        self.aboutteamtext.setObjectName(u"aboutteamtext")
        self.aboutteamtext.setStyleSheet(u"font: 700 13pt \"Nexa Text Demo\"")

        self.verticalLayout.addWidget(self.aboutteamtext)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.BrowseLabel = QLabel(self.BrowsePage)
        self.BrowseLabel.setObjectName(u"BrowseLabel")
        self.BrowseLabel.setGeometry(QRect(230, 220, 58, 16))
        self.BrowseLabel.setStyleSheet(u"color: rgb(255, 255, 255)")
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
#if QT_CONFIG(tooltip)
        self.aboutlogo.setToolTip(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.aboutlogo.setWhatsThis(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.aboutlogo.setText("")
        self.abouttext1.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Do you hate having to group up with </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">students you don't know?</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Have you ever been stuck doing </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">all the work?</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Us too.</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.abouttext2.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Stinder aims to solve those problems for those who would like to pair up with those with </span></p><p align=\"center\"><span style=\" font-weight:400;\">similar work ethic and motivations. </span></p><p align=\"center\"><span style=\" font-weight:400;\">Fill out your student information for your profile and browse through your class population </span></p><p align=\"center\"><span style=\" font-weight:400;\">for those with similar qualities to work as effectively as possible in a group setting!</span></p><p align=\"center\"><span style=\" font-weight:400;\">Filter students by major, coursework, schedule and more* to </span></p><p align=\"center\"><span style=\" font-weight:400;\">find your perfect match!</span><br/></p></body></html>", None))
        self.abouttext3.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Stinder. </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Never have a bad (study) date again.</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.aboutteamtext.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:12pt; text-decoration: underline;\">Meet Team Swipers</span></p><p align=\"center\"><span style=\" font-weight:400;\">Eddie Gibbons</span></p><p align=\"center\"><span style=\" font-weight:400;\">Allison Denham</span></p><p align=\"center\"><span style=\" font-weight:400;\">Carlos Echenique</span></p><p align=\"center\"><span style=\" font-weight:400;\">Wyatt Townsend</span></p><p align=\"center\"><span style=\" font-weight:400;\">Yuchen Xiong</span><br/></p></body></html>", None))
        self.BrowseLabel.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.label.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Profile</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Email</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Major</span></p></body></html>", None))
        self.NameLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
        self.EmailLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
        self.MajorLabel.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

