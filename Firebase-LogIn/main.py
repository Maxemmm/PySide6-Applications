from PySide6.QtCore import Qt, QSize, QUrl, QTranslator, QCoreApplication, QLocale
from PySide6.QtGui import QIcon, QPixmap, QDesktopServices, QAction, QFont, QFontDatabase, QImage, QTransform
from PySide6.QtWidgets import QApplication, QLineEdit, QScrollArea, QAbstractButton, QGraphicsView, QWidget, QMainWindow, QFileSystemModel, QTreeWidgetItem, QSizePolicy, QToolBar, QLabel, QListWidgetItem, QFileDialog, QListView, QMenu, QProgressBar

import firebase_admin
from core.LoginWindows import MainWindow

# https://www.youtube.com/watch?v=M1JjK9DXC6U : FIREBASE AUTHENTICATION
# https://console.firebase.google.com/u/3/ : FIREBASE CONSOLE
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()