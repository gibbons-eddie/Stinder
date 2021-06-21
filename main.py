import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from logo_test_ui import Ui_Stinder


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Stinder()
        self.ui.setupUi(self)

        # PAGE 1
        self.ui.HomeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homePage))

        # PAGE 2
        self.ui.BrowseButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.BrowsePage))

        # PAGE 3
        self.ui.ProfileButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ProfilePage))


if __name__ == "__main__":
    app = QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
