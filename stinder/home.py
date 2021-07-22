# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoTest.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sqlite3
from os import linesep
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from stinder.stinder_images_rc import *

class Ui_Stinder(object):
    counter = 0
    students = 0
    s_length = 0

    def setupUi(self, Stinder):
        self.students, self.s_length = self.list()
        if not Stinder.objectName():
            Stinder.setObjectName(u"Stinder")
        Stinder.resize(903, 641)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(33, 33, 34)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProfileButton = QPushButton(self.frame_2, clicked=lambda: self.likes_counter())
        self.ProfileButton.setObjectName(u"ProfileButton")
        self.ProfileButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout.addWidget(self.ProfileButton, 2, 0, 1, 1)

        self.BrowseButton = QPushButton(self.frame_2)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout.addWidget(self.BrowseButton, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.logo = QLabel(self.frame_2)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(81, 41))
        self.logo.setMaximumSize(QSize(81, 41))
        self.logo.setPixmap(QPixmap(u":/logo/images/stinder_logo.png"))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 4, 0, 1, 1)

        self.AboutButton = QPushButton(self.frame_2)
        self.AboutButton.setObjectName(u"AboutButton")
        self.AboutButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout.addWidget(self.AboutButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.gridLayout_3 = QGridLayout(self.AboutPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.AboutPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 715, 816))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aboutlogo = QLabel(self.scrollAreaWidgetContents)
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

        self.verticalLayout_2.addWidget(self.aboutlogo)

        self.abouttext1 = QLabel(self.scrollAreaWidgetContents)
        self.abouttext1.setObjectName(u"abouttext1")
        self.abouttext1.setMinimumSize(QSize(15, 0))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.abouttext1.setFont(font)
        self.abouttext1.setAutoFillBackground(False)
        self.abouttext1.setStyleSheet(u"font: 500 15pt \"Nexa Bold\"")
        self.abouttext1.setScaledContents(False)
        self.abouttext1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.abouttext1)

        self.abouttext2 = QLabel(self.scrollAreaWidgetContents)
        self.abouttext2.setObjectName(u"abouttext2")
        self.abouttext2.setStyleSheet(u"font: 500 8pt \"Nexa\"")
        self.abouttext2.setScaledContents(False)
        self.abouttext2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.abouttext2.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.abouttext2)

        self.abouttext3 = QLabel(self.scrollAreaWidgetContents)
        self.abouttext3.setObjectName(u"abouttext3")
        self.abouttext3.setStyleSheet(u"font: 500 8pt \"Nexa Bold\"")

        self.verticalLayout_2.addWidget(self.abouttext3)

        self.aboutteamtext = QLabel(self.scrollAreaWidgetContents)
        self.aboutteamtext.setObjectName(u"aboutteamtext")
        self.aboutteamtext.setStyleSheet(u"font: 700 13pt \"Nexa\"")

        self.verticalLayout_2.addWidget(self.aboutteamtext)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.gridLayout_4 = QGridLayout(self.BrowsePage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.BrowsePage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: transparent;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(600, 350))
        self.frame_7.setStyleSheet(u"border-radius: 15px;\n"
"border: 2px solid rgb(73, 73, 75);\n"
"background-color:rgb(33, 33, 34);\n"
"padding: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.CardLabel_FirstName = QLabel(self.frame_7)
        self.CardLabel_FirstName.setObjectName(u"CardLabel_FirstName")
        self.CardLabel_FirstName.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_FirstName.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa Bold\";\n"
"background: transparent;\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.CardLabel_FirstName)

        self.Discover_FirstName = QLabel(self.frame_7)
        self.Discover_FirstName.setObjectName(u"Discover_FirstName")
        self.Discover_FirstName.setMinimumSize(QSize(189, 42))
        self.Discover_FirstName.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.Discover_FirstName)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.CardLabel_LastName = QLabel(self.frame_7)
        self.CardLabel_LastName.setObjectName(u"CardLabel_LastName")
        self.CardLabel_LastName.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_LastName.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa Bold\";\n"
