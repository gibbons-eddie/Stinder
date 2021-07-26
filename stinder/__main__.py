import sqlite3
import os
import re
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtGui import QIcon, QFontDatabase, QFont
from sqlite3 import Error

from stinder.home import Ui_Stinder
from stinder.login import Ui_Stinder_Login
from stinder.resources.images import *
from stinder.resources.fonts import *

from stinder.stinder_images_rc import *

class LogInWindow(QDialog):
    def __init__(self):
        QFontDatabase.addApplicationFont("stinder/resources/fonts/NexaRegular.otf")
        QFontDatabase.addApplicationFont("stinder/resources/fonts/Nexa_Bold.otf")
        super(LogInWindow, self).__init__()
        self.setFixedSize(646, 476)
        self.setIcon()
        # self.setStinderFont()
        self.loginUi = Ui_Stinder_Login()
        self.loginUi.setupUi(self)

        # PAGE 1
        self.loginUi.LogInBtn.clicked.connect(self.handleSignIn)
        self.loginUi.SignUpBtn.clicked.connect(lambda: self.loginUi.loginPages.setCurrentWidget(self.loginUi.BasicPage))
        # PAGE 2
        self.loginUi.ContinueBtn.clicked.connect(self.handleBasicPage)
        # PAGE 3
        self.loginUi.ContinueBtnP2.clicked.connect(self.handleCreateAcct)
        self.emailAddr = None

    # Override close event to close whole app when dialog is closed
    def closeEvent(self, event):
        sys.exit()

    def setIcon(self):
        appIcon = QIcon("stinder/resources/images/stinder_book_logo.png")
        self.setWindowIcon(appIcon)

    def setStinderFont(self):
        appFont = (":/fonts/fonts/Nexa")
        self.setFont(appFont)

    def checkRegexEmail(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email)):
            print("valid email address")
        else:
            print("invalid email address")
            self.loginUi.errorLabelP1.setText("Invalid email address.")

    def handleSignIn(self):
        email = self.loginUi.LoginInput.text()
        exists_conn = sqlite3.connect("stinder/users.db")
        curs = exists_conn.cursor()
        self.emailAddr = email

        self.checkRegexEmail(email)
        if len(email) == 0:
            self.loginUi.errorLabelP1.setText("Please input an email address.")
        elif curs.execute("SELECT * FROM contacts WHERE email = ?", (email,)).fetchone():
            exists_conn.close()
            self.accept()
        else:
            self.loginUi.errorLabelP1.setText("Email address not found.")

    def handleBasicPage(self):
        fName = self.loginUi.FirstNameInput.text()
        lName = self.loginUi.LastNameTb.text()
        email = self.loginUi.EmailInput.text()
        major = self.loginUi.MajorInput.currentText()

        self.checkRegexEmail(email)
        if len(fName) == 0 or len(lName) == 0 or len(email) == 0 or major == "---Please Select Major---":
            self.loginUi.errorLabel.setText("Please input all fields.")
        else:
            self.loginUi.loginPages.setCurrentWidget(self.loginUi.DetailPage)

    def handleCreateAcct(self):
        # check if login is valid
        fName = self.loginUi.FirstNameInput.text()
        lName = self.loginUi.LastNameTb.text()
        email = self.loginUi.EmailInput.text()
        major = self.loginUi.MajorInput.currentText()
        year = self.loginUi.YearInput.currentText()
        method = self.loginUi.MethodInput.currentText()
        loc = self.loginUi.LocInput.currentText()
        job = self.loginUi.JobInput.currentText()
        day = self.loginUi.TimeInput.currentText()
        sHistory = self.loginUi.StudyHistInput.currentText()
        placeholder = "---Please Select---"

        if year == placeholder or method == placeholder or loc == placeholder or job == placeholder or \
                day == placeholder or sHistory == placeholder:
            self.loginUi.errorLabelP2.setText("Please input all fields.")
        else:
            login_conn = sqlite3.connect("stinder/users.db")
            login_cur = login_conn.cursor()
            login_cur.execute(
                "INSERT OR REPLACE INTO contacts(Fname, Lname, major, email, year, method, loc, job, day, sHistory) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (fName, lName, major, email, year, method, loc, job, day, sHistory)
            )
            login_conn.commit()
            login_conn.close()
            print("Added to database")
            # print(loc) # testing
            self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        QFontDatabase.addApplicationFont("stinder/resources/fonts/NexaRegular.otf")
        QFontDatabase.addApplicationFont("stinder/resources/fonts/Nexa_Bold.otf")
        super(MainWindow, self).__init__()
        self.resize(855, 538)
        self.setIcon()
        self.ui = Ui_Stinder()
        self.ui.setupUi(self)
        # PAGE 1
        self.ui.AboutButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.AboutPage))
        # PAGE 2
        self.ui.BrowseButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsePage))
        # PAGE 3
        self.ui.ProfileButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ProfilePage))

        # Adds information from database to profile page
        profileconn = sqlite3.connect("stinder/users.db")
        profilecur = profileconn.cursor()
        logininstance = LogInWindow()
        e = logininstance # How do i get the email input from the LoginWindow class?
        # This is the query to get user information once the email has been found
        # e = profilecur.execute("SELECT * FROM contacts WHERE email = ? ", (emailAddr,)).fetchone()

        maxid = profilecur.execute("SELECT MAX(rowid) FROM contacts")
        maxid = profilecur.fetchone()
        str = profilecur.execute("SELECT * FROM contacts WHERE rowid = ?", maxid)
        str = profilecur.fetchone()
        profileconn.close()
        fName = str[0]
        lName = str[1]
        major = str[2]
        profileEmail = str[3]
        name = fName + " " + lName

        self.ui.UserName.setText(name)
        self.ui.UserEmail.setText(profileEmail)
        self.ui.UserMajor.setText(major)

    def setIcon(self):
        appIcon = QIcon("stinder/resources/images/stinder_book_logo.png")
        self.setWindowIcon(appIcon)

    def load_contacts(self):  # Place holder for the function to load the data of each user as they are 'swiped' through
        connection = sqlite3.connect("stinder/users.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM contacts")
        print(cursor.fetchall())  # Delete later, this just shows all contacts in table

        # Add Functionality to link data to profile card once they are created
        # FOR REFERENCE: Database table format created from below
        #    CREATE TABLE contacts
        #        name VARCHAR(40) PRIMARY KEY NOT NULL,
        #        major VARCHAR(40) NOT NULL,
        #        classes VARCHAR(50),
        #        email VARCHAR(40)

        connection.close()


