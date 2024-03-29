import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QFileDialog
from PySide6.QtCore import QTranslator, Qt
from PySide6.QtGui import QKeySequence, QAction, QActionGroup
import json

# Import the UI module generated by pyside6-uic
from ui_interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load translations from JSON
        self.translations = self.load_translations("en-us")

        # Load the UI from the converted Python file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create language menu
        self.language_menu = self.ui.menuLanguage

        # Create actions for language menu
        self.action_english = self.ui.actionEnglish
        self.action_french = self.ui.actionFrench
        self.action_chinese = self.ui.actionChinese
        self.action_arabic = self.ui.actionArabic

        # Add actions to the menu with exclusive checkable behavior
        # set action checkable
        self.action_english.setCheckable(True)
        self.action_french.setCheckable(True)
        self.action_chinese.setCheckable(True)
        self.action_arabic.setCheckable(True)
        # set action checked
        self.action_english.setChecked(True)

        # create a QActionGroup
        self.language_group = QActionGroup(self)
        # add actions to the QActionGroup
        self.language_group.addAction(self.action_english)
        self.language_group.addAction(self.action_french)
        self.language_group.addAction(self.action_chinese)
        self.language_group.addAction(self.action_arabic)

        # Connect actions to slots
        self.action_english.triggered.connect(lambda: self.change_language("en-us"))
        self.action_french.triggered.connect(lambda: self.change_language("fr-fr"))
        self.action_chinese.triggered.connect(lambda: self.change_language("zh-cn"))
        self.action_arabic.triggered.connect(lambda: self.change_language("ar-AE"))

        # Apply initial translations
        self.translate_ui()

    def load_translations(self, language):
        try:
            with open('translations.json', 'r', encoding='utf-8') as file:
                translations = json.load(file)
                return translations.get(language, {})
        except FileNotFoundError:
            print("Translation file not found.")
            return {}

    def change_language(self, language):
        # Load translations from JSON and update UI
        self.translations = self.load_translations(language)
        self.translate_ui()

    def translate_ui(self):
        # Update UI elements with translated strings
        self.ui.pushButton.setText(self.translations.get("pushButton", ""))
        self.ui.pushButton_2.setText(self.translations.get("pushButton_2", ""))
        self.ui.label.setText(self.translations.get("label", ""))
        self.ui.menuLanguage.setTitle(self.translations.get("menuLanguage", ""))
        self.ui.actionFrench.setText(self.translations.get("actionFrench", ""))
        self.ui.actionEnglish.setText(self.translations.get("actionEnglish", ""))
        self.ui.actionChinese.setText(self.translations.get("actionChinese", ""))
        self.ui.actionArabic.setText(self.translations.get("actionArabic", ""))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
