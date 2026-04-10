from PyQt6.QtWidgets import *
from database import Database

class Reports(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Reports")

        layout = QVBoxLayout()

        table = QTableWidget()
        data = self.db.fertilizer_report()

        table.setRowCount(len(data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Crop", "Total Fertilizer"])

        for r, row in enumerate(data):
            for c, val in enumerate(row):
                table.setItem(r, c, QTableWidgetItem(str(val)))

        layout.addWidget(QLabel("Fertilizer Usage Report"))
        layout.addWidget(table)

        self.setLayout(layout)
