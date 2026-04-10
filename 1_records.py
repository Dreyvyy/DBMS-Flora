from PyQt6.QtWidgets import *
from database import Database

class Records(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Records")

        layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        self.search.textChanged.connect(self.load)

        self.table = QTableWidget()
        self.table.cellClicked.connect(self.select)

        self.crop = QComboBox()
        self.soil = QComboBox()
        self.fert = QComboBox()
        self.season = QComboBox()
        self.season.addItems(["Dry", "Rainy"])
        self.amount = QLineEdit()

        self.load_dropdowns()

        form = QHBoxLayout()
        form.addWidget(self.crop)
        form.addWidget(self.soil)
        form.addWidget(self.fert)
        form.addWidget(self.season)
        form.addWidget(self.amount)

        btns = QHBoxLayout()
        for text, func in [("Add", self.add), ("Update", self.update), ("Delete", self.delete)]:
            b = QPushButton(text)
            b.clicked.connect(func)
            btns.addWidget(b)

        layout.addWidget(self.search)
        layout.addWidget(self.table)
        layout.addLayout(form)
        layout.addLayout(btns)

        self.setLayout(layout)
        self.load()

    def load_dropdowns(self):
        for i in self.db.get_crops():
            self.crop.addItem(i[1], i[0])
        for i in self.db.get_soil():
            self.soil.addItem(i[1], i[0])
        for i in self.db.get_fert():
            self.fert.addItem(i[1], i[0])

    def load(self):
        data = self.db.fetch_records(self.search.text())
        self.table.setRowCount(len(data))
        self.table.setColumnCount(6)
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    def select(self):
        row = self.table.currentRow()
        self.amount.setText(self.table.item(row, 5).text())

    def add(self):
        self.db.insert_record(
            self.crop.currentData(),
            self.soil.currentData(),
            self.fert.currentData(),
            self.season.currentText(),
            int(self.amount.text())
        )
        self.load()

    def update(self):
        row = self.table.currentRow()
        id = int(self.table.item(row, 0).text())
        self.db.update_record(
            id,
            self.crop.currentData(),
            self.soil.currentData(),
            self.fert.currentData(),
            self.season.currentText(),
            int(self.amount.text())
        )
        self.load()

    def delete(self):
        row = self.table.currentRow()
        id = int(self.table.item(row, 0).text())
        self.db.delete_record(id)
        self.load()
