# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Goverment.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1303, 658)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 90, 101, 121))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 10, 331, 31))
        self.label.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1303, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05d3\u05d9\u05e0\u05ea \u05d9\u05e9\u05e8\u05d0\u05dc \u05de\u05e2\u05e8\u05db\u05ea \u05d1\u05d7\u05d9\u05e8\u05d5\u05ea", None))
    # retranslateUi

