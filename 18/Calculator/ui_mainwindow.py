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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(522, 355)
        palette = QPalette()
        brush = QBrush(QColor(255, 231, 253, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"border-radius:10px;\n"
"background_color:rgb(255, 221, 249)")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(35)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(211, 180, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 7)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btn_7.setFont(font1)
        self.btn_7.setAcceptDrops(False)
        self.btn_7.setAutoFillBackground(False)
        self.btn_7.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font1)
        self.btn_8.setAcceptDrops(False)
        self.btn_8.setAutoFillBackground(False)
        self.btn_8.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font1)
        self.btn_9.setAcceptDrops(False)
        self.btn_9.setAutoFillBackground(False)
        self.btn_9.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_ac = QPushButton(self.centralwidget)
        self.btn_ac.setObjectName(u"btn_ac")
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.btn_ac.setFont(font2)
        self.btn_ac.setAcceptDrops(False)
        self.btn_ac.setAutoFillBackground(False)
        self.btn_ac.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(247, 255, 155);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_ac, 1, 3, 1, 1)

        self.btn_negpos = QPushButton(self.centralwidget)
        self.btn_negpos.setObjectName(u"btn_negpos")
        sizePolicy.setHeightForWidth(self.btn_negpos.sizePolicy().hasHeightForWidth())
        self.btn_negpos.setSizePolicy(sizePolicy)
        self.btn_negpos.setFont(font2)
        self.btn_negpos.setAcceptDrops(False)
        self.btn_negpos.setAutoFillBackground(False)
        self.btn_negpos.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_negpos, 1, 4, 1, 1)

        self.btn_pre = QPushButton(self.centralwidget)
        self.btn_pre.setObjectName(u"btn_pre")
        sizePolicy.setHeightForWidth(self.btn_pre.sizePolicy().hasHeightForWidth())
        self.btn_pre.setSizePolicy(sizePolicy)
        self.btn_pre.setFont(font2)
        self.btn_pre.setAcceptDrops(False)
        self.btn_pre.setAutoFillBackground(False)
        self.btn_pre.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_pre, 1, 5, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Baskerville Old Face"])
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.btn_sqrt.setFont(font3)
        self.btn_sqrt.setAcceptDrops(False)
        self.btn_sqrt.setAutoFillBackground(False)
        self.btn_sqrt.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_sqrt, 1, 6, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font1)
        self.btn_4.setAcceptDrops(False)
        self.btn_4.setAutoFillBackground(False)
        self.btn_4.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font1)
        self.btn_5.setAcceptDrops(False)
        self.btn_5.setAutoFillBackground(False)
        self.btn_5.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font1)
        self.btn_6.setAcceptDrops(False)
        self.btn_6.setAutoFillBackground(False)
        self.btn_6.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(35)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.btn_mul.setFont(font4)
        self.btn_mul.setAcceptDrops(False)
        self.btn_mul.setAutoFillBackground(False)
        self.btn_mul.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_mul, 2, 3, 1, 1)

        self.btn_dev = QPushButton(self.centralwidget)
        self.btn_dev.setObjectName(u"btn_dev")
        sizePolicy.setHeightForWidth(self.btn_dev.sizePolicy().hasHeightForWidth())
        self.btn_dev.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(35)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.btn_dev.setFont(font5)
        self.btn_dev.setAcceptDrops(False)
        self.btn_dev.setAutoFillBackground(False)
        self.btn_dev.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_dev, 2, 4, 1, 1)

        self.btn_sum = QPushButton(self.centralwidget)
        self.btn_sum.setObjectName(u"btn_sum")
        sizePolicy.setHeightForWidth(self.btn_sum.sizePolicy().hasHeightForWidth())
        self.btn_sum.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(30)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.btn_sum.setFont(font6)
        self.btn_sum.setAcceptDrops(False)
        self.btn_sum.setAutoFillBackground(False)
        self.btn_sum.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_sum, 2, 5, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"MRT_Two Bold"])
        font7.setPointSize(30)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.btn_sub.setFont(font7)
        self.btn_sub.setAcceptDrops(False)
        self.btn_sub.setAutoFillBackground(False)
        self.btn_sub.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(206, 255, 201);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_sub, 2, 6, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setFont(font1)
        self.btn_1.setAcceptDrops(False)
        self.btn_1.setAutoFillBackground(False)
        self.btn_1.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font1)
        self.btn_2.setAcceptDrops(False)
        self.btn_2.setAutoFillBackground(False)
        self.btn_2.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font1)
        self.btn_3.setAcceptDrops(False)
        self.btn_3.setAutoFillBackground(False)
        self.btn_3.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_log = QPushButton(self.centralwidget)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(24)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        font8.setStyleStrategy(QFont.PreferDefault)
        self.btn_log.setFont(font8)
        self.btn_log.setAcceptDrops(False)
        self.btn_log.setAutoFillBackground(False)
        self.btn_log.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_log, 3, 3, 1, 1)

        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy)
        self.btn_sin.setFont(font8)
        self.btn_sin.setAcceptDrops(False)
        self.btn_sin.setAutoFillBackground(False)
        self.btn_sin.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_sin, 3, 4, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy)
        self.btn_cos.setFont(font8)
        self.btn_cos.setAcceptDrops(False)
        self.btn_cos.setAutoFillBackground(False)
        self.btn_cos.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_cos, 3, 5, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setFont(font6)
        self.btn_equal.setAcceptDrops(False)
        self.btn_equal.setAutoFillBackground(False)
        self.btn_equal.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_equal, 3, 6, 2, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setFont(font1)
        self.btn_0.setAcceptDrops(False)
        self.btn_0.setAutoFillBackground(False)
        self.btn_0.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)

        self.btn_10 = QPushButton(self.centralwidget)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)
        self.btn_10.setFont(font1)
        self.btn_10.setAcceptDrops(False)
        self.btn_10.setAutoFillBackground(False)
        self.btn_10.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(211, 180, 255);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_10, 4, 2, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        sizePolicy.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy)
        self.btn_ln.setFont(font8)
        self.btn_ln.setAcceptDrops(False)
        self.btn_ln.setAutoFillBackground(False)
        self.btn_ln.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_ln, 4, 3, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy)
        self.btn_tan.setFont(font8)
        self.btn_tan.setAcceptDrops(False)
        self.btn_tan.setAutoFillBackground(False)
        self.btn_tan.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_tan, 4, 4, 1, 1)

        self.btn_cot = QPushButton(self.centralwidget)
        self.btn_cot.setObjectName(u"btn_cot")
        sizePolicy.setHeightForWidth(self.btn_cot.sizePolicy().hasHeightForWidth())
        self.btn_cot.setSizePolicy(sizePolicy)
        self.btn_cot.setFont(font8)
        self.btn_cot.setAcceptDrops(False)
        self.btn_cot.setAutoFillBackground(False)
        self.btn_cot.setStyleSheet(u"color : #ffffff;\n"
"background-color: rgb(255, 111, 142);\n"
"border-radius:10px;")

        self.gridLayout.addWidget(self.btn_cot, 4, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_1, self.btn_2)
        QWidget.setTabOrder(self.btn_2, self.btn_3)
        QWidget.setTabOrder(self.btn_3, self.btn_4)
        QWidget.setTabOrder(self.btn_4, self.btn_5)
        QWidget.setTabOrder(self.btn_5, self.btn_6)
        QWidget.setTabOrder(self.btn_6, self.btn_7)
        QWidget.setTabOrder(self.btn_7, self.btn_8)
        QWidget.setTabOrder(self.btn_8, self.btn_9)
        QWidget.setTabOrder(self.btn_9, self.btn_0)
        QWidget.setTabOrder(self.btn_0, self.btn_10)
        QWidget.setTabOrder(self.btn_10, self.btn_ac)
        QWidget.setTabOrder(self.btn_ac, self.btn_negpos)
        QWidget.setTabOrder(self.btn_negpos, self.btn_sub)
        QWidget.setTabOrder(self.btn_sub, self.btn_sum)
        QWidget.setTabOrder(self.btn_sum, self.btn_pre)
        QWidget.setTabOrder(self.btn_pre, self.btn_dev)
        QWidget.setTabOrder(self.btn_dev, self.btn_mul)
        QWidget.setTabOrder(self.btn_mul, self.btn_sqrt)
        QWidget.setTabOrder(self.btn_sqrt, self.btn_log)
        QWidget.setTabOrder(self.btn_log, self.btn_sin)
        QWidget.setTabOrder(self.btn_sin, self.btn_cos)
        QWidget.setTabOrder(self.btn_cos, self.btn_cot)
        QWidget.setTabOrder(self.btn_cot, self.btn_tan)
        QWidget.setTabOrder(self.btn_tan, self.btn_equal)
        QWidget.setTabOrder(self.btn_equal, self.lineEdit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ac.setText(QCoreApplication.translate("MainWindow", u"AC", None))
#if QT_CONFIG(shortcut)
        self.btn_ac.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_negpos.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
#if QT_CONFIG(shortcut)
        self.btn_negpos.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.btn_pre.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(shortcut)
        self.btn_pre.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dev.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        self.btn_dev.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_sum.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.btn_sin.setText(QCoreApplication.translate("MainWindow", u"Sin", None))
        self.btn_cos.setText(QCoreApplication.translate("MainWindow", u"Cos", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_equal.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_10.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_10.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"Ln", None))
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"Tan", None))
        self.btn_cot.setText(QCoreApplication.translate("MainWindow", u"Cot", None))
    # retranslateUi