"background: transparent;\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.CardLabel_LastName)

        self.Discover_LastName = QLabel(self.frame_7)
        self.Discover_LastName.setObjectName(u"Discover_LastName")
        self.Discover_LastName.setMinimumSize(QSize(189, 42))
        self.Discover_LastName.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_11.addWidget(self.Discover_LastName)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetFixedSize)
        self.CardLabel_Major = QLabel(self.frame_7)
        self.CardLabel_Major.setObjectName(u"CardLabel_Major")
        self.CardLabel_Major.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_Major.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa Bold\";\n"
"background: transparent;\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.CardLabel_Major)

        self.Discover_Major = QLabel(self.frame_7)
        self.Discover_Major.setObjectName(u"Discover_Major")
        self.Discover_Major.setMinimumSize(QSize(189, 42))
        self.Discover_Major.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_12.addWidget(self.Discover_Major)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.CardLabel_Email = QLabel(self.frame_7)
        self.CardLabel_Email.setObjectName(u"CardLabel_Email")
        self.CardLabel_Email.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_Email.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa Bold\";\n"
"background: transparent;\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.CardLabel_Email)

        self.Discover_Email = QLabel(self.frame_7)
        self.Discover_Email.setObjectName(u"Discover_Email")
        self.Discover_Email.setMinimumSize(QSize(189, 42))
        self.Discover_Email.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_13.addWidget(self.Discover_Email)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.CardLabel_Year = QLabel(self.frame_7)
        self.CardLabel_Year.setObjectName(u"CardLabel_Year")
        self.CardLabel_Year.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_Year.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa Bold\";\n"
"background: transparent;\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.CardLabel_Year)

        self.Discover_Year = QLabel(self.frame_7)
        self.Discover_Year.setObjectName(u"Discover_Year")
        self.Discover_Year.setMinimumSize(QSize(189, 42))
        self.Discover_Year.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_14.addWidget(self.Discover_Year)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)


        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.BrowsePage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: transparent;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.FilterButton = QPushButton(self.frame_5, clicked=lambda: self.handleFilter())
        self.FilterButton.setObjectName(u"FilterButton")
        self.FilterButton.setMaximumSize(QSize(500, 16777215))
        self.FilterButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout_6.addWidget(self.FilterButton, 5, 4, 1, 1)

        self.NextButton = QPushButton(self.frame_5, clicked=lambda: self.next_user(self.students, self.s_length))
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setMinimumSize(QSize(150, 0))
        self.NextButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout_6.addWidget(self.NextButton, 0, 4, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.frame_5)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalScrollBar, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.FilterDropdown = QComboBox(self.frame_5)
        self.FilterDropdown.addItem("")
        self.FilterDropdown.addItem("")
        self.FilterDropdown.addItem("")
        self.FilterDropdown.setObjectName(u"FilterDropdown")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FilterDropdown.sizePolicy().hasHeightForWidth())
        self.FilterDropdown.setSizePolicy(sizePolicy1)
        self.FilterDropdown.setMinimumSize(QSize(150, 0))
        self.FilterDropdown.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"\n"
"font: 500 13pt \"Nexa Bold\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 56, 140, 255), stop:1 rgba(0, 244, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"padding: 6px;\n"
"")

        self.gridLayout_6.addWidget(self.FilterDropdown, 5, 3, 1, 1)

        self.PreviousButton = QPushButton(self.frame_5, clicked=lambda: self.prev_user(self.students, self.s_length))
        self.PreviousButton.setObjectName(u"PreviousButton")
        self.PreviousButton.setMinimumSize(QSize(150, 0))
        self.PreviousButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")

        self.gridLayout_6.addWidget(self.PreviousButton, 0, 1, 1, 1)

        self.FilterLine = QLineEdit(self.frame_5)
        self.FilterLine.setObjectName(u"FilterLine")
        self.FilterLine.setLayoutDirection(Qt.LeftToRight)
        self.FilterLine.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
