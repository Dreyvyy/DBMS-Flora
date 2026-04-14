from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QBrush, QColor
from database import Database

# ── Palette ────────────────────────────────────────────────────────────────
BG_DEEP    = "#111A0E"
BG_PANEL   = "#162010"
BG_ROW_ALT = "#1E2B18"
BG_HOVER   = "#243020"
BORDER     = "#2B3D20"
ACCENT     = "#A8C832"
ACCENT2    = "#6BAF3C"
TEXT_PRI   = "#E8F0D0"
TEXT_SEC   = "#7A9060"
TEXT_HEAD  = "#A8C832"
RED_SOFT   = "#C84040"
RED_BG     = "#2A1010"

# ── Stylesheets ────────────────────────────────────────────────────────────
GLOBAL_STYLE = f"""
    * {{ font-family: 'Segoe UI', monospace; }}
    QMainWindow, QWidget {{ background-color: {BG_DEEP}; color: {TEXT_PRI}; }}
    QStackedWidget {{ background-color: {BG_DEEP}; }}
    QScrollBar:vertical {{ background: {BG_PANEL}; width: 6px; border-radius: 3px; }}
    QScrollBar::handle:vertical {{ background: {BORDER}; border-radius: 3px; }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
    QMessageBox {{ background-color: {BG_PANEL}; color: {TEXT_PRI}; }}
    QMessageBox QPushButton {{
        background-color: {ACCENT2}; color: {BG_DEEP};
        border: none; border-radius: 6px; padding: 6px 18px; font-weight: 700;
    }}
"""

SIDEBAR_STYLE = f"""
    QFrame#sidebar {{ background-color: {BG_PANEL}; border-right: 1px solid {BORDER}; }}
    #logo {{ font-size: 17px; font-weight: 900; color: {ACCENT}; padding: 8px 20px 0 20px; letter-spacing: 3px; }}
    #tagline {{ font-size: 8px; color: {TEXT_SEC}; padding: 0 20px 10px 20px; letter-spacing: 3px; }}
    #username {{ font-size: 11px; color: {TEXT_SEC}; padding: 4px 20px 14px 20px; letter-spacing: 1px; }}
    #nav-btn {{
        background-color: transparent; color: {TEXT_SEC};
        font-size: 13px; font-weight: 600; text-align: left;
        padding: 11px 20px; margin: 1px 10px; border: none; border-radius: 8px;
    }}
    #nav-btn:hover {{ background-color: {BG_HOVER}; color: {TEXT_PRI}; }}
    #nav-btn-active {{
        background-color: {BG_HOVER}; color: {ACCENT};
        font-size: 13px; font-weight: 700; text-align: left;
        padding: 11px 17px; margin: 1px 10px;
        border: none; border-left: 3px solid {ACCENT}; border-radius: 8px;
    }}
    #logout-btn {{
        background-color: {RED_BG}; color: {RED_SOFT};
        font-size: 12px; font-weight: 700; padding: 10px; margin: 10px;
        border: 1px solid {RED_SOFT}; border-radius: 8px; letter-spacing: 1px;
    }}
    #logout-btn:hover {{ background-color: {RED_SOFT}; color: white; }}
"""

TABLE_STYLE = f"""
    QTableWidget {{
        background-color: transparent; border: none;
        gridline-color: transparent; font-size: 13px; color: {TEXT_PRI}; outline: none;
    }}
    QTableWidget::item {{
        padding: 0 16px; border: none; border-bottom: 1px solid {BORDER};
        background-color: transparent; color: {TEXT_PRI};
    }}
    QTableWidget::item:alternate {{ background-color: {BG_ROW_ALT}; }}
    QTableWidget::item:selected {{ background-color: {BG_HOVER}; color: {ACCENT}; }}
    QHeaderView {{ background-color: transparent; border: none; }}
    QHeaderView::section {{
        background-color: {BG_PANEL}; color: {TEXT_HEAD};
        padding: 12px 16px; border: none; border-bottom: 1px solid {BORDER};
        font-weight: 800; font-size: 10px; letter-spacing: 2px;
    }}
    QTableWidget QTableCornerButton::section {{ background-color: {BG_PANEL}; border: none; }}
"""

COMBO_STYLE = f"""
    QComboBox {{
        padding: 9px 14px; border: 1px solid {BORDER}; border-radius: 8px;
        background-color: {BG_PANEL}; color: {TEXT_PRI}; font-size: 13px; min-width: 110px;
    }}
    QComboBox:hover {{ border: 1px solid {ACCENT2}; }}
    QComboBox::drop-down {{ border: none; width: 20px; }}
    QComboBox::down-arrow {{
        image: none; border-left: 4px solid transparent; border-right: 4px solid transparent;
        border-top: 5px solid {TEXT_SEC}; width: 0; height: 0; margin-right: 8px;
    }}
    QComboBox QAbstractItemView {{
        background-color: {BG_PANEL}; border: 1px solid {BORDER}; border-radius: 8px;
        color: {TEXT_PRI}; selection-background-color: {BG_HOVER}; selection-color: {ACCENT}; outline: none;
    }}
"""

INPUT_STYLE = f"""
    QLineEdit {{
        padding: 9px 14px; border: 1px solid {BORDER}; border-radius: 8px;
        background-color: {BG_PANEL}; color: {TEXT_PRI}; font-size: 13px;
    }}
    QLineEdit:focus {{ border: 1px solid {ACCENT2}; }}
"""

BTN_PRIMARY = f"""
    QPushButton {{
        background-color: {ACCENT2}; color: {BG_DEEP}; border: none; border-radius: 8px;
        padding: 9px 22px; font-size: 13px; font-weight: 800;
    }}
    QPushButton:hover {{ background-color: {ACCENT}; }}
    QPushButton:pressed {{ background-color: #4A8A2C; }}
"""

BTN_GHOST = f"""
    QPushButton {{
        background-color: {BG_PANEL}; color: {TEXT_PRI};
        border: 1px solid {BORDER}; border-radius: 8px; padding: 9px 22px; font-size: 13px; font-weight: 700;
    }}
    QPushButton:hover {{ border: 1px solid {ACCENT2}; color: {ACCENT}; }}
"""

BTN_DANGER = f"""
    QPushButton {{
        background-color: {RED_BG}; color: {RED_SOFT};
        border: 1px solid {RED_SOFT}; border-radius: 8px; padding: 9px 22px; font-size: 13px; font-weight: 700;
    }}
    QPushButton:hover {{ background-color: {RED_SOFT}; color: white; }}
"""

TAB_STYLE = f"""
    QTabWidget::pane {{ border: none; background-color: transparent; }}
    QTabBar::tab {{
        background-color: transparent; color: {TEXT_SEC};
        padding: 10px 22px; font-size: 12px; font-weight: 700;
        border: none; border-bottom: 2px solid transparent; margin-right: 2px; letter-spacing: 1px;
    }}
    QTabBar::tab:selected {{ color: {ACCENT}; border-bottom: 2px solid {ACCENT}; }}
    QTabBar::tab:hover:!selected {{ color: {TEXT_PRI}; }}
"""


# ── Helpers ────────────────────────────────────────────────────────────────
def page_title(text):
    lbl = QLabel(text)
    lbl.setStyleSheet(f"font-size: 22px; font-weight: 900; color: {TEXT_PRI}; letter-spacing: 1px; background: transparent;")
    return lbl


def stat_card(icon, value, label):
    card = QFrame()
    card.setStyleSheet(f"QFrame {{ background-color: {BG_PANEL}; border: 1px solid {BORDER}; border-radius: 12px; }}")
    card.setFixedHeight(90)
    h = QHBoxLayout()
    h.setContentsMargins(20, 16, 20, 16)
    h.setSpacing(14)
    ico = QLabel(icon)
    ico.setStyleSheet("font-size: 26px; background: transparent; border: none;")
    h.addWidget(ico)
    v = QVBoxLayout()
    v.setSpacing(2)
    val_lbl = QLabel(str(value))
    val_lbl.setStyleSheet(f"font-size: 22px; font-weight: 900; color: {TEXT_PRI}; background: transparent; border: none;")
    sub_lbl = QLabel(label.upper())
    sub_lbl.setStyleSheet(f"font-size: 9px; font-weight: 700; color: {TEXT_SEC}; letter-spacing: 2px; background: transparent; border: none;")
    v.addWidget(val_lbl)
    v.addWidget(sub_lbl)
    h.addLayout(v)
    h.addStretch()
    card.setLayout(h)
    return card


def section_card():
    f = QFrame()
    f.setStyleSheet(f"QFrame {{ background-color: {BG_PANEL}; border: 1px solid {BORDER}; border-radius: 12px; }}")
    return f


def make_table():
    t = QTableWidget()
    t.setAlternatingRowColors(True)
    t.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
    t.setShowGrid(False)
    t.verticalHeader().setVisible(False)
    t.horizontalHeader().setHighlightSections(False)
    t.setFrameShape(QFrame.Shape.NoFrame)
    t.setStyleSheet(TABLE_STYLE)
    t.verticalHeader().setDefaultSectionSize(50)
    t.horizontalHeader().setStretchLastSection(True)
    t.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    t.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    t.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
    return t


# ── Sidebar ────────────────────────────────────────────────────────────────
class FloraSidebar(QFrame):
    def __init__(self, stacked_widget, username):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setObjectName("sidebar")
        self.setFixedWidth(220)
        self.nav_buttons = []

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 30, 0, 20)
        layout.setSpacing(2)

        logo = QLabel("🌱 FLORA")
        logo.setObjectName("logo")
        layout.addWidget(logo)

        tagline = QLabel("CROP MANAGEMENT SYSTEM")
        tagline.setObjectName("tagline")
        layout.addWidget(tagline)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet(f"background-color: {BORDER}; max-height: 1px; margin: 4px 16px;")
        layout.addWidget(sep)

        uname = QLabel(f"● {username}")
        uname.setObjectName("username")
        layout.addWidget(uname)
        layout.addSpacing(10)

        for label, idx in [("Dashboard", 0), ("Records", 1), ("Reports", 2), ("About", 3)]:
            btn = QPushButton(f"  {label}")
            btn.setObjectName("nav-btn")
            btn.clicked.connect(lambda _, i=idx: self.navigate(i))
            layout.addWidget(btn)
            self.nav_buttons.append(btn)

        layout.addStretch()

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setStyleSheet(f"background-color: {BORDER}; max-height: 1px; margin: 4px 16px;")
        layout.addWidget(sep2)
        layout.addSpacing(6)

        logout_btn = QPushButton("LOG OUT")
        logout_btn.setObjectName("logout-btn")
        logout_btn.clicked.connect(self.logout)
        layout.addWidget(logout_btn)

        self.setLayout(layout)
        self.navigate(0)

    def navigate(self, index):
        self.stacked_widget.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setObjectName("nav-btn-active" if i == index else "nav-btn")
            btn.setStyle(btn.style())

    def logout(self):
        reply = QMessageBox.question(self, 'Confirm Logout', 'Are you sure you want to logout?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.window().close()
            from login import show_login_window
            show_login_window()


# ── Dashboard ──────────────────────────────────────────────────────────────
class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.stats_cards = []
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(20)
        layout.addWidget(page_title("Dashboard"))
        
        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(14)
        layout.addLayout(self.cards_layout)
        
        self.footer = QLabel("Grow your data with Flora 🌿")
        self.footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer.setStyleSheet(f"font-size: 13px; color: {TEXT_SEC}; margin-top: 30px; background: transparent;")
        layout.addStretch()
        layout.addWidget(self.footer)
        self.setLayout(layout)
        
        self.refresh_data()
    
    def refresh_data(self):
        # Clear existing cards
        while self.cards_layout.count():
            item = self.cards_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Fetch fresh data
        total_crops   = len(self.db.get_crops())
        total_records = len(self.db.fetch_records(""))
        crop_rep      = self.db.crop_report()
        most_planted  = crop_rep[0][0] if crop_rep else "N/A"
        records       = self.db.fetch_records("")
        avg_fert      = round(sum(x[5] for x in records) / max(total_records, 1), 1) if records else 0
        
        # Create new cards
        self.cards_layout.addWidget(stat_card("🌾", total_crops,       "Crop Types"))
        self.cards_layout.addWidget(stat_card("📋", total_records,     "Total Records"))
        self.cards_layout.addWidget(stat_card("🏆", most_planted,      "Most Planted"))
        self.cards_layout.addWidget(stat_card("💧", f"{avg_fert} kg",  "Avg Fertilizer"))


# ── Records ────────────────────────────────────────────────────────────────
class RecordsPage(QWidget):
    data_changed = pyqtSignal()  # Signal to notify other pages of data changes
    
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(16)

        header = QHBoxLayout()
        header.addWidget(page_title("Records"))
        header.addStretch()

        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍  Search records...")
        self.search.setFixedWidth(260)
        self.search.setFixedHeight(38)
        self.search.setStyleSheet(INPUT_STYLE)
        self.search.textChanged.connect(self.load)
        header.addWidget(self.search)
        layout.addLayout(header)

        card = section_card()
        card_v = QVBoxLayout()
        card_v.setContentsMargins(0, 0, 0, 0)
        self.table = make_table()
        self.table.cellClicked.connect(self.select)
        card_v.addWidget(self.table)
        card.setLayout(card_v)
        layout.addWidget(card, stretch=1)

        bottom = QHBoxLayout()
        bottom.setSpacing(10)

        self.crop   = QComboBox(); self.crop.setStyleSheet(COMBO_STYLE);   self.crop.setFixedHeight(38)
        self.soil   = QComboBox(); self.soil.setStyleSheet(COMBO_STYLE);   self.soil.setFixedHeight(38)
        self.fert   = QComboBox(); self.fert.setStyleSheet(COMBO_STYLE);   self.fert.setFixedHeight(38)
        self.season = QComboBox(); self.season.setStyleSheet(COMBO_STYLE); self.season.setFixedHeight(38)
        self.season.addItems(["Dry", "Rainy"])

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount (kg)")
        self.amount.setStyleSheet(INPUT_STYLE)
        self.amount.setFixedHeight(38)
        self.amount.setFixedWidth(130)

        for w in [self.crop, self.soil, self.fert, self.season, self.amount]:
            bottom.addWidget(w)
        bottom.addStretch()

        add_btn = QPushButton("Add");    add_btn.setStyleSheet(BTN_PRIMARY); add_btn.setFixedHeight(38); add_btn.clicked.connect(self.add)
        upd_btn = QPushButton("Update"); upd_btn.setStyleSheet(BTN_GHOST);   upd_btn.setFixedHeight(38); upd_btn.clicked.connect(self.update)
        del_btn = QPushButton("Delete"); del_btn.setStyleSheet(BTN_DANGER);  del_btn.setFixedHeight(38); del_btn.clicked.connect(self.delete)
        for b in [add_btn, upd_btn, del_btn]:
            bottom.addWidget(b)

        layout.addLayout(bottom)
        self.setLayout(layout)
        self.load_dropdowns()
        self.load()

    def load_dropdowns(self):
        for i in self.db.get_crops(): self.crop.addItem(i[1], i[0])
        for i in self.db.get_soil():  self.soil.addItem(i[1], i[0])
        for i in self.db.get_fert():  self.fert.addItem(i[1], i[0])

    def load(self):
        data = self.db.fetch_records(self.search.text())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "CROP", "SOIL", "FERTILIZER", "SEASON", "AMOUNT (KG)"])
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                self.table.setItem(r, c, item)
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

    def select(self):
        row = self.table.currentRow()
        if row >= 0:
            self.amount.setText(self.table.item(row, 5).text())

    def notify_data_changed(self):
        """Emit signal to notify other pages that data has changed"""
        self.data_changed.emit()

    def add(self):
        if self.amount.text():
            try:
                self.db.insert_record(self.crop.currentData(), self.soil.currentData(),
                                      self.fert.currentData(), self.season.currentText(),
                                      int(self.amount.text()))
                self.amount.clear(); self.load()
                self.notify_data_changed()  # Notify other pages
                QMessageBox.information(self, "Success", "Record added successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def update(self):
        row = self.table.currentRow()
        if row >= 0 and self.amount.text():
            try:
                rid = int(self.table.item(row, 0).text())
                self.db.update_record(rid, self.crop.currentData(), self.soil.currentData(),
                                      self.fert.currentData(), self.season.currentText(),
                                      int(self.amount.text()))
                self.load()
                self.notify_data_changed()  # Notify other pages
                QMessageBox.information(self, "Success", "Record updated!")
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Error", "Select a record and enter an amount")

    def delete(self):
        row = self.table.currentRow()
        if row >= 0:
            reply = QMessageBox.question(self, 'Confirm Delete', 'Delete this record?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    rid = int(self.table.item(row, 0).text())
                    self.db.delete_record(rid); self.load(); self.amount.clear()
                    self.notify_data_changed()  # Notify other pages
                    QMessageBox.information(self, "Success", "Record deleted!")
                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Error", "Select a record to delete")


# ── Reports ────────────────────────────────────────────────────────────────
def build_report_table(columns, data, float_cols=None):
    t = make_table()
    t.setColumnCount(len(columns))
    t.setHorizontalHeaderLabels(columns)
    t.setRowCount(len(data))
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            txt = f"{val:.2f}" if (float_cols and c in float_cols and isinstance(val, (int, float))) else str(val)
            item = QTableWidgetItem(txt)
            item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            t.setItem(r, c, item)
    t.resizeColumnsToContents()
    t.horizontalHeader().setStretchLastSection(True)
    return t


class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(16)
        layout.addWidget(page_title("Crop Reports"))

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(TAB_STYLE)
        self.tabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        
        self.refresh_all_reports()
    
    def refresh_all_reports(self):
        """Refresh all report tabs with latest data"""
        # Clear existing tabs
        self.tabs.clear()
        
        # Create fresh reports
        def wrap(table):
            card = section_card()
            v = QVBoxLayout(); v.setContentsMargins(0, 0, 0, 0)
            v.addWidget(table); card.setLayout(v)
            w = QWidget(); w.setStyleSheet("background: transparent;")
            wl = QVBoxLayout(); wl.setContentsMargins(0, 12, 0, 0)
            wl.addWidget(card); w.setLayout(wl)
            return w
        
        # Basic Report
        basic_data = self.db.crop_report()
        self.tabs.addTab(wrap(build_report_table(
            ["CROP", "TIMES PLANTED"],
            basic_data
        )), "Basic Report")
        
        # Detailed Report
        detailed_data = self.db.crop_detailed_report()
        self.tabs.addTab(wrap(build_report_table(
            ["CROP", "TIMES PLANTED", "TOTAL FERT (KG)", "AVG (KG)", "MIN (KG)", "MAX (KG)"],
            detailed_data, float_cols={2, 3, 4, 5}
        )), "Detailed Report")
        
        # Seasonal Report
        seasonal_data = self.db.crop_seasonal_report()
        self.tabs.addTab(wrap(build_report_table(
            ["CROP", "SEASON", "TIMES PLANTED", "TOTAL FERT (KG)"],
            seasonal_data, float_cols={3}
        )), "Seasonal Report")
    
    def refresh(self):
        """Public method to refresh reports"""
        self.refresh_all_reports()


# ── About ──────────────────────────────────────────────────────────────────
class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(20)
        layout.addWidget(page_title("About"))

        card = section_card()
        cl = QVBoxLayout()
        cl.setContentsMargins(40, 40, 40, 40)
        cl.setSpacing(16)

        logo = QLabel("🌱")
        logo.setStyleSheet("font-size: 52px; background: transparent;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cl.addWidget(logo)

        text = QLabel(
            f"<h2 style='color:{TEXT_PRI}; text-align:center; font-size:16px; letter-spacing:2px;'>FLORA — CROP MANAGEMENT SYSTEM</h2>"
            f"<p style='font-size:13px; color:{TEXT_SEC}; text-align:center; line-height:1.8;'>"
            "A simple application to manage crop records,<br>soil types, and generate detailed crop reports.</p>"
            f"<br><hr style='border:none; border-top:1px solid {BORDER};'><br>"
            f"<p style='font-size:12px; color:{TEXT_SEC}; text-align:center; line-height:2.2;'>"
            f"<b style='color:{TEXT_PRI};'>Version:</b> 1.0<br>"
            f"<b style='color:{TEXT_PRI};'>Created by:</b> Group 3 — CPE22S1<br>"
            f"<b style='color:{TEXT_PRI};'>Year:</b> 2025<br><br>"
            f"<span style='color:{TEXT_SEC};'>© 2025 Flora. All rights reserved.</span></p>"
        )
        text.setWordWrap(True)
        text.setTextFormat(Qt.TextFormat.RichText)
        text.setStyleSheet("background: transparent;")
        cl.addWidget(text)
        card.setLayout(cl)
        layout.addWidget(card)
        layout.addStretch()
        self.setLayout(layout)


# ── Main Window ────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Flora — Crop Management System")
        self.setMinimumSize(1060, 660)

        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.stacked = QStackedWidget()
        
        # Create pages
        self.dashboard_page = DashboardPage()
        self.records_page = RecordsPage()
        self.reports_page = ReportsPage()
        self.about_page = AboutPage()
        
        # Connect data changed signal from records page
        self.records_page.data_changed.connect(self.on_data_changed)
        
        # Add pages to stacked widget
        self.stacked.addWidget(self.dashboard_page)
        self.stacked.addWidget(self.records_page)
        self.stacked.addWidget(self.reports_page)
        self.stacked.addWidget(self.about_page)

        sidebar = FloraSidebar(self.stacked, username)
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stacked, 1)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setStyleSheet(GLOBAL_STYLE + SIDEBAR_STYLE)
    
    def on_data_changed(self):
        """Called when data is added, updated, or deleted"""
        # Refresh dashboard
        self.dashboard_page.refresh_data()
        # Refresh reports
        self.reports_page.refresh()
        # Refresh records page (though it already refreshes itself, this ensures consistency)
        self.records_page.load()


def show_main_window(username):
    """Function to show the main dashboard window"""
    main_window = MainWindow(username)
    main_window.show()
    return main_window
