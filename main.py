import sys
from PyQt6.QtWidgets import QApplication
from login import Login

app = QApplication(sys.argv)

login_window = None

def show_login():
    global login_window
    login_window = Login()
    login_window.show()

if __name__ == "__main__":
    show_login()
    sys.exit(app.exec())
