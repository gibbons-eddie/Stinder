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
        Stinder.resize(1093, 641)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(33, 33, 34)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.ProfileButton = QPushButton(self.frame_2)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.gridLayout_3 = QGridLayout(self.AboutPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.AboutPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.AboutPage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.gridLayout_4 = QGridLayout(self.BrowsePage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.BrowsePage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: transparent;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

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

        self.gridLayout_6.addWidget(self.NextButton, 0, 1, 1, 1)

        self.FilterButton = QPushButton(self.frame_5)
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

        self.gridLayout_6.addWidget(self.FilterButton, 4, 2, 1, 1)

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

        self.gridLayout_6.addWidget(self.PreviousButton, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.CategotyButton = QPushButton(self.frame_5)
        self.CategotyButton.setObjectName(u"CategotyButton")
        self.CategotyButton.setStyleSheet(u"font: 500 13pt \"Nexa Bold\";\n"
                                          "background-color: rgb(98, 214, 81);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-radius: 5px; border: 2px rgb(33, 33, 34);\n"
                                          "border-bottom: 3px solid rgb(72, 156, 59);\n"
                                          "border-left:  1px solid rgb(72, 156, 59);\n"
                                          "border-right:  1px solid rgb(72, 156, 59);\n"
                                          "padding: 6px;")

        self.gridLayout_6.addWidget(self.CategotyButton, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 1, 2, 1, 1)

        self.FilterDropdown = QComboBox(self.frame_5)
        self.FilterDropdown.setObjectName(u"FilterDropdown")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilterDropdown.sizePolicy().hasHeightForWidth())
        self.FilterDropdown.setSizePolicy(sizePolicy)
        self.FilterDropdown.setMinimumSize(QSize(150, 0))
        self.FilterDropdown.setStyleSheet(u"background-color: white;\n"
                                          "")

        self.gridLayout_6.addWidget(self.FilterDropdown, 3, 2, 1, 1)

        self.gridLayout_4.addWidget(self.frame_5, 1, 1, 1, 1)

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
                                               "font: 15pt \"Segoe UI\";\n"
                                               "background: transparent;\n"
                                               "\n"
                                               "")

        self.horizontalLayout_10.addWidget(self.CardLabel_FirstName)

        self.Discover_FirstName = QLabel(self.frame_7)
        self.Discover_FirstName.setObjectName(u"Discover_FirstName")
        self.Discover_FirstName.setMinimumSize(QSize(189, 42))
        self.Discover_FirstName.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
                                          "")

        self.horizontalLayout_10.addWidget(self.Discover_FirstName)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.CardLabel_LastName = QLabel(self.frame_7)
        self.CardLabel_LastName.setObjectName(u"CardLabel_LastName")
        self.CardLabel_LastName.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_LastName.setStyleSheet(u"color: white; \n"
                                              "font: 15pt \"Segoe UI\";\n"
                                              "background: transparent;\n"
                                              "\n"
                                              "")

        self.horizontalLayout_11.addWidget(self.CardLabel_LastName)

        self.Discover_LastName = QLabel(self.frame_7)
        self.Discover_LastName.setObjectName(u"Discover_LastName")
        self.Discover_LastName.setMinimumSize(QSize(189, 42))
        self.Discover_LastName.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
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
                                           "font: 15pt \"Segoe UI\";\n"
                                           "background: transparent;\n"
                                           "\n"
                                           "")

        self.horizontalLayout_12.addWidget(self.CardLabel_Major)

        self.Discover_Major = QLabel(self.frame_7)
        self.Discover_Major.setObjectName(u"Discover_Major")
        self.Discover_Major.setMinimumSize(QSize(189, 42))
        self.Discover_Major.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
                                          "")

        self.horizontalLayout_12.addWidget(self.Discover_Major)

        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.CardLabel_Email = QLabel(self.frame_7)
        self.CardLabel_Email.setObjectName(u"CardLabel_Email")
        self.CardLabel_Email.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_Email.setStyleSheet(u"color: white; \n"
                                           "font: 15pt \"Segoe UI\";\n"
                                           "background: transparent;\n"
                                           "\n"
                                           "")

        self.horizontalLayout_13.addWidget(self.CardLabel_Email)

        self.Discover_Email = QLabel(self.frame_7)
        self.Discover_Email.setObjectName(u"Discover_Email")
        self.Discover_Email.setMinimumSize(QSize(189, 42))
        self.Discover_Email.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
                                          "")

        self.horizontalLayout_13.addWidget(self.Discover_Email)

        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.CardLabel_Year = QLabel(self.frame_7)
        self.CardLabel_Year.setObjectName(u"CardLabel_Year")
        self.CardLabel_Year.setMaximumSize(QSize(150, 16777215))
        self.CardLabel_Year.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
                                          "")

        self.horizontalLayout_14.addWidget(self.CardLabel_Year)

        self.Discover_Year = QLabel(self.frame_7)
        self.Discover_Year.setObjectName(u"Discover_Year")
        self.Discover_Year.setMinimumSize(QSize(189, 42))
        self.Discover_Year.setStyleSheet(u"color: white; \n"
                                          "font: 15pt \"Segoe UI\";\n"
                                          "background: transparent;\n"
                                          "\n"
                                          "")

        self.horizontalLayout_14.addWidget(self.Discover_Year)

        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

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
        font = QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: white; \n"
                                   "font: 30pt \"Segoe UI\";\n"
                                   "background: transparent;\n"
                                   "\n"
                                   "")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setStyleSheet(u"color: white; \n"
                                 "font: 15pt \"Segoe UI\";\n"
                                 "background: transparent;\n"
                                 "\n"
                                 "")

        self.verticalLayout.addWidget(self.label)

        self.UserName = QLabel(self.frame)
        self.UserName.setObjectName(u"UserName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy1)
        self.UserName.setMinimumSize(QSize(300, 0))
        self.UserName.setStyleSheet(u"color: white; \n"
                                    "font: 15pt \"Segoe UI\";\n"
                                    "background: transparent;\n"
                                    "border-bottom: 2px solid white;\n"
                                    "\n"
                                    "")

        self.verticalLayout.addWidget(self.UserName)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setStyleSheet(u"color: white; \n"
                                   "font: 15pt \"Segoe UI\";\n"
                                   "background: transparent;\n"
                                   "\n"
                                   "")

        self.verticalLayout.addWidget(self.label_2)

        self.UserEmail = QLabel(self.frame)
        self.UserEmail.setObjectName(u"UserEmail")
        sizePolicy1.setHeightForWidth(self.UserEmail.sizePolicy().hasHeightForWidth())
        self.UserEmail.setSizePolicy(sizePolicy1)
        self.UserEmail.setMinimumSize(QSize(300, 0))
        self.UserEmail.setStyleSheet(u"color: white; \n"
                                     "font: 15pt \"Segoe UI\";\n"
                                     "background: transparent;\n"
                                     "border-bottom: 2px solid white;\n"
                                     "\n"
                                     "")

        self.verticalLayout.addWidget(self.UserEmail)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setStyleSheet(u"color: white; \n"
                                   "font: 15pt \"Segoe UI\";\n"
                                   "background: transparent;\n"
                                   "\n"
                                   "")

        self.verticalLayout.addWidget(self.label_3)

        self.UserMajor = QLabel(self.frame)
        self.UserMajor.setObjectName(u"UserMajor")
        sizePolicy1.setHeightForWidth(self.UserMajor.sizePolicy().hasHeightForWidth())
        self.UserMajor.setSizePolicy(sizePolicy1)
        self.UserMajor.setMinimumSize(QSize(300, 0))
        self.UserMajor.setStyleSheet(u"color: white; \n"
                                     "font: 15pt \"Segoe UI\";\n"
                                     "background: transparent;\n"
                                     "border-bottom: 2px solid white;\n"
                                     "\n"
                                     "")

        self.verticalLayout.addWidget(self.UserMajor)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stackedWidget.addWidget(self.ProfilePage)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        Stinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stinder)

        self.stackedWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Stinder)

    # setupUi

    def retranslateUi(self, Stinder):
        a_user = self.students[0].split(',')
        Stinder.setWindowTitle(QCoreApplication.translate("Stinder", u"Stinder", None))
        self.actionTemp_Button.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_2.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.actionTemp_Button_3.setText(QCoreApplication.translate("Stinder", u"Temp Button", None))
        self.BrowseButton.setText(QCoreApplication.translate("Stinder", u"Browse", None))
        self.ProfileButton.setText(QCoreApplication.translate("Stinder", u"Profile", None))
        self.logo.setText("")
        self.AboutButton.setText(QCoreApplication.translate("Stinder", u"About", None))
        self.NextButton.setText(QCoreApplication.translate("Stinder", u"Next", None))
        self.FilterButton.setText(QCoreApplication.translate("Stinder", u"Filter", None))
        self.PreviousButton.setText(QCoreApplication.translate("Stinder", u"Previous", None))
        self.CategotyButton.setText(QCoreApplication.translate("Stinder", u"Category", None))
        self.FilterDropdown.setPlaceholderText(QCoreApplication.translate("Stinder", u"Filter By", None))
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
        self.label_4.setText(QCoreApplication.translate("Stinder", u"Your Profile", None))
        self.label.setText(QCoreApplication.translate("Stinder", u"Name:", None))
        self.UserName.setText("")
        self.label_2.setText(QCoreApplication.translate("Stinder", u"Email:", None))
        self.UserEmail.setText("")
        self.label_3.setText(QCoreApplication.translate("Stinder", u"Major:", None))
        self.UserMajor.setText("")
    # retranslateUi

    def next_user(self, users, length):
        counter = self.counter
        counter = counter + 1
        if counter == length:
            counter = counter - 1
        self.counter = counter
        user = users[counter].split(',')
        self.Discover_FirstName.setText(user[0])
        self.Discover_LastName.setText(user[1])
        self.Discover_Major.setText(user[2])
        self.Discover_Email.setText(user[3])
        self.Discover_Year.setText(user[4])


    def prev_user(self, users, length):
        counter = self.counter
        if counter == 0:
            counter = counter + 1
        counter = counter - 1
        self.counter = counter
        user = users[counter].split(',')
        self.Discover_FirstName.setText(user[0])
        self.Discover_LastName.setText(user[1])
        self.Discover_Major.setText(user[2])
        self.Discover_Email.setText(user[3])
        self.Discover_Year.setText(user[4])


    def list(self):
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT * FROM contacts")
            users = []
            length = 0
            for row in cursor:
                user = row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4]
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
                fltr_user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[
                    2] + "\n\nEmail: " + \
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
                    fltr_user = "First Name: " + row[0] + "\n\nLast Name: " + row[1] + "\n\nMajor: " + row[
                        2] + "\n\nEmail: " + \
                                row[3] + "\n\nYear: " + row[4]
                    fltr_users.append(fltr_user)
                    fltr_length = fltr_length + 1

            filter_conn.close()
            print(fltr_length, "students")
            self.students = fltr_users
            self.s_length = fltr_length
            self.prev_user(self.students, self.s_length)
            self.counter = 0
