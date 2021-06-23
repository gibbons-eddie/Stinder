import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from sqlite3 import Error

from logo_test_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PAGE 1
        self.ui.HomeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))
        # PAGE 2
        self.ui.BrowseButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsePage))
        # PAGE 3
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ProfilePage))

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World",
        #                              alignment=QtCore.Qt.AlignCenter)

        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)

        # self.button.clicked.connect(self.magic)

    # @QtCore.Slot()
    # def magic(self):
    # self.text.setText(random.choice(self.hello))

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
    c.execute("INSERT INTO contacts(name, major, classes, email) VALUES('Joe', 'Computer Science', 'COP3502', 'joe@ufl.edu')")
    c.execute("INSERT INTO contacts(name, major, classes, email) VALUES('Jack', 'Data Science', 'IUL1000', 'jack@ufl.edu')")
    c.execute("INSERT INTO contacts(name, major, classes, email) VALUES('Jill', 'Chemistry', 'CHM2532', 'jill@ufl.edu')")
    c.execute("INSERT INTO contacts(name, major, classes, email) VALUES('Joseph', 'Biology', 'CHM2531', 'joseph@ufl.edu')")
    c.execute("INSERT INTO contacts(name, major, classes, email) VALUES('Jorge', 'Computer Science', 'COP3503', 'jorge@ufl.edu')")

if __name__ == "__main__":
    app = QApplication([])

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

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
