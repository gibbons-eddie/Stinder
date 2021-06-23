import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from logo_test_ui import Ui_Stinder
from Login import Ui_Dialog


class LogInWindow(QDialog):
    def __init__(self):
        super(LogInWindow, self).__init__()
        self.loginUi = Ui_Dialog()
        self.loginUi.setupUi(self)
        self.loginUi.SignInBtn.clicked.connect(self.handleLogin)

        self.loginUi.SignUpBtn.clicked.connect(lambda: self.loginUi.stackedWidget.setCurrentWidget(self.loginUi.SignUp))
        self.loginUi.SignInBtn_2.clicked.connect(lambda: self.loginUi.stackedWidget.setCurrentWidget(self.loginUi.LogIn))

    def handleLogin(self):
        # check if login is valid?
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


if __name__ == "__main__":
    app = QApplication([])
    login = LogInWindow()

    if login.exec() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
