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


def insert_data():
    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
        """
        INSERT INTO contacts (
            name,
            major,
            class,
            email
        )
        VALUES (?, ?, ?, ?)
        """
    )

    data = [
        ("Joe", "Computer Science", "COP3502", "joe@example.com"),
        ("Jack", "Sport Management", "CHM2045", "jack@example.com"),
        ("Lisa", "Data Science", "IUF1000", "lisa@example.com"),
        ("Allie", "Biology", "CHM2045", "allie@example.com"),
    ]
    for name, major, classes, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(major)
        insertDataQuery.addBindValue(classes)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()


if __name__ == "__main__":
    app = QApplication([])

    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("users.db")

    if not con.open():
        print("Database Error: %s" % con.lastError().databaseText())
        sys.exit(1)

    createTableQuery = QSqlQuery()
    createTableQuery.exec(
        """
        CREATE TABLE contacts (
            name VARCHAR(40) PRIMARY KEY NOT NULL,
            major VARCHAR(40) NOT NULL,
            classes VARCHAR(50),
            email VARCHAR(40)
        )
        """
    )

    print(con.tables())
    insert_data()

    print(con.record("contacts"))
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
