import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtGui import QColor, QPalette
from ColorTheme import ColorTheme


from ui_interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Make sure to call setupUi to set up the UI components
        
        # Set the stylesheet to Fusion
        stylesheet = "Fusion"

        # Set up the default color theme to light with the light palette
        QApplication.instance().setStyle(stylesheet)
        QApplication.instance().setPalette(ColorTheme().get_light_palette())

        self.ui.comboBox.currentIndexChanged.connect(self.toggleTheme)

    def toggleTheme(self):
        # Set the stylesheet to Fusion
        stylesheet = "Fusion"
        
        # Determine the selected theme from the combobox
        selectedTheme = self.ui.comboBox.currentText()

        # Use Fusion style with the native dark color palette
        if selectedTheme == "Dark":
            QApplication.instance().setStyle(stylesheet)
            QApplication.instance().setPalette(ColorTheme().get_dark_palette())
        elif selectedTheme == "Light":
            QApplication.instance().setStyle(stylesheet)
            QApplication.instance().setPalette(ColorTheme().get_light_palette())
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
