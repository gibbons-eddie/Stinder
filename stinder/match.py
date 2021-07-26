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


class Ui_LikeDialog(object):
    def setupUi(self, LikeDialog):
        if not LikeDialog.objectName():
            LikeDialog.setObjectName(u"LikeDialog")
        LikeDialog.resize(414, 305)
        LikeDialog.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.MatchVerticalLayout = QVBoxLayout(LikeDialog)
        self.MatchVerticalLayout.setObjectName(u"MatchVerticalLayout")
        self.MatchTitle = QLabel(LikeDialog)
        self.MatchTitle.setObjectName(u"MatchTitle")

        self.MatchVerticalLayout.addWidget(self.MatchTitle)

        self.titleSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.MatchVerticalLayout.addItem(self.titleSpacer)

        self.pushButton = QPushButton(LikeDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.MatchVerticalLayout.addWidget(self.pushButton)


        self.retranslateUi(LikeDialog)

        QMetaObject.connectSlotsByName(LikeDialog)
    # setupUi

    def retranslateUi(self, LikeDialog):
        LikeDialog.setWindowTitle(QCoreApplication.translate("LikeDialog", u"Dialog", None))
        self.MatchTitle.setText(QCoreApplication.translate("LikeDialog", u"You've got a match!", None))
        self.pushButton.setText(QCoreApplication.translate("LikeDialog", u"OK", None))
    # retranslateUi

