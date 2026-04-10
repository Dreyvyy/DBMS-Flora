from PyQt6.QtWidgets import *
from records import Records
from reports import Reports

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("🌱 Crop Management System"))

        btn1 = QPushButton("Manage Records")
        btn2 = QPushButton("View Reports")
        btn3 = QPushButton("Logout")

        btn1.clicked.connect(self.open_records)
        btn2.clicked.connect(self.open_reports)
        btn3.clicked.connect(self.logout)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)

    def open_records(self):
        self.w = Records()
        self.w.show()

    def open_reports(self):
        self.r = Reports()
        self.r.show()

    def logout(self):
        # CLOSE dashboard only
        self.close()

        # reopen login through main entry point
        from main import show_login
        show_login()
