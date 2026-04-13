# main.py
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor
import sys
from database import Database

# In MainWindow, update the stylesheet:

class FloraSidebar(QFrame):
    def __init__(self, stacked_widget, username):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setObjectName("sidebar")
        self.setFixedWidth(280)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 30, 0, 0)
        layout.setSpacing(15)
        
        # Logo / Title
        logo = QLabel("🌱 FLORA")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        # Decorative line
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("background-color: #A76D5E; max-height: 2px;")
        layout.addWidget(line)
        
        # Username label (display actual username)
        self.username_label = QLabel(f"Welcome, {username}")
        self.username_label.setObjectName("username")
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        
        layout.addSpacing(20)
        
        # Dashboard button with icon
        self.dashboard_btn = QPushButton("Dashboard")
        self.dashboard_btn.setObjectName("nav-btn")
        self.dashboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.dashboard_btn)
        
        # Records button with icon
        self.records_btn = QPushButton("Records")
        self.records_btn.setObjectName("nav-btn")
        self.records_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(self.records_btn)
        
        # Reports button with icon
        self.reports_btn = QPushButton("Reports")
        self.reports_btn.setObjectName("nav-btn")
        self.reports_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(self.reports_btn)
        
        # About button with icon
        self.about_btn = QPushButton("ℹAbout")
        self.about_btn.setObjectName("nav-btn")
        self.about_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        layout.addWidget(self.about_btn)
        
        layout.addStretch()
        
        # Logout button
        self.logout_btn = QPushButton("Log-out")
        self.logout_btn.setObjectName("logout-btn")
        self.logout_btn.clicked.connect(self.logout)
        layout.addWidget(self.logout_btn)
        
        self.setLayout(layout)
    
    def logout(self):
        # Close the main window and show login
        reply = QMessageBox.question(self, 'Confirm Logout', 
                                    'Are you sure you want to logout?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.window().close()
            from login import show_login_window
            show_login_window()

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Dashboard")
        title.setObjectName("page-title")
        title.setStyleSheet("""
            font-size: 32px;
            font-weight: 600;
            color: #2F3E46;
            font-family: 'Poppins';
            padding-bottom: 15px;
            border-bottom: 3px solid #A76D5E;
        """)
        layout.addWidget(title)

        # --- Dashboard Summary Cards ---
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: #FEFAE0;
                border-radius: 15px;
            }
        """)
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)

        # Quick stat cards
        total_crops = len(self.db.get_crops())
        total_records = len(self.db.fetch_records(""))
        most_planted = self.db.crop_report()[0][0] if self.db.crop_report() else "N/A"
        avg_fert = round(sum(x[5] for x in self.db.fetch_records("")) / max(total_records, 1), 2)

        def stat_card(label, value, color):
            card = QFrame()
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: {color};
                    border-radius: 12px;
                    padding: 15px;
                }}
                QLabel {{
                    color: white;
                    font-family: 'Poppins';
                }}
            """)
            vbox = QVBoxLayout()
            t = QLabel(label)
            t.setStyleSheet("font-size: 14px; font-weight: 500;")
            v = QLabel(str(value))
            v.setStyleSheet("font-size: 28px; font-weight: 700;")
            vbox.addWidget(t)
            vbox.addWidget(v)
            card.setLayout(vbox)
            return card

        stats_layout.addWidget(stat_card("Total Crops", total_crops, "#4E944F"))
        stats_layout.addWidget(stat_card("Total Records", total_records, "#6A994E"))
        stats_layout.addWidget(stat_card("Most Planted", most_planted, "#A76D5E"))
        stats_layout.addWidget(stat_card("Avg Fertilizer (kg)", avg_fert, "#386641"))

        stats_frame.setLayout(stats_layout)
        layout.addWidget(stats_frame)
        layout.addSpacing(25)

        # --- Quick Actions ---
        actions_frame = QFrame()
        actions_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(20)

        actions = [
            ("➕ Add New Record", "#B8A99A"),
            ("📄 View Reports", "#A76D5E"),
            ("ℹ About Flora", "#6B705C"),
        ]

        for text, color in actions:
            btn = QPushButton(text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    border-radius: 10px;
                    padding: 15px 25px;
                    font-family: 'Poppins';
                    font-size: 14px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: #DFCCBA;
                    color: #2c3e50;
                }}
            """)
            actions_layout.addWidget(btn)

        actions_frame.setLayout(actions_layout)
        layout.addWidget(actions_frame)

        # Friendly welcome
        footer_label = QLabel("Grow your data with Flora 🌿")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setStyleSheet("""
            font-family: 'Poppins';
            font-size: 16px;
            color: #2C3E50;
            margin-top: 20px;
        """)
        layout.addWidget(footer_label)

        self.setLayout(layout)

class RecordsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Records")
        title.setObjectName("page-title")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #2c3e50; padding-bottom: 20px; border-bottom: 2px solid #A76D5E;")
        layout.addWidget(title)
        
        # Search bar
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 Search records...")
        self.search.setObjectName("search-box")
        self.search.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 1px solid #dcdde1;
                border-radius: 5px;
                background-color: #FFFFFF;
                margin-bottom: 20px;
            }
            QLineEdit:focus {
                border: 1px solid #A76D5E;
            }
        """)
        self.search.textChanged.connect(self.load)
        layout.addWidget(self.search)
        
        # Table
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #F4F4F4;
                alternate-background-color: #F9F9F9;
                font-family: 'Poppins';
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                color: #2C3E50;
            }
            QTableWidget::item:selected {
                background-color: #A76D5E;
                color: white;
            }
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Poppins';
            }
            QTableView::item:hover {
                background-color: #F0F0F0;
            }
            """)
        self.table.cellClicked.connect(self.select)
        layout.addWidget(self.table)
        
        # Form row
        form_layout = QHBoxLayout()
        form_layout.setSpacing(10)
        
        self.crop = QComboBox()
        self.soil = QComboBox()
        self.fert = QComboBox()
        self.season = QComboBox()
        self.season.addItems(["Dry", "Rainy"])
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount (kg)")
        
        # Style for form inputs
        input_style = """
            QComboBox, QLineEdit {
                padding: 8px;
                border: 1px solid #dcdde1;
                border-radius: 4px;
                background-color: #FFFFFF;
                color: #2c3e50;
                font-size: 13px;
            }
            QComboBox:hover, QLineEdit:hover {
                border: 1px solid #A76D5E;
            }
            QComboBox:focus, QLineEdit:focus {
                border: 1px solid #A76D5E;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-width: 0px;
            }
        """
        
        for widget in [self.crop, self.soil, self.fert, self.season, self.amount]:
            widget.setObjectName("form-input")
            widget.setStyleSheet(input_style)
            form_layout.addWidget(widget)
        
        layout.addLayout(form_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        
        button_style = """
            QPushButton {
                background-color: #B8A99A;
                color: #FFFFFF;
                border: none;
                border-radius: 4px;
                padding: 8px 20px;
                margin: 0 5px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #A76D5E;
            }
            QPushButton:pressed {
                background-color: #8B5E3C;
            }
        """
        
        for text, func in [("Add", self.add), ("Update", self.update), ("Delete", self.delete)]:
            btn = QPushButton(text)
            btn.setStyleSheet(button_style)
            btn.clicked.connect(func)
            btn_layout.addWidget(btn)
        
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        self.load_dropdowns()
        self.load()
    
    def load_dropdowns(self):
        # Style for dropdown items
        dropdown_style = """
            QComboBox {
                padding: 8px;
                border: 1px solid #dcdde1;
                border-radius: 4px;
                background-color: #FFFFFF;
                color: #2c3e50;
                font-size: 13px;
            }
            QComboBox:hover {
                border: 1px solid #A76D5E;
            }
            QComboBox QAbstractItemView {
                background-color: #FFFFFF;
                color: #2c3e50;
                selection-background-color: #A76D5E;
                selection-color: #FFFFFF;
            }
        """
        
        for i in self.db.get_crops():
            self.crop.addItem(i[1], i[0])
        for i in self.db.get_soil():
            self.soil.addItem(i[1], i[0])
        for i in self.db.get_fert():
            self.fert.addItem(i[1], i[0])
        
        # Apply styling to dropdowns
        self.crop.setStyleSheet(dropdown_style)
        self.soil.setStyleSheet(dropdown_style)
        self.fert.setStyleSheet(dropdown_style)
        self.season.setStyleSheet(dropdown_style)
    
    def load(self):
        data = self.db.fetch_records(self.search.text())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Crop", "Soil", "Fertilizer", "Season", "Amount"])
        self.table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)
        
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setForeground(QBrush(QColor(44, 62, 80)))
                self.table.setItem(r, c, item)
        
        self.table.resizeColumnsToContents()
    
    def select(self):
        row = self.table.currentRow()
        if row >= 0:
            self.amount.setText(self.table.item(row, 5).text())
    
    def add(self):
        if self.amount.text():
            try:
                self.db.insert_record(
                    self.crop.currentData(),
                    self.soil.currentData(),
                    self.fert.currentData(),
                    self.season.currentText(),
                    int(self.amount.text())
                )
                self.amount.clear()
                self.load()
                QMessageBox.information(self, "Success", "Record added successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to add record: {str(e)}")
    
    def update(self):
        row = self.table.currentRow()
        if row >= 0 and self.amount.text():
            try:
                id = int(self.table.item(row, 0).text())
                self.db.update_record(
                    id,
                    self.crop.currentData(),
                    self.soil.currentData(),
                    self.fert.currentData(),
                    self.season.currentText(),
                    int(self.amount.text())
                )
                self.load()
                QMessageBox.information(self, "Success", "Record updated successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to update record: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please select a record and enter an amount")
    
    def delete(self):
        row = self.table.currentRow()
        if row >= 0:
            reply = QMessageBox.question(self, 'Confirm Delete', 
                                        'Are you sure you want to delete this record?',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    id = int(self.table.item(row, 0).text())
                    self.db.delete_record(id)
                    self.load()
                    self.amount.clear()
                    QMessageBox.information(self, "Success", "Record deleted successfully!")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to delete record: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Please select a record to delete")

class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Crop Reports")
        title.setObjectName("page-title")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #783D19; padding-bottom: 20px; border-bottom: 2px solid #FFFFFF;")
        layout.addWidget(title)
        
        # Create tab widget with custom styling
        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #F4F4F4;
                alternate-background-color: #F9F9F9;
                font-family: 'Poppins';
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                color: #2C3E50;
            }
            QTableWidget::item:selected {
                background-color: #A76D5E;
                color: white;
            }
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Poppins';
            }
            QTableView::item:hover {
                background-color: #F0F0F0;
                color: #A76D5E
            }
            """)
        
        # Basic Crop Report Tab
        basic_tab = QWidget()
        basic_layout = QVBoxLayout()
        
        basic_title = QLabel("Crop Planting Frequency")
        basic_title.setObjectName("report-title")
        basic_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #DFCCBA; margin-top: 20px; margin-bottom: 10px;")
        basic_layout.addWidget(basic_title)
        
        self.basic_table = QTableWidget()
        self.basic_table.setAlternatingRowColors(True)
        self.basic_table.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #F4F4F4;
                alternate-background-color: #F9F9F9;
                font-family: 'Poppins';
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                color: #2C3E50;
            }
            QTableWidget::item:selected {
                background-color: #A76D5E;
                color: white;
            }
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Poppins';
            }
            QTableView::item:hover {
                background-color: #F0F0F0;
            }
            """)
        
        data = self.db.crop_report()
        
        self.basic_table.setRowCount(len(data))
        self.basic_table.setColumnCount(2)
        self.basic_table.setHorizontalHeaderLabels(["Crop", "Times Planted"])
        
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setForeground(QBrush(QColor(44, 62, 80)))
                self.basic_table.setItem(r, c, item)
        
        self.basic_table.resizeColumnsToContents()
        basic_layout.addWidget(self.basic_table)
        basic_tab.setLayout(basic_layout)
        
        # Detailed Crop Report Tab
        detailed_tab = QWidget()
        detailed_layout = QVBoxLayout()
        
        detailed_title = QLabel("Detailed Crop Report")
        detailed_title.setObjectName("report-title")
        detailed_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #DFCCBA; margin-top: 20px; margin-bottom: 10px;")
        detailed_layout.addWidget(detailed_title)
        
        self.detailed_table = QTableWidget()
        self.detailed_table.setAlternatingRowColors(True)
        self.detailed_table.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #F4F4F4;
                alternate-background-color: #F9F9F9;
                font-family: 'Poppins';
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                color: #2C3E50;
            }
            QTableWidget::item:selected {
                background-color: #A76D5E;
                color: white;
            }
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Poppins';
            }
            QTableView::item:hover {
                background-color: #F0F0F0;
            }
            """)
        
        detailed_data = self.db.crop_detailed_report()
        
        self.detailed_table.setRowCount(len(detailed_data))
        self.detailed_table.setColumnCount(6)
        self.detailed_table.setHorizontalHeaderLabels([
            "Crop", "Times Planted", "Total Fertilizer (kg)", 
            "Avg Fertilizer (kg)", "Min Fertilizer (kg)", "Max Fertilizer (kg)"
        ])
        
        for r, row in enumerate(detailed_data):
            for c, val in enumerate(row):
                if c in [2, 3, 4, 5] and isinstance(val, (int, float)):
                    item = QTableWidgetItem(f"{val:.2f}")
                else:
                    item = QTableWidgetItem(str(val))
                item.setForeground(QBrush(QColor(44, 62, 80)))
                self.detailed_table.setItem(r, c, item)
        
        self.detailed_table.resizeColumnsToContents()
        detailed_layout.addWidget(self.detailed_table)
        detailed_tab.setLayout(detailed_layout)
        
        # Seasonal Crop Report Tab
        seasonal_tab = QWidget()
        seasonal_layout = QVBoxLayout()
        
        seasonal_title = QLabel("Seasonal Crop Report")
        seasonal_title.setObjectName("report-title")
        seasonal_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #DFCCBA; margin-top: 20px; margin-bottom: 10px;")
        seasonal_layout.addWidget(seasonal_title)
        
        self.seasonal_table = QTableWidget()
        self.seasonal_table.setAlternatingRowColors(True)
        self.seasonal_table.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #F4F4F4;
                alternate-background-color: #F9F9F9;
                font-family: 'Poppins';
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
                color: #2C3E50;
            }
            QTableWidget::item:selected {
                background-color: #A76D5E;
                color: white;
            }
            QHeaderView::section {
                background-color: #B8A99A;
                color: #FFFFFF;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Poppins';
            }
            QTableView::item:hover {
                background-color: #F0F0F0;
            }
            """)
        
        seasonal_data = self.db.crop_seasonal_report()
        
        self.seasonal_table.setRowCount(len(seasonal_data))
        self.seasonal_table.setColumnCount(4)
        self.seasonal_table.setHorizontalHeaderLabels([
            "Crop", "Season", "Times Planted", "Total Fertilizer (kg)"
        ])
        
        for r, row in enumerate(seasonal_data):
            for c, val in enumerate(row):
                if c == 3 and isinstance(val, (int, float)):
                    item = QTableWidgetItem(f"{val:.2f}")
                else:
                    item = QTableWidgetItem(str(val))
                item.setForeground(QBrush(QColor(44, 62, 80)))
                self.seasonal_table.setItem(r, c, item)
        
        self.seasonal_table.resizeColumnsToContents()
        seasonal_layout.addWidget(self.seasonal_table)
        seasonal_tab.setLayout(seasonal_layout)
        
        # Add tabs
        tab_widget.addTab(basic_tab, "Basic Report")
        tab_widget.addTab(detailed_tab, "Detailed Report")
        tab_widget.addTab(seasonal_tab, "Seasonal Report")
        
        layout.addWidget(tab_widget)
        
        self.setLayout(layout)

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("About")
        title.setObjectName("page-title")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #2c3e50; padding-bottom: 20px; border-bottom: 2px solid #A76D5E;")
        layout.addWidget(title)
        
        # Create a frame for about content
        about_frame = QFrame()
        about_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        about_layout = QVBoxLayout()
        
        # App icon/logo
        logo_label = QLabel("🌱")
        logo_label.setStyleSheet("font-size: 48px;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        about_layout.addWidget(logo_label)
        
        about_text = QLabel(
            "<h2 style='color: #2c3e50; text-align: center;'>Flora - Crop Management System</h2>"
            "<br>"
            "<p style='font-size: 14px; color: #2d3436; text-align: center;'>"
            "A simple application to manage crop records, "
            "soil types, and generate crop reports.</p>"
            "<br>"
            "<hr>"
            "<p style='font-size: 12px; color: #7f8c8d; text-align: center;'>"
            "<b>Version:</b> 1.0<br>"
            "<b>Created by:</b> Group 3 - CPE22S1<br>"
            "<b>Year:</b> 2025<br>"
            "<br>"
            "© 2025 Flora. All rights reserved.</p>"
        )
        about_text.setWordWrap(True)
        about_text.setTextFormat(Qt.TextFormat.RichText)
        about_layout.addWidget(about_text)
        
        about_frame.setLayout(about_layout)
        layout.addWidget(about_frame)
        layout.addStretch()
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Flora")
        self.setMinimumSize(900, 600)
        
        # Main container
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Stacked widget for pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(DashboardPage())
        self.stacked_widget.addWidget(RecordsPage())
        self.stacked_widget.addWidget(ReportsPage())
        self.stacked_widget.addWidget(AboutPage())
        
        # Sidebar with username
        sidebar = FloraSidebar(self.stacked_widget, username)
        
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stacked_widget, 1)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #FEFAE0;
            }
            #sidebar {
                background-color: #B8A99A;
                border-right: 2px solid #A76D5E;
            }
            #logo {
                font-size: 28px;
                font-weight: bold;
                font-family: 'MuseoModerno';
                color: #FEFAE0;
                padding: 15px;
                letter-spacing: 2px;
            }
            #username {
                font-size: 20px;
                font-family: 'MuseoModerno';
                color: #FEFAE0;
                padding: 10px;
                margin: 5px 15px;
            }
            #nav-btn {
                background-color: transparent;
                color: #FEFAE0;
                font-size: 25px;
                font-family: 'MuseoModerno';
                text-align: right;
                padding: 12px 20px;
                margin: 5px 10px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            #nav-btn:hover {
                background-color: #DFCCBA;
                color: #783D19;
                padding-left: 25px;
            }
            #logout-btn {
                background-color: #A76D5E;
                color: white;
                font-size: 16px;
                font-family: 'MuseoModerno';
                padding: 12px;
                margin: 10px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                text-align: center;
            }
            #logout-btn:hover {
                background-color: #c0392b;
                padding-left: 20px;
            }
        """)

def show_main_window(username):
    """Function to show the main dashboard window"""
    main_window = MainWindow(username)
    main_window.show()
    return main_window
