# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Match.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from stinder.stinder_images_rc import *
from stinder.home import *

class Ui_LikeDialog(object):
    def setupUi(self, LikeDialog):
        if not LikeDialog.objectName():
            LikeDialog.setObjectName(u"LikeDialog")
        LikeDialog.resize(646, 439)
        LikeDialog.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.MatchVerticalLayout = QVBoxLayout(LikeDialog)
        self.MatchVerticalLayout.setObjectName(u"MatchVerticalLayout")
        self.MatchTitle = QLabel(LikeDialog)
        self.MatchTitle.setObjectName(u"MatchTitle")
        font = QFont()
        font.setBold(True)
        self.MatchTitle.setFont(font)
        self.MatchTitle.setStyleSheet(u"")
        self.MatchTitle.setScaledContents(True)

        self.MatchVerticalLayout.addWidget(self.MatchTitle)

        self.LogoImage = QLabel(LikeDialog)
        self.LogoImage.setObjectName(u"LogoImage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogoImage.sizePolicy().hasHeightForWidth())
        self.LogoImage.setSizePolicy(sizePolicy)
        self.LogoImage.setStyleSheet(u"padding: 30px 70px;")
        self.LogoImage.setPixmap(QPixmap(u":/logo/images/stinder_book_logo.png"))
        self.LogoImage.setScaledContents(True)
        self.LogoImage.setMargin(0)
        self.LogoImage.setIndent(-2)

        self.MatchVerticalLayout.addWidget(self.LogoImage, 0, Qt.AlignHCenter)

        self.InfoLabel = QLabel(LikeDialog)
        self.InfoLabel.setObjectName(u"InfoLabel")

        self.MatchVerticalLayout.addWidget(self.InfoLabel)

        self.buttonSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.MatchVerticalLayout.addItem(self.buttonSpacer)

        self.OKButton = QPushButton(LikeDialog)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setStyleSheet(u"")

        self.MatchVerticalLayout.addWidget(self.OKButton)


        self.retranslateUi(LikeDialog)

        QMetaObject.connectSlotsByName(LikeDialog)
    # setupUi

    def retranslateUi(self, LikeDialog):
        LikeDialog.setWindowTitle(QCoreApplication.translate("LikeDialog", u"You've got a match!", None))
        self.MatchTitle.setText(QCoreApplication.translate("LikeDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">You've got a match!</span></p></body></html>", None))
        self.LogoImage.setText("")
        self.InfoLabel.setText(QCoreApplication.translate("LikeDialog", u"TextLabel", None))
        self.OKButton.setText(QCoreApplication.translate("LikeDialog", u"OK", None))
    # retranslateUi

    def setUserInfo(self, user):
        self.InfoLabel.setText(user)

