# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerQuUtmn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(355, 465)
        RegisterWindow.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"    border: 1px solid lightgray;\n"
"}\n"
"\n"
"QLineEdit:hover { /* Do the QLineEdit hover effect, it should be light blue */\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:focus { /* Do the QLineEdit focus effect, it should be blue */\n"
"    border: 1px solid #3498db;\n"
"}\n"
"\n"
"QLineEdit:disabled {	/* Do the QLineEdit disabled effect, it should be gray */\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QLabel#label {\n"
"	image: url(:images/images/airfrance-old-logo.svg);\n"
"}")
        RegisterWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 30)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/user.svg"))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setMinimumSize(QSize(300, 35))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/icons/icons/lock.svg"))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 35))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setUnderline(False)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(45, 120, 220);")

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(300, 35))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(300, 35))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/google-color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setUnderline(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(45, 120, 220);")

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.widget, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_5.setText("")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.label_6.setText("")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("RegisterWindow", u"Remember me", None))
        self.label_4.setText(QCoreApplication.translate("RegisterWindow", u"Forget password ?", None))
        self.pushButton.setText(QCoreApplication.translate("RegisterWindow", u"Log In", None))
        self.pushButton_2.setText(QCoreApplication.translate("RegisterWindow", u" Log In", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWindow", u"No account ?", None))
        self.label_2.setText(QCoreApplication.translate("RegisterWindow", u"Sign Up", None))
    # retranslateUi

