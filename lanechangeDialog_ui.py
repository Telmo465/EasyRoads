# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lanechangeDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_LaneChangeDialog(object):
    def setupUi(self, LaneChangeDialog):
        if not LaneChangeDialog.objectName():
            LaneChangeDialog.setObjectName(u"LaneChangeDialog")
        LaneChangeDialog.setEnabled(True)
        LaneChangeDialog.resize(500, 600)
        LaneChangeDialog.setMinimumSize(QSize(500, 600))
        LaneChangeDialog.setMaximumSize(QSize(500, 600))
        LaneChangeDialog.setStyleSheet(u"QDialog{\n"
"	background-color: #d5d5d5;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selection-background-color: #2980B9;\n"
"}")
        self.label = QLabel(LaneChangeDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.line = QFrame(LaneChangeDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 741, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.checkBox = QCheckBox(LaneChangeDialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(41, 111, 55, 26))
        self.checkBox.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.checkBox.setFont(font1)
        self.checkBox_2 = QCheckBox(LaneChangeDialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QRect(41, 339, 97, 35))
        self.checkBox_2.setMinimumSize(QSize(0, 35))
        self.checkBox_2.setMaximumSize(QSize(16777215, 35))
        self.checkBox_2.setFont(font1)
        self.frame = QFrame(LaneChangeDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setGeometry(QRect(20, 150, 461, 191))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 10, 122, 22))
        self.label_3.setFont(font1)
        self.lane_lineEdit_4 = QLineEdit(self.frame)
        self.lane_lineEdit_4.setObjectName(u"lane_lineEdit_4")
        self.lane_lineEdit_4.setGeometry(QRect(291, 138, 123, 35))
        self.lane_lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_4.setMaximumSize(QSize(16777215, 35))
        self.lane_lineEdit_3 = QLineEdit(self.frame)
        self.lane_lineEdit_3.setObjectName(u"lane_lineEdit_3")
        self.lane_lineEdit_3.setGeometry(QRect(210, 40, 123, 35))
        self.lane_lineEdit_3.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_3.setMaximumSize(QSize(16777215, 35))
        self.lane_lineEdit_5 = QLineEdit(self.frame)
        self.lane_lineEdit_5.setObjectName(u"lane_lineEdit_5")
        self.lane_lineEdit_5.setGeometry(QRect(160, 138, 123, 35))
        self.lane_lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_5.setMaximumSize(QSize(16777215, 35))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 110, 122, 22))
        self.label_6.setFont(font1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 110, 111, 22))
        self.label_5.setFont(font1)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 110, 131, 22))
        self.label_7.setFont(font1)
        self.lane_lineEdit_2 = QLineEdit(self.frame)
        self.lane_lineEdit_2.setObjectName(u"lane_lineEdit_2")
        self.lane_lineEdit_2.setGeometry(QRect(50, 40, 123, 35))
        self.lane_lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_2.setMaximumSize(QSize(16777215, 35))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 10, 161, 22))
        self.label_4.setFont(font1)
        self.direction_comboBox = QComboBox(self.frame)
        self.direction_comboBox.addItem("")
        self.direction_comboBox.addItem("")
        self.direction_comboBox.setObjectName(u"direction_comboBox")
        self.direction_comboBox.setGeometry(QRect(30, 138, 122, 35))
        self.direction_comboBox.setMinimumSize(QSize(0, 35))
        self.direction_comboBox.setMaximumSize(QSize(16777215, 35))
        self.frame_2 = QFrame(LaneChangeDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(False)
        self.frame_2.setGeometry(QRect(30, 380, 421, 101))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.direction_comboBox_2 = QComboBox(self.frame_2)
        self.direction_comboBox_2.addItem("")
        self.direction_comboBox_2.addItem("")
        self.direction_comboBox_2.setObjectName(u"direction_comboBox_2")
        self.direction_comboBox_2.setGeometry(QRect(230, 50, 122, 35))
        self.direction_comboBox_2.setMinimumSize(QSize(0, 35))
        self.direction_comboBox_2.setMaximumSize(QSize(16777215, 35))
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(211, 22, 165, 22))
        self.label_9.setFont(font1)
        self.lane_lineEdit_6 = QLineEdit(self.frame_2)
        self.lane_lineEdit_6.setObjectName(u"lane_lineEdit_6")
        self.lane_lineEdit_6.setGeometry(QRect(10, 50, 165, 35))
        self.lane_lineEdit_6.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit_6.setMaximumSize(QSize(16777215, 35))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 22, 165, 22))
        self.label_8.setFont(font1)
        self.edit_lane_btn = QPushButton(LaneChangeDialog)
        self.edit_lane_btn.setObjectName(u"edit_lane_btn")
        self.edit_lane_btn.setGeometry(QRect(60, 520, 75, 24))
        self.cancel_lane_btn = QPushButton(LaneChangeDialog)
        self.cancel_lane_btn.setObjectName(u"cancel_lane_btn")
        self.cancel_lane_btn.setGeometry(QRect(141, 520, 75, 24))

        self.retranslateUi(LaneChangeDialog)
        self.checkBox.toggled.connect(self.frame.setEnabled)
        self.checkBox_2.toggled.connect(self.frame_2.setEnabled)

        QMetaObject.connectSlotsByName(LaneChangeDialog)
    # setupUi

    def retranslateUi(self, LaneChangeDialog):
        LaneChangeDialog.setWindowTitle(QCoreApplication.translate("LaneChangeDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("LaneChangeDialog", u"Lane Change 00", None))
        self.checkBox.setText(QCoreApplication.translate("LaneChangeDialog", u"Line", None))
        self.checkBox_2.setText(QCoreApplication.translate("LaneChangeDialog", u"GuardRail", None))
        self.label_3.setText(QCoreApplication.translate("LaneChangeDialog", u"Line YOffset (m)", None))
        self.label_6.setText(QCoreApplication.translate("LaneChangeDialog", u"Line Orientation", None))
        self.label_5.setText(QCoreApplication.translate("LaneChangeDialog", u"Line Gap (m)", None))
        self.label_7.setText(QCoreApplication.translate("LaneChangeDialog", u"Line Distance (m)", None))
        self.label_4.setText(QCoreApplication.translate("LaneChangeDialog", u"Line Size/Width (m)", None))
        self.direction_comboBox.setItemText(0, QCoreApplication.translate("LaneChangeDialog", u"Onwards", None))
        self.direction_comboBox.setItemText(1, QCoreApplication.translate("LaneChangeDialog", u"Towards", None))

        self.direction_comboBox_2.setItemText(0, QCoreApplication.translate("LaneChangeDialog", u"Onwards", None))
        self.direction_comboBox_2.setItemText(1, QCoreApplication.translate("LaneChangeDialog", u"Towards", None))

        self.label_9.setText(QCoreApplication.translate("LaneChangeDialog", u"GuardRail Orientation", None))
        self.label_8.setText(QCoreApplication.translate("LaneChangeDialog", u"GuardRail YOffset (m)", None))
        self.edit_lane_btn.setText(QCoreApplication.translate("LaneChangeDialog", u"Edit Lane", None))
#if QT_CONFIG(shortcut)
        self.edit_lane_btn.setShortcut(QCoreApplication.translate("LaneChangeDialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancel_lane_btn.setText(QCoreApplication.translate("LaneChangeDialog", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.cancel_lane_btn.setShortcut(QCoreApplication.translate("LaneChangeDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

