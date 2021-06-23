import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlQuery

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


if __name__ == "__main__":
    app = QApplication([])

    # Below block of code shows functionality for database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM contacts")
    print(c.fetchall())

    conn.close()
    # End of database functionality test -- delete block after testing because it won't be needed

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())