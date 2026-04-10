# register.py
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from database import Database

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Register")
        self.setFixedSize(1000, 500)
        
        # Center the window on screen
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("🌱 Create Account")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Username field
        self.u = QLineEdit()
        self.u.setPlaceholderText("Username")
        self.u.setStyleSheet("""
            QLineEdit {
                padding: 10px; 
                font-size: 14px;
                border: 1px solid #dcdde1;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        # Password field
        self.p = QLineEdit()
        self.p.setPlaceholderText("Password")
        self.p.setEchoMode(QLineEdit.EchoMode.Password)
        self.p.setStyleSheet("""
            QLineEdit {
                padding: 10px; 
                font-size: 14px;
                border: 1px solid #dcdde1;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        # Confirm password field
        self.confirm_p = QLineEdit()
        self.confirm_p.setPlaceholderText("Confirm Password")
        self.confirm_p.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_p.setStyleSheet("""
            QLineEdit {
                padding: 10px; 
                font-size: 14px;
                border: 1px solid #dcdde1;
                border-radius: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        
        # Create account button
        btn = QPushButton("Create Account")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)
        
        btn.clicked.connect(self.create)
        
        # Back to login link
        back_btn = QPushButton("Back to Login")
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #3498db;
                padding: 5px;
                font-size: 12px;
                border: none;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: #2980b9;
            }
        """)
        back_btn.clicked.connect(self.back_to_login)
        
        layout.addWidget(self.u)
        layout.addWidget(self.p)
        layout.addWidget(self.confirm_p)
        layout.addWidget(btn)
        layout.addWidget(back_btn)
        
        self.setLayout(layout)
    
    def create(self):
        # Validate inputs
        username = self.u.text().strip()
        password = self.p.text()
        confirm_password = self.confirm_p.text()
        
        # Check if fields are empty
        if not username:
            QMessageBox.warning(self, "Error", "Please enter a username")
            return
        
        if not password:
            QMessageBox.warning(self, "Error", "Please enter a password")
            return
        
        # Check if passwords match
        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match")
            # Clear password fields
            self.p.clear()
            self.confirm_p.clear()
            return
        
        # Check password length
        if len(password) < 4:
            QMessageBox.warning(self, "Error", "Password must be at least 4 characters long")
            self.p.clear()
            self.confirm_p.clear()
            return
        
        # Attempt to register
        if self.db.register(username, password):
            QMessageBox.information(self, "Success", "Account created successfully!\n\nYou can now login with your credentials.")
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Username already exists. Please choose a different username.")
            self.u.clear()
            self.p.clear()
            self.confirm_p.clear()
            self.u.setFocus()
    
    def back_to_login(self):
        """Close registration window to return to login"""
        self.close()
