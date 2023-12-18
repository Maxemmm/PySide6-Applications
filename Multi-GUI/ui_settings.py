# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsGByRaj.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(635, 488)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.horizontalLayout_7.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.horizontalSlider_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_4.addWidget(self.radioButton_2)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.frame)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_3.addWidget(self.checkBox_7)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"Help: Interface Options", None))
        self.pushButton_2.setText(QCoreApplication.translate("SettingsWindow", u"Reset All...", None))
        self.pushButton_3.setText(QCoreApplication.translate("SettingsWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("SettingsWindow", u"OK", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWindow", u"Preview border", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Color", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Opacity", None))
        self.lineEdit.setText(QCoreApplication.translate("SettingsWindow", u"50", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsWindow", u"Progressive previews", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"Multi-pass preview", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SettingsWindow", u"3 Passes", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SettingsWindow", u"4 Passes", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SettingsWindow", u"5 Passes", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("SettingsWindow", u"Legacy", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("SettingsWindow", u"Off", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("SettingsWindow", u"Mouse wheel in scrollboxes", None))
        self.radioButton.setText(QCoreApplication.translate("SettingsWindow", u"Scrolls the scrollbox itself", None))
        self.radioButton_2.setText(QCoreApplication.translate("SettingsWindow", u"Adjusts the controls in the scrollbox", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsWindow", u"Reduce preview size for large images", None))
        self.checkBox_2.setText(QCoreApplication.translate("SettingsWindow", u"Show elapsed rendering time", None))
        self.checkBox_3.setText(QCoreApplication.translate("SettingsWindow", u"Invert mouse wheel when zooming", None))
        self.checkBox_4.setText(QCoreApplication.translate("SettingsWindow", u"Show channel descriptions when rendering channels", None))
        self.checkBox_5.setText(QCoreApplication.translate("SettingsWindow", u"Notify when a filter needs a region with an integer aspect ratio", None))
        self.checkBox_6.setText(QCoreApplication.translate("SettingsWindow", u"Notify when the output image might be non-seamless", None))
        self.checkBox_7.setText(QCoreApplication.translate("SettingsWindow", u"Use cache preservation for previews (improves interactivity)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SettingsWindow", u"Interface", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SettingsWindow", u"Palettes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SettingsWindow", u"Memory", None))
    # retranslateUi