"background-color: rgb(98, 214, 81);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
"border-bottom: 3px solid rgb(72, 156, 59);\n"
"border-left:  1px solid rgb(72, 156, 59);\n"
"border-right:  1px solid rgb(72, 156, 59);\n"
"padding: 6px;")
        self.FilterLine.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.FilterLine, 5, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.BrowsePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.horizontalLayout = QHBoxLayout(self.ProfilePage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.ProfilePage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 0))
        self.frame.setStyleSheet(u"background: transparent;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_4.setFont(font1)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: white; \n"
"font: 30pt \"Nexa\";\n"
"background: transparent;\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.UserName = QLabel(self.frame)
        self.UserName.setObjectName(u"UserName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy2)
        self.UserName.setMinimumSize(QSize(300, 0))
        self.UserName.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"border-bottom: 2px solid white;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.UserName)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.UserEmail = QLabel(self.frame)
        self.UserEmail.setObjectName(u"UserEmail")
        sizePolicy2.setHeightForWidth(self.UserEmail.sizePolicy().hasHeightForWidth())
        self.UserEmail.setSizePolicy(sizePolicy2)
        self.UserEmail.setMinimumSize(QSize(300, 0))
        self.UserEmail.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"border-bottom: 2px solid white;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.UserEmail)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_3)

        self.UserMajor = QLabel(self.frame)
        self.UserMajor.setObjectName(u"UserMajor")
        sizePolicy2.setHeightForWidth(self.UserMajor.sizePolicy().hasHeightForWidth())
        self.UserMajor.setSizePolicy(sizePolicy2)
        self.UserMajor.setMinimumSize(QSize(300, 0))
        self.UserMajor.setStyleSheet(u"color: white; \n"
"font: 15pt \"Nexa\";\n"
"background: transparent;\n"
"border-bottom: 2px solid white;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.UserMajor)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.LikesLabel = QLabel(self.frame)
        self.LikesLabel.setObjectName(u"LikesLabel")
        self.LikesLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.LikesLabel)


        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stackedWidget.addWidget(self.ProfilePage)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        Stinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stinder)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Stinder)
    # setupUi

    def retranslateUi(self, Stinder):
        a_user = self.students[0]
        Stinder.setWindowTitle(QCoreApplication.translate("Stinder", u"Stinder", None))
        self.actionTemp_Button.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_2.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_3.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.ProfileButton.setText(QCoreApplication.translate("Stinder", u"Profile", None))
        self.BrowseButton.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.logo.setText("")
        self.AboutButton.setText(QCoreApplication.translate("Stinder", u"About", None))
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
        self.aboutteamtext.setText(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><br/><span style=\" font-size:12pt; text-decoration: underline;\">Meet Team Swipers</span></p><p align=\"center\"><span style=\" font-weight:400;\">Eddie Gibbons</span></p><p align=\"center\"><span style=\" font-weight:400;\">Allison Denham</span></p><p align=\"center\"><span style=\" font-weight:400;\">Carlos Echenique</span></p><p align=\"center\"><span style=\" font-weight:400;\">Wyatt Townsend</span><br/></p></body></html>", None))
        self.CardLabel_FirstName.setText(QCoreApplication.translate("Stinder", u"First Name:", None))
        self.Discover_FirstName.setText(a_user[0])
        self.CardLabel_LastName.setText(QCoreApplication.translate("Stinder", u"Last Name:", None))
        self.Discover_LastName.setText(a_user[1])
        self.CardLabel_Major.setText(QCoreApplication.translate("Stinder", u"Major:", None))
        self.Discover_Major.setText(a_user[2])
        self.CardLabel_Email.setText(QCoreApplication.translate("Stinder", u"Email:", None))
        self.Discover_Email.setText(a_user[3])
        self.CardLabel_Year.setText(QCoreApplication.translate("Stinder", u"Year:", None))
        self.Discover_Year.setText(a_user[4])
        self.FilterButton.setText(QCoreApplication.translate("Stinder", u"Filter", None))
        self.NextButton.setText(QCoreApplication.translate("Stinder", u"Next", None))
        self.FilterDropdown.setItemText(0, QCoreApplication.translate("Stinder", u"Filter By", None))
        self.FilterDropdown.setItemText(1, QCoreApplication.translate("Stinder", u"Major", None))
        self.FilterDropdown.setItemText(2, QCoreApplication.translate("Stinder", u"Year", None))

        self.FilterDropdown.setPlaceholderText(QCoreApplication.translate("Stinder", u"Filter By", None))
        self.PreviousButton.setText(QCoreApplication.translate("Stinder", u"Previous", None))
