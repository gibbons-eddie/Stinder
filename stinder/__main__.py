import sqlite3
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtGui import QIcon
from sqlite3 import Error

from stinder.home import Ui_Stinder
from stinder.login import Ui_Stinder_Login


class LogInWindow(QDialog):
    def __init__(self):
        super(LogInWindow, self).__init__()
        self.setFixedSize(646, 476)
        self.setIcon()
        self.loginUi = Ui_Stinder_Login()
        self.loginUi.setupUi(self)

        self.loginUi.ContinueBtn.clicked.connect(self.handleLogin)

    def setIcon(self):
        appIcon = QIcon("resources/images/stinder_book_logo.png")
        self.setWindowIcon(appIcon)

    def handleLogin(self):
        # check if login is valid
        fName = self.loginUi.FirstNameInput.text()
        lName = self.loginUi.LastNameTb.text()
        email = self.loginUi.EmailInput.text()
        major = self.loginUi.MajorInput.currentText()

        if len(fName) == 0 or len(lName) == 0 or len(email) == 0:
            self.loginUi.errorLabel.setText("Please input all fields.")
        else:
            login_conn = sqlite3.connect("users.db")
            login_cur = login_conn.cursor()
            login_cur.execute(
                "INSERT OR REPLACE INTO contacts(Fname, Lname, major, email) VALUES (?, ?, ?, ?)", (fName, lName, major, email)
            )
            login_conn.commit()
            login_conn.close()
            print("Added to database")
            self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(646, 476)
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
        profileconn = sqlite3.connect("users.db")
        profilecur = profileconn.cursor()

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

        self.ui.NameLabel.setText(name)
        self.ui.EmailLabel.setText(profileEmail)
        self.ui.MajorLabel.setText(major)

    def setIcon(self):
        appIcon = QIcon("resources/images/stinder_book_logo.png")
        self.setWindowIcon(appIcon)

    def load_contacts(self):  # Place holder for the function to load the data of each user as they are 'swiped' through
        connection = sqlite3.connect("users.db")
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
    conn = sqlite3.connect("users.db")
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