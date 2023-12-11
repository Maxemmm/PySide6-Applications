from PySide6.QtCore import Qt, QSize, QUrl, QTranslator, QCoreApplication, QLocale
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices, QAction, QFont, QFontDatabase, QImage, QTransform
from PySide6.QtWidgets import QApplication, QLineEdit, QScrollArea, QAbstractButton, QGraphicsView, QWidget, QMainWindow, QFileSystemModel, QTreeWidgetItem, QSizePolicy, QToolBar, QLabel, QListWidgetItem, QFileDialog, QListView, QMenu, QProgressBar

from .gui.ui_register import Ui_RegisterWindow
from .gui.ui_singup import Ui_SignupWindow

class SignupWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Firebase SignUp")

        # WINDOW SETUP
        self.setFixedSize(self.size()) # Set window to fixed size

        # RETURN BUTTON SETUP
        self.ui.pushButton_2.clicked.connect(self.open_login_window)

    def open_login_window(self):
        self.login_window = MainWindow()
        self.login_window.show()

        # close signup window
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Firebase LogIn")

        # WINDOW SETUP
        self.setFixedSize(self.size()) # Set window to fixed size

        # USER FORM SETUP
        # Password icon setup
        reveal_action = self.ui.lineEdit_2.addAction(QIcon(":/icons/icons/eye-off.svg"), QLineEdit.ActionPosition.TrailingPosition)
        reveal_action.triggered.connect(lambda: self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal) if self.ui.lineEdit_2.echoMode() == QLineEdit.EchoMode.Password else self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password))
        reveal_action.triggered.connect(lambda: reveal_action.setIcon(QIcon(":/icons/icons/eye-off.svg")) if self.ui.lineEdit_2.echoMode() == QLineEdit.EchoMode.Password else reveal_action.setIcon(QIcon(":/icons/icons/eye.svg")))

        # SIGN UP BUTTON SETUP
        # TODO: change SIGN UP label to a QPushButton
        self.ui.label_2.mousePressEvent = self.open_signup_window

    def open_signup_window(self, event):
        self.signup_window = SignupWindow()
        self.signup_window.show()

        # close main window
        self.close()