#if QT_CONFIG(whatsthis)
        self.FilterLine.setWhatsThis(QCoreApplication.translate("Stinder", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.FilterLine.setText("")
        self.FilterLine.setPlaceholderText(QCoreApplication.translate("Stinder", u"Category", None))
        self.label_4.setText(QCoreApplication.translate("Stinder", u"Profile", None))
        self.label.setText(QCoreApplication.translate("Stinder", u"Name:", None))
        self.UserName.setText("")
        self.label_2.setText(QCoreApplication.translate("Stinder", u"Email:", None))
        self.UserEmail.setText("")
        self.label_3.setText(QCoreApplication.translate("Stinder", u"Major:", None))
        self.UserMajor.setText("")
        self.LikesLabel.setText("")
    # retranslateUi

    def next_user(self, users, length):
        counter = self.counter
        counter = counter + 1
        if counter == length:
            counter = counter - 1
        self.counter = counter
        self.Discover_FirstName.setText(users[counter][0])
        self.Discover_LastName.setText(users[counter][1])
        self.Discover_Major.setText(users[counter][2])
        self.Discover_Email.setText(users[counter][3])
        self.Discover_Year.setText(users[counter][4])


    def prev_user(self, users, length):
        counter = self.counter
        if counter == 0:
            counter = counter + 1
        counter = counter - 1
        self.counter = counter
        self.Discover_FirstName.setText(users[counter][0])
        self.Discover_LastName.setText(users[counter][1])
        self.Discover_Major.setText(users[counter][2])
        self.Discover_Email.setText(users[counter][3])
        self.Discover_Year.setText(users[counter][4])

    def list(self):
        connection = sqlite3.connect("stinder/users.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM contacts")
            users = []
            length = 0
            for row in cursor:
                user_fN = row[0]
                user_lN = row[1]
                user_m = row[2]
                user_e = row[3]
                user_y = row[4]
                user_i = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                         row[3] + "\n\nYear: " + row[4]
                user = [user_fN, user_lN, user_m, user_e, user_y, user_i]
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
                fltr_user_fN = row[0]
                fltr_user_lN = row[1]
                fltr_user_m = row[2]
                fltr_user_e = row[3]
                fltr_user_y = row[4]
                fltr_user_i = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                    row[3] + "\n\nYear: " + row[4]
                fltr_user = [fltr_user_fN,  fltr_user_lN, fltr_user_m, fltr_user_e, fltr_user_y, fltr_user_i]
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
                    fltr_user_fN = row[0]
                    fltr_user_lN = row[1]
                    fltr_user_m = row[2]
                    fltr_user_e = row[3]
                    fltr_user_y = row[4]
                    fltr_user_i = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[2] + "\n\nEmail: " + \
                        row[3] + "\n\nYear: " + row[4]
                    fltr_user = [fltr_user_fN,  fltr_user_lN, fltr_user_m, fltr_user_e, fltr_user_y, fltr_user_i]
                    fltr_users.append(fltr_user)
                    fltr_length = fltr_length + 1

            filter_conn.close()
            print(fltr_length, "students")
            self.students = fltr_users
            self.s_length = fltr_length
            self.counter = 0
            self.prev_user(self.students, self.s_length)
    
    def likes_counter(self):
        u_email = self.UserEmail.text()
        
        likes_conn = sqlite3.connect("stinder/users.db")
        likes_cur = likes_conn.cursor()

        likes_cur.execute("SELECT like_fname, like_lname, like_email FROM likes where user_email = ?", (u_email,))
        likes_conn.commit()
        users_liked = []
        like_counter = 0

        for row in likes_cur:
            like_fN = row[0]
            like_lN = row[1]
            like_e = row[2]
            like = [like_fN, like_lN, like_e]
            users_liked.append(like)
            like_counter = like_counter + 1

        likes_conn.close()
        result = ""
        if like_counter == 1:
            result = "You have received " + str(like_counter) + " like!"
        else:
            result = "You have received " + str(like_counter) + " likes!"
        self.LikesLabel.setText(result)