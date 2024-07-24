import sys
import os
import io
import folium
import math
import random
from teste import calc_gps_sections
from teste import height_profile
import openrouteservice as ors
from openrouteservice import convert
from functools import reduce
client =  ors.Client(key='5b3ce3597851110001cf6248673af3d65161476698e39eba4b28fc12')

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QWidget, QFileDialog, QStackedWidget, QFrame, QComboBox, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QCheckBox
from PySide6.QtCore import QFile, QTextStream, Qt, Slot, Signal, QObject
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel, QWebChannelAbstractTransport
from PySide6 import QtCore
from PySide6.QtGui import QClipboard

from second_window import Ui_SecondWindow
from side_bar import Ui_MainWindow
from lanesDialog import Ui_LanesDialog
from lanechangeDialog import Ui_LaneChangeDialog
from SectionsDialog import Ui_SectionsDialog
from TrafficDialog import Ui_TrafficDialog
from Edit_traffDialog import Ui_Edit_traffDialog

#function create random sections course
def random_course(total_length, CD):
        min_segment_length = 100  # Minimum segment length in meters
        max_segment_length = 1000  # Maximum segment length in meters
        num_segments = max(1, 2*round(total_length / max_segment_length))  # Calculate the number of segments
        segments = []
        new_segments = []
        remaining_length = total_length
        for _ in range(num_segments - 1):
            # Generate a random length for the segment, ensuring it's at least 50 meters and does not exceed the maximum length
            segment_length = random.randint(min_segment_length, min(max_segment_length, remaining_length - min_segment_length * (num_segments - len(segments) - 1)))
            segments.append(segment_length)
            remaining_length -= segment_length
        
        # The last segment takes the remaining length
        segments.append(remaining_length)
    
        curve_segments = math.ceil(CD/100*len(segments))
        # Randomly select indices for the curve segments
        curve_indices = random.sample(range(len(segments)), curve_segments)
        
        # Print Bend and Straight segments
        for i in range(len(segments)):
            if i in curve_indices:
                direction = random.choice([-1, 1])
                new_segments.append(f"Bend({segments[i]},{segments[i] * direction})")
            else:
                new_segments.append(f"Straight({segments[i]})")
        return new_segments

