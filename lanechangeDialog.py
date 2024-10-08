# Form implementation generated from reading ui file 'lanechangeDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_LaneChangeDialog(object):
    def setupUi(self, LaneChangeDialog):
        LaneChangeDialog.setObjectName("LaneChangeDialog")
        LaneChangeDialog.setEnabled(True)
        LaneChangeDialog.resize(500, 600)
        LaneChangeDialog.setMinimumSize(QtCore.QSize(500, 600))
        LaneChangeDialog.setMaximumSize(QtCore.QSize(500, 600))
        LaneChangeDialog.setStyleSheet("QDialog{\n"
"    background-color: #d5d5d5;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid gray;\n"
"    border-radius: 6px;\n"
"    padding-left: 15px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 2px solid white;\n"
"    border-radius: 8px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background-color: black;\n"
"    color: white;\n"
"    height: 35px;\n"
"    padding-left: 15px;\n"
"    font-weight: bold;\n"
"    selection-background-color: #2980B9;\n"
"}")
        self.label = QtWidgets.QLabel(parent=LaneChangeDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=LaneChangeDialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QCheckBox(parent=LaneChangeDialog)
        self.checkBox.setGeometry(QtCore.QRect(41, 111, 55, 26))
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=LaneChangeDialog)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QtCore.QRect(41, 339, 97, 35))
        self.checkBox_2.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.frame = QtWidgets.QFrame(parent=LaneChangeDialog)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(20, 150, 461, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lane_lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lane_lineEdit_4.setGeometry(QtCore.QRect(291, 138, 123, 35))
        self.lane_lineEdit_4.setMinimumSize(QtCore.QSize(0, 35))
        self.lane_lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lane_lineEdit_4.setObjectName("lane_lineEdit_4")
        self.lane_lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lane_lineEdit_3.setGeometry(QtCore.QRect(210, 40, 123, 35))
        self.lane_lineEdit_3.setMinimumSize(QtCore.QSize(0, 35))
        self.lane_lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lane_lineEdit_3.setObjectName("lane_lineEdit_3")
        self.lane_lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lane_lineEdit_5.setGeometry(QtCore.QRect(160, 138, 123, 35))
        self.lane_lineEdit_5.setMinimumSize(QtCore.QSize(0, 35))
        self.lane_lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lane_lineEdit_5.setObjectName("lane_lineEdit_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 122, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(310, 110, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(160, 110, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lane_lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lane_lineEdit_2.setGeometry(QtCore.QRect(50, 40, 123, 35))
        self.lane_lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.lane_lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lane_lineEdit_2.setObjectName("lane_lineEdit_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(200, 10, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.direction_comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.direction_comboBox.setGeometry(QtCore.QRect(30, 138, 122, 35))
        self.direction_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.direction_comboBox.setMaximumSize(QtCore.QSize(16777215, 35))
        self.direction_comboBox.setObjectName("direction_comboBox")
        self.direction_comboBox.addItem("")
        self.direction_comboBox.addItem("")
        self.frame_2 = QtWidgets.QFrame(parent=LaneChangeDialog)
        self.frame_2.setEnabled(False)
        self.frame_2.setGeometry(QtCore.QRect(30, 380, 421, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.direction_comboBox_2 = QtWidgets.QComboBox(parent=self.frame_2)
        self.direction_comboBox_2.setGeometry(QtCore.QRect(230, 50, 122, 35))
        self.direction_comboBox_2.setMinimumSize(QtCore.QSize(0, 35))
        self.direction_comboBox_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.direction_comboBox_2.setObjectName("direction_comboBox_2")
        self.direction_comboBox_2.addItem("")
        self.direction_comboBox_2.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(211, 22, 165, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lane_lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lane_lineEdit_6.setGeometry(QtCore.QRect(10, 50, 165, 35))
        self.lane_lineEdit_6.setMinimumSize(QtCore.QSize(0, 35))
        self.lane_lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.lane_lineEdit_6.setObjectName("lane_lineEdit_6")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 22, 165, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.edit_lane_btn = QtWidgets.QPushButton(parent=LaneChangeDialog)
        self.edit_lane_btn.setGeometry(QtCore.QRect(60, 520, 75, 24))
        self.edit_lane_btn.setObjectName("edit_lane_btn")
        self.cancel_lane_btn = QtWidgets.QPushButton(parent=LaneChangeDialog)
        self.cancel_lane_btn.setGeometry(QtCore.QRect(141, 520, 75, 24))
        self.cancel_lane_btn.setObjectName("cancel_lane_btn")

        self.retranslateUi(LaneChangeDialog)
        self.checkBox.toggled['bool'].connect(self.frame.setEnabled) # type: ignore
        self.checkBox_2.toggled['bool'].connect(self.frame_2.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LaneChangeDialog)

    def retranslateUi(self, LaneChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        LaneChangeDialog.setWindowTitle(_translate("LaneChangeDialog", "Dialog"))
        self.label.setText(_translate("LaneChangeDialog", "Lane Change 00"))
        self.checkBox.setText(_translate("LaneChangeDialog", "Line"))
        self.checkBox_2.setText(_translate("LaneChangeDialog", "GuardRail"))
        self.label_3.setText(_translate("LaneChangeDialog", "Line YOffset (m)"))
        self.label_6.setText(_translate("LaneChangeDialog", "Line Orientation"))
        self.label_5.setText(_translate("LaneChangeDialog", "Line Gap (m)"))
        self.label_7.setText(_translate("LaneChangeDialog", "Line Distance (m)"))
        self.label_4.setText(_translate("LaneChangeDialog", "Line Size/Width (m)"))
        self.direction_comboBox.setItemText(0, _translate("LaneChangeDialog", "Onwards"))
        self.direction_comboBox.setItemText(1, _translate("LaneChangeDialog", "Towards"))
        self.direction_comboBox_2.setItemText(0, _translate("LaneChangeDialog", "Onwards"))
        self.direction_comboBox_2.setItemText(1, _translate("LaneChangeDialog", "Towards"))
        self.label_9.setText(_translate("LaneChangeDialog", "GuardRail Orientation"))
        self.label_8.setText(_translate("LaneChangeDialog", "GuardRail YOffset (m)"))
        self.edit_lane_btn.setText(_translate("LaneChangeDialog", "Edit Lane"))
        self.edit_lane_btn.setShortcut(_translate("LaneChangeDialog", "Return"))
        self.cancel_lane_btn.setText(_translate("LaneChangeDialog", "Cancel"))
        self.cancel_lane_btn.setShortcut(_translate("LaneChangeDialog", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LaneChangeDialog = QtWidgets.QDialog()
    ui = Ui_LaneChangeDialog()
    ui.setupUi(LaneChangeDialog)
    LaneChangeDialog.show()
    sys.exit(app.exec())
