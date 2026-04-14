from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from database import Database
from register import Register

class Login(QWidget):
    def __init__(self):
        super().__init__()

        try:
            self.db = Database()
            if not self.db.cursor:
                QMessageBox.critical(
                    self, 
                    "Database Connection Error",
                    "Cannot connect to the database.\n\n"
                    "Please ensure:\n"
                    "1. SQL Server is running\n"
                    "2. Database 'FLORA' exists\n"
                    "3. Connection settings are correct\n\n"
                    "The application will close."
                )
                self.close()
                return
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Database Error",
                f"Failed to initialize database: {str(e)}\n\nThe application will close."
            )
            self.close()
            return
            
        self.setWindowTitle("Flora — Login")
        self.setFixedSize(1000,800)
        
        self.center_window()
        
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Left panel - decorative
        left_panel = QFrame()
        left_panel.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a472a, stop:1 #2d5a3f);
                border-top-left-radius: 15px;
                border-bottom-left-radius: 15px;
            }
        """)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Decorative elements on left panel
        leaf_icon = QLabel("🌿")
        leaf_icon.setStyleSheet("font-size: 80px; background: transparent;")
        leaf_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        left_title = QLabel("Welcome to Flora")
        left_title.setStyleSheet("""
            font-size: 28px; 
            font-weight: bold; 
            color: white; 
            background: transparent;
            margin-top: 20px;
        """)
        left_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        left_subtitle = QLabel("Crop Management System")
        left_subtitle.setStyleSheet("""
            font-size: 14px; 
            color: #a8e6cf; 
            background: transparent;
            margin-bottom: 30px;
        """)
        left_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        features = QLabel("• Track crop records\n• Monitor fertilizer usage\n• Generate detailed reports\n• Analyze seasonal trends")
        features.setStyleSheet("""
            font-size: 13px; 
            color: #d4f1e3; 
            background: transparent;
            line-height: 1.8;
            padding: 20px;
        """)
        features.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        left_layout.addStretch()
        left_layout.addWidget(leaf_icon)
        left_layout.addWidget(left_title)
        left_layout.addWidget(left_subtitle)
        left_layout.addWidget(features)
        left_layout.addStretch()
        
        left_panel.setLayout(left_layout)
        
        # Right panel - login form
        right_panel = QFrame()
        right_panel.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
            }
        """)
        
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(60, 80, 60, 80)
        right_layout.setSpacing(20)
        
        # Logo and title
        logo = QLabel("🌱")
        logo.setStyleSheet("font-size: 48px; background: transparent;")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title = QLabel("FLORA")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 32px; 
            font-weight: bold; 
            color: #2c3e50;
            letter-spacing: 3px;
            margin-bottom: 10px;
        """)
        
        subtitle = QLabel("Sign in to continue")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 13px; 
            color: #7f8c8d;
            margin-bottom: 30px;
        """)
        
        # Username field
        username_label = QLabel("Username")
        username_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #34495e; margin-bottom: 5px;")
        
        self.user = QLineEdit()
        self.user.setPlaceholderText("Enter your username")
        self.user.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                color: #A76D5E;
            }
            QLineEdit:focus {
                border: 2px solid #2d5a3f;
                background-color: #DFCCB1;
            }
            QLineEdit:hover {
                border: 2px solid #a8e6cf;
            }
        """)
        
        # Password field
        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #34495e; margin-bottom: 5px; margin-top: 10px;")
        
        self.passw = QLineEdit()
        self.passw.setPlaceholderText("Enter your password")
        self.passw.setEchoMode(QLineEdit.EchoMode.Password)
        self.passw.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                color: #A76D5E;
            }
            QLineEdit:focus {
                border: 2px solid #2d5a3f;
                background-color: #DFCCB1;
            }
            QLineEdit:hover {
                border: 2px solid #a8e6cf;
            }
        """)
        
        # Show/Hide password toggle
        self.show_password = QCheckBox("Show password")
        self.show_password.setStyleSheet("""
            QCheckBox {
                color: #7f8c8d;
                font-size: 11px;
                margin-top: 5px;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
        """)
        self.show_password.stateChanged.connect(self.toggle_password_visibility)
        
        btn = QPushButton("LOGIN")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #2d5a3f;
                color: white;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                margin-top: 20px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #1a472a;
            }
            QPushButton:pressed {
                background-color: #0d2b1a;
            }
        """)
        
        # Create Account button
        reg = QPushButton("CREATE NEW ACCOUNT")
        reg.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2d5a3f;
                padding: 10px;
                font-size: 12px;
                font-weight: bold;
                border: 2px solid #2d5a3f;
                border-radius: 8px;
                margin-top: 10px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #2d5a3f;
                color: white;
            }
        """)
        
        btn.clicked.connect(self.login)
        reg.clicked.connect(self.open_reg)
        
        self.passw.returnPressed.connect(self.login)
        self.user.returnPressed.connect(self.login)
        
        right_layout.addWidget(logo)
        right_layout.addWidget(title)
        right_layout.addWidget(subtitle)
        right_layout.addWidget(username_label)
        right_layout.addWidget(self.user)
        right_layout.addWidget(password_label)
        right_layout.addWidget(self.passw)
        right_layout.addWidget(self.show_password)
        right_layout.addWidget(btn)
        right_layout.addWidget(reg)
        right_layout.addStretch()
        
        right_panel.setLayout(right_layout)
        
        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)
        
        self.setLayout(main_layout)

        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }
        """)
    
    def center_window(self):
        """Center the window on the screen"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def toggle_password_visibility(self, state):
        """Toggle password visibility when checkbox is clicked"""
        if state == Qt.CheckState.Checked.value:
            self.passw.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passw.setEchoMode(QLineEdit.EchoMode.Password)
    
    def login(self):
        """Handle login action"""
        if not self.db.cursor:
            QMessageBox.critical(self, "Database Error", "Database connection is not available.")
            return
            
        username = self.user.text().strip()
        password = self.passw.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password")
            return
        
        user_id, username = self.db.login(username, password)
        if user_id:
            from dashboard import show_main_window
            self.main_window = show_main_window(username)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
            self.passw.clear()
            self.passw.setFocus()
    
    def open_reg(self):
        """Open registration window"""
        self.r = Register()
        self.r.show()

def show_login_window():
    """Function to show the login window"""
    login_window = Login()
    login_window.show()
    return login_window
