from ..utils import get_connection

class Software:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def insert(self, data):
        if data['buying_date'] == "":
            data['buying_date'] == None
        sql = """
            INSERT INTO software(name, sap, zedat, oei, barcode, license, buying_date, notes,
                id_department)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(sql, (data['name'], data['sap'], data['zedat'], data['oei'],
            data['barcode'], data['license'], data['buying_date'], data['notes'],
            data['id_department']))

    def update(self, data):
        if data['buying_date'] == "":
            data['buying_date'] = None
        sql = """
            UPDATE software
            SET name = %s, sap = %s, zedat = %s, oei = %s, barcode = %s, license = %s,
                buying_date = %s, notes = %s, id_department = %s
            WHERE id = %s"""
        self.cursor.execute(sql, (data['name'], data['sap'], data['zedat'], data['oei'],
            data['barcode'], data['license'], data['buying_date'], data['notes'],
            data['id_department'], data['id']))

    def get_all(self):
        sql = """
            SELECT software.id, software.name, software.sap, software.zedat, software.oei,
                software.barcode, software.license, software.buying_date, software.notes,
                department.name
            FROM software JOIN department ON software.id_department = department.id"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get(self, id):
        sql = """
            SELECT software.id, software.name, software.sap, software.zedat, software.oei,
                software.barcode, software.license, software.buying_date, software.notes,
                software.id_department, department.name
            FROM software JOIN department ON software.id_department = department.id
            WHERE software.id = %s"""
        self.cursor.execute(sql, (id))
        return self.cursor.fetchone()

    def delete(self, id):
        sql = "DELETE FROM software WHERE id = %s"
        self.cursor.execute(sql, (id))


    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
