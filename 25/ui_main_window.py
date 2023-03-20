# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(446, 395)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 85, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.tabWidget.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(8)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.widget = QWidget(self.tab_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 381, 161))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)

        self.time_berlin = QTextEdit(self.widget)
        self.time_berlin.setObjectName(u"time_berlin")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_berlin.sizePolicy().hasHeightForWidth())
        self.time_berlin.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Seven Segment"])
        font2.setPointSize(20)
        self.time_berlin.setFont(font2)
        self.time_berlin.setStyleSheet(u"border:none;\n"
"border-radius:15px;\n"
"background-color:rgb(255, 138, 5);\n"
"color:#fff;")

        self.gridLayout_2.addWidget(self.time_berlin, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.time_newyork = QTextEdit(self.widget)
        self.time_newyork.setObjectName(u"time_newyork")
        sizePolicy.setHeightForWidth(self.time_newyork.sizePolicy().hasHeightForWidth())
        self.time_newyork.setSizePolicy(sizePolicy)
        self.time_newyork.setFont(font2)
        self.time_newyork.setStyleSheet(u"border:none;\n"
"border-radius:15px;\n"
"background-color:rgb(255, 138, 5);\n"
"color:#fff;")

        self.gridLayout_2.addWidget(self.time_newyork, 2, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.time_tehran = QTextEdit(self.widget)
        self.time_tehran.setObjectName(u"time_tehran")
        sizePolicy.setHeightForWidth(self.time_tehran.sizePolicy().hasHeightForWidth())
        self.time_tehran.setSizePolicy(sizePolicy)
        self.time_tehran.setFont(font2)
        self.time_tehran.setStyleSheet(u"border:none;\n"
"border-radius:15px;\n"
"background-color:rgb(255, 138, 5);\n"
"color:#fff;")

        self.gridLayout_2.addWidget(self.time_tehran, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 231))
        self.GL_Alarms = QGridLayout(self.gridLayoutWidget)
        self.GL_Alarms.setObjectName(u"GL_Alarms")
        self.GL_Alarms.setContentsMargins(0, 0, 0, 0)
        self.timeEdit = QTimeEdit(self.tab_2)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(10, 250, 261, 41))
        font3 = QFont()
        font3.setFamilies([u"Seven Segment"])
        font3.setPointSize(15)
        font3.setBold(False)
        self.timeEdit.setFont(font3)
        self.timeEdit.setStyleSheet(u"\n"
"bacckground-color:rgb(255, 138, 5);")
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setDisplayFormat(u"hh:mm:ss AP")
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setTime(QTime(0, 1, 1))
        self.btn_add_alarm = QPushButton(self.tab_2)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setGeometry(QRect(300, 250, 91, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe Print"])
        font4.setPointSize(24)
        font4.setBold(False)
        self.btn_add_alarm.setFont(font4)
        self.btn_add_alarm.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_stopwatch = QLabel(self.tab_3)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(120, 70, 141, 51))
        font5 = QFont()
        font5.setFamilies([u"Seven Segment"])
        font5.setPointSize(50)
        font5.setBold(False)
        self.label_stopwatch.setFont(font5)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(34, 190, 101, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe Print"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.btn_start_stopwatch.setFont(font6)
        self.btn_start_stopwatch.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(144, 190, 91, 31))
        self.btn_stop_stopwatch.setFont(font6)
        self.btn_stop_stopwatch.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(250, 190, 101, 31))
        self.btn_reset_stopwatch.setFont(font6)
        self.btn_reset_stopwatch.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.lineEdit_hour_timer = QLineEdit(self.tab_4)
        self.lineEdit_hour_timer.setObjectName(u"lineEdit_hour_timer")
        self.lineEdit_hour_timer.setGeometry(QRect(30, 70, 101, 91))
        self.lineEdit_hour_timer.setFont(font5)
        self.lineEdit_hour_timer.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_hour_timer.setStyleSheet(u"border:none;")
        self.lineEdit_hour_timer.setAlignment(Qt.AlignCenter)
        self.lineEdit_min_timer = QLineEdit(self.tab_4)
        self.lineEdit_min_timer.setObjectName(u"lineEdit_min_timer")
        self.lineEdit_min_timer.setGeometry(QRect(140, 70, 101, 91))
        self.lineEdit_min_timer.setFont(font5)
        self.lineEdit_min_timer.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_min_timer.setStyleSheet(u"border:none;")
        self.lineEdit_min_timer.setAlignment(Qt.AlignCenter)
        self.lineEdit_second_timer = QLineEdit(self.tab_4)
        self.lineEdit_second_timer.setObjectName(u"lineEdit_second_timer")
        self.lineEdit_second_timer.setGeometry(QRect(250, 70, 101, 91))
        self.lineEdit_second_timer.setFont(font5)
        self.lineEdit_second_timer.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_second_timer.setStyleSheet(u"border:none;")
        self.lineEdit_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(156, 200, 91, 31))
        self.btn_stop_timer.setFont(font6)
        self.btn_stop_timer.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(40, 200, 101, 31))
        self.btn_start_timer.setFont(font6)
        self.btn_start_timer.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(260, 200, 91, 31))
        self.btn_reset_timer.setFont(font6)
        self.btn_reset_timer.setStyleSheet(u"background-color:rgb(255, 138, 5);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 446, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"-2:30", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Berlin - Germany", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"-7:30", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NewYork - US", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tehran - Iran", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.lineEdit_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_min_timer.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.lineEdit_second_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

