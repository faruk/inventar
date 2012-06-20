from ..utils import get_connection

class Hardware:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def insert(self, data):
        if data['buying_date'] == "":
            data['buying_date'] = None
        sql = """
            INSERT INTO hardware (name, sap, zedat, oei, barcode, buying_date,
                notes, id_room, id_department)
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s )
            """
        self.cursor.execute(sql, (data['name'], data['sap'], data['zedat'], data['oei'],
            data['barcode'], data['buying_date'], data['notes'], data['id_room'],
            data['id_department']))

    def update(self, data):
        if data['buying_date'] == "":
            data['buying_date'] = None
        sql = """
            UPDATE hardware
            SET name = %s, sap = %s, zedat = %s, oei = %s, barcode = %s, buying_date = %s,
                notes = %s, id_room = %s, id_department = %s
            WHERE id = %s
            """
        self.cursor.execute(sql, (data['name'], data['sap'], data['zedat'], data['oei'],
            data['barcode'], data['buying_date'], data['notes'], data['id_room'],
            data['id_department'], data['id']))

    def delete(self, id):
        sql = "DELETE FROM hardware WHERE id=%s"
        self.cursor.execute(sql, (id))

    def get_all(self):
        sql = """
            SELECT hardware.id, hardware.name, hardware.sap, hardware.zedat, hardware.oei,
                hardware.barcode, hardware.buying_date, hardware.notes, room.name, department.name
            FROM hardware
                JOIN room ON hardware.id_room = room.id
                JOIN department ON hardware.id_department = department.id
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get(self, id):
        sql = """
            SELECT hardware.id, hardware.name, hardware.sap, hardware.zedat, hardware.oei,
                hardware.barcode, hardware.buying_date, hardware.notes, hardware.id_room,
                room.name, hardware.id_department, department.name
            FROM hardware
                JOIN room ON hardware.id_room = room.id
                JOIN department ON hardware.id_department = department.id
            """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
