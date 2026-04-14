import pyodbc

class Database:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=LIANNEDREY\\SQLEXPRESS;'
                'DATABASE=FLORA;'
                'Trusted_Connection=yes;'
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Database connection error: {e}")
            raise

    def login(self, username, password):
        """Verify login credentials and return user_id and username"""
        try:
            query = "SELECT User_Id, Username FROM Users WHERE Username = ? AND Password = ?"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            if result:
                return result[0], result[1]
            return None, None
        except Exception as e:
            print(f"Login error: {e}")
            return None, None

    def register(self, username, password):
        """Register a new user"""
        try:
            self.cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username,))
            if self.cursor.fetchone():
                return False
            
            self.cursor.execute("INSERT INTO Users (Username, Password) VALUES (?,?)", (username, password))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Registration error: {e}")
            self.conn.rollback()
            return False

    def get_crops(self):
        try:
            self.cursor.execute("SELECT Crop_Id, Crop_name FROM Crops")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching crops: {e}")
            return []

    def get_soil(self):
        try:
            self.cursor.execute("SELECT Soil_Id, Soil_Type FROM Soil")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching soil types: {e}")
            return []

    def get_fert(self):
        try:
            self.cursor.execute("SELECT Fertilizer_Id, Fertilizer_name FROM Fertilizer")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching fertilizers: {e}")
            return []

    def fetch_records(self, search=""):
        try:
            query = """
            SELECT r.Record_Id, c.Crop_name, s.Soil_Type, f.Fertilizer_name,
                   r.Season, r.Amount_Fertilizer_Used_KG
            FROM Records r
            JOIN Crops c ON r.Crop_Id = c.Crop_Id
            JOIN Soil s ON r.Soil_Id = s.Soil_Id
            JOIN Fertilizer f ON r.Fertilizer_Id = f.Fertilizer_Id
            """
            if search:
                query += " WHERE c.Crop_name LIKE ? OR r.Season LIKE ?"
                self.cursor.execute(query, (f"%{search}%", f"%{search}%"))
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []

    def insert_record(self, crop_id, soil_id, fertilizer_id, season, amount):
        try:
            self.cursor.execute(
                "INSERT INTO Records (Crop_Id, Soil_Id, Fertilizer_Id, Season, Amount_Fertilizer_Used_KG) VALUES (?,?,?,?,?)", 
                (crop_id, soil_id, fertilizer_id, season, amount)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error inserting record: {e}")
            self.conn.rollback()
            return False

    def update_record(self, record_id, crop_id, soil_id, fertilizer_id, season, amount):
        try:
            self.cursor.execute("""
            UPDATE Records 
            SET Crop_Id=?, Soil_Id=?, Fertilizer_Id=?, Season=?, Amount_Fertilizer_Used_KG=?
            WHERE Record_Id=?""", (crop_id, soil_id, fertilizer_id, season, amount, record_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating record: {e}")
            self.conn.rollback()
            return False

    def delete_record(self, record_id):
        try:
            self.cursor.execute("DELETE FROM Records WHERE Record_Id=?", (record_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting record: {e}")
            self.conn.rollback()
            return False
        
    def crop_report(self):
        """Generate report showing crop usage/planting frequency"""
        try:
            self.cursor.execute("""
                SELECT c.Crop_name, COUNT(r.Record_Id) as Times_Planted
                FROM Records r
                JOIN Crops c ON r.Crop_Id = c.Crop_Id
                GROUP BY c.Crop_name
                ORDER BY Times_Planted DESC
            """)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating crop report: {e}")
            return []

    def crop_detailed_report(self):
        """Generate detailed crop report including total fertilizer used and average per planting"""
        try:
            self.cursor.execute("""
                SELECT 
                    c.Crop_name,
                    COUNT(r.Record_Id) as Times_Planted,
                    SUM(r.Amount_Fertilizer_Used_KG) as Total_Fertilizer_KG,
                    AVG(r.Amount_Fertilizer_Used_KG) as Avg_Fertilizer_Per_Planting_KG,
                    MIN(r.Amount_Fertilizer_Used_KG) as Min_Fertilizer_KG,
                    MAX(r.Amount_Fertilizer_Used_KG) as Max_Fertilizer_KG
                FROM Records r
                JOIN Crops c ON r.Crop_Id = c.Crop_Id
                GROUP BY c.Crop_name
                ORDER BY Total_Fertilizer_KG DESC
            """)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating detailed crop report: {e}")
            return []

    def crop_seasonal_report(self):
        """Generate crop report grouped by season"""
        try:
            self.cursor.execute("""
                SELECT 
                    c.Crop_name,
                    r.Season,
                    COUNT(r.Record_Id) as Times_Planted,
                    SUM(r.Amount_Fertilizer_Used_KG) as Total_Fertilizer_KG
                FROM Records r
                JOIN Crops c ON r.Crop_Id = c.Crop_Id
                GROUP BY c.Crop_name, r.Season
                ORDER BY c.Crop_name, r.Season DESC
            """)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error generating seasonal crop report: {e}")
            return []
