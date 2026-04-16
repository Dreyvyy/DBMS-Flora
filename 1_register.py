from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from database import Database

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Flora — Create Account")
        self.setFixedSize(1000, 750)
        
        # Center the window
        self.center_window()
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)
        
        # Header
        title = QLabel("Create Account")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold; 
            color: #2c3e50;
            margin-bottom: 20px;
        """)
        
        subtitle = QLabel("Join Flora to manage your crops")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 12px; 
            color: #7f8c8d;
            margin-bottom: 30px;
        """)
        
        # Username field
        username_label = QLabel("Username")
        username_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #34495e; margin-bottom: 5px;")
        
        self.user = QLineEdit()
        self.user.setPlaceholderText("Choose a username")
        self.user.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                color: #000000;
            }
            QLineEdit:focus {
                border: 2px solid #2d5a3f;
            }
        """)
        
        # Password field
        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #34495e; margin-bottom: 5px; margin-top: 10px;")
        
        self.passw = QLineEdit()
        self.passw.setPlaceholderText("Create a password")
        self.passw.setEchoMode(QLineEdit.EchoMode.Password)
        self.passw.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                color: #000000;
            }
            QLineEdit:focus {
                border: 2px solid #2d5a3f;
            }
        """)
        
        # Confirm password field
        confirm_label = QLabel("Confirm Password")
        confirm_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #34495e; margin-bottom: 5px; margin-top: 10px;")
        
        self.confirm_pass = QLineEdit()
        self.confirm_pass.setPlaceholderText("Confirm your password")
        self.confirm_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_pass.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 14px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                color: #000000;
            }
            QLineEdit:focus {
                border: 2px solid #2d5a3f;
            }
        """)
        
        # Register button
        reg_btn = QPushButton("REGISTER")
        reg_btn.setStyleSheet("""
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
        """)
        
        # Cancel button
        cancel_btn = QPushButton("CANCEL")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7f8c8d;
                padding: 10px;
                font-size: 12px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                cursor: pointer;
            }
            QPushButton:hover {
                border-color: #2d5a3f;
                color: #2d5a3f;
            }
        """)
        
        # Connect signals
        reg_btn.clicked.connect(self.register)
        cancel_btn.clicked.connect(self.close)
        
        # Enable Enter key on password fields
        self.passw.returnPressed.connect(self.register)
        self.confirm_pass.returnPressed.connect(self.register)
        
        # Add to layout
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(username_label)
        layout.addWidget(self.user)
        layout.addWidget(password_label)
        layout.addWidget(self.passw)
        layout.addWidget(confirm_label)
        layout.addWidget(self.confirm_pass)
        layout.addWidget(reg_btn)
        layout.addWidget(cancel_btn)
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Apply global style
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                font-family: 'Segoe UI', 'Arial', sans-serif;
                color: #000000;
            }
        """)
    
    def center_window(self):
        """Center the window on the screen"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def register(self):
        """Handle registration"""
        username = self.user.text().strip()
        password = self.passw.text()
        confirm = self.confirm_pass.text()
        
        # Validation
        if not username or not password or not confirm:
            QMessageBox.warning(self, "Error", "Please fill in all fields")
            return
        
        if len(username) < 3:
            QMessageBox.warning(self, "Error", "Username must be at least 3 characters long")
            return
        
        if len(password) < 4:
            QMessageBox.warning(self, "Error", "Password must be at least 4 characters long")
            return
        
        if password != confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match")
            self.passw.clear()
            self.confirm_pass.clear()
            return
        
        # Attempt registration
        if self.db.register(username, password):
            QMessageBox.information(self, "Success", "Account created successfully!\nYou can now login.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Username already exists. Please choose another one.")
            self.user.clear()
            self.user.setFocus()
