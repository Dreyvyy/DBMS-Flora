# login.py
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from database import Database
from register import Register

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Login")
        self.setFixedSize(1000, 500)
        
        # Center the window
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Title
        title = QLabel("🌱 Flora")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)
        
        self.user = QLineEdit()
        self.user.setPlaceholderText("Username")
        self.user.setStyleSheet("padding: 10px; font-size: 14px;")
        
        self.passw = QLineEdit()
        self.passw.setPlaceholderText("Password")
        self.passw.setEchoMode(QLineEdit.EchoMode.Password)
        self.passw.setStyleSheet("padding: 10px; font-size: 14px;")
        
        btn = QPushButton("Login")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        reg = QPushButton("Create Account")
        reg.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        
        btn.clicked.connect(self.login)
        reg.clicked.connect(self.open_reg)
        
        layout.addWidget(self.user)
        layout.addWidget(self.passw)
        layout.addWidget(btn)
        layout.addWidget(reg)
        
        self.setLayout(layout)
    
    def login(self):
        user_id, username = self.db.login(self.user.text(), self.passw.text())
        if user_id:
            # Import here to avoid circular import
            from dashboard import show_main_window
            self.main_window = show_main_window(username)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
    
    def open_reg(self):
        self.r = Register()
        self.r.show()

def show_login_window():
    """Function to show the login window"""
    login_window = Login()
    login_window.show()
    return login_window

if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login.show()
    app.exec()
