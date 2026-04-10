from PyQt6.QtWidgets import *
from database import Database
from dashboard import Dashboard
from register import Register

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.user = QLineEdit()
        self.user.setPlaceholderText("Username")

        self.passw = QLineEdit()
        self.passw.setPlaceholderText("Password")
        self.passw.setEchoMode(QLineEdit.EchoMode.Password)

        btn = QPushButton("Login")
        reg = QPushButton("Register")

        btn.clicked.connect(self.login)
        reg.clicked.connect(self.open_reg)

        layout.addWidget(self.user)
        layout.addWidget(self.passw)
        layout.addWidget(btn)
        layout.addWidget(reg)

        self.setLayout(layout)

    def login(self):
        if self.db.login(self.user.text(), self.passw.text()):
            self.dash = Dashboard()
            self.dash.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid login")

    def open_reg(self):
        self.r = Register()
        self.r.show()
