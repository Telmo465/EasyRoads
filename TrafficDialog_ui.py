# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrafficDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_TrafficDialog(object):
    def setupUi(self, TrafficDialog):
        if not TrafficDialog.objectName():
            TrafficDialog.setObjectName(u"TrafficDialog")
        TrafficDialog.resize(500, 400)
        TrafficDialog.setMinimumSize(QSize(500, 400))
        TrafficDialog.setMaximumSize(QSize(500, 400))
        self.label = QLabel(TrafficDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 241, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.line = QFrame(TrafficDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 90, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.comboBox = QComboBox(TrafficDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(50, 160, 121, 31))
        self.label_3 = QLabel(TrafficDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 130, 122, 22))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.comboBox_2 = QComboBox(TrafficDialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(200, 160, 121, 31))
        self.label_4 = QLabel(TrafficDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 130, 122, 22))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(TrafficDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 130, 122, 22))
        self.label_5.setFont(font1)
        self.comboBox_3 = QComboBox(TrafficDialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(360, 160, 121, 31))
        self.label_6 = QLabel(TrafficDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 230, 141, 22))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(TrafficDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 230, 122, 22))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(TrafficDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 230, 122, 22))
        self.label_8.setFont(font1)
        self.comboBox_6 = QComboBox(TrafficDialog)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(200, 260, 121, 31))
        self.lane_lineEdit_5 = QLineEdit(TrafficDialog)
        self.lane_lineEdit_5.setObjectName(u"lane_lineEdit_5")
        self.lane_lineEdit_5.setGeometry(QRect(50, 260, 123, 35))
        self.lane_lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_5.setMaximumSize(QSize(16777215, 35))
        self.lane_lineEdit_6 = QLineEdit(TrafficDialog)
        self.lane_lineEdit_6.setObjectName(u"lane_lineEdit_6")
        self.lane_lineEdit_6.setGeometry(QRect(360, 260, 123, 35))
        self.lane_lineEdit_6.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_6.setMaximumSize(QSize(16777215, 35))
        self.add_traffic = QPushButton(TrafficDialog)
        self.add_traffic.setObjectName(u"add_traffic")
        self.add_traffic.setGeometry(QRect(279, 350, 75, 24))
        self.cancel_ltraffic = QPushButton(TrafficDialog)
        self.cancel_ltraffic.setObjectName(u"cancel_ltraffic")
        self.cancel_ltraffic.setGeometry(QRect(360, 350, 75, 24))

        self.retranslateUi(TrafficDialog)

        QMetaObject.connectSlotsByName(TrafficDialog)
    # setupUi

    def retranslateUi(self, TrafficDialog):
        TrafficDialog.setWindowTitle(QCoreApplication.translate("TrafficDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("TrafficDialog", u"Add Traffic", None))
        self.label_3.setText(QCoreApplication.translate("TrafficDialog", u"Lanes", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("TrafficDialog", u"Source", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("TrafficDialog", u"Vehicle", None))

        self.label_4.setText(QCoreApplication.translate("TrafficDialog", u"Type", None))
        self.label_5.setText(QCoreApplication.translate("TrafficDialog", u"Vehicles", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("TrafficDialog", u"Car", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("TrafficDialog", u"Truck", None))

        self.label_6.setText(QCoreApplication.translate("TrafficDialog", u"Distance (m)", None))
        self.label_7.setText(QCoreApplication.translate("TrafficDialog", u"Quantity", None))
        self.label_8.setText(QCoreApplication.translate("TrafficDialog", u"Position", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("TrafficDialog", u"SimCar", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("TrafficDialog", u"Course", None))

        self.add_traffic.setText(QCoreApplication.translate("TrafficDialog", u"Add Traffic", None))
#if QT_CONFIG(shortcut)
        self.add_traffic.setShortcut(QCoreApplication.translate("TrafficDialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancel_ltraffic.setText(QCoreApplication.translate("TrafficDialog", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.cancel_ltraffic.setShortcut(QCoreApplication.translate("TrafficDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

