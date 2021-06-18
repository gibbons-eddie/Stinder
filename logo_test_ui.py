# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logoTest.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# import stinder logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 476)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 47, 90, 255), stop:1 rgba(84, 44, 179, 255))")
        MainWindow.setAnimated(True)
        self.actionTemp_Button = QAction(MainWindow)
        self.actionTemp_Button.setObjectName(u"actionTemp_Button")
        self.actionTemp_Button_2 = QAction(MainWindow)
        self.actionTemp_Button_2.setObjectName(u"actionTemp_Button_2")
        self.actionTemp_Button_3 = QAction(MainWindow)
        self.actionTemp_Button_3.setObjectName(u"actionTemp_Button_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 81, 481))
        self.frame.setStyleSheet(u"background-color:rgb(33, 33, 34)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.HomeButton = QPushButton(self.frame)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setGeometry(QRect(0, 1, 81, 41))
        self.BrowseButton = QPushButton(self.frame)
        self.BrowseButton.setObjectName(u"BrowseButton")
        self.BrowseButton.setGeometry(QRect(0, 51, 81, 41))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 100, 81, 41))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(80, 0, 561, 471))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.HomeLabel = QLabel(self.homePage)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setGeometry(QRect(180, 190, 161, 101))
        self.HomeLabel.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.homePage)
        self.BrowsePage = QWidget()
        self.BrowsePage.setObjectName(u"BrowsePage")
        self.label = QLabel(self.BrowsePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 220, 58, 16))
        self.stackedWidget.addWidget(self.BrowsePage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.label_2 = QLabel(self.ProfilePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 220, 58, 16))
        self.stackedWidget.addWidget(self.ProfilePage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTemp_Button.setText(QCoreApplication.translate("MainWindow", u"Temp Button", None))
        self.actionTemp_Button_2.setText(QCoreApplication.translate("MainWindow", u"Temp Button", None))
        self.actionTemp_Button_3.setText(QCoreApplication.translate("MainWindow", u"Temp Button", None))
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.BrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.HomeLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

