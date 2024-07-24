# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_traffDialog.ui'
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

class Ui_Edit_traffDialog(object):
    def setupUi(self, Edit_traffDialog):
        if not Edit_traffDialog.objectName():
            Edit_traffDialog.setObjectName(u"Edit_traffDialog")
        Edit_traffDialog.resize(500, 400)
        Edit_traffDialog.setMinimumSize(QSize(500, 400))
        Edit_traffDialog.setMaximumSize(QSize(500, 400))
        self.add_traffic = QPushButton(Edit_traffDialog)
        self.add_traffic.setObjectName(u"add_traffic")
        self.add_traffic.setGeometry(QRect(319, 330, 75, 24))
        self.lane_lineEdit_5 = QLineEdit(Edit_traffDialog)
        self.lane_lineEdit_5.setObjectName(u"lane_lineEdit_5")
        self.lane_lineEdit_5.setGeometry(QRect(40, 230, 123, 35))
        self.lane_lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_5.setMaximumSize(QSize(16777215, 35))
        self.label_7 = QLabel(Edit_traffDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 200, 122, 22))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_3 = QLabel(Edit_traffDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 122, 22))
        self.label_3.setFont(font)
        self.label_6 = QLabel(Edit_traffDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 200, 141, 22))
        self.label_6.setFont(font)
        self.line = QFrame(Edit_traffDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 60, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(Edit_traffDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 241, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.comboBox = QComboBox(Edit_traffDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 130, 121, 31))
        self.label_8 = QLabel(Edit_traffDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 200, 122, 22))
        self.label_8.setFont(font)
        self.comboBox_3 = QComboBox(Edit_traffDialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(350, 130, 121, 31))
        self.comboBox_6 = QComboBox(Edit_traffDialog)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(190, 230, 121, 31))
        self.lane_lineEdit_6 = QLineEdit(Edit_traffDialog)
        self.lane_lineEdit_6.setObjectName(u"lane_lineEdit_6")
        self.lane_lineEdit_6.setGeometry(QRect(350, 230, 123, 35))
        self.lane_lineEdit_6.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_6.setMaximumSize(QSize(16777215, 35))
        self.label_4 = QLabel(Edit_traffDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 100, 122, 22))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Edit_traffDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 100, 122, 22))
        self.label_5.setFont(font)
        self.comboBox_2 = QComboBox(Edit_traffDialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(190, 130, 121, 31))
        self.cancel_ltraffic = QPushButton(Edit_traffDialog)
        self.cancel_ltraffic.setObjectName(u"cancel_ltraffic")
        self.cancel_ltraffic.setGeometry(QRect(400, 330, 75, 24))

        self.retranslateUi(Edit_traffDialog)

        QMetaObject.connectSlotsByName(Edit_traffDialog)
    # setupUi

    def retranslateUi(self, Edit_traffDialog):
        Edit_traffDialog.setWindowTitle(QCoreApplication.translate("Edit_traffDialog", u"Dialog", None))
        self.add_traffic.setText(QCoreApplication.translate("Edit_traffDialog", u"Edit Traffic", None))
#if QT_CONFIG(shortcut)
        self.add_traffic.setShortcut(QCoreApplication.translate("Edit_traffDialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_7.setText(QCoreApplication.translate("Edit_traffDialog", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("Edit_traffDialog", u"Lanes", None))
        self.label_6.setText(QCoreApplication.translate("Edit_traffDialog", u"Distance (m)", None))
        self.label.setText(QCoreApplication.translate("Edit_traffDialog", u"Edit Traffic", None))
        self.label_8.setText(QCoreApplication.translate("Edit_traffDialog", u"Position", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Edit_traffDialog", u"Car", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Edit_traffDialog", u"Truck", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("Edit_traffDialog", u"SimCar", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Edit_traffDialog", u"Course", None))

        self.label_4.setText(QCoreApplication.translate("Edit_traffDialog", u"Type", None))
        self.label_5.setText(QCoreApplication.translate("Edit_traffDialog", u"Vehicles", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Edit_traffDialog", u"Source", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Edit_traffDialog", u"Vehicle", None))

        self.cancel_ltraffic.setText(QCoreApplication.translate("Edit_traffDialog", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.cancel_ltraffic.setShortcut(QCoreApplication.translate("Edit_traffDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

