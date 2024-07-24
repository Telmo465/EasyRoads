# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lanesDialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_LanesDialog(object):
    def setupUi(self, LanesDialog):
        if not LanesDialog.objectName():
            LanesDialog.setObjectName(u"LanesDialog")
        LanesDialog.resize(528, 400)
        LanesDialog.setMinimumSize(QSize(528, 400))
        LanesDialog.setMaximumSize(QSize(528, 400))
        LanesDialog.setStyleSheet(u"QDialog{\n"
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
        self.line = QFrame(LanesDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 541, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(LanesDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(LanesDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 180, 151, 71))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.direction_comboBox = QComboBox(self.layoutWidget)
        self.direction_comboBox.addItem("")
        self.direction_comboBox.addItem("")
        self.direction_comboBox.setObjectName(u"direction_comboBox")
        self.direction_comboBox.setMinimumSize(QSize(0, 35))
        self.direction_comboBox.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.direction_comboBox)

        self.layoutWidget1 = QWidget(LanesDialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 90, 501, 65))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.lane_lineEdit = QLineEdit(self.layoutWidget1)
        self.lane_lineEdit.setObjectName(u"lane_lineEdit")
        self.lane_lineEdit.setMinimumSize(QSize(0, 35))
        self.lane_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.lane_lineEdit)

        self.layoutWidget2 = QWidget(LanesDialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(250, 200, 211, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.save_lane_btn = QPushButton(self.layoutWidget2)
        self.save_lane_btn.setObjectName(u"save_lane_btn")

        self.horizontalLayout.addWidget(self.save_lane_btn)

        self.cancel_lane_btn = QPushButton(self.layoutWidget2)
        self.cancel_lane_btn.setObjectName(u"cancel_lane_btn")

        self.horizontalLayout.addWidget(self.cancel_lane_btn)


        self.retranslateUi(LanesDialog)

        QMetaObject.connectSlotsByName(LanesDialog)
    # setupUi

    def retranslateUi(self, LanesDialog):
        LanesDialog.setWindowTitle(QCoreApplication.translate("LanesDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("LanesDialog", u"Add New Lane", None))
        self.label_3.setText(QCoreApplication.translate("LanesDialog", u"Direction", None))
        self.direction_comboBox.setItemText(0, QCoreApplication.translate("LanesDialog", u"Onwards", None))
        self.direction_comboBox.setItemText(1, QCoreApplication.translate("LanesDialog", u"Towards", None))

        self.label_2.setText(QCoreApplication.translate("LanesDialog", u"Lane Width (m)", None))
        self.save_lane_btn.setText(QCoreApplication.translate("LanesDialog", u"Add Lane", None))
#if QT_CONFIG(shortcut)
        self.save_lane_btn.setShortcut(QCoreApplication.translate("LanesDialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancel_lane_btn.setText(QCoreApplication.translate("LanesDialog", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.cancel_lane_btn.setShortcut(QCoreApplication.translate("LanesDialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