def createcontactstable(conn, tablesql):
    try:
        c = conn.cursor()
        c.execute(tablesql)
    except Error as e:
        print(e)


def fillcontacts():
    c.execute(
        "INSERT INTO contacts(name, major, classes, email) VALUES('Joe','Johnson', 'Computer Science', 'joe@ufl.edu')")
    c.execute(
        "INSERT INTO contacts(name, major, classes, email) VALUES('Jack', 'Smith', 'Data Science', 'jack@ufl.edu')")
    c.execute(
        "INSERT INTO contacts(name, major, classes, email) VALUES('Jill', 'Chen','Chemistry', 'jill@ufl.edu')")
    c.execute(
        "INSERT INTO contacts(name, major, classes, email) VALUES('Joseph','Brown', 'Biology', 'joseph@ufl.edu')")
    c.execute(
        "INSERT INTO contacts(name, major, classes, email) VALUES('Jorge', 'Parker','Computer Science', 'jorge@ufl.edu')")


if __name__ == "__main__":
    app = QApplication([])
    login = LogInWindow()

    if login.exec() == QDialog.Accepted:
        window = MainWindow()
        window.show()

    # Below block of code shows functionality for database
    conn = sqlite3.connect("stinder/users.db")
    c = conn.cursor()
    """ # I keep getting an error with the commented out code because it keeps trying to add data that is already there 

    tablequery = "CREATE TABLE IF NOT EXISTS contacts(name VARCHAR(40) PRIMARY KEY NOT NULL, major VARCHAR(40) NOT NULL, classes VARCHAR(50),email VARCHAR(40))"
    createcontactstable(conn, tablequery)
    fillcontacts() 
    rows = c.execute("SELECT * FROM contacts")
    for row in rows:
        print(row)
"""

    conn.close()
    # End of database functionality test -- delete block after testing because it won't be needed

    sys.exit(app.exec())
