# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SectionsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SectionsDialog(object):
    def setupUi(self, SectionsDialog):
        if not SectionsDialog.objectName():
            SectionsDialog.setObjectName(u"SectionsDialog")
        SectionsDialog.resize(500, 400)
        SectionsDialog.setMinimumSize(QSize(500, 400))
        SectionsDialog.setMaximumSize(QSize(500, 400))
        self.direction_comboBox = QComboBox(SectionsDialog)
        self.direction_comboBox.addItem("")
        self.direction_comboBox.addItem("")
        self.direction_comboBox.setObjectName(u"direction_comboBox")
        self.direction_comboBox.setGeometry(QRect(40, 58, 122, 35))
        self.direction_comboBox.setMinimumSize(QSize(0, 35))
        self.direction_comboBox.setMaximumSize(QSize(16777215, 35))
        self.label_6 = QLabel(SectionsDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 30, 122, 22))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.lane_lineEdit_4 = QLineEdit(SectionsDialog)
        self.lane_lineEdit_4.setObjectName(u"lane_lineEdit_4")
        self.lane_lineEdit_4.setGeometry(QRect(181, 148, 123, 35))
        self.lane_lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_4.setMaximumSize(QSize(16777215, 35))
        self.lane_lineEdit_5 = QLineEdit(SectionsDialog)
        self.lane_lineEdit_5.setObjectName(u"lane_lineEdit_5")
        self.lane_lineEdit_5.setGeometry(QRect(50, 148, 123, 35))
        self.lane_lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_5.setMaximumSize(QSize(16777215, 35))
        self.label_5 = QLabel(SectionsDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(181, 120, 91, 22))
        self.label_5.setFont(font)
        self.label_7 = QLabel(SectionsDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 120, 100, 22))
        self.label_7.setFont(font)
        self.edit_lane_btn = QPushButton(SectionsDialog)
        self.edit_lane_btn.setObjectName(u"edit_lane_btn")
        self.edit_lane_btn.setGeometry(QRect(209, 220, 75, 24))
        self.cancel_lane_btn = QPushButton(SectionsDialog)
        self.cancel_lane_btn.setObjectName(u"cancel_lane_btn")
        self.cancel_lane_btn.setGeometry(QRect(290, 220, 75, 24))

        self.retranslateUi(SectionsDialog)

        QMetaObject.connectSlotsByName(SectionsDialog)
    # setupUi

    def retranslateUi(self, SectionsDialog):
        SectionsDialog.setWindowTitle(QCoreApplication.translate("SectionsDialog", u"Dialog", None))
        self.direction_comboBox.setItemText(0, QCoreApplication.translate("SectionsDialog", u"Straight", None))
        self.direction_comboBox.setItemText(1, QCoreApplication.translate("SectionsDialog", u"Bend", None))

        self.label_6.setText(QCoreApplication.translate("SectionsDialog", u"Section Type", None))
        self.label_5.setText(QCoreApplication.translate("SectionsDialog", u"Radius (m)", None))
        self.label_7.setText(QCoreApplication.translate("SectionsDialog", u"Lenght (m)", None))
        self.edit_lane_btn.setText(QCoreApplication.translate("SectionsDialog", u"Add Lane", None))
        self.cancel_lane_btn.setText(QCoreApplication.translate("SectionsDialog", u"Cancel", None))
    # retranslateUi