#function to plot the Straight / Bend segments
def plot_segments(ax, segments):
    points = [(0, 0)]  # Starting point

    for segment in segments:
        if "Straight" in segment:
            length = int(segment.split('(')[1].split(')')[0])
            last_x, last_y = points[-1]
            new_point = (last_x, last_y + length)
            points.append(new_point)
        elif "Bend" in segment:
            length = int(segment.split(',')[1].split(')')[0])
            last_x, last_y = points[-1]
            new_point = (last_x + length / 2, last_y + abs(length))
            points.append(new_point)
    
    # Convert points to arrays for plotting
    points = np.array(points)
    ax.plot(points[:, 0], points[:, 1], '-')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized() 

        #Folium Window
        self.second_window = QMainWindow()
        self.second_ui = Ui_SecondWindow()
        self.second_ui.setupUi(self.second_window)

        #Add lanes Window
        self.lanes_window = QMainWindow()
        self.lanes_ui = Ui_LanesDialog()
        self.lanes_ui.setupUi(self.lanes_window)

        #Edit lanechange Window
        self.lanes_change_window = QMainWindow()
        self.lanes_change_ui = Ui_LaneChangeDialog()
        self.lanes_change_ui.setupUi(self.lanes_change_window)

        #Add sections Window
        self.sections_window = QMainWindow()
        self.sections_ui = Ui_SectionsDialog()
        self.sections_ui.setupUi(self.sections_window)
        self.sections_ui.lane_lineEdit_4.setDisabled(True)

        #Add traffic Window
        self.traffic_window = QMainWindow()
        self.traffic_ui = Ui_TrafficDialog()
        self.traffic_ui.setupUi(self.traffic_window)

        #Edit traffic Window
        self.edit_traffic_window = QMainWindow()
        self.edit_traffic_ui = Ui_Edit_traffDialog()
        self.edit_traffic_ui.setupUi(self.edit_traffic_window)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.ui.tableWidget_2.hide()
        
        self.route_type()

        self.ui.comboBox.activated.connect(self.route_type)
        
        #Define widgets open path
        self.path_location = self.findChild(QPushButton, "destination")
        self.label_9 = self.findChild(QLabel, "label_9")
        self.path_location.clicked.connect(self.clicker)

        #Define widgets export in home window
        self.export = self.findChild(QPushButton, "export_2")
        self.export.clicked.connect(self.exportConfig)
        self.save_data = self.findChild(QCheckBox, "save_data")

        #Define widgets GPS open
        self.coordinate_1 = self.findChild(QPushButton, "coordinate_1")
        self.coordinate_2 = self.findChild(QPushButton, "coordinate_2")
        self.coordinate_value_1 = self.findChild(QLineEdit, "coordinatedef_1")
        self.coordinate_value_2 = self.findChild(QLineEdit, "coordinatedef_2")
        self.height_input = self.findChild(QLineEdit, "height_input")
        self.coordinate_1.clicked.connect(self.open_window)
        self.coordinate_2.clicked.connect(self.open_window)

        self.setup_folium_map()

        #Define widgets Manual Sections
        self.type_section = self.findChild(QComboBox, "comboBox")
        self.add_section = self.findChild(QPushButton, "add_section_btn")
        self.clear_all_sections = self.findChild(QPushButton, "clear_all_section")
        self.remove_section = self.findChild(QPushButton, "remove_section")
        self.sections = self.findChild(QTableWidget, "tableWidget_3")
        self.sections.verticalHeader().setVisible(False)
        self.sections.setEditTriggers(QTableWidget.NoEditTriggers)

        self.sections_ui.edit_lane_btn.clicked.connect(self.confirm_section)
        self.sections_ui.edit_lane_btn.clicked.connect(self.sections_window.close)
        self.sections_ui.direction_comboBox.currentTextChanged.connect(self.on_direction_changed)
        self.sections_ui.cancel_lane_btn.clicked.connect(self.cancel_sec)
        self.sections_ui.cancel_lane_btn.clicked.connect(self.sections_window.close)

        self.add_section.clicked.connect(self.open_sections_window)
        self.clear_all_sections.clicked.connect(self.clear_sec)
        self.remove_section.clicked.connect(self.remove_sec)

        #Define widgets lanes
        self.add_lane_btn = self.findChild(QPushButton, "add_lane_btn")
        self.clear_all_lanes = self.findChild(QPushButton, "clear_all_lanes")
        self.remove_lane = self.findChild(QPushButton, "remove_lane")
        self.confirm_lanes = self.findChild(QPushButton, "confirm_lanes")
        self.edit_lanechange = self.findChild(QPushButton, "edit_lanechange")
        self.lanes_info = self.findChild(QTableWidget, "tableWidget")
        self.lane_change = self.findChild(QTableWidget, "tableWidget_2")
        self.lanes_info.verticalHeader().setVisible(False)
        self.lane_change.verticalHeader().setVisible(False)
        self.lanes_info.setEditTriggers(QTableWidget.NoEditTriggers)
        self.lane_change.setEditTriggers(QTableWidget.NoEditTriggers)

        self.edit_lanechange.clicked.connect(self.open_laneschange_window)
        
        self.confirm_lanes.clicked.connect(self.confirm)
        self.add_lane_btn.clicked.connect(self.open_lanes_window)
        self.clear_all_lanes.clicked.connect(self.clear_all)
        self.remove_lane.clicked.connect(self.delete_it)

        self.lanes_ui.save_lane_btn.clicked.connect(self.add_it)
        self.lanes_ui.cancel_lane_btn.clicked.connect(self.cancel_it)
        self.lanes_ui.save_lane_btn.clicked.connect(self.lanes_window.close)
        self.lanes_ui.cancel_lane_btn.clicked.connect(self.lanes_window.close)

        self.lanes_change_ui.edit_lane_btn.clicked.connect(self.edit_lane)
        self.lanes_change_ui.edit_lane_btn.clicked.connect(self.lanes_change_window.close)
        self.lanes_change_ui.cancel_lane_btn.clicked.connect(self.cancel_edit)
        self.lanes_change_ui.cancel_lane_btn.clicked.connect(self.lanes_change_window.close)
        
        #Define widgets landscapes
        self.landscape_list = self.findChild(QComboBox, "landscape_list")
        self.landscape_information = self.findChild(QLabel, "landscape_information")
        self.landscape_information.setWordWrap(True)
        self.landscape_left = self.findChild(QComboBox, "landscape_left")
        self.landscape_right = self.findChild(QComboBox, "landscape_right")

        self.landscape_list.activated.connect(self.landscape_description)

        # Define widgets name of course
        self.course_name = self.findChild(QLineEdit, "course_name")
        self.widget = self.findChild(QWidget, "widget")
        self.label_12 = self.widget.findChild(QLabel, "label_12")

        self.course_name.textChanged.connect(self.changeText)

        #define widgets traffic
        self.add_traffic = self.findChild(QPushButton, "add_traffic")
        self.edit_traffic = self.findChild(QPushButton, "edit_traffic")
        self.remove_traffic = self.findChild(QPushButton, "remove_traffic")
        self.traffic = self.findChild(QTableWidget, "tableWidget_4")
        self.traffic.verticalHeader().setVisible(False)
        self.traffic.setEditTriggers(QTableWidget.NoEditTriggers)

        self.add_traffic.clicked.connect(self.open_traffic)
        self.traffic_ui.add_traffic.clicked.connect(self.add_traff)
        self.traffic_ui.add_traffic.clicked.connect(self.traffic_window.close)

        self.remove_traffic.clicked.connect(self.remove_traff)

        self.edit_traffic.clicked.connect(self.open_edit_traffic)
        self.edit_traffic_ui.add_traffic.clicked.connect(self.edit_traff)
        self.edit_traffic_ui.add_traffic.clicked.connect(self.edit_traffic_window.close)

        self.traffic_ui.cancel_ltraffic.clicked.connect(self.traffic_window.close)
        self.edit_traffic_ui.cancel_ltraffic.clicked.connect(self.edit_traffic_window.close)

        # Define widgets menu
        self.ui.home_btn_1.toggled.connect(self.on_home_btn_1_toggled)
        self.ui.home_btn_2.toggled.connect(self.on_home_btn_2_toggled)
        self.ui.route_btn_1.toggled.connect(self.on_route_btn_1_toggled)
        self.ui.route_btn_2.toggled.connect(self.on_route_btn_2_toggled)
        self.ui.crossection_btn_1.toggled.connect(self.on_crossection_btn_1_toggled)
        self.ui.crossection_btn_2.toggled.connect(self.on_crossection_btn_2_toggled)
        self.ui.landscape_btn_1.toggled.connect(self.on_landscape_btn_1_toggled)
        self.ui.landscape_btn_2.toggled.connect(self.on_landscape_btn_2_toggled)
        self.ui.traffic_btn_1.toggled.connect(self.on_traffic_btn_1_toggled)
        self.ui.traffic_btn_2.toggled.connect(self.on_traffic_btn_2_toggled)

        #Define widgets plot view
        self.view_map = self.findChild(QFrame, "frame_11")

        self.horizontalLayout_4 = QHBoxLayout(self.view_map)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.preview = self.findChild(QPushButton, "preview")
        self.preview.clicked.connect(self.plotOnCanvas)


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontalLayout_4.addWidget(self.canvas)
        self.plotOnCanvas()
        
    #Function for Enable/Disable Route Creation Types
    def route_type(self):
        if self.ui.comboBox.currentText() == "GPS":
            self.ui.frame_2.setEnabled(True)
            self.ui.frame_3.setEnabled(False)
            self.ui.frame_21.setEnabled(False)
        elif self.ui.comboBox.currentText() == "Random":
            self.ui.frame_2.setEnabled(False)
            self.ui.frame_3.setEnabled(True)
            self.ui.frame_21.setEnabled(False)
        elif self.ui.comboBox.currentText() == "Manual":
            self.ui.frame_2.setEnabled(False)
            self.ui.frame_3.setEnabled(False)
            self.ui.frame_21.setEnabled(True)

    #Function to display the route in a plot format
    def plotOnCanvas(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        #If GPS
        if self.ui.comboBox.currentText() == "GPS":
        
            coord1 = self.coordinate_value_1.text().split(',')
            coord2 = self.coordinate_value_2.text().split(',')
            
            coords = [[float(coord1[1]), float(coord1[0])], [float(coord2[1]), float(coord2[0])]]
            #print("coordinates:", coords)
            route = client.directions(coordinates=coords,profile='driving-car',format='geojson')
            
            geometry = client.directions(coords)['routes'][0]['geometry']
            decoded = convert.decode_polyline(geometry)

            points_list = decoded.get('coordinates')
            points_array = np.array(decoded.get('coordinates'))
            #print(points_array)
            self.gps_segments = calc_gps_sections(points_list)

            x, y = points_array.T

            ax.plot(x, y, '-')

        #If RANDOM
        elif self.ui.comboBox.currentText() == "Random":
            total_length = int(self.ui.total_lenght.text())
            curvature = int(self.ui.curvature.text() or 0)
            self.segments = random_course(total_length, curvature)
            self.random_segments = self.segments
            #print(self.segments)
            plot_segments(ax, self.segments)

        #If MANUAL
        elif self.ui.comboBox.currentText() == "Manual":
            self.segments = []
            row_count = self.sections.rowCount()
            for row in range(row_count):
                section_type = self.sections.item(row, 0).text()
                section_length = self.sections.item(row, 1).text()
                section_radius = self.sections.item(row, 2).text()
                
                if section_type == "Straight":
                    segment = f"Straight({section_length})"
                else:  # Assume "Bend" or other types if needed
                    segment = f"Bend({section_length},{section_radius})"
                
                self.segments.append(segment)
            self.manual_segments = self.segments
            plot_segments(ax, self.segments)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.figure.tight_layout()

        self.canvas.draw()        

    #Function to setup folium map
    def setup_folium_map(self):
        # Create a Folium map
        self.folium_map = folium.Map(location=list(reversed([ -8.636255008060868, 41.13669024075316])), tiles="cartodbpositron", zoom_start=8)

        self.folium_map.add_child(folium.ClickForMarker("${lat}, ${lng}"))

        # Convert the map to HTML and display it in the second UI
        data = io.BytesIO()
        self.folium_map.save(data, close_file=False)
        self.second_ui.webEngineView.setHtml(data.getvalue().decode())

    #functs to open new windows
        #Folium Map
    def open_window(self):
        self.second_window.show()

        #Add lanes window
    def open_lanes_window(self):
        self.lanes_window.show()

        #Add section window
    def open_sections_window(self):
        self.sections_window.show()

        #Edit traffic window
    def open_edit_traffic(self):
        selected_row = self.traffic.currentRow()
        if selected_row != -1:
            self.edit_traffic_ui.comboBox.setCurrentIndex(-1)
            self.edit_traffic_ui.comboBox.clear()
            row_count = self.lanes_info.rowCount()
            for index in range(row_count):
                self.edit_traffic_ui.comboBox.addItem(str(index))

            def get_item_text(row, column):
                item = self.traffic.item(row, column)
                return item.text() if item is not None else ""
            
            self.edit_traffic_ui.comboBox.setCurrentText(get_item_text(selected_row, 0))
            self.edit_traffic_ui.comboBox_2.setCurrentText(get_item_text(selected_row, 1))
            self.edit_traffic_ui.comboBox_3.setCurrentText(get_item_text(selected_row, 2))
            self.edit_traffic_ui.lane_lineEdit_5.setText(get_item_text(selected_row, 3))
            self.edit_traffic_ui.comboBox_6.setCurrentText(get_item_text(selected_row, 4))
            self.edit_traffic_ui.lane_lineEdit_6.setText(get_item_text(selected_row, 5))

            self.edit_traffic_window.show()
        
        #Add traffic window
    def open_traffic(self):

        self.traffic_ui.comboBox.setCurrentIndex(-1)
        self.traffic_ui.comboBox.clear()
        row_count = self.lanes_info.rowCount()
        
        if row_count != 0:
            for index in range(row_count):
                self.traffic_ui.comboBox.addItem(str(index))

            self.traffic_window.show()

        #Add laneschange window
    def open_laneschange_window(self):
        selected_row = self.lane_change.currentRow()
        index = self.lane_change.item(selected_row, 0).text()
        self.lanes_change_ui.label.setText("Lane Change " + str(index))

        def get_item_text(row, column):
            item = self.lane_change.item(row, column)
            return item.text() if item is not None else ""

        self.lanes_change_ui.lane_lineEdit_2.setText(get_item_text(selected_row, 2))
        self.lanes_change_ui.lane_lineEdit_3.setText(get_item_text(selected_row, 3))
        self.lanes_change_ui.direction_comboBox.setCurrentText(get_item_text(selected_row, 4))
        self.lanes_change_ui.lane_lineEdit_4.setText(get_item_text(selected_row, 5))
        self.lanes_change_ui.lane_lineEdit_5.setText(get_item_text(selected_row, 6))
        self.lanes_change_ui.lane_lineEdit_6.setText(get_item_text(selected_row, 8))
        self.lanes_change_ui.direction_comboBox_2.setCurrentText(get_item_text(selected_row, 9))

        self.lanes_change_window.show()

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            btn.setAutoExclusive(True)
                    
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_route_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_route_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_crossection_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_crossection_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_landscape_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_landscape_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_traffic_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_traffic_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    #functions crossections
    #create laneschange Window
    def confirm(self):
        self.lane_change.show()
        self.update_second_table()

    #Delete all lanes
    def clear_all(self):
        self.lanes_info.setRowCount(0)
        self.lane_change.setRowCount(0)

    #Add lane
    def add_it(self):
        # Call the original add_it logic
        # Get the index of the currently selected row
        selected_row = self.lanes_info.currentRow()

        # If no row is selected, set selected_row to -1
        if selected_row == -1:
            selected_row = self.lanes_info.rowCount() - 1
        
        # Retrieve data from UI elements
        lane_width = self.lanes_ui.lane_lineEdit.text()
        lane_direction = self.lanes_ui.direction_comboBox.currentText()

        # Insert data into the table
        row_count = self.lanes_info.rowCount()
        new_row_index = selected_row + 1 if selected_row != -1 else row_count
        self.lanes_info.insertRow(new_row_index)
        self.lanes_info.setItem(new_row_index, 0, QTableWidgetItem(str(row_count)))  # Set lane index
        self.lanes_info.setItem(new_row_index, 1, QTableWidgetItem(lane_width))  # Set lane width
        self.lanes_info.setItem(new_row_index, 2, QTableWidgetItem(lane_direction))  # Set lane direction

        # Clear the lane_lineEdit text
        self.lanes_ui.lane_lineEdit.clear()
        
        self.update_index()
        self.lane_change.hide()

    #Edit lane
    def edit_lane(self):
        selected_row = self.lane_change.currentRow()

        line_yoffset = ""
        line_size = ""
        line_orientation = ""
        line_distance = ""
        line_gap = ""
        guardrail_yoffset = ""
        guardrail_orientation = ""

        line = "0"
        guardrail = "0"

        if self.lanes_change_ui.checkBox.isChecked():  
            line = "1"
            line_yoffset = self.lanes_change_ui.lane_lineEdit_2.text()
            line_size = self.lanes_change_ui.lane_lineEdit_3.text()
            line_orientation = self.lanes_change_ui.direction_comboBox.currentText()
            line_distance = self.lanes_change_ui.lane_lineEdit_5.text()
            line_gap = self.lanes_change_ui.lane_lineEdit_4.text()
            
            self.lane_change.setItem(selected_row, 2, QTableWidgetItem(line_yoffset))
            self.lane_change.setItem(selected_row, 3, QTableWidgetItem(line_size))
            self.lane_change.setItem(selected_row, 4, QTableWidgetItem(line_orientation))
            self.lane_change.setItem(selected_row, 5, QTableWidgetItem(line_distance))
            self.lane_change.setItem(selected_row, 6, QTableWidgetItem(line_gap))

        if self.lanes_change_ui.checkBox_2.isChecked():
            guardrail = "1"
            guardrail_yoffset = self.lanes_change_ui.lane_lineEdit_6.text()
            guardrail_orientation = self.lanes_change_ui.direction_comboBox_2.currentText()
            
            self.lane_change.setItem(selected_row, 8, QTableWidgetItem(guardrail_yoffset))
            self.lane_change.setItem(selected_row, 9, QTableWidgetItem(guardrail_orientation))
        
        self.lane_change.setItem(selected_row, 1, QTableWidgetItem(line))
        self.lane_change.setItem(selected_row, 7, QTableWidgetItem(guardrail))

    #Cancel Add Lane 
    def cancel_it(self):
        self.lanes_ui.lane_lineEdit.setText("")

    #Cancel LaneChange Edit 
    def cancel_edit(self):
        self.lanes_change_ui.lane_lineEdit_2.setText("")
        self.lanes_change_ui.lane_lineEdit_3.setText("")
        self.lanes_change_ui.lane_lineEdit_4.setText("")
        self.lanes_change_ui.lane_lineEdit_5.setText("")
        self.lanes_change_ui.lane_lineEdit_6.setText("")
        self.lanes_change_ui.checkBox.setChecked(False)
        self.lanes_change_ui.checkBox_2.setChecked(False)

    #Delete lane
    def delete_it(self):
        clicked = self.lanes_info.currentRow()
        self.lanes_info.removeRow(clicked)
        self.update_index()
        self.lane_change.setRowCount(0)
        self.lane_change.hide()

    #Update LaneChanges Table
    def update_second_table(self):
        # Clear the lane_change table
        self.lane_change.clearContents()

        # Get the row count of lanes_info table
        row_count = self.lanes_info.rowCount()

        # Generate indexes for the rows in lane_change table
        indexes = ["00"]  # Start with "00"

        if row_count > 1:
            # Generate indexes for additional rows if there are more than one lane
            indexes.extend([f"{row}{row + 1}" for row in range(row_count - 1)])  # Generate indexes "01", "12", ..., "nn"
            # Add the last row index if lanes_info has more than one row
            indexes.append(f"{row_count - 1}{row_count - 1}")  # Add the last row index "nn" with adjusted row

        # Set the number of rows in lane_change table based on the number of indexes
        self.lane_change.setRowCount(len(indexes))

        # Populate the index column of lane_change table with the generated indexes
        for row, index in enumerate(indexes):
            item = QTableWidgetItem(index)
            self.lane_change.setItem(row, 0, item)

    #Update Indexes on lane Table
    def update_index(self):
        row_count = self.lanes_info.rowCount()
        for row in range(row_count):
            self.lanes_info.item(row, 0).setText(str(row))

    #functions sections
    #Delete all sections
    def clear_sec(self):
        self.sections.setRowCount(0)

    #Enable / Disable Radius
    def on_direction_changed(self, text):
        if text.lower() == "straight":
            self.sections_ui.lane_lineEdit_4.setDisabled(True)
            self.sections_ui.lane_lineEdit_4.setText("")
        else:
            self.sections_ui.lane_lineEdit_4.setDisabled(False)

    #Add section
    def confirm_section(self):
        selected_row = self.sections.currentRow()

        if selected_row == -1:
            selected_row = self.sections.rowCount() - 1

        section_type = self.sections_ui.direction_comboBox.currentText()
        section_lenght = self.sections_ui.lane_lineEdit_5.text()
        section_radius = self.sections_ui.lane_lineEdit_4.text()

        row_count = self.sections.rowCount()
        new_row_index = selected_row + 1 if selected_row != -1 else row_count
        self.sections.insertRow(new_row_index)
        self.sections.setItem(new_row_index, 0, QTableWidgetItem(section_type))  # Set lane index
        self.sections.setItem(new_row_index, 1, QTableWidgetItem(section_lenght))  # Set lane width
        self.sections.setItem(new_row_index, 2, QTableWidgetItem(section_radius))  # Set lane direction

        self.sections_ui.lane_lineEdit_5.clear()
        self.sections_ui.lane_lineEdit_4.clear()

    #Cancel add Section
    def cancel_sec(self):
        self.sections_ui.lane_lineEdit_4.setText("")
        self.sections_ui.lane_lineEdit_5.setText("")

    #Delete selected section
    def remove_sec(self):
        clicked = self.sections.currentRow()
        self.sections.removeRow(clicked)

    #functions traffic
    #Add traffic
    def add_traff(self):

        # Get the index of the currently selected row
        selected_row = self.traffic.currentRow()

        # If no row is selected, set selected_row to -1
        if selected_row == -1:
            selected_row = self.traffic.rowCount() - 1

        lane = self.traffic_ui.comboBox.currentText()
        type_traff = self.traffic_ui.comboBox_2.currentText()
        vehicle = self.traffic_ui.comboBox_3.currentText()
        quantity = self.traffic_ui.lane_lineEdit_5.text()
        position = self.traffic_ui.comboBox_6.currentText()
        distance = self.traffic_ui.lane_lineEdit_6.text()

        row_count = self.traffic.rowCount()
        new_row_index = selected_row + 1 if selected_row != -1 else row_count

        self.traffic.insertRow(new_row_index)
        self.traffic.setItem(new_row_index, 0, QTableWidgetItem(lane))
        self.traffic.setItem(new_row_index, 1, QTableWidgetItem(type_traff))
        self.traffic.setItem(new_row_index, 2, QTableWidgetItem(vehicle))
        self.traffic.setItem(new_row_index, 3, QTableWidgetItem(quantity))
        self.traffic.setItem(new_row_index, 4, QTableWidgetItem(position))
        self.traffic.setItem(new_row_index, 5, QTableWidgetItem(distance))

        self.traffic_ui.lane_lineEdit_5.clear()
        self.traffic_ui.lane_lineEdit_6.clear()

    #Edit traffic
    def edit_traff(self):
        selected_row = self.traffic.currentRow()

        lane = self.edit_traffic_ui.comboBox.currentText()
        type_traff = self.edit_traffic_ui.comboBox_2.currentText()
        vehicle = self.edit_traffic_ui.comboBox_3.currentText()
        quantity = self.edit_traffic_ui.lane_lineEdit_5.text()
        position = self.edit_traffic_ui.comboBox_6.currentText()
        distance = self.edit_traffic_ui.lane_lineEdit_6.text()

        self.traffic.setItem(selected_row, 0, QTableWidgetItem(lane))
        self.traffic.setItem(selected_row, 1, QTableWidgetItem(type_traff))
        self.traffic.setItem(selected_row, 2, QTableWidgetItem(vehicle))
        self.traffic.setItem(selected_row, 3, QTableWidgetItem(quantity))
        self.traffic.setItem(selected_row, 4, QTableWidgetItem(position))
        self.traffic.setItem(selected_row, 5, QTableWidgetItem(distance))

    #Remove selected traffic
    def remove_traff(self):
        clicked = self.traffic.currentRow()
        self.traffic.removeRow(clicked)

    #function update course name view
    def changeText(self):
        self.label_12.setText(self.course_name.text())

    #function select directory path
    def clicker(self):
        dirname = QFileDialog.getExistingDirectory(self, "Open Folder", ".\\" )

        if dirname:
            self.label_9.setText(str(dirname))

    #function landscapes descriptions
    def landscape_description(self):
        landscape = self.landscape_list.currentText()
        match landscape:
            case "Select One":
                self.landscape_information.setText("Description of Landscapes.")
            case "Alley1":
                self.landscape_information.setText("Creates an alley of smaller roadside trees.")
            case "Alley2":
                self.landscape_information.setText("Creates an alley of slim and high-rising trees.")
            case "AncientVillage":
                self.landscape_information.setText("Creates a village with timber frame buildings and small trees.")
            case "CityWall":
                self.landscape_information.setText("Creates a city wall which runs along the road.")
            case "CountryVillage":
                self.landscape_information.setText("Creates a village with stone buildings and small trees.")
            case "DryMeadow":
                self.landscape_information.setText("Creates a dried-out meadow made of different kinds of grass.")
            case "Farmed":
                self.landscape_information.setText("Creates grain and corn fields which are made accessible by farm tracks.")
            case "Forest":
                self.landscape_information.setText("Creates a coniferous forest. Near the road, additional forest shrubs and ground covering plants are displayed.")
            case "FruitTree":
                self.landscape_information.setText("Creates orchards. The fruit trees are placed on a grassland.")
            case "Grassland":
                self.landscape_information.setText("Creates grassland made of different kinds of grass and flowers.")
            case "GroundFog":
                self.landscape_information.setText("Creates an area filled with wafts of mist.")
            case "Hedge":
                self.landscape_information.setText("Creates a hedge made of small trees and bushes.")
            case "Inhabited":
                self.landscape_information.setText("Creates an estate of bungalows with people and small trees.")
            case "LeafForest":
                self.landscape_information.setText("Creates a broad-leaved forest. Near the road, additional forest shrubs and ground covering plants are displayed.")
            case "Meadow":
                self.landscape_information.setText("Creates a meadow or a recently cut grassland made of different kinds of grass.")
            case "Meadows":
                self.landscape_information.setText("Creates meadows which are limited by fences and made accessible by farm tracks")
            case "RoadsideBush":
                self.landscape_information.setText("Creates a row of bushes along the road.")
            case "SoundBarrierMetal":
                self.landscape_information.setText("Creates a sound barrier made from metal elements, which are placed along the road.")
            case "SoundBarrierWood":
                self.landscape_information.setText("Creates a sound barrier made from wooden elements, which are placed along the road.")
            case "Suburb":
                self.landscape_information.setText("Creates a suburb with modern residential buildings and small trees.")
            case "Vineyard":
                self.landscape_information.setText("Creates a vineyard.")
            case "Wooded":
                self.landscape_information.setText("Creates an area that is covered in trees.")

    def exportConfig(self):
        directory = self.label_9.text()
        course_name = self.course_name.text() or 'Course'
        landscape_left = self.landscape_left.currentText()
        landscape_right = self.landscape_right.currentText()
        self.plotOnCanvas()
        type_section = self.type_section.currentText()
        fileName = f"{course_name}.cfg"
        filePath = os.path.join(directory, fileName)

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Ensure the file does not overwrite an existing one
        base_filePath = filePath
        counter = 1
        while os.path.exists(filePath):
            filePath = f"{base_filePath[:-4]}_{counter}.cfg"
            counter += 1

        try:
            # Prepare the content for the .cfg file
            content = self.generateConfigContent(course_name, landscape_left, landscape_right,type_section)

            # Write the content to the file
            with open(filePath, 'w') as file:
                file.write(content)

            QMessageBox.information(self, 'Success', f'Configuration file saved to {filePath}')

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while saving the file: {e}')

    def generateConfigContent(self, course_name, landscape_left, landscape_right, type_section):

        # Check if save_data is checked and add corresponding content
        save_data_content = ""
        if self.save_data.isChecked():
            save_data_content = """
        
        Pool Record : Full
        {
            Executeable = true;

			SGEWorld.RenderMode = 2;

            DPUDataFile DataFile
            {
                Computer = {LOCALHOST};
                Index = 2000;
                Separator = ",";
                HeaderType = 1; 				
                LD_UserDataToken01 = VAR_NPARTICIPANT;
                Path = "DATA\\";
                Record = {
                    Mockup.AcceleratorPedal("AcceleratorPedal"),
                    Mockup.BrakePedal("BrakePedal"),
                    Mockup.SteeringWheel("SteeringWheel"),
                    VDyn.v_kmh("v_kmh")
                };
            };
        };
        """
        # Define landscape configurations
        landscape_configurations = {
            "Alley1": """
                MinObjDist = 10;
                MaxObjDist = 50;
            """,
            "Alley2": """
                MinObjDist = 10;
                MaxObjDist = 50;
            """,
            "AncientVillage": """
                MinObjDist = 10;
                AncientHouseDensity = 30;
                SmallTreeDensity = 30;

                MinObjdist = 10;
                MaxObjdist = 100;
            """,
            "CityWall": """
                MinObjPos = 0;
                MinObjDist = 1.5;
                MaxObjDist = 2.4;
            """,
            "CountryVillage": """
                MinObjdist = 20;
                MaxObjdist = 60;
                CountryHouseDensity = 3;
                SmallTreeDensity = 30;
            """,
            "DryMeadow": """
                MinObjDist = 0;
            """,
            "Farmed": """
                MinObjDist = 0;
                MaxObjdist = 30;
            """,
            "Forest": """
                MinObjdist = 2.5;
                MaxObjdist = 50;
            """,
            "FruitTree": """
                MinObjdist = 10;
            """,
            "Grassland": """
                MinObjDist = 0;
                MaxObjdist = 50;
            """,
            "GroundFog": """
                MinObjDist = 0;
                MaxObjDist = 20;
            """,
            "Hedge": """
                MinObjDist = 0;
                MaxObjDist = 30;
            """,
            "Inhabited": """
                MinObjdist = 20;
                MaxObjdist = 60;
                HouseDensity = 10;
                PersonDensity = 10;
                SmallTreeDensity = 10;
            """,
            "LeafForest": """
                MinObjdist = 0;
            """,
            "Meadow": """
                MinObjdist = 0;
                MaxObjDist = 30;
            """,
            "Meadows": """
                MinObjdist = 0;
                MaxObjDist = 70;
            """,
            "RoadsideBush": """
                MinObjdist = 1;
                MaxObjDist = 2;
            """,
            "SoundBarrierMetal": """
                MinObjDist = 1.5;
                MaxObjDist = 2.4;
            """,
            "SoundBarrierWood": """
                MinObjDist = 1.5;
                MaxObjDist = 2.4;
            """,
            "Suburb": """
                MinObjDist = 20;
                MaxObjDist = 100;
                SuburbHouseDensity = 30;
                SmallTreeDensity = 30;
            """,
            "Vineyard": """
                MinObjDist = 10;
                MaxObjDist = 100;
            """,
            "Wooded": """
                MinObjDist = 20;
                MaxObjDist = 100;
                HouseDensity = 10;
                TreeDensity = 20;
            """
        }

        # Generate landscape content based on the selected landscape names
        def generate_landscape_content(landscape_name, side):
            if landscape_name in landscape_configurations:
                return f"""
            LandscapeType{side} {landscape_name}
            {{{landscape_configurations[landscape_name]}}};
            """
            else:
                return f"""
            """

        # Generate landscape content
        landscape_left_content = generate_landscape_content(landscape_left, "Left")
        landscape_right_content = generate_landscape_content(landscape_right, "Right")
        
        # Generate lanes_info content from QTableWidget
        lanes_info_content = ""
        row_count = self.lanes_info.rowCount()
        for idx in range(row_count):
            col0 = self.lanes_info.item(idx, 0).text()
            col1 = self.lanes_info.item(idx, 1).text()
            col2 = self.lanes_info.item(idx, 2).text()
            row_content = f"({col0}, {col1}, 0.0, {col2}, Tar1, 1.0, 0.0, {{(None, 0.0)}})"
            if idx < row_count - 1:
                row_content += ","
            lanes_info_content += f"\n            {row_content}"

        # Generate lane_transitions content from QTableWidget
        lane_transitions_content = ""
        row_count = self.lane_change.rowCount()
        for idx in range(row_count):
            index0_item = self.lane_change.item(idx, 0)
            if index0_item:
                index0 = index0_item.text()
                col0 = index0[0]
                col1 = index0[1]
            else:
                continue

            col2_item = self.lane_change.item(idx, 1)
            col3_item = self.lane_change.item(idx, 2)
            col4_item = self.lane_change.item(idx, 3)
            col5_item = self.lane_change.item(idx, 4)
            col6_item = self.lane_change.item(idx, 5)
            col7_item = self.lane_change.item(idx, 6)
            col8_item = self.lane_change.item(idx, 7)
            col9_item = self.lane_change.item(idx, 8)
            col10_item = self.lane_change.item(idx, 9)

            col2 = col2_item.text() if col2_item else ""
            col3 = col3_item.text() if col3_item else ""
            if col3 == "" : col3="0.0"
            col4 = col4_item.text() if col4_item else ""
            col5 = col5_item.text() if col5_item else ""
            col6 = col6_item.text() if col6_item else ""
            col7 = col7_item.text() if col7_item else ""
            col8 = col8_item.text() if col8_item else ""
            col9 = col9_item.text() if col9_item else ""
            if col9 == "" : col9="0.0"
            col10 = col10_item.text() if col10_item else ""

            row_transitions = f"({col0}, {col1}, {{"
            if col2 == "1":
                row_transitions += f"(Line, {col3}, {col4}, {col5}, {col6}, {col7})"
            if col2 == "1" and col6 == "1":
                row_transitions += f","
            if col8 == "1":
                row_transitions += f"(Guardrail, {col9}, 1.0, {col10}, 0.0, 0.0)"
            row_transitions += " })"
            if idx < row_count - 1:
                row_transitions += ","
            lane_transitions_content += f"\n            {row_transitions}"

        # Determine the segments based on the source
        match type_section:
            case "Manual":
                segments = self.manual_segments
            case "Random":
                segments = self.random_segments
            case "GPS":
                segments = self.gps_segments
            case _:
                segments = []

        # Write segments to file
        segments_content = ";\n            ".join(segments) + ";"

        # Calculate total length of the course
        total_length = 0
        for segment in segments:
            segment_type, values = segment.split('(')
            length = int(values.split(',')[0].rstrip(')'))
            total_length += length

        # Get max height from QLineEdit
        max_height = float(self.height_input.text()) if self.height_input.text() else None 
        # Generate height profile
        height_profile_content = height_profile(total_length,max_height) if self.height_input.text() else height_profile(total_length)
        height_profile_content = "\n            ".join(height_profile_content)
        # Generate traffic content from QTableWidget
        traffic_content = ""
        row_count = self.traffic.rowCount()
        for idx in range(row_count):
            row_type = self.traffic.item(idx, 1).text()
            position_module = self.traffic.item(idx, 4).text()
            position_details = self.traffic.item(idx, 5).text()
            
            if row_type == "Source":
                group = self.traffic.item(idx, 2).text()
                number_of_vehicles = self.traffic.item(idx, 3).text()
                if position_module == "SimCar":
                    position = f"(SimCar, {position_details}, {self.traffic.item(idx, 0).text()})"
                else:
                    position = f"(u0, {position_details}, {self.traffic.item(idx, 0).text()})"
                
                traffic_content += f"""
            SourceX S{idx:02d}
            {{
                Position = {position};
                Group = {group};
                NumberOfVehicles = {number_of_vehicles};
                Distance = 10;
                BehaviourScheme = Standard;
                Flowpoints = 
                {{
                    (ModuleTime, 0, Activate)
                }};
            }};
            """
            elif row_type == "Vehicle":
                if position_module == "SimCar":
                    position = f"(SimCar, {position_details}, {self.traffic.item(idx, 0).text()})"
                else:
                    position = f"(u0, {position_details}, {self.traffic.item(idx, 0).text()})"

                traffic_content += f"""
            Vehicle uw{idx:02d}
            {{
                Vehicle = Car;
                Position = {position};
                Behaviour = Standard;
                Flowpoints =
                {{
                    (ModuleTime, 0, Activate)
                }};
            }};
            """

        # Build the content for the .cfg file using the application variables
        content = f"""
SILAB Configuration
{{
    Computerconfiguration Computers
    {{
        include System\\CompBase.inc

        includeif includes\\Comp_Test.inc
    }};
    
    DPUConfiguration DPUs
    {{
        include System\\DPUBase_SGE.inc

        {save_data_content}
    }};
}};

include system\\SYSBase.inc

SILAB System
{{
    WatchdogPeriod = 10000;
    LaunchData1 = ("Filename",VAR_DATAFILENAME,LD_EDIT_DEFAULT,"Data");
}};

includeif SGE/SGE_700.cfg
includeif MOV/MOP_700.inc
include SCNX/SCNXSGE_700.cfg
includeif SNDX/SNDX.cfg

SILAB TRF
{{
    include SILAB_TRFX_700.cfg
}};

SILAB SCN
{{
    include SCNX/SCNX_700.cfg

    # CrossSections ###################################################

    CrossSection {course_name}_crossSection
	{{
		ve = 60.0;
        Shoulder = {{1.0, 2.4, -0.7, Shoulder1}};
        Overlay = {{TarNew1, 1.0}};
		LaneInfos =
        {{{lanes_info_content}
        }};
        LaneTransitions =
		{{{lane_transitions_content}
        }};
	}};
    

    # Modules #######################################################
    
    define Module {course_name}
    {{
        ModuleID = 100;

        define Course U0
        {{
            NodeID = 4;
            CrossSection = {course_name}_crossSection;

            # Segments
            {segments_content}

            HeightProfile =
            {{
            {height_profile_content}    
            }};

            # LandscapeTypeLeft
            {landscape_left_content}

            # LandscapeTypeRight
            {landscape_right_content}

        }};

        U0 u0;

        Connections =
        {{
            Port1 <-> u0.Begin,
            u0.End <-> Port2
        }};

        Traffic uw0
        {{{traffic_content}
        }};
    
    }};
    
     # Map: ##########################################################
    Map Map1
    {{
        {course_name} uu00;

        SetupPoints =
        {{
            ("Setup0", uu00.Port1)
        }};
    }};
}};
"""
        return content.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file
    # with open("style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    # loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
