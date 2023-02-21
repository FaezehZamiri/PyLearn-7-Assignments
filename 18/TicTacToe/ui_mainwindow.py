# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(352, 473)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 103, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Forte"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Player = QRadioButton(self.centralwidget)
        self.Player.setObjectName(u"Player")
        self.Player.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Forte"])
        font1.setPointSize(15)
        self.Player.setFont(font1)
        self.Player.setStyleSheet(u"color:#ffffff;")
        self.Player.setCheckable(True)
        self.Player.setChecked(True)

        self.gridLayout.addWidget(self.Player, 0, 0, 1, 1)

        self.CPU = QRadioButton(self.centralwidget)
        self.CPU.setObjectName(u"CPU")
        self.CPU.setFont(font1)
        self.CPU.setStyleSheet(u"color:#ffffff;")

        self.gridLayout.addWidget(self.CPU, 0, 1, 1, 1)

        self.btn_startagain = QPushButton(self.centralwidget)
        self.btn_startagain.setObjectName(u"btn_startagain")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_startagain.sizePolicy().hasHeightForWidth())
        self.btn_startagain.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Forte"])
        font2.setPointSize(13)
        self.btn_startagain.setFont(font2)
        self.btn_startagain.setStyleSheet(u"background-color:rgb(255, 85, 0);\n"
"color:#ffffff;\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_startagain, 0, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Forte"])
        font3.setPointSize(40)
        self.btn_1.setFont(font3)
        self.btn_1.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_1, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font3)
        self.btn_2.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_2, 1, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font3)
        self.btn_3.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_3, 1, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font3)
        self.btn_4.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font3)
        self.btn_5.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font3)
        self.btn_6.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font3)
        self.btn_7.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font3)
        self.btn_8.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font3)
        self.btn_9.setStyleSheet(u"background-color:rgb(0, 0, 67);\n"
"border-radius:15px;\n"
"box-shadow:20px 20px #888888;")

        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"color:#fff;")
        self.btn_xwin = QPushButton(self.groupBox)
        self.btn_xwin.setObjectName(u"btn_xwin")
        self.btn_xwin.setGeometry(QRect(10, 20, 81, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_xwin.sizePolicy().hasHeightForWidth())
        self.btn_xwin.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Forte"])
        font4.setPointSize(20)
        self.btn_xwin.setFont(font4)
        self.btn_xwin.setStyleSheet(u"color:#ffffff;\n"
"background-color:#000067;\n"
"border:none;")

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"color:#fff;")
        self.btn_tie = QPushButton(self.groupBox_2)
        self.btn_tie.setObjectName(u"btn_tie")
        self.btn_tie.setGeometry(QRect(10, 20, 81, 41))
        sizePolicy1.setHeightForWidth(self.btn_tie.sizePolicy().hasHeightForWidth())
        self.btn_tie.setSizePolicy(sizePolicy1)
        self.btn_tie.setFont(font4)
        self.btn_tie.setStyleSheet(u"color:#ffffff;\n"
"background-color:#000067;\n"
"border:none;")

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"color:#fff;")
        self.btn_owin = QPushButton(self.groupBox_3)
        self.btn_owin.setObjectName(u"btn_owin")
        self.btn_owin.setGeometry(QRect(10, 20, 81, 41))
        sizePolicy1.setHeightForWidth(self.btn_owin.sizePolicy().hasHeightForWidth())
        self.btn_owin.setSizePolicy(sizePolicy1)
        self.btn_owin.setFont(font4)
        self.btn_owin.setStyleSheet(u"color:#ffffff;\n"
"background-color:#000067;\n"
"border:none;")

        self.horizontalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Player.setText(QCoreApplication.translate("MainWindow", u"Player ", None))
        self.CPU.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.btn_startagain.setText(QCoreApplication.translate("MainWindow", u"Start Again", None))
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_4.setText("")
        self.btn_5.setText("")
        self.btn_6.setText("")
        self.btn_7.setText("")
        self.btn_8.setText("")
        self.btn_9.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"X  (You)", None))
        self.btn_xwin.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"TIES", None))
        self.btn_tie.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"O (CPU)", None))
        self.btn_owin.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

