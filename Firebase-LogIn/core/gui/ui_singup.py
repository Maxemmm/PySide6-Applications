# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singupHfYrqw.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        if not SignupWindow.objectName():
            SignupWindow.setObjectName(u"SignupWindow")
        SignupWindow.resize(355, 465)
        SignupWindow.setStyleSheet(u"QLineEdit {\n"
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
"QPushButton {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"    border: 1px solid lightgray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #3498db;\n"
"}")
        self.centralwidget = QWidget(SignupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, 0, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icons/user.svg"))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 35))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/icons/lock.svg"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 35))

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/lock.svg"))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 35))

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 10)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/info.svg"))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(300, 35))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 25, -1, 5)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(300, 35))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 40)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(300, 35))
        self.pushButton_2.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        SignupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignupWindow)

        QMetaObject.connectSlotsByName(SignupWindow)
    # setupUi

    def retranslateUi(self, SignupWindow):
        SignupWindow.setWindowTitle(QCoreApplication.translate("SignupWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("SignupWindow", u"Sign Up", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Username", None))
        self.label_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Password", None))
        self.label_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Confirm password", None))
        self.label_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("SignupWindow", u"Password Hint", None))
        self.pushButton.setText(QCoreApplication.translate("SignupWindow", u"Sign Up", None))
        self.pushButton_2.setText(QCoreApplication.translate("SignupWindow", u" Return", None))
    # retranslateUi

