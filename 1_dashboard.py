# main.py
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QLineEdit, QTableWidget, QTableWidgetItem, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor
import sys
from database import Database

class FloraSidebar(QFrame):
    def __init__(self, stacked_widget, username):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setObjectName("sidebar")
        self.setFixedWidth(250)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 30, 0, 0)
        layout.setSpacing(20)
        
        # Logo / Title
        logo = QLabel("🌱 Flora")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)
        
        # Username label (display actual username)
        self.username_label = QLabel(username)
        self.username_label.setObjectName("username")
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        
        layout.addSpacing(30)
        
        # Dashboard button
        self.dashboard_btn = QPushButton("Dashboard")
        self.dashboard_btn.setObjectName("nav-btn")
        self.dashboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.dashboard_btn)
        
        # Records button
        self.records_btn = QPushButton("Records")
        self.records_btn.setObjectName("nav-btn")
        self.records_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(self.records_btn)
        
        # Reports button
        self.reports_btn = QPushButton("Reports")
        self.reports_btn.setObjectName("nav-btn")
        self.reports_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(self.reports_btn)
        
        # About button
        self.about_btn = QPushButton("About")
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
        self.window().close()
        from login import show_login_window
        show_login_window()

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Dashboard")
        title.setObjectName("page-title")
        layout.addWidget(title)
        
        # Dashboard content
        content = QLabel("Welcome to Flora Dashboard\n\nManage your crop records and view reports.")
        content.setWordWrap(True)
        content.setStyleSheet("font-size: 16px; color: #2d3436;")
        layout.addWidget(content)
        
        layout.addStretch()
        self.setLayout(layout)

class RecordsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Records")
        title.setObjectName("page-title")
        layout.addWidget(title)
        
        # Search bar
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search records...")
        self.search.setObjectName("search-box")
        self.search.textChanged.connect(self.load)
        layout.addWidget(self.search)
        
        # Table
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.cellClicked.connect(self.select)
        layout.addWidget(self.table)
        
        # Form row
        form_layout = QHBoxLayout()
        self.crop = QComboBox()
        self.soil = QComboBox()
        self.fert = QComboBox()
        self.season = QComboBox()
        self.season.addItems(["Dry", "Rainy"])
        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount (kg)")
        
        for widget in [self.crop, self.soil, self.fert, self.season, self.amount]:
            widget.setObjectName("form-input")
            form_layout.addWidget(widget)
        
        layout.addLayout(form_layout)
        
        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        for text, func in [("Add", self.add), ("Update", self.update), ("Delete", self.delete)]:
            btn = QPushButton(text)
            btn.setObjectName("action-btn")
            btn.clicked.connect(func)
            btn_layout.addWidget(btn)
        btn_layout.addStretch()
        
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        self.load_dropdowns()
        self.load()
    
    def load_dropdowns(self):
        for i in self.db.get_crops():
            self.crop.addItem(i[1], i[0])
        for i in self.db.get_soil():
            self.soil.addItem(i[1], i[0])
        for i in self.db.get_fert():
            self.fert.addItem(i[1], i[0])
    
    def load(self):
        data = self.db.fetch_records(self.search.text())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Crop", "Soil", "Fertilizer", "Season", "Amount"])
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
            self.db.insert_record(
                self.crop.currentData(),
                self.soil.currentData(),
                self.fert.currentData(),
                self.season.currentText(),
                int(self.amount.text())
            )
            self.amount.clear()
            self.load()
    
    def update(self):
        row = self.table.currentRow()
        if row >= 0 and self.amount.text():
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
    
    def delete(self):
        row = self.table.currentRow()
        if row >= 0:
            id = int(self.table.item(row, 0).text())
            self.db.delete_record(id)
            self.load()

class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Reports")
        title.setObjectName("page-title")
        layout.addWidget(title)
        
        # Fertilizer Usage Report
        report_title = QLabel("Fertilizer Usage Report")
        report_title.setObjectName("report-title")
        layout.addWidget(report_title)
        
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        data = self.db.fertilizer_report()
        
        self.table.setRowCount(len(data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Crop", "Total Fertilizer (kg)"])
        
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setForeground(QBrush(QColor(44, 62, 80)))
                self.table.setItem(r, c, item)
        
        self.table.resizeColumnsToContents()
        layout.addWidget(self.table)
        layout.addStretch()
        
        self.setLayout(layout)

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("About")
        title.setObjectName("page-title")
        layout.addWidget(title)
        
        about_text = QLabel(
            "Flora - Crop Management System\n\n"
            "Version 1.0\n\n"
            "A simple application to manage crop records, "
            "soil types, fertilizers, and generate usage reports.\n\n"
            "© 2025 Flora"
        )
        about_text.setWordWrap(True)
        about_text.setStyleSheet("font-size: 14px; color: #2d3436;")
        layout.addWidget(about_text)
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
        
        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
            }
            #sidebar {
                background-color: #2c3e50;
                border-right: 1px solid #34495e;
            }
            #logo {
                font-size: 24px;
                font-weight: bold;
                color: #ecf0f1;
                padding: 10px;
            }
            #username {
                font-size: 14px;
                color: #bdc3c7;
                padding: 5px;
                border-bottom: 1px solid #34495e;
            }
            #nav-btn {
                background-color: transparent;
                color: #ecf0f1;
                font-size: 14px;
                text-align: left;
                padding: 12px 20px;
                border: none;
                border-radius: 0px;
            }
            #nav-btn:hover {
                background-color: #34495e;
            }
            #logout-btn {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                padding: 10px;
                margin: 10px;
                border: none;
                border-radius: 5px;
            }
            #logout-btn:hover {
                background-color: #c0392b;
            }
            #page-title {
                font-size: 28px;
                font-weight: bold;
                color: #2c3e50;
                padding-bottom: 20px;
                border-bottom: 2px solid #3498db;
            }
            #report-title {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            #search-box {
                padding: 10px;
                font-size: 14px;
                border: 1px solid #dcdde1;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 5px;
                gridline-color: #f0f0f0;
            }
            QTableWidget::item {
                padding: 5px;
                color: #2c3e50;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
            #form-input, QComboBox, QLineEdit {
                padding: 8px;
                border: 1px solid #dcdde1;
                border-radius: 4px;
                background-color: white;
                min-width: 100px;
                color: #2c3e50;
            }
            QComboBox {
                color: #2c3e50;
            }
            QComboBox QAbstractItemView {
                color: #2c3e50;
            }
            #action-btn {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                margin: 0 5px;
            }
            #action-btn:hover {
                background-color: #2980b9;
            }
            QLineEdit {
                color: #2c3e50;
            }
            QLineEdit::placeholder {
                color: #bdc3c7;
            }
        """)

def show_main_window(username):
    """Function to show the main dashboard window"""
    main_window = MainWindow(username)
    main_window.show()
    return main_window
