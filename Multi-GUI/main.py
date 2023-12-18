from PySide6.QtWidgets import QApplication, QMainWindow
from ui_interface import Ui_MainWindow
from ui_settings import Ui_SettingsWindow
import sys

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # When clicking on actionOptions_2 button, call function
        self.ui.actionOptions_2.triggered.connect(self.open_options)

    def open_options(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
