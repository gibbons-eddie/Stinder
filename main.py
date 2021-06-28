import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from sqlite3 import Error

from logo_test_ui import Ui_Stinder
from Login import Ui_Dialog


class LogInWindow(QDialog):
    def __init__(self):
        super(LogInWindow, self).__init__()
        self.loginUi = Ui_Dialog()
        self.loginUi.setupUi(self)
        self.loginUi.SignInBtn.clicked.connect(self.handleLogin)
        self.loginUi.CreateAcctTextbox.clicked.connect(self.handleSignUp)

        self.loginUi.SignUpBtn.clicked.connect(lambda: self.loginUi.stackedWidget.setCurrentWidget(self.loginUi.SignUp))
        self.loginUi.SignInBtn_2.clicked.connect(
            lambda: self.loginUi.stackedWidget.setCurrentWidget(self.loginUi.LogIn))

    def handleLogin(self):
        # check if login is valid?
        if True:
            self.accept()

    def handleSignUp(self):
        firstname = self.loginUi.FirstNameTextbox.text()
        lastname = self.loginUi.LastNameTextbox.text()
        email = self.loginUi.EmailAddrTextbox.text()
        phone = self.loginUi.PhoneNumberTextbox.text()
        major = self.loginUi.MajorBox.currentText()
        password = self.loginUi.PasswordTextbox.text()

        if True:
            self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Stinder()
        self.ui.setupUi(self)

        # PAGE 1
        self.ui.AboutButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.AboutPage))
        # PAGE 2
        self.ui.BrowseButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsePage))
        # PAGE 3
        self.ui.ProfileButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ProfilePage))

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