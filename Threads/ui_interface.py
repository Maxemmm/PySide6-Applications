# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacemvPizL.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 290)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl1_btn1 = QPushButton(self.groupBox)
        self.start_thread_pnl1_btn1.setObjectName(u"start_thread_pnl1_btn1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_thread_pnl1_btn1.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl1_btn1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.start_thread_pnl1_btn1)

        self.stop_thread_pnl1_btn1 = QPushButton(self.groupBox)
        self.stop_thread_pnl1_btn1.setObjectName(u"stop_thread_pnl1_btn1")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl1_btn1.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl1_btn1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.stop_thread_pnl1_btn1)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl1_btn2 = QPushButton(self.groupBox)
        self.start_thread_pnl1_btn2.setObjectName(u"start_thread_pnl1_btn2")
        sizePolicy.setHeightForWidth(self.start_thread_pnl1_btn2.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl1_btn2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.start_thread_pnl1_btn2)

        self.stop_thread_pnl1_btn2 = QPushButton(self.groupBox)
        self.stop_thread_pnl1_btn2.setObjectName(u"stop_thread_pnl1_btn2")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl1_btn2.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl1_btn2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.stop_thread_pnl1_btn2)

        self.progressBar_2 = QProgressBar(self.groupBox)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy1.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy1)
        self.progressBar_2.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl1_btn3 = QPushButton(self.groupBox)
        self.start_thread_pnl1_btn3.setObjectName(u"start_thread_pnl1_btn3")
        sizePolicy.setHeightForWidth(self.start_thread_pnl1_btn3.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl1_btn3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.start_thread_pnl1_btn3)

        self.stop_thread_pnl1_btn3 = QPushButton(self.groupBox)
        self.stop_thread_pnl1_btn3.setObjectName(u"stop_thread_pnl1_btn3")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl1_btn3.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl1_btn3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.stop_thread_pnl1_btn3)

        self.progressBar_3 = QProgressBar(self.groupBox)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy1.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy1)
        self.progressBar_3.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl2_btn1 = QPushButton(self.groupBox_2)
        self.start_thread_pnl2_btn1.setObjectName(u"start_thread_pnl2_btn1")
        sizePolicy.setHeightForWidth(self.start_thread_pnl2_btn1.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl2_btn1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.start_thread_pnl2_btn1)

        self.stop_thread_pnl2_btn1 = QPushButton(self.groupBox_2)
        self.stop_thread_pnl2_btn1.setObjectName(u"stop_thread_pnl2_btn1")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl2_btn1.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl2_btn1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.stop_thread_pnl2_btn1)

        self.progressBar_4 = QProgressBar(self.groupBox_2)
        self.progressBar_4.setObjectName(u"progressBar_4")
        sizePolicy1.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy1)
        self.progressBar_4.setValue(24)

        self.horizontalLayout_4.addWidget(self.progressBar_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl2_btn2 = QPushButton(self.groupBox_2)
        self.start_thread_pnl2_btn2.setObjectName(u"start_thread_pnl2_btn2")
        sizePolicy.setHeightForWidth(self.start_thread_pnl2_btn2.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl2_btn2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.start_thread_pnl2_btn2)

        self.stop_thread_pnl2_btn2 = QPushButton(self.groupBox_2)
        self.stop_thread_pnl2_btn2.setObjectName(u"stop_thread_pnl2_btn2")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl2_btn2.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl2_btn2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.stop_thread_pnl2_btn2)

        self.progressBar_5 = QProgressBar(self.groupBox_2)
        self.progressBar_5.setObjectName(u"progressBar_5")
        sizePolicy1.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy1)
        self.progressBar_5.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.start_thread_pnl2_btn3 = QPushButton(self.groupBox_2)
        self.start_thread_pnl2_btn3.setObjectName(u"start_thread_pnl2_btn3")
        sizePolicy.setHeightForWidth(self.start_thread_pnl2_btn3.sizePolicy().hasHeightForWidth())
        self.start_thread_pnl2_btn3.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.start_thread_pnl2_btn3)

        self.stop_thread_pnl2_btn3 = QPushButton(self.groupBox_2)
        self.stop_thread_pnl2_btn3.setObjectName(u"stop_thread_pnl2_btn3")
        sizePolicy.setHeightForWidth(self.stop_thread_pnl2_btn3.sizePolicy().hasHeightForWidth())
        self.stop_thread_pnl2_btn3.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.stop_thread_pnl2_btn3)

        self.progressBar_6 = QProgressBar(self.groupBox_2)
        self.progressBar_6.setObjectName(u"progressBar_6")
        sizePolicy1.setHeightForWidth(self.progressBar_6.sizePolicy().hasHeightForWidth())
        self.progressBar_6.setSizePolicy(sizePolicy1)
        self.progressBar_6.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Threads Panel 1", None))
        self.start_thread_pnl1_btn1.setText(QCoreApplication.translate("MainWindow", u"Start Thread 1", None))
        self.stop_thread_pnl1_btn1.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 1", None))
        self.start_thread_pnl1_btn2.setText(QCoreApplication.translate("MainWindow", u"Start Thread 2", None))
        self.stop_thread_pnl1_btn2.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 2", None))
        self.start_thread_pnl1_btn3.setText(QCoreApplication.translate("MainWindow", u"Start Thread 3", None))
        self.stop_thread_pnl1_btn3.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Threads Panel 2", None))
        self.start_thread_pnl2_btn1.setText(QCoreApplication.translate("MainWindow", u"Start Thread 1", None))
        self.stop_thread_pnl2_btn1.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 1", None))
        self.start_thread_pnl2_btn2.setText(QCoreApplication.translate("MainWindow", u"Start Thread 2", None))
        self.stop_thread_pnl2_btn2.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 2", None))
        self.start_thread_pnl2_btn3.setText(QCoreApplication.translate("MainWindow", u"Start Thread 3", None))
        self.stop_thread_pnl2_btn3.setText(QCoreApplication.translate("MainWindow", u"Stop Thread 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

