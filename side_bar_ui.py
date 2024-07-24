# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1444, 716)
        icon = QIcon()
        icon.addFile(u"icons/road-route-map-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_1 = QLabel(self.icon_only_widget)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(50, 50))
        self.logo_label_1.setMaximumSize(QSize(50, 50))
        self.logo_label_1.setPixmap(QPixmap(u"icons/road-route-map-icon.png"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn_1 = QPushButton(self.icon_only_widget)
        self.home_btn_1.setObjectName(u"home_btn_1")
        self.home_btn_1.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setIconSize(QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_1)

        self.route_btn_1 = QPushButton(self.icon_only_widget)
        self.route_btn_1.setObjectName(u"route_btn_1")
        icon2 = QIcon()
        icon2.addFile(u"icons/map.png", QSize(), QIcon.Normal, QIcon.Off)
        self.route_btn_1.setIcon(icon2)
        self.route_btn_1.setIconSize(QSize(20, 20))
        self.route_btn_1.setCheckable(True)
        self.route_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.route_btn_1)

        self.crossection_btn_1 = QPushButton(self.icon_only_widget)
        self.crossection_btn_1.setObjectName(u"crossection_btn_1")
        icon3 = QIcon()
        icon3.addFile(u"icons/road.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crossection_btn_1.setIcon(icon3)
        self.crossection_btn_1.setIconSize(QSize(20, 20))
        self.crossection_btn_1.setCheckable(True)
        self.crossection_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.crossection_btn_1)

        self.landscape_btn_1 = QPushButton(self.icon_only_widget)
        self.landscape_btn_1.setObjectName(u"landscape_btn_1")
        icon4 = QIcon()
        icon4.addFile(u"icons/tree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.landscape_btn_1.setIcon(icon4)
        self.landscape_btn_1.setIconSize(QSize(20, 20))
        self.landscape_btn_1.setCheckable(True)
        self.landscape_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.landscape_btn_1)

        self.traffic_btn_1 = QPushButton(self.icon_only_widget)
        self.traffic_btn_1.setObjectName(u"traffic_btn_1")
        self.traffic_btn_1.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"icons/car.png", QSize(), QIcon.Normal, QIcon.Off)
        self.traffic_btn_1.setIcon(icon5)
        self.traffic_btn_1.setIconSize(QSize(20, 20))
        self.traffic_btn_1.setCheckable(True)
        self.traffic_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.traffic_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn_1 = QPushButton(self.icon_only_widget)
        self.exit_btn_1.setObjectName(u"exit_btn_1")
        icon6 = QIcon()
        icon6.addFile(u"icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_1.setIcon(icon6)
        self.exit_btn_1.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.exit_btn_1)


        self.horizontalLayout_6.addWidget(self.icon_only_widget)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.full_menu_widget.setStyleSheet(u"color = blue;")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u"icons/road-route-map-icon.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font = QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_2 = QPushButton(self.full_menu_widget)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_2)

        self.route_btn_2 = QPushButton(self.full_menu_widget)
        self.route_btn_2.setObjectName(u"route_btn_2")
        self.route_btn_2.setIcon(icon2)
        self.route_btn_2.setIconSize(QSize(14, 14))
        self.route_btn_2.setCheckable(True)
        self.route_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.route_btn_2)

        self.crossection_btn_2 = QPushButton(self.full_menu_widget)
        self.crossection_btn_2.setObjectName(u"crossection_btn_2")
        self.crossection_btn_2.setIcon(icon3)
        self.crossection_btn_2.setIconSize(QSize(14, 14))
        self.crossection_btn_2.setCheckable(True)
        self.crossection_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.crossection_btn_2)

        self.landscape_btn_2 = QPushButton(self.full_menu_widget)
        self.landscape_btn_2.setObjectName(u"landscape_btn_2")
        self.landscape_btn_2.setIcon(icon4)
        self.landscape_btn_2.setIconSize(QSize(14, 14))
        self.landscape_btn_2.setCheckable(True)
        self.landscape_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.landscape_btn_2)

        self.traffic_btn_2 = QPushButton(self.full_menu_widget)
        self.traffic_btn_2.setObjectName(u"traffic_btn_2")
        self.traffic_btn_2.setIcon(icon5)
        self.traffic_btn_2.setIconSize(QSize(14, 14))
        self.traffic_btn_2.setCheckable(True)
        self.traffic_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.traffic_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        self.exit_btn_2.setIcon(icon6)
        self.exit_btn_2.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.horizontalLayout_6.addWidget(self.full_menu_widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.change_btn = QPushButton(self.widget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(26)
        self.change_btn.setFont(font1)
        self.change_btn.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u"icons/ui-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon7)
        self.change_btn.setIconSize(QSize(40, 40))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_12.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.horizontalSpacer_2 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.gridLayout_2 = QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.home = QFrame(self.home_page)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(1150, 0))
        self.home.setFrameShape(QFrame.StyledPanel)
        self.home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_18 = QFrame(self.home)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label = QLabel(self.frame_18)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label)

        self.course_name = QLineEdit(self.frame_18)
        self.course_name.setObjectName(u"course_name")
        self.course_name.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.course_name.setFont(font4)

        self.horizontalLayout_17.addWidget(self.course_name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.frame_18)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.save_data = QCheckBox(self.home)
        self.save_data.setObjectName(u"save_data")
        self.save_data.setFont(font3)

        self.verticalLayout_6.addWidget(self.save_data)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.frame_19 = QFrame(self.home)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.destination = QPushButton(self.frame_19)
        self.destination.setObjectName(u"destination")
        self.destination.setFont(font3)

        self.horizontalLayout_18.addWidget(self.destination)

        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_9.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.export_2 = QPushButton(self.home)
        self.export_2.setObjectName(u"export_2")
        self.export_2.setMaximumSize(QSize(200, 16777215))
        self.export_2.setFont(font3)

        self.verticalLayout_6.addWidget(self.export_2)


        self.gridLayout_2.addWidget(self.home, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.home_page)
        self.label_10.setObjectName(u"label_10")
        font6 = QFont()
        font6.setBold(True)
        self.label_10.setFont(font6)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_page)
        self.route_page = QWidget()
        self.route_page.setObjectName(u"route_page")
        self.gridLayout_3 = QGridLayout(self.route_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.route = QFrame(self.route_page)
        self.route.setObjectName(u"route")
        self.route.setMinimumSize(QSize(1150, 0))
        self.route.setFrameShape(QFrame.StyledPanel)
        self.route.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.route)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_16 = QFrame(self.route)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_15 = QFrame(self.frame_16)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.comboBox = QComboBox(self.frame_15)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.setFont(font3)

        self.horizontalLayout_16.addWidget(self.comboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        font7 = QFont()
        font7.setPointSize(16)
        self.label_4.setFont(font7)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.total_lenght = QLineEdit(self.frame_4)
        self.total_lenght.setObjectName(u"total_lenght")

        self.horizontalLayout_8.addWidget(self.total_lenght)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.curvature = QLineEdit(self.frame_5)
        self.curvature.setObjectName(u"curvature")

        self.horizontalLayout_9.addWidget(self.curvature)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.horizontalLayout_19.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_16)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.coordinatedef_1 = QLineEdit(self.frame_6)
        self.coordinatedef_1.setObjectName(u"coordinatedef_1")
        self.coordinatedef_1.setEnabled(True)
        self.coordinatedef_1.setMinimumSize(QSize(132, 21))

        self.horizontalLayout_10.addWidget(self.coordinatedef_1)

        self.coordinate_1 = QPushButton(self.frame_6)
        self.coordinate_1.setObjectName(u"coordinate_1")
        self.coordinate_1.setIcon(icon2)
        self.coordinate_1.setIconSize(QSize(20, 20))
        self.coordinate_1.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.coordinate_1)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.coordinatedef_2 = QLineEdit(self.frame_7)
        self.coordinatedef_2.setObjectName(u"coordinatedef_2")
        self.coordinatedef_2.setMinimumSize(QSize(132, 21))

        self.horizontalLayout_11.addWidget(self.coordinatedef_2)

        self.coordinate_2 = QPushButton(self.frame_7)
        self.coordinate_2.setObjectName(u"coordinate_2")
        self.coordinate_2.setIcon(icon2)
        self.coordinate_2.setIconSize(QSize(20, 20))
        self.coordinate_2.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.coordinate_2)


        self.verticalLayout_9.addWidget(self.frame_7)


        self.horizontalLayout_19.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_21 = QFrame(self.route)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.add_section_btn = QPushButton(self.frame_21)
        self.add_section_btn.setObjectName(u"add_section_btn")
        self.add_section_btn.setMinimumSize(QSize(150, 0))
        self.add_section_btn.setMaximumSize(QSize(150, 16777215))
        self.add_section_btn.setFont(font3)

        self.horizontalLayout_22.addWidget(self.add_section_btn)

        self.remove_section = QPushButton(self.frame_21)
        self.remove_section.setObjectName(u"remove_section")
        self.remove_section.setMinimumSize(QSize(150, 0))
        self.remove_section.setMaximumSize(QSize(150, 16777215))
        self.remove_section.setFont(font3)

        self.horizontalLayout_22.addWidget(self.remove_section)

        self.clear_all_section = QPushButton(self.frame_21)
        self.clear_all_section.setObjectName(u"clear_all_section")
        self.clear_all_section.setMinimumSize(QSize(150, 0))
        self.clear_all_section.setMaximumSize(QSize(150, 16777215))
        self.clear_all_section.setFont(font3)

        self.horizontalLayout_22.addWidget(self.clear_all_section)


        self.verticalLayout_14.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_3 = QSpacerItem(17, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.frame_12 = QFrame(self.frame_21)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(454, 250))
        self.frame_12.setMaximumSize(QSize(454, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.tableWidget_3 = QTableWidget(self.frame_12)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMaximumSize(QSize(454, 16777215))
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_16.addWidget(self.tableWidget_3)


        self.verticalLayout_14.addWidget(self.frame_12)


        self.horizontalLayout_23.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addWidget(self.frame_21)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.frame_14 = QFrame(self.route)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.height_input = QLineEdit(self.frame_14)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setMinimumSize(QSize(132, 21))
        self.height_input.setMaximumSize(QSize(132, 21))

        self.horizontalLayout_15.addWidget(self.height_input)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.label_11 = QLabel(self.route)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.verticalLayout_15.addWidget(self.label_11)

        self.label_14 = QLabel(self.route)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)

        self.verticalLayout_15.addWidget(self.label_14)


        self.horizontalLayout_24.addLayout(self.verticalLayout_15)

        self.frame_17 = QFrame(self.route)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_11 = QFrame(self.frame_17)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(351, 361))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_5)

        self.preview = QPushButton(self.frame_17)
        self.preview.setObjectName(u"preview")
        self.preview.setMinimumSize(QSize(0, 0))
        self.preview.setMaximumSize(QSize(100, 16777215))
        self.preview.setFont(font3)

        self.horizontalLayout_21.addWidget(self.preview)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.horizontalLayout_24.addWidget(self.frame_17)


        self.gridLayout_3.addWidget(self.route, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.route_page)
        self.crossection_page = QWidget()
        self.crossection_page.setObjectName(u"crossection_page")
        self.gridLayout_4 = QGridLayout(self.crossection_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_1234 = QFrame(self.crossection_page)
        self.frame_1234.setObjectName(u"frame_1234")
        self.frame_1234.setMinimumSize(QSize(1150, 658))
        self.frame_1234.setStyleSheet(u"")
        self.frame_1234.setFrameShape(QFrame.StyledPanel)
        self.frame_1234.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_1234)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(11, 49, 452, 192))
        self.tableWidget.setMinimumSize(QSize(452, 0))
        self.tableWidget.setMaximumSize(QSize(452, 16777215))
        self.tableWidget.setFont(font4)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2 = QTableWidget(self.frame_1234)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(11, 283, 1050, 192))
        self.tableWidget_2.setMinimumSize(QSize(1050, 0))
        self.tableWidget_2.setMaximumSize(QSize(1050, 16777215))
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.edit_lanechange = QPushButton(self.frame_1234)
        self.edit_lanechange.setObjectName(u"edit_lanechange")
        self.edit_lanechange.setGeometry(QRect(11, 481, 225, 30))
        self.edit_lanechange.setMinimumSize(QSize(225, 30))
        self.edit_lanechange.setMaximumSize(QSize(225, 16777215))
        self.edit_lanechange.setFont(font3)
        self.layoutWidget = QWidget(self.frame_1234)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 464, 32))
        self.horizontalLayout_20 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.add_lane_btn = QPushButton(self.layoutWidget)
        self.add_lane_btn.setObjectName(u"add_lane_btn")
        self.add_lane_btn.setMinimumSize(QSize(150, 0))
        self.add_lane_btn.setMaximumSize(QSize(150, 16777215))
        self.add_lane_btn.setFont(font3)

        self.horizontalLayout_20.addWidget(self.add_lane_btn)

        self.remove_lane = QPushButton(self.layoutWidget)
        self.remove_lane.setObjectName(u"remove_lane")
        self.remove_lane.setMinimumSize(QSize(150, 0))
        self.remove_lane.setMaximumSize(QSize(150, 16777215))
        self.remove_lane.setFont(font3)

        self.horizontalLayout_20.addWidget(self.remove_lane)

        self.clear_all_lanes = QPushButton(self.layoutWidget)
        self.clear_all_lanes.setObjectName(u"clear_all_lanes")
        self.clear_all_lanes.setMinimumSize(QSize(150, 0))
        self.clear_all_lanes.setMaximumSize(QSize(150, 16777215))
        self.clear_all_lanes.setFont(font3)

        self.horizontalLayout_20.addWidget(self.clear_all_lanes)

        self.confirm_lanes = QPushButton(self.frame_1234)
        self.confirm_lanes.setObjectName(u"confirm_lanes")
        self.confirm_lanes.setGeometry(QRect(11, 247, 141, 30))
        self.confirm_lanes.setMinimumSize(QSize(141, 30))
        self.confirm_lanes.setMaximumSize(QSize(150, 16777215))
        self.confirm_lanes.setFont(font3)
        self.label_13 = QLabel(self.frame_1234)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 640, 731, 16))
        self.label_13.setFont(font6)

        self.gridLayout_4.addWidget(self.frame_1234, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.crossection_page)
        self.landscape_page = QWidget()
        self.landscape_page.setObjectName(u"landscape_page")
        self.horizontalLayout_5 = QHBoxLayout(self.landscape_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.landscape = QFrame(self.landscape_page)
        self.landscape.setObjectName(u"landscape")
        self.landscape.setMinimumSize(QSize(1150, 0))
        self.landscape.setFrameShape(QFrame.StyledPanel)
        self.landscape.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.landscape)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_10 = QFrame(self.landscape)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.landscape_information = QLabel(self.frame_10)
        self.landscape_information.setObjectName(u"landscape_information")
        self.landscape_information.setMinimumSize(QSize(600, 0))
        self.landscape_information.setMaximumSize(QSize(600, 16777215))
        font8 = QFont()
        font8.setPointSize(14)
        self.landscape_information.setFont(font8)

        self.horizontalLayout_7.addWidget(self.landscape_information)

        self.landscape_list = QComboBox(self.frame_10)
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.addItem("")
        self.landscape_list.setObjectName(u"landscape_list")
        self.landscape_list.setFont(font8)

        self.horizontalLayout_7.addWidget(self.landscape_list)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.landscape)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        font9 = QFont()
        font9.setPointSize(20)
        self.label_2.setFont(font9)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.landscape_left = QComboBox(self.frame_9)
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.addItem("")
        self.landscape_left.setObjectName(u"landscape_left")
        self.landscape_left.setMinimumSize(QSize(250, 0))
        self.landscape_left.setMaximumSize(QSize(250, 16777215))
        self.landscape_left.setFont(font4)

        self.horizontalLayout_13.addWidget(self.landscape_left)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font9)

        self.horizontalLayout_13.addWidget(self.label_3)

        self.landscape_right = QComboBox(self.frame_9)
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.addItem("")
        self.landscape_right.setObjectName(u"landscape_right")
        self.landscape_right.setMinimumSize(QSize(250, 0))
        self.landscape_right.setMaximumSize(QSize(250, 16777215))
        self.landscape_right.setFont(font4)

        self.horizontalLayout_13.addWidget(self.landscape_right)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_10.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.landscape, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.landscape_page)
        self.traffic_page = QWidget()
        self.traffic_page.setObjectName(u"traffic_page")
        self.horizontalLayout_14 = QHBoxLayout(self.traffic_page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_13 = QFrame(self.traffic_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(1150, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.add_traffic = QPushButton(self.frame_13)
        self.add_traffic.setObjectName(u"add_traffic")
        self.add_traffic.setMinimumSize(QSize(150, 0))
        self.add_traffic.setMaximumSize(QSize(150, 16777215))
        self.add_traffic.setFont(font3)

        self.horizontalLayout_26.addWidget(self.add_traffic)

        self.remove_traffic = QPushButton(self.frame_13)
        self.remove_traffic.setObjectName(u"remove_traffic")
        self.remove_traffic.setMinimumSize(QSize(150, 0))
        self.remove_traffic.setMaximumSize(QSize(150, 16777215))
        self.remove_traffic.setFont(font3)

        self.horizontalLayout_26.addWidget(self.remove_traffic)

        self.edit_traffic = QPushButton(self.frame_13)
        self.edit_traffic.setObjectName(u"edit_traffic")
        self.edit_traffic.setMinimumSize(QSize(150, 0))
        self.edit_traffic.setMaximumSize(QSize(150, 16777215))
        self.edit_traffic.setFont(font3)

        self.horizontalLayout_26.addWidget(self.edit_traffic)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_11)


        self.verticalLayout_17.addLayout(self.horizontalLayout_26)

        self.tableWidget_4 = QTableWidget(self.frame_13)
        if (self.tableWidget_4.columnCount() < 6):
            self.tableWidget_4.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMinimumSize(QSize(620, 250))
        self.tableWidget_4.setMaximumSize(QSize(620, 250))

        self.verticalLayout_17.addWidget(self.tableWidget_4)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_14.addWidget(self.frame_13, 0, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.traffic_page)

        self.verticalLayout_5.addWidget(self.stackedWidget, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.route_btn_1.toggled.connect(self.route_btn_2.setChecked)
        self.crossection_btn_1.toggled.connect(self.crossection_btn_2.setChecked)
        self.landscape_btn_1.toggled.connect(self.landscape_btn_2.setChecked)
        self.traffic_btn_1.toggled.connect(self.traffic_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.route_btn_2.toggled.connect(self.route_btn_1.setChecked)
        self.crossection_btn_2.toggled.connect(self.crossection_btn_1.setChecked)
        self.landscape_btn_2.toggled.connect(self.landscape_btn_1.setChecked)
        self.traffic_btn_2.toggled.connect(self.traffic_btn_1.setChecked)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyRoads", None))
        self.logo_label_1.setText("")
        self.home_btn_1.setText("")
        self.route_btn_1.setText("")
        self.crossection_btn_1.setText("")
        self.landscape_btn_1.setText("")
        self.traffic_btn_1.setText("")
        self.exit_btn_1.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"EasyRoads", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(shortcut)
        self.home_btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.route_btn_2.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.crossection_btn_2.setText(QCoreApplication.translate("MainWindow", u"Crossection", None))
        self.landscape_btn_2.setText(QCoreApplication.translate("MainWindow", u"Landscape", None))
        self.traffic_btn_2.setText(QCoreApplication.translate("MainWindow", u"Traffic", None))
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.change_btn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Course Name", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Course Name", None))
        self.save_data.setText(QCoreApplication.translate("MainWindow", u"Save Simulation Data", None))
        self.destination.setText(QCoreApplication.translate("MainWindow", u"Path: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Note: This application uses points to describe decimal numbers.", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Manual", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Random", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GPS", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total length (m)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Curvature Distribution %", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Coordinate 1</span></p></body></html>", None))
        self.coordinate_1.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Coordinate 2</span></p></body></html>", None))
        self.coordinate_2.setText("")
        self.add_section_btn.setText(QCoreApplication.translate("MainWindow", u"Add  Section", None))
        self.remove_section.setText(QCoreApplication.translate("MainWindow", u"Remove Section", None))
        self.clear_all_section.setText(QCoreApplication.translate("MainWindow", u"Clear All Sections", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Radius", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Max Height (m)</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"! Info: Choose one method to create the segments in the top left box. ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"In GPS mode, open the map, click to add a waypoint, and click again to view the coordinates; copy it by pressing Ctrl+C and paste with Ctrl+V.", None))
        self.preview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Width", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Direction", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Line YOffset", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Line Size (m)", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Line Orientation", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Line Distance", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Line Gap", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Guardrail", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Guardrail YOffset", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Guardrail Orientation", None));
        self.edit_lanechange.setText(QCoreApplication.translate("MainWindow", u"Edit Selected Lane Change", None))
        self.add_lane_btn.setText(QCoreApplication.translate("MainWindow", u"Add Lane", None))
        self.remove_lane.setText(QCoreApplication.translate("MainWindow", u"Remove Lane", None))
        self.clear_all_lanes.setText(QCoreApplication.translate("MainWindow", u"Clear All Lanes", None))
        self.confirm_lanes.setText(QCoreApplication.translate("MainWindow", u"Confirm Lanes", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"! Info: Add lanes on the top table. Whenever all lanes are defined, confirm it and start editing the lane changes.", None))
        self.landscape_information.setText(QCoreApplication.translate("MainWindow", u"Select a Landscape on the box at right; a short description will appear.", None))
        self.landscape_list.setItemText(0, QCoreApplication.translate("MainWindow", u"Select One", None))
        self.landscape_list.setItemText(1, QCoreApplication.translate("MainWindow", u"Alley1", None))
        self.landscape_list.setItemText(2, QCoreApplication.translate("MainWindow", u"Alley2", None))
        self.landscape_list.setItemText(3, QCoreApplication.translate("MainWindow", u"AncientVillage", None))
        self.landscape_list.setItemText(4, QCoreApplication.translate("MainWindow", u"CityWall", None))
        self.landscape_list.setItemText(5, QCoreApplication.translate("MainWindow", u"CountryVillage", None))
        self.landscape_list.setItemText(6, QCoreApplication.translate("MainWindow", u"DryMeadow", None))
        self.landscape_list.setItemText(7, QCoreApplication.translate("MainWindow", u"Farmed", None))
        self.landscape_list.setItemText(8, QCoreApplication.translate("MainWindow", u"Forest", None))
        self.landscape_list.setItemText(9, QCoreApplication.translate("MainWindow", u"FruitTree", None))
        self.landscape_list.setItemText(10, QCoreApplication.translate("MainWindow", u"Grassland", None))
        self.landscape_list.setItemText(11, QCoreApplication.translate("MainWindow", u"GroundFog", None))
        self.landscape_list.setItemText(12, QCoreApplication.translate("MainWindow", u"Hedge", None))
        self.landscape_list.setItemText(13, QCoreApplication.translate("MainWindow", u"Inhabited", None))
        self.landscape_list.setItemText(14, QCoreApplication.translate("MainWindow", u"LeafForest", None))
        self.landscape_list.setItemText(15, QCoreApplication.translate("MainWindow", u"Meadow", None))
        self.landscape_list.setItemText(16, QCoreApplication.translate("MainWindow", u"Meadows", None))
        self.landscape_list.setItemText(17, QCoreApplication.translate("MainWindow", u"RoadsideBush", None))
        self.landscape_list.setItemText(18, QCoreApplication.translate("MainWindow", u"SoundBarrierMetal", None))
        self.landscape_list.setItemText(19, QCoreApplication.translate("MainWindow", u"SoundBarrierWood", None))
        self.landscape_list.setItemText(20, QCoreApplication.translate("MainWindow", u"Suburb", None))
        self.landscape_list.setItemText(21, QCoreApplication.translate("MainWindow", u"Vineyard", None))
        self.landscape_list.setItemText(22, QCoreApplication.translate("MainWindow", u"Wooded", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Landscape Left", None))
        self.landscape_left.setItemText(0, QCoreApplication.translate("MainWindow", u"Select One", None))
        self.landscape_left.setItemText(1, QCoreApplication.translate("MainWindow", u"Alley1", None))
        self.landscape_left.setItemText(2, QCoreApplication.translate("MainWindow", u"Alley2", None))
        self.landscape_left.setItemText(3, QCoreApplication.translate("MainWindow", u"AncientVillage", None))
        self.landscape_left.setItemText(4, QCoreApplication.translate("MainWindow", u"CityWall", None))
        self.landscape_left.setItemText(5, QCoreApplication.translate("MainWindow", u"CountryVillage", None))
        self.landscape_left.setItemText(6, QCoreApplication.translate("MainWindow", u"DryMeadow", None))
        self.landscape_left.setItemText(7, QCoreApplication.translate("MainWindow", u"Farmed", None))
        self.landscape_left.setItemText(8, QCoreApplication.translate("MainWindow", u"Forest", None))
        self.landscape_left.setItemText(9, QCoreApplication.translate("MainWindow", u"FruitTree", None))
        self.landscape_left.setItemText(10, QCoreApplication.translate("MainWindow", u"Grassland", None))
        self.landscape_left.setItemText(11, QCoreApplication.translate("MainWindow", u"GroundFog", None))
        self.landscape_left.setItemText(12, QCoreApplication.translate("MainWindow", u"Hedge", None))
        self.landscape_left.setItemText(13, QCoreApplication.translate("MainWindow", u"Inhabited", None))
        self.landscape_left.setItemText(14, QCoreApplication.translate("MainWindow", u"LeafForest", None))
        self.landscape_left.setItemText(15, QCoreApplication.translate("MainWindow", u"Meadow", None))
        self.landscape_left.setItemText(16, QCoreApplication.translate("MainWindow", u"Meadows", None))
        self.landscape_left.setItemText(17, QCoreApplication.translate("MainWindow", u"RoadsideBush", None))
        self.landscape_left.setItemText(18, QCoreApplication.translate("MainWindow", u"SoundBarrierMetal", None))
        self.landscape_left.setItemText(19, QCoreApplication.translate("MainWindow", u"SoundBarrierWood", None))
        self.landscape_left.setItemText(20, QCoreApplication.translate("MainWindow", u"Suburb", None))
        self.landscape_left.setItemText(21, QCoreApplication.translate("MainWindow", u"Vineyard", None))
        self.landscape_left.setItemText(22, QCoreApplication.translate("MainWindow", u"Wooded", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Landscape Right", None))
        self.landscape_right.setItemText(0, QCoreApplication.translate("MainWindow", u"Select One", None))
        self.landscape_right.setItemText(1, QCoreApplication.translate("MainWindow", u"Alley1", None))
        self.landscape_right.setItemText(2, QCoreApplication.translate("MainWindow", u"Alley2", None))
        self.landscape_right.setItemText(3, QCoreApplication.translate("MainWindow", u"AncientVillage", None))
        self.landscape_right.setItemText(4, QCoreApplication.translate("MainWindow", u"CityWall", None))
        self.landscape_right.setItemText(5, QCoreApplication.translate("MainWindow", u"CountryVillage", None))
        self.landscape_right.setItemText(6, QCoreApplication.translate("MainWindow", u"DryMeadow", None))
        self.landscape_right.setItemText(7, QCoreApplication.translate("MainWindow", u"Farmed", None))
        self.landscape_right.setItemText(8, QCoreApplication.translate("MainWindow", u"Forest", None))
        self.landscape_right.setItemText(9, QCoreApplication.translate("MainWindow", u"FruitTree", None))
        self.landscape_right.setItemText(10, QCoreApplication.translate("MainWindow", u"Grassland", None))
        self.landscape_right.setItemText(11, QCoreApplication.translate("MainWindow", u"GroundFog", None))
        self.landscape_right.setItemText(12, QCoreApplication.translate("MainWindow", u"Hedge", None))
        self.landscape_right.setItemText(13, QCoreApplication.translate("MainWindow", u"Inhabited", None))
        self.landscape_right.setItemText(14, QCoreApplication.translate("MainWindow", u"LeafForest", None))
        self.landscape_right.setItemText(15, QCoreApplication.translate("MainWindow", u"Meadow", None))
        self.landscape_right.setItemText(16, QCoreApplication.translate("MainWindow", u"Meadows", None))
        self.landscape_right.setItemText(17, QCoreApplication.translate("MainWindow", u"RoadsideBush", None))
        self.landscape_right.setItemText(18, QCoreApplication.translate("MainWindow", u"SoundBarrierMetal", None))
        self.landscape_right.setItemText(19, QCoreApplication.translate("MainWindow", u"SoundBarrierWood", None))
        self.landscape_right.setItemText(20, QCoreApplication.translate("MainWindow", u"Suburb", None))
        self.landscape_right.setItemText(21, QCoreApplication.translate("MainWindow", u"Vineyard", None))
        self.landscape_right.setItemText(22, QCoreApplication.translate("MainWindow", u"Wooded", None))

        self.add_traffic.setText(QCoreApplication.translate("MainWindow", u"Add Traffic", None))
        self.remove_traffic.setText(QCoreApplication.translate("MainWindow", u"Remove Traffic", None))
        self.edit_traffic.setText(QCoreApplication.translate("MainWindow", u"Edit Traffic", None))
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Lane", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Vehicle(s)", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Distance", None));
    # retranslateUi

