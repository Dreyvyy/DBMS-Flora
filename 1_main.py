# app.py - Main entry point for your application
import sys
from PyQt6.QtWidgets import QApplication
from login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec())
