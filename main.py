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


def insert_data(n, m, c, e):
    query = QSqlQuery()
    query.exec(
        f"""INSERT INTO contacts (name, major, classes, email)
        VALUES ('{n}', '{m}', '{c}', '{e}')"""
    )

if __name__ == "__main__":
    app = QApplication(sys.argv)


    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
