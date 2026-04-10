import pyodbc

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LIANNEDREY\\SQLEXPRESS;'
            'DATABASE=FLORA;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    def login(self, u, p):
        self.cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (u, p))
        return self.cursor.fetchone()

    def register(self, u, p):
        try:
            self.cursor.execute("INSERT INTO Users VALUES (?,?)", (u, p))
            self.conn.commit()
            return True
        except:
            return False

    def get_crops(self):
        self.cursor.execute("SELECT Crop_Id, Crop_name FROM Crops")
        return self.cursor.fetchall()

    def get_soil(self):
        self.cursor.execute("SELECT Soil_Id, Soil_Type FROM Soil")
        return self.cursor.fetchall()

    def get_fert(self):
        self.cursor.execute("SELECT Fertilizer_Id, Fertilizer_name FROM Fertilizer")
        return self.cursor.fetchall()

    def fetch_records(self, search=""):
        query = """
        SELECT r.Record_Id, c.Crop_name, s.Soil_Type, f.Fertilizer_name,
               r.Season, r.Amount_Fertilizer_Used_KG
        FROM Records r
        JOIN Crops c ON r.Crop_Id=c.Crop_Id
        JOIN Soil s ON r.Soil_Id=s.Soil_Id
        JOIN Fertilizer f ON r.Fertilizer_Id=f.Fertilizer_Id
        """
        if search:
            query += " WHERE c.Crop_name LIKE ? OR r.Season LIKE ?"
            self.cursor.execute(query, (f"%{search}%", f"%{search}%"))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_record(self, c, s, f, se, a):
        self.cursor.execute("INSERT INTO Records VALUES (?,?,?,?,?)", (c, s, f, se, a))
        self.conn.commit()

    def update_record(self, id, c, s, f, se, a):
        self.cursor.execute("""
        UPDATE Records SET Crop_Id=?, Soil_Id=?, Fertilizer_Id=?, Season=?, Amount_Fertilizer_Used_KG=?
        WHERE Record_Id=?""", (c, s, f, se, a, id))
        self.conn.commit()

    def delete_record(self, id):
        self.cursor.execute("DELETE FROM Records WHERE Record_Id=?", (id,))
        self.conn.commit()

    def fertilizer_report(self):
        self.cursor.execute("""
        SELECT c.Crop_name, SUM(r.Amount_Fertilizer_Used_KG)
        FROM Records r
        JOIN Crops c ON r.Crop_Id=c.Crop_Id
        GROUP BY c.Crop_name
        """)
        return self.cursor.fetchall()
