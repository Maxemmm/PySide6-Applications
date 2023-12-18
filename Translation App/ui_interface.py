# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceyBNNql.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(224, 173)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.actionFrench = QAction(MainWindow)
        self.actionFrench.setObjectName(u"actionFrench")
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionArabic = QAction(MainWindow)
        self.actionArabic.setObjectName(u"actionArabic")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 224, 22))
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionFrench)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)
        self.menuLanguage.addAction(self.actionArabic)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFrench.setText(QCoreApplication.translate("MainWindow", u"French", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.actionArabic.setText(QCoreApplication.translate("MainWindow", u"Arabic", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Button 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Testing", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Button 2", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi

