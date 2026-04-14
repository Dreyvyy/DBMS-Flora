# dashboard.py
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QBrush, QColor, QFont
from database import Database

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

SOFT_GREEN = "#98A086"
WARM_BROWN = "#C4A071"
CREAM      = "#DFCCB1"
DARK_BROWN = "#846044"
PURPLE     = "#A765D5"  

TABLE_STYLE = f"""
    QTableWidget {{
        background-color: {BG_PANEL};
        border: 1px solid {BORDER};
        border-radius: 10px;
        gridline-color: {BORDER};
        font-size: 13px;
        color: {TEXT_PRI};
        outline: none;
        alternate-background-color: {BG_ROW_ALT};
    }}
    QTableWidget::item {{
        padding: 12px 16px;
        border-bottom: 1px solid {BORDER};
        border-right: none;
        background-color: transparent;
    }}
    QTableWidget::item:alternate {{
        background-color: {BG_ROW_ALT};
    }}
    QTableWidget::item:selected {{
        background-color: {BG_HOVER};
        color: {ACCENT};
        border-left: 3px solid {ACCENT};
    }}
    QTableWidget::item:hover {{
        background-color: {BG_HOVER};
    }}
    QHeaderView::section {{
        background-color: {BG_PANEL};
        color: {ACCENT};
        padding: 14px 16px;
        border: none;
        border-bottom: 2px solid {ACCENT2};
        font-weight: 800;
        font-size: 11px;
        letter-spacing: 1.5px;
    }}
    QHeaderView::section:first {{
        border-top-left-radius: 10px;
    }}
    QHeaderView::section:last {{
        border-top-right-radius: 10px;
    }}
    QTableWidget QTableCornerButton::section {{
        background-color: {BG_PANEL};
        border: none;
        border-top-left-radius: 10px;
    }}
"""

COMBO_STYLE = f"""
    QComboBox {{
        padding: 10px 14px;
        border: 1px solid {BORDER};
        border-radius: 8px;
        background-color: {BG_PANEL};
        color: {TEXT_PRI};
        font-size: 13px;
        font-weight: 500;
        min-width: 120px;
    }}
    QComboBox:hover {{
        border: 1px solid {ACCENT2};
        background-color: {BG_HOVER};
    }}
    QComboBox:focus {{
        border: 2px solid {ACCENT};
    }}
    QComboBox::drop-down {{
        border: none;
        width: 25px;
    }}
    QComboBox::down-arrow {{
        image: none;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 6px solid {ACCENT};
        width: 0;
        height: 0;
        margin-right: 8px;
    }}
    QComboBox QAbstractItemView {{
        background-color: {BG_PANEL};
        border: 1px solid {BORDER};
        border-radius: 8px;
        color: {TEXT_PRI};
        selection-background-color: {BG_HOVER};
        selection-color: {ACCENT};
        outline: none;
        padding: 5px;
    }}
    QComboBox QAbstractItemView::item {{
        padding: 8px;
        border-radius: 5px;
    }}
    QComboBox QAbstractItemView::item:hover {{
        background-color: {BG_HOVER};
        color: {ACCENT};
    }}
"""

INPUT_STYLE = f"""
    QLineEdit {{
        padding: 10px 14px;
        border: 1px solid {BORDER};
        border-radius: 8px;
        background-color: {BG_PANEL};
        color: {TEXT_PRI};
        font-size: 13px;
        font-weight: 500;
    }}
    QLineEdit:focus {{
        border: 2px solid {ACCENT};
        background-color: {BG_DEEP};
    }}
    QLineEdit:hover {{
        border: 1px solid {ACCENT2};
    }}
    QLineEdit[placeholderText=""] {{
        color: {TEXT_SEC};
    }}
"""

# Enhanced Button Styles
BTN_PRIMARY = f"""
    QPushButton {{
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 {ACCENT2}, stop:1 {ACCENT});
        color: {BG_DEEP};
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }}
    QPushButton:hover {{
        background-color: {ACCENT};
        transform: scale(1.02);
    }}
    QPushButton:pressed {{
        background-color: #4A8A2C;
    }}
"""

BTN_GHOST = f"""
    QPushButton {{
        background-color: transparent;
        color: {TEXT_PRI};
        border: 1px solid {BORDER};
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 13px;
        font-weight: 700;
    }}
    QPushButton:hover {{
        border: 1px solid {ACCENT2};
        color: {ACCENT};
        background-color: {BG_HOVER};
    }}
"""

BTN_DANGER = f"""
    QPushButton {{
        background-color: {RED_BG};
        color: {RED_SOFT};
        border: 1px solid {RED_SOFT};
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 13px;
        font-weight: 700;
    }}
    QPushButton:hover {{
        background-color: {RED_SOFT};
        color: white;
    }}
"""

# Enhanced Tab Style
TAB_STYLE = f"""
    QTabWidget::pane {{
        border: 1px solid {BORDER};
        border-radius: 10px;
        background-color: {BG_PANEL};
        padding: 10px;
    }}
    QTabBar::tab {{
        background-color: transparent;
        color: {TEXT_SEC};
        padding: 12px 24px;
        font-size: 12px;
        font-weight: 700;
        border: none;
        border-bottom: 3px solid transparent;
        margin-right: 5px;
        letter-spacing: 1px;
    }}
    QTabBar::tab:selected {{
        color: {ACCENT};
        border-bottom: 3px solid {ACCENT};
        background-color: {BG_HOVER};
        border-radius: 5px 5px 0 0;
    }}
    QTabBar::tab:hover:!selected {{
        color: {TEXT_PRI};
        border-bottom: 3px solid {ACCENT2};
    }}
"""

# ── GLOBAL STYLE (Keep existing but add table enhancements) ───────────────
GLOBAL_STYLE = f"""
    * {{ font-family: 'Segoe UI', 'Arial', sans-serif; }}
    QMainWindow, QWidget {{ background-color: {BG_DEEP}; color: {TEXT_PRI}; }}
    QStackedWidget {{ background-color: {BG_DEEP}; }}
    QScrollBar:vertical {{ background: {BG_PANEL}; width: 8px; border-radius: 4px; }}
    QScrollBar::handle:vertical {{ background: {BORDER}; border-radius: 4px; min-height: 20px; }}
    QScrollBar::handle:vertical:hover {{ background: {ACCENT2}; }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
    QMessageBox {{ background-color: {BG_PANEL}; color: {TEXT_PRI}; }}
    QMessageBox QPushButton {{
        background-color: {ACCENT2}; color: {BG_DEEP};
        border: none; border-radius: 6px; padding: 8px 20px; font-weight: 700;
        min-width: 80px;
    }}
    QMessageBox QPushButton:hover {{ background-color: {ACCENT}; }}
    QToolTip {{
        background-color: {BG_PANEL};
        color: {ACCENT};
        border: 1px solid {ACCENT};
        border-radius: 5px;
        padding: 5px;
    }}
"""

SIDEBAR_STYLE = f"""
    QFrame#sidebar {{ background-color: {BG_PANEL}; border-right: 1px solid {BORDER}; }}
    #logo {{ font-size: 18px; font-weight: 900; color: {ACCENT}; padding: 8px 20px 0 20px; letter-spacing: 3px; }}
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

# ── Helpers ────────────────────────────────────────────────────────────────
def page_title(text):
    lbl = QLabel(text)
    lbl.setStyleSheet(f"""
        font-size: 28px; 
        font-weight: 900; 
        color: {ACCENT}; 
        letter-spacing: 2px; 
        background: transparent;
        margin-bottom: 10px;
    """)
    return lbl

def stat_card(icon, value, label, color=ACCENT):
    card = QFrame()
    card.setStyleSheet(f"""
        QFrame {{ 
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {BG_PANEL}, stop:1 {BG_HOVER});
            border: 1px solid {BORDER}; 
            border-radius: 12px;
        }}
        QFrame:hover {{
            border: 1px solid {ACCENT2};
            transform: scale(1.02);
        }}
    """)
    card.setFixedHeight(100)
    h = QHBoxLayout()
    h.setContentsMargins(20, 16, 20, 16)
    h.setSpacing(14)
    
    ico = QLabel(icon)
    ico.setStyleSheet(f"font-size: 32px; background: transparent; border: none;")
    h.addWidget(ico)
    
    v = QVBoxLayout()
    v.setSpacing(2)
    val_lbl = QLabel(str(value))
    val_lbl.setStyleSheet(f"""
        font-size: 28px; 
        font-weight: 900; 
        color: {color}; 
        background: transparent; 
        border: none;
        font-family: 'Segoe UI', 'Arial', monospace;
    """)
    sub_lbl = QLabel(label.upper())
    sub_lbl.setStyleSheet(f"""
        font-size: 9px; 
        font-weight: 800; 
        color: {TEXT_SEC}; 
        letter-spacing: 2px; 
        background: transparent; 
        border: none;
    """)
    v.addWidget(val_lbl)
    v.addWidget(sub_lbl)
    h.addLayout(v)
    h.addStretch()
    card.setLayout(h)
    return card

def section_card():
    f = QFrame()
    f.setStyleSheet(f"""
        QFrame {{ 
            background-color: {BG_PANEL}; 
            border: 1px solid {BORDER}; 
            border-radius: 12px;
        }}
    """)
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
    t.verticalHeader().setDefaultSectionSize(55)
    t.horizontalHeader().setStretchLastSection(True)
    t.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    t.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    t.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
    t.setSortingEnabled(True)  # Enable sorting by clicking headers
    
    # Set font for better readability
    font = QFont("Segoe UI", 10)
    t.setFont(font)
    
    return t

# ── Sidebar ────────────────────────────────────────────────────────────────
class FloraSidebar(QFrame):
    def __init__(self, stacked_widget, username):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setObjectName("sidebar")
        self.setFixedWidth(240)
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
        sep.setStyleSheet(f"background-color: {BORDER}; max-height: 1px; margin: 8px 16px;")
        layout.addWidget(sep)

        uname = QLabel(f"● {username}")
        uname.setObjectName("username")
        layout.addWidget(uname)
        layout.addSpacing(10)

        for label, idx in [("📊 Dashboard", 0), ("📝 Records", 1), ("📈 Reports", 2), ("ℹ️ About", 3)]:
            btn = QPushButton(label)
            btn.setObjectName("nav-btn")
            btn.clicked.connect(lambda _, i=idx: self.navigate(i))
            layout.addWidget(btn)
            self.nav_buttons.append(btn)

        layout.addStretch()

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setStyleSheet(f"background-color: {BORDER}; max-height: 1px; margin: 8px 16px;")
        layout.addWidget(sep2)
        layout.addSpacing(6)

        logout_btn = QPushButton("🚪 LOG OUT")
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
        layout.setSpacing(25)
        layout.addWidget(page_title("Dashboard"))
        
        self.cards_layout = QHBoxLayout()
        self.cards_layout.setSpacing(16)
        layout.addLayout(self.cards_layout)
        
        # Add welcome message
        welcome = QLabel("Welcome back! Here's your farm overview 🌾")
        welcome.setStyleSheet(f"""
            font-size: 14px; 
            color: {TEXT_SEC}; 
            margin-top: 10px;
            margin-bottom: 20px;
            background: transparent;
            font-style: italic;
        """)
        layout.addWidget(welcome)
        
        self.footer = QLabel("✨ Grow your data with Flora — Smart farming, better harvests ✨")
        self.footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer.setStyleSheet(f"""
            font-size: 12px; 
            color: {TEXT_SEC}; 
            margin-top: 40px; 
            background: transparent;
            padding: 15px;
            border-top: 1px solid {BORDER};
        """)
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
        
        # Create new cards with different colors
        colors = [ACCENT, ACCENT2, WARM_BROWN, CREAM]
        self.cards_layout.addWidget(stat_card("🌾", total_crops, "Crop Types", colors[0]))
        self.cards_layout.addWidget(stat_card("📋", total_records, "Total Records", colors[1]))
        self.cards_layout.addWidget(stat_card("🏆", most_planted, "Most Planted", colors[2]))
        self.cards_layout.addWidget(stat_card("💧", f"{avg_fert} kg", "Avg Fertilizer", colors[3]))

# ── Records Page (Enhanced Table) ─────────────────────────────────────────
class RecordsPage(QWidget):
    data_changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(20)

        header = QHBoxLayout()
        header.addWidget(page_title("Crop Records"))
        header.addStretch()

        # Search bar with icon
        search_container = QFrame()
        search_container.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_PANEL};
                border: 1px solid {BORDER};
                border-radius: 10px;
                padding: 2px;
            }}
        """)
        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(10, 5, 10, 5)
        search_icon = QLabel("🔍")
        search_icon.setStyleSheet("background: transparent; font-size: 14px;")
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search by crop name or season...")
        self.search.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
                padding: 8px;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: none;
            }
        """)
        search_layout.addWidget(search_icon)
        search_layout.addWidget(self.search)
        search_container.setLayout(search_layout)
        search_container.setFixedWidth(300)
        self.search.textChanged.connect(self.load)
        header.addWidget(search_container)
        layout.addLayout(header)

        # Table container
        card = section_card()
        card_v = QVBoxLayout()
        card_v.setContentsMargins(0, 0, 0, 0)
        self.table = make_table()
        self.table.setColumnWidth(0, 50)  # ID column width
        self.table.cellClicked.connect(self.select)
        card_v.addWidget(self.table)
        card.setLayout(card_v)
        layout.addWidget(card, stretch=1)

        # Input form
        form_card = QFrame()
        form_card.setStyleSheet(f"""
            QFrame {{
                background-color: {BG_PANEL};
                border: 1px solid {BORDER};
                border-radius: 12px;
                padding: 15px;
            }}
        """)
        form_layout = QHBoxLayout()
        form_layout.setSpacing(12)

        self.crop = QComboBox()
        self.crop.setStyleSheet(COMBO_STYLE)
        self.crop.setFixedHeight(42)
        self.crop.setMinimumWidth(150)
        
        self.soil = QComboBox()
        self.soil.setStyleSheet(COMBO_STYLE)
        self.soil.setFixedHeight(42)
        self.soil.setMinimumWidth(120)
        
        self.fert = QComboBox()
        self.fert.setStyleSheet(COMBO_STYLE)
        self.fert.setFixedHeight(42)
        self.fert.setMinimumWidth(150)
        
        self.season = QComboBox()
        self.season.setStyleSheet(COMBO_STYLE)
        self.season.setFixedHeight(42)
        self.season.setMinimumWidth(100)
        self.season.addItems(["🌞 Dry", "☔ Rainy"])

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount (kg)")
        self.amount.setStyleSheet(INPUT_STYLE)
        self.amount.setFixedHeight(42)
        self.amount.setFixedWidth(130)

        for w in [self.crop, self.soil, self.fert, self.season, self.amount]:
            form_layout.addWidget(w)
        form_layout.addStretch()

        # Button container
        btn_container = QHBoxLayout()
        btn_container.setSpacing(10)
        
        add_btn = QPushButton("➕ Add")
        add_btn.setStyleSheet(BTN_PRIMARY)
        add_btn.setFixedHeight(42)
        add_btn.clicked.connect(self.add)
        
        upd_btn = QPushButton("✏️ Update")
        upd_btn.setStyleSheet(BTN_GHOST)
        upd_btn.setFixedHeight(42)
        upd_btn.clicked.connect(self.update)
        
        del_btn = QPushButton("🗑️ Delete")
        del_btn.setStyleSheet(BTN_DANGER)
        del_btn.setFixedHeight(42)
        del_btn.clicked.connect(self.delete)
        
        for b in [add_btn, upd_btn, del_btn]:
            btn_container.addWidget(b)
        
        form_layout.addLayout(btn_container)
        form_card.setLayout(form_layout)
        layout.addWidget(form_card)

        self.setLayout(layout)
        self.load_dropdowns()
        self.load()

    def load_dropdowns(self):
        # Clear existing items
        self.crop.clear()
        self.soil.clear()
        self.fert.clear()
        
        # Add items with icons
        for i in self.db.get_crops(): 
            self.crop.addItem(f"🌾 {i[1]}", i[0])
        for i in self.db.get_soil():  
            self.soil.addItem(f"🟫 {i[1]}", i[0])
        for i in self.db.get_fert():  
            self.fert.addItem(f"🧪 {i[1]}", i[0])

    def load(self):
        data = self.db.fetch_records(self.search.text())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "🌾 CROP", "🟫 SOIL", "🧪 FERTILIZER", "🌦️ SEASON", "⚖️ AMOUNT (KG)"])
        
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                # Set tooltip for better readability
                item.setToolTip(str(val))
                self.table.setItem(r, c, item)
        
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)
        
        # Set ID column width
        self.table.setColumnWidth(0, 60)
        
        # Update status
        self.table.setToolTip(f"Showing {len(data)} record(s)")

    def select(self):
        row = self.table.currentRow()
        if row >= 0:
            self.amount.setText(self.table.item(row, 5).text())
            # Highlight the selected row
            self.table.selectRow(row)

    def notify_data_changed(self):
        self.data_changed.emit()

    def add(self):
        if self.amount.text():
            try:
                self.db.insert_record(self.crop.currentData(), self.soil.currentData(),
                                      self.fert.currentData(), self.season.currentText().split()[-1],
                                      int(self.amount.text()))
                self.amount.clear()
                self.load()
                self.notify_data_changed()
                QMessageBox.information(self, "Success", "✅ Record added successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"❌ {str(e)}")

    def update(self):
        row = self.table.currentRow()
        if row >= 0 and self.amount.text():
            try:
                rid = int(self.table.item(row, 0).text())
                self.db.update_record(rid, self.crop.currentData(), self.soil.currentData(),
                                      self.fert.currentData(), self.season.currentText().split()[-1],
                                      int(self.amount.text()))
                self.load()
                self.notify_data_changed()
                QMessageBox.information(self, "Success", "✅ Record updated successfully!")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"❌ {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "⚠️ Select a record and enter an amount")

    def delete(self):
        row = self.table.currentRow()
        if row >= 0:
            reply = QMessageBox.question(self, 'Confirm Delete', 
                                         '⚠️ Are you sure you want to delete this record?\nThis action cannot be undone.',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    rid = int(self.table.item(row, 0).text())
                    self.db.delete_record(rid)
                    self.load()
                    self.amount.clear()
                    self.notify_data_changed()
                    QMessageBox.information(self, "Success", "✅ Record deleted successfully!")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"❌ {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "⚠️ Select a record to delete")

# ── Reports Page (Keep existing but enhance) ──────────────────────────────
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
        layout.setSpacing(20)
        layout.addWidget(page_title("Analytics Reports"))

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(TAB_STYLE)
        self.tabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        
        self.refresh_all_reports()
    
    def refresh_all_reports(self):
        self.tabs.clear()
        
        def wrap(table, title=""):
            card = section_card()
            v = QVBoxLayout()
            v.setContentsMargins(0, 0, 0, 0)
            
            # Add title if provided
            if title:
                title_label = QLabel(title)
                title_label.setStyleSheet(f"""
                    font-size: 16px;
                    font-weight: bold;
                    color: {ACCENT};
                    padding: 15px 15px 0 15px;
                    background: transparent;
                """)
                v.addWidget(title_label)
            
            v.addWidget(table)
            card.setLayout(v)
            w = QWidget()
            w.setStyleSheet("background: transparent;")
            wl = QVBoxLayout()
            wl.setContentsMargins(0, 12, 0, 0)
            wl.addWidget(card)
            w.setLayout(wl)
            return w
        
        # Basic Report
        basic_data = self.db.crop_report()
        self.tabs.addTab(wrap(build_report_table(
            ["🌾 CROP", "📊 TIMES PLANTED"],
            basic_data
        ), "Crop Planting Frequency"), "Basic Report")
        
        # Detailed Report
        detailed_data = self.db.crop_detailed_report()
        self.tabs.addTab(wrap(build_report_table(
            ["🌾 CROP", "📊 TIMES PLANTED", "⚖️ TOTAL FERT (KG)", "📈 AVG (KG)", "📉 MIN (KG)", "📊 MAX (KG)"],
            detailed_data, float_cols={2, 3, 4, 5}
        ), "Detailed Fertilizer Analysis"), "Detailed Report")
        
        # Seasonal Report
        seasonal_data = self.db.crop_seasonal_report()
        self.tabs.addTab(wrap(build_report_table(
            ["🌾 CROP", "🌦️ SEASON", "📊 TIMES PLANTED", "⚖️ TOTAL FERT (KG)"],
            seasonal_data, float_cols={3}
        ), "Seasonal Performance"), "Seasonal Report")
    
    def refresh(self):
        self.refresh_all_reports()

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(20)
        layout.addWidget(page_title("About Flora"))

        card = section_card()
        cl = QVBoxLayout()
        cl.setContentsMargins(40, 40, 40, 40)
        cl.setSpacing(16)

        logo = QLabel("🌱")
        logo.setStyleSheet("font-size: 64px; background: transparent;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cl.addWidget(logo)

        text = QLabel(
            f"<h2 style='color:{ACCENT}; text-align:center; font-size:20px; letter-spacing:2px;'>FLORA</h2>"
            f"<h3 style='color:{TEXT_PRI}; text-align:center; font-size:14px; margin-top:-10px;'>CROP MANAGEMENT SYSTEM</h3>"
            f"<p style='font-size:13px; color:{TEXT_SEC}; text-align:center; line-height:1.8; margin-top:20px;'>"
            "A comprehensive application to manage crop records,<br>"
            "track fertilizer usage, and generate detailed analytical reports.</p>"
            f"<br><hr style='border:none; border-top:1px solid {BORDER};'><br>"
            f"<p style='font-size:12px; color:{TEXT_SEC}; text-align:center; line-height:2.2;'>"
            f"<b style='color:{ACCENT};'>Version:</b> 2.0<br>"
            f"<b style='color:{ACCENT};'>Created by:</b> Group 3 — CPE22S1<br>"
            f"<b style='color:{ACCENT};'>Year:</b> 2025<br><br>"
            f"<span style='color:{WARM_BROWN};'>© 2025 Flora. Smart farming for a sustainable future.</span></p>"
        )
        text.setWordWrap(True)
        text.setTextFormat(Qt.TextFormat.RichText)
        text.setStyleSheet("background: transparent;")
        cl.addWidget(text)
        card.setLayout(cl)
        layout.addWidget(card)
        layout.addStretch()
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Flora — Crop Management System")
        self.setMinimumSize(1200, 700)

        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.stacked = QStackedWidget()
        
        self.dashboard_page = DashboardPage()
        self.records_page = RecordsPage()
        self.reports_page = ReportsPage()
        self.about_page = AboutPage()
        
        self.records_page.data_changed.connect(self.on_data_changed)
        
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
        self.dashboard_page.refresh_data()
        self.reports_page.refresh()
        self.records_page.load()

def show_main_window(username):
    main_window = MainWindow(username)
    main_window.show()
    return main_window
